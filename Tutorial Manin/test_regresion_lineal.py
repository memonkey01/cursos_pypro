from manim import *

class LinearRegression(Scene):
    def construct(self):
        title = Text("Regresión Lineal", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Definición de la Regresión Lineal
        definition = Text(
            "La regresión lineal es una técnica estadística utilizada para modelar "
            "la relación entre una variable dependiente y una o más variables independientes.",
            t2c={"regresión lineal": BLUE, "técnica estadística": BLUE},
            font_size=24,
        )
        self.play(Write(definition))
        self.wait(2)
        self.play(definition.animate.to_edge(UP))

        # Fórmula de la Regresión Lineal Simple
        formula_simple = MathTex("y = \\beta_0 + \\beta_1 x + \\epsilon", font_size=36)
        self.play(Write(formula_simple))
        self.wait(2)
        self.play(formula_simple.animate.to_edge(UP))

        # Supuestos del Modelo
        supuestos_title = Text("Supuestos del Modelo", font_size=36)
        self.play(Write(supuestos_title))
        self.wait(1)
        self.play(supuestos_title.animate.to_edge(UP))

        supuestos = BulletedList(
            "Linealidad",
            "Independencia",
            "Homoscedasticidad",
            "No Multicolinealidad",
            "Normalidad de los Errores",
            font_size=24,
        )
        self.play(Write(supuestos))
        self.wait(2)
        self.play(supuestos.animate.to_edge(UP))

        # Solución mediante OLS
        ols_title = Text("Solución mediante Mínimos Cuadrados Ordinarios (OLS)", font_size=36)
        self.play(Write(ols_title))
        self.wait(1)
        self.play(ols_title.animate.to_edge(UP))

        sse_formula = MathTex(
            "\\text{SSE} = \\sum_{i=1}^n (y_i - \\hat{y}_i)^2 = "
            "\\sum_{i=1}^n (y_i - (\\beta_0 + \\beta_1 x_{i1} + \\cdots + \\beta_p x_{ip}))^2",
            font_size=24,
        )
        self.play(Write(sse_formula))
        self.wait(2)
        self.play(sse_formula.animate.to_edge(UP))

        normal_equations = MathTex("X^T X \\beta = X^T y", font_size=36)
        self.play(Write(normal_equations))
        self.wait(2)
        self.play(normal_equations.animate.to_edge(UP))

        # Evaluación de los Supuestos
        evaluacion_title = Text("Evaluación de los Supuestos", font_size=36)
        self.play(Write(evaluacion_title))
        self.wait(1)
        self.play(evaluacion_title.animate.to_edge(UP))

        evaluacion = BulletedList(
            "Linealidad: Gráficos de dispersión",
            "Independencia: Prueba de Durbin-Watson",
            "Homoscedasticidad: Gráfico de residuos vs valores ajustados",
            "No Multicolinealidad: Factor de inflación de la varianza (VIF)",
            "Normalidad de los Errores: Histograma y prueba de Shapiro-Wilk",
            font_size=24,
        )
        self.play(Write(evaluacion))
        self.wait(2)
        self.play(evaluacion.animate.to_edge(UP))

        # Aplicación en Econometría
        econometria_title = Text("Aplicación en Econometría", font_size=36)
        self.play(Write(econometria_title))
        self.wait(1)
        self.play(econometria_title.animate.to_edge(UP))

        econometria_text = Text(
            "En econometría, la regresión lineal se utiliza para analizar relaciones económicas "
            "y hacer predicciones, por ejemplo, estudiando la relación entre el PIB y el gasto en consumo.",
            t2c={"econometría": BLUE, "regresión lineal": BLUE},
            font_size=24,
        )
        self.play(Write(econometria_text))
        self.wait(2)

        self.wait(2)
