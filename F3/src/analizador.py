import pandas as pd


class AnalizadorBase:
    """
    Clase base para todos los analizadores del proyecto.

    Define la estructura general que deberán seguir
    las clases derivadas.
    """

    def __init__(self, df):
        self._df = df

    def analizar(self):
        """
        Método genérico que será sobrescrito por las
        clases hijas.
        """
        raise NotImplementedError(
            "Las clases hijas deben implementar este método."
        )


class AnalizadorVariacionPrecios(AnalizadorBase):
    """
    Analiza la evolución anual de los precios de los
    productos alimentarios presentes en el dataset.
    """

    def __init__(self, df):
        """
        Inicializa el analizador.
        """
        super().__init__(df)

    def analizar(self):
        """
        Implementación específica del método analizar.
        """

        return self.calcular_variaciones_anuales()

    def calcular_precios_promedio_anuales(self):
        """
        Calcula el precio promedio anual de cada producto.
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
        Calcula la variación porcentual año a año para
        cada producto.
        """

        precios = self.calcular_precios_promedio_anuales()

        precios = precios.sort_values(
            by=["commodity", "year"]
        )

        precios["variacion_pct"] = (
            precios
            .groupby("commodity")["precio_promedio"]
            .pct_change()
            * 100
        )

        return precios


class AnalizadorEstadistico(AnalizadorBase):
    """
    Genera estadísticas descriptivas sobre
    los precios del dataset.
    """

    def __init__(self, df):
        super().__init__(df)

    def analizar(self):
        """
        Implementación específica para análisis
        estadístico.
        """

        return self._df["usdprice"].describe()