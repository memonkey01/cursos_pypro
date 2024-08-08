from manim import *

class EconometricsIntro(Scene):
    def construct(self):
        # Introducción a la econometría
        intro_text1 = Text("¿Qué es la econometría?").scale(0.9)
        intro_text2 = Text(
            "Básicamente, existen dos tipos de economistas: \n"
            "aquellos que desarrollan teorías y aquellos que prueban esas teorías."
        ).scale(0.7)
        intro_text3 = Text(
            "Los econometristas prueban teorías usando técnicas estadísticas \n"
            "para entender y explicar fenómenos sociales con dimensiones económicas."
        ).scale(0.7)

        self.play(Write(intro_text1))
        self.wait(3)
        self.play(ReplacementTransform(intro_text1, intro_text2))
        self.wait(3)
        self.play(ReplacementTransform(intro_text2, intro_text3))
        self.wait(3)

        # Ejemplo de hipótesis
        hypothesis_intro = Text("Ejemplo de hipótesis:").scale(0.9)
        hypothesis_text = Text(
            "La duración de la educación tiene un impacto positivo en las tasas salariales."
        ).scale(0.7)

        self.play(ReplacementTransform(intro_text3, hypothesis_intro))
        self.wait(3)
        self.play(ReplacementTransform(hypothesis_intro, hypothesis_text))
        self.wait(3)

        # Técnicas de regresión
        regression_intro = Text("Técnicas de regresión:").scale(0.9)
        regression_text1 = Text(
            "Se utilizan para modelar y analizar la relación entre variables."
        ).scale(0.7)
        regression_eq = MathTex(
            r"Salario = \\beta_0 + \\beta_1 (Educacion) + \\epsilon"
        )

        self.play(ReplacementTransform(hypothesis_text, regression_intro))
        self.wait(3)
        self.play(ReplacementTransform(regression_intro, regression_text1))
        self.wait(3)
        self.play(ReplacementTransform(regression_text1, regression_eq))
        self.wait(3)

        # Elasticidad precio de la demanda
        elasticity_intro = Text("Elasticidad precio de la demanda:").scale(0.9)
        elasticity_text1 = Text(
            "Mide la sensibilidad de la cantidad demandada \n"
            "ante cambios en el precio de un bien."
        ).scale(0.7)
        elasticity_eq = MathTex(
            r"E_p = \\frac{\\Delta Q / Q}{\\Delta P / P}"
        )

        self.play(ReplacementTransform(regression_eq, elasticity_intro))
        self.wait(3)
        self.play(ReplacementTransform(elasticity_intro, elasticity_text1))
        self.wait(3)
        self.play(ReplacementTransform(elasticity_text1, elasticity_eq))
        self.wait(3)

        # Conclusión
        conclusion_text = Text(
            "La econometría combina teoría económica y datos \n"
            "para cuantificar relaciones y probar hipótesis."
        ).scale(0.7)

        self.play(ReplacementTransform(elasticity_eq, conclusion_text))
        self.wait(3)

        self.play(FadeOut(conclusion_text))
