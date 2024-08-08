from manim import *

class EconometricsIntro(Scene):
    def construct(self):
        # Título del video
        title = Text("¿Qué es la econometría?").scale(1.2)
        self.play(Write(title))
        self.wait(3)

        # Definición de Econometría
        definition = Text(
            "La econometría es un subdominio de la economía que aplica modelos matemáticos y estadísticos \n"
            "junto con teorías económicas para entender, explicar y medir la causalidad en los sistemas económicos."
        ).scale(0.7)
        self.play(ReplacementTransform(title, definition))
        self.wait(3)

        # Ejemplo de hipótesis
        hypothesis = Text(
            "Ejemplo de hipótesis: \n"
            "La duración de la educación tiene un impacto positivo en las tasas salariales."
        ).scale(0.7)
        self.play(ReplacementTransform(definition, hypothesis))
        self.wait(3)

        # Relación cuantitativa
        quantitative_relation = Text(
            "Relación cuantitativa: \n"
            "1 año adicional de escolarización aumenta el salario en un 5%."
        ).scale(0.7)
        self.play(ReplacementTransform(hypothesis, quantitative_relation))
        self.wait(3)

        # Introducción a las técnicas de regresión
        regression_intro = Text(
            "Técnicas de regresión: \n"
            "Se utilizan para modelar y analizar la relación entre variables."
        ).scale(0.7)
        self.play(ReplacementTransform(quantitative_relation, regression_intro))
        self.wait(3)

        # Ecuación de regresión lineal
        regression_eq = MathTex("y = \\beta_0 + \\beta_1 x + \\epsilon").scale(1.2)
        self.play(ReplacementTransform(regression_intro, regression_eq))
        self.wait(3)

        # Descripción de los términos de la ecuación
        regression_terms = MathTex(
            "donde:\n"
            "y: variable dependiente\n"
            "x: variable independiente\n"
            "\\beta_0: intersección\n"
            "\\beta_1: pendiente\n"
            "\\epsilon: término de error"
        ).scale(0.7)
        self.play(ReplacementTransform(regression_eq, regression_terms))
        self.wait(3)

        # Métodos de Econometría
        methods_intro = Text("Métodos de Econometría").scale(1.2)
        self.play(ReplacementTransform(regression_terms, methods_intro))
        self.wait(3)

        # Listado de métodos
        methods_list = Text(
            "1. Estadísticas descriptivas\n"
            "2. Pruebas de hipótesis\n"
            "3. Regresión\n"
            "4. Pronósticos"
        ).scale(0.7)
        self.play(ReplacementTransform(methods_intro, methods_list))
        self.wait(3)

        # Estadísticas descriptivas
        descriptive_stats = Text("Estadísticas descriptivas").scale(1.2)
        self.play(ReplacementTransform(methods_list, descriptive_stats))
        self.wait(3)

        # Ejemplos de estadísticas descriptivas
        descriptive_examples = MathTex(
            "Incluyen medidas como:\n"
            "Media (\\bar{x}), Mediana, Moda, Desviación estándar (\\sigma)"
        ).scale(0.7)
        self.play(ReplacementTransform(descriptive_stats, descriptive_examples))
        self.wait(3)

        # Pruebas de hipótesis
        hypothesis_testing = Text("Pruebas de hipótesis").scale(1.2)
        self.play(ReplacementTransform(descriptive_examples, hypothesis_testing))
        self.wait(3)

        # Ejemplos de pruebas de hipótesis
        hypothesis_examples = Text(
            "Determinan si existe suficiente evidencia en una muestra de datos\n"
            "para inferir que una condición es verdadera para toda la población.\n"
            "Ejemplos: pruebas t, pruebas chi-cuadrado."
        ).scale(0.7)
        self.play(ReplacementTransform(hypothesis_testing, hypothesis_examples))
        self.wait(3)

        # Regresión
        regression_methods = Text("Regresión").scale(1.2)
        self.play(ReplacementTransform(hypothesis_examples, regression_methods))
        self.wait(3)

        # Ecuación de regresión de nuevo
        regression_eq_again = MathTex("y = \\beta_0 + \\beta_1 x + \\epsilon").scale(1.2)
        self.play(ReplacementTransform(regression_methods, regression_eq_again))
        self.wait(3)

        # Pronósticos
        forecasting_methods = Text("Pronósticos").scale(1.2)
        self.play(ReplacementTransform(regression_eq_again, forecasting_methods))
        self.wait(3)

        # Ejemplos de técnicas de pronóstico
        forecasting_examples = Text(
            "Uso de modelos estadísticos para predecir futuros valores basados en datos históricos.\n"
            "Ejemplos: Modelos ARIMA, Suavizado exponencial."
        ).scale(0.7)
        self.play(ReplacementTransform(forecasting_methods, forecasting_examples))
        self.wait(3)

        # Conclusión
        conclusion = Text(
            "La econometría es fundamental para entender y analizar fenómenos económicos\n"
            "utilizando modelos matemáticos y estadísticos, con aplicaciones en negocios y aprendizaje automático."
        ).scale(0.7)
        self.play(ReplacementTransform(forecasting_examples, conclusion))
        self.wait(3)

        self.play(FadeOut(conclusion))
        self.wait(1)
