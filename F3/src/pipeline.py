from preprocesador import Preprocesador
from analizador import (
    AnalizadorVariacionPrecios,
    AnalizadorEstadistico
)


class PipelineAnalisis:
    """
    Coordina la ejecución completa del flujo de análisis,
    desde la carga de archivos raw hasta la generación de
    resultados estadísticos.

    Esta clase reduce el acoplamiento entre componentes al
    centralizar la instanciación y encadenamiento de
    Preprocesador y los analizadores. El código cliente
    solo necesita conocer PipelineAnalisis, no los módulos
    internos.

    Parámetros
    ----------
    carpeta_raw : str o Path
        Ruta a la carpeta que contiene los archivos CSV anuales
        del WFP. Los archivos deben tener extensión .csv.

    Atributos
    ---------
    _carpeta_raw : str o Path
        Ruta interna a la carpeta de archivos raw.
    _df : pd.DataFrame o None
        DataFrame procesado. Vale None hasta que se ejecuta
        el método ejecutar().

    Ejemplo
    -------
    >>> pipeline = PipelineAnalisis("../../F1/data")
    >>> variaciones, estadisticas = pipeline.ejecutar()
    """

    def __init__(self, carpeta_raw):
        """
        Inicializa el pipeline con la ruta a la carpeta raw.

        Parámetros
        ----------
        carpeta_raw : str o Path
            Ruta a la carpeta con archivos CSV anuales del WFP.
        """

        self._carpeta_raw = carpeta_raw
        self._df = None

    def ejecutar(self):
        """
        Ejecuta el flujo completo de preprocesamiento y análisis.

        El flujo comprende:
        1. Instanciar Preprocesador con la carpeta raw.
        2. Cargar y consolidar archivos CSV.
        3. Validar columnas requeridas.
        4. Filtrar países europeos.
        5. Convertir fechas y crear variables temporales.
        6. Eliminar nulos en usdprice.
        7. Normalizar usdprice con z-score.
        8. Validar el dataset resultante.
        9. Calcular variaciones anuales de precios.
        10. Calcular estadísticas descriptivas.

        Retorna
        -------
        tuple[pd.DataFrame, pd.Series]
            Tupla con (variaciones_anuales, estadisticas_descriptivas).
            variaciones_anuales contiene precios promedio y variación
            porcentual por producto y año.
            estadisticas_descriptivas contiene describe() de usdprice.

        Excepciones
        -----------
        FileNotFoundError
            Si la carpeta raw no existe.
        ValueError
            Si no hay archivos CSV o faltan columnas requeridas.
        AssertionError
            Si el dataset no pasa las validaciones formales.
        """

        preprocesador = Preprocesador(self._carpeta_raw)

        self._df = (
            preprocesador
            .cargar_archivos()
            .validar_columnas_requeridas()
            .filtrar_europa()
            .convertir_fechas()
            .eliminar_nulos_usdprice()
            .normalizar_usdprice()
            .validar()
            .obtener_dataframe()
        )

        analizador_variacion = AnalizadorVariacionPrecios(self._df)
        variaciones = analizador_variacion.analizar()

        analizador_estadistico = AnalizadorEstadistico(self._df)
        estadisticas = analizador_estadistico.analizar()

        return variaciones, estadisticas