from preprocesador import Preprocesador
from analizador import (
    AnalizadorVariacionPrecios,
    AnalizadorEstadistico
)


class PipelineAnalisis:
    """
    Coordina la ejecución completa del análisis.

    Esta clase centraliza la carga del dataset,
    el cálculo de variaciones y la generación
    de estadísticas descriptivas.
    """

    def __init__(self, ruta_csv):
        """
        Inicializa el pipeline.
        """
        self._ruta_csv = ruta_csv
        self._df = None

    def ejecutar(self):
        """
        Ejecuta el flujo completo del análisis.
        """

        # Carga dataset.
        preprocesador = Preprocesador(
            self._ruta_csv
        )

        self._df = (
            preprocesador
            .cargar()
            .obtener_dataframe()
        )

        # Calcula variaciones.
        analizador_variacion = (
            AnalizadorVariacionPrecios(self._df)
        )

        variaciones = (
            analizador_variacion
            .analizar()
        )

        # Calcula estadísticas.
        analizador_estadistico = (
            AnalizadorEstadistico(self._df)
        )

        estadisticas = (
            analizador_estadistico
            .analizar()
        )

        return variaciones, estadisticas