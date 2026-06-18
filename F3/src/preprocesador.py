from pathlib import Path
import pandas as pd


COLUMNAS_REQUERIDAS = [
    "date", "countryiso3", "commodity",
    "usdprice", "market", "category",
]

PAISES_EUROPA = [
    "ALB", "AUT", "BEL", "BGR", "BIH", "BLR", "CHE", "CYP", "CZE",
    "DEU", "DNK", "ESP", "EST", "FIN", "FRA", "GBR", "GRC",
    "HRV", "HUN", "IRL", "ITA", "LTU", "LVA", "MDA", "MKD",
    "NLD", "NOR", "POL", "PRT", "ROU", "RUS", "SRB", "SVK", "SVN",
    "SWE", "TUR", "UKR",
]


class Preprocesador:
    """
    Encapsula el pipeline completo de preprocesamiento
    desde archivos raw hasta un DataFrame limpio y validado.

    Opera sobre una carpeta que contiene archivos CSV anuales
    de la base Global Food Prices del WFP. Realiza carga,
    consolidación, filtrado geográfico, conversión de fechas,
    tratamiento de nulos, normalización y validación.

    Parámetros
    ----------
    carpeta_raw : str o Path
        Ruta a la carpeta que contiene los archivos CSV anuales.
        Los archivos deben tener extensión .csv.

    Atributos
    ---------
    _carpeta_raw : Path
        Ruta interna a la carpeta de archivos raw.
    _df : pd.DataFrame o None
        DataFrame interno que acumula las transformaciones.
        Vale None hasta que se invoca cargar_archivos().

    Ejemplo
    -------
    >>> prep = Preprocesador("../../F1/data")
    >>> df = (prep
    ...     .cargar_archivos()
    ...     .validar_columnas_requeridas()
    ...     .filtrar_europa()
    ...     .convertir_fechas()
    ...     .eliminar_nulos_usdprice()
    ...     .normalizar_usdprice()
    ...     .validar()
    ...     .obtener_dataframe())
    """

    def __init__(self, carpeta_raw):

        self._carpeta_raw = Path(carpeta_raw)
        self._df = None

    def cargar_archivos(self):
        """
        Carga todos los archivos CSV presentes en la carpeta raw
        y los consolida en un único DataFrame.

        Agrega la variable archivo_origen para mantener trazabilidad
        del origen de cada registro. Los archivos se buscan
        automáticamente mediante glob("*.csv").

        Retorna
        -------
        Preprocesador
            La instancia actual (permite encadenamiento de métodos).

        Excepciones
        -----------
        FileNotFoundError
            Si la carpeta indicada no existe.
        ValueError
            Si no se encuentran archivos CSV en la carpeta.

        Complejidad
        -----------
        O(n) donde n es el número total de registros en todos los CSV.
        """

        if not self._carpeta_raw.exists():
            raise FileNotFoundError(
                f"La carpeta no existe: {self._carpeta_raw}"
            )

        archivos = sorted(self._carpeta_raw.glob("*.csv"))

        if not archivos:
            raise ValueError(
                f"No se encontraron archivos CSV en: {self._carpeta_raw}"
            )

        dfs = []

        for ruta in archivos:

            try:
                df_parcial = pd.read_csv(ruta)
                df_parcial["archivo_origen"] = ruta.name
                dfs.append(df_parcial)
                print(f"  Cargado: {ruta.name} "
                      f"({len(df_parcial):,} filas)")

            except Exception as error:
                print(f"  Advertencia: no se pudo cargar {ruta.name} — {error}")

        self._df = pd.concat(dfs, ignore_index=True)

        print(
            f"\nDataset consolidado: "
            f"{self._df.shape[0]:,} filas, "
            f"{self._df.shape[1]} columnas"
        )

        return self

    def filtrar_europa(self):

        self._df = self._df[
            self._df["countryiso3"]
            .isin(PAISES_EUROPA)
        ]

        print(
            f"Registros europeos: "
            f"{len(self._df)}"
        )

        return self

    def convertir_fechas(self):

        self._df["date"] = pd.to_datetime(
            self._df["date"],
            errors="coerce"
        )

        self._df["year"] = (
            self._df["date"].dt.year
        )

        self._df["month"] = (
            self._df["date"].dt.month
        )

        return self

    def eliminar_nulos_usdprice(self):

        self._df = self._df.dropna(
            subset=["usdprice"]
        )

        return self

    def validar(self):

        assert (
            self._df.duplicated().sum() == 0
        ), "Existen registros duplicados."

        assert (
            self._df["usdprice"]
            .isna()
            .sum()
            == 0
        ), "Existen nulos en usdprice."

        assert (
            self._df["year"]
            .between(2020, 2025)
            .all()
        ), "Existen años fuera del rango esperado."

        print(
            "Validaciones superadas correctamente."
        )

        return self

    def obtener_dataframe(self):

        return self._df