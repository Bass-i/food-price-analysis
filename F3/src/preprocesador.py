from pathlib import Path
import pandas as pd


class Preprocesador:
    """
    Clase responsable de cargar y entregar el dataset procesado
    generado durante la Fase 2.

    Aplica encapsulamiento manteniendo el DataFrame como un atributo
    interno protegido.
    """

    def __init__(self, ruta_csv):
        """
        Inicializa la clase con la ruta del archivo CSV.
        """
        self._ruta_csv = Path(ruta_csv)
        self._df = None

    def cargar(self):
        """
        Carga el archivo CSV en memoria.
        """
        self._df = pd.read_csv(self._ruta_csv)

        print(
            f"Dataset cargado correctamente: "
            f"{self._df.shape[0]} filas, "
            f"{self._df.shape[1]} columnas"
        )

        return self

    def obtener_dataframe(self):
        """
        Retorna el DataFrame cargado.
        """
        return self._df

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
        ), "Existen valores nulos en usdprice."

        assert (
            self._df["year"]
            .between(2020, 2025)
            .all()
        ), "Existen años fuera del rango esperado."

        print(
            "Validaciones superadas correctamente."
        )

        return self