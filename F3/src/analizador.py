import pandas as pd


class AnalizadorBase:
    """
    Clase base abstracta para todos los analizadores del proyecto.

    Define la interfaz común que deben implementar las clases
    derivadas mediante el método analizar(). El uso de una clase
    base permite aplicar polimorfismo: distintos analizadores pueden
    ejecutarse con la misma llamada analizar(), sin que el código
    cliente necesite conocer el tipo específico de analizador.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset procesado con al menos las columnas usdprice,
        commodity y year.

    Atributos
    ---------
    _df : pd.DataFrame
        Dataset interno protegido contra modificaciones externas.
    """

    def __init__(self, df):
        """
        Inicializa el analizador con el DataFrame procesado.

        Parámetros
        ----------
        df : pd.DataFrame
            Dataset limpio y validado proveniente del Preprocesador.
        """
        self._df = df

    def analizar(self):
        """
        Método abstracto que debe ser implementado por cada subclase.

        Define la interfaz común de todos los analizadores.
        No debe invocarse directamente sobre AnalizadorBase.

        Retorna
        -------
        NotImplementedError
            Siempre, si se llama directamente sobre la clase base.

        Excepciones
        -----------
        NotImplementedError
            Si la subclase no sobreescribe este método.
        """
        raise NotImplementedError(
            "Las clases hijas deben implementar el método analizar()."
        )


class AnalizadorVariacionPrecios(AnalizadorBase):
    """
    Calcula la evolución anual de los precios de productos
    alimentarios y las variaciones porcentuales año a año.

    Hereda de AnalizadorBase e implementa el método analizar()
    para calcular variaciones de precios agrupadas por producto
    y año calendario.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset procesado. Debe contener las columnas
        commodity, year y usdprice.
    """

    def __init__(self, df):
        """
        Inicializa el analizador de variación de precios.

        Parámetros
        ----------
        df : pd.DataFrame
            Dataset limpio con columnas commodity, year y usdprice.
        """
        super().__init__(df)

    def analizar(self):
        """
        Implementación del método analizar() para variación de precios.

        Calcula el precio promedio anual por producto y luego
        la variación porcentual año a año mediante pct_change().

        Retorna
        -------
        pd.DataFrame
            DataFrame con columnas: commodity, year, precio_promedio,
            variacion_pct. La columna variacion_pct es NaN para el
            primer año de cada producto (sin año anterior de referencia).

        Complejidad
        -----------
        O(n log n) dominado por el groupby interno, donde n es el
        número de filas del DataFrame.
        """
        return self.calcular_variaciones_anuales()

    def calcular_precios_promedio_anuales(self):
        """
        Calcula el precio promedio anual de cada producto alimentario.

        Agrupa los registros por commodity y year, calculando la media
        de usdprice para cada combinación.

        Retorna
        -------
        pd.DataFrame
            DataFrame con columnas: commodity, year, precio_promedio.
            Una fila por combinación única de producto y año.

        Complejidad
        -----------
        O(n log n) donde n es el número de filas del DataFrame,
        por el proceso de agrupación y ordenamiento interno.
        """

        precios_anuales = (
            self._df
            .groupby(["commodity", "year"])["usdprice"]
            .mean()
            .reset_index()
        )

        precios_anuales.rename(
            columns={"usdprice": "precio_promedio"},
            inplace=True
        )

        return precios_anuales

    def calcular_variaciones_anuales(self):
        """
        Calcula la variación porcentual año a año para cada producto.

        Utiliza pct_change() agrupado por commodity para calcular
        la diferencia relativa entre el precio promedio de un año
        y el del año anterior, expresada como porcentaje.

        Retorna
        -------
        pd.DataFrame
            DataFrame con columnas: commodity, year, precio_promedio,
            variacion_pct. Ordenado por commodity y year.

        Complejidad
        -----------
        O(n log n) donde n es el número de filas del DataFrame.
        """

        precios = self.calcular_precios_promedio_anuales()

        precios = precios.sort_values(by=["commodity", "year"])

        precios["variacion_pct"] = (
            precios
            .groupby("commodity")["precio_promedio"]
            .pct_change()
            * 100
        )

        return precios


class AnalizadorEstadistico(AnalizadorBase):
    """
    Genera estadísticas descriptivas sobre los precios del dataset.

    Hereda de AnalizadorBase e implementa analizar() para calcular
    las estadísticas básicas de la variable usdprice, incluyendo
    conteo, media, desviación estándar, mínimo, percentiles y máximo.

    Parámetros
    ----------
    df : pd.DataFrame
        Dataset procesado. Debe contener la columna usdprice.
    """

    def __init__(self, df):
        """
        Inicializa el analizador estadístico.

        Parámetros
        ----------
        df : pd.DataFrame
            Dataset limpio con columna usdprice.
        """
        super().__init__(df)

    def analizar(self):
        """
        Implementación del método analizar() para estadísticas descriptivas.

        Aplica describe() sobre la columna usdprice, retornando las
        estadísticas estándar de distribución.

        Retorna
        -------
        pd.Series
            Serie con índices: count, mean, std, min, 25%, 50%, 75%, max,
            correspondientes a las estadísticas descriptivas de usdprice.

        Complejidad
        -----------
        O(n log n) dominado por el cálculo de percentiles, donde n es
        el número de filas del DataFrame.
        """

        return self._df["usdprice"].describe()