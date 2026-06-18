from pathlib import Path
import pandas as pd


PAISES_EUROPA = [
    "ALB", "AUT", "BEL", "BGR", "BIH", "BLR", "CHE", "CYP", "CZE",
    "DEU", "DNK", "ESP", "EST", "FIN", "FRA", "GBR", "GRC",
    "HRV", "HUN", "IRL", "ITA", "LTU", "LVA", "MDA", "MKD",
    "NLD", "NOR", "POL", "PRT", "ROU", "RUS", "SRB", "SVK", "SVN",
    "SWE", "TUR", "UKR",
]


class Preprocesador:
    """
    Encapsula el pipeline de preprocesamiento
    utilizado en la Fase 3.
    """

    def __init__(self, rutas_csv):

        self._rutas_csv = rutas_csv
        self._df = None

    def cargar_archivos(self):

        dfs = []

        for ruta in self._rutas_csv:

            print(f"Cargando: {ruta}")

            dfs.append(
                pd.read_csv(ruta)
            )

        self._df = pd.concat(
            dfs,
            ignore_index=True
        )

        print(
            f"Dataset consolidado: "
            f"{self._df.shape[0]} filas, "
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