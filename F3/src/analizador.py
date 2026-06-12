import pandas as pd

class AnalizadorVariacionPrecios:
    """
    Analiza la evolución anual de los precios de los
    productos alimentarios presentes en el dataset.
    """

    def __init__(self, df):
        """
        Inicializa el analizador.
        """
        self._df = df

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