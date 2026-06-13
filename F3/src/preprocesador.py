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