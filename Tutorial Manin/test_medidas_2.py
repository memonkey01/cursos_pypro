from manim import *

class CentralTendencyEquations(Scene):
    def construct(self):
        # Título
        title = Text("Medidas de Tendencia Central").scale(0.9)
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

        # Media Aritmética
        mean_title = Text("Media Aritmética (Promedio)").scale(0.7)
        mean_eq = MathTex("\\bar{X} = \\frac{1}{n} \\sum_{i=1}^{n} X_i").scale(0.8)
        mean_desc = Text("La media aritmética es la suma de todos los valores dividida por el número total de valores.").scale(0.6)

        self.play(Write(mean_title))
        self.wait(2)
        self.play(mean_title.animate.to_edge(UP))
        self.play(Write(mean_eq))
        self.wait(2)
        self.play(mean_eq.animate.shift(UP*2))
        self.play(Write(mean_desc))
        self.wait(3)
        self.play(FadeOut(mean_title), FadeOut(mean_eq), FadeOut(mean_desc))

        # Mediana
        median_title = Text("Mediana").scale(0.7)
        median_eq_odd = Text("Si n es impar: Mediana = valor medio").scale(0.6)
        median_eq_even = Text("Si n es par: Mediana = promedio de los dos valores medios").scale(0.6)
        median_desc = Text("La mediana es el valor que separa la mitad superior e inferior de un conjunto de datos ordenados.").scale(0.6)

        self.play(Write(median_title))
        self.wait(2)
        self.play(median_title.animate.to_edge(UP))
        self.play(Write(median_eq_odd))
        self.wait(2)
        self.play(median_eq_odd.animate.shift(UP*1.5))
        self.play(Write(median_eq_even))
        self.wait(2)
        self.play(median_eq_even.animate.shift(UP*1.5))
        self.play(Write(median_desc))
        self.wait(3)
        self.play(FadeOut(median_title), FadeOut(median_eq_odd), FadeOut(median_eq_even), FadeOut(median_desc))

        # Moda
        mode_title = Text("Moda").scale(0.7)
        mode_eq = Text("Moda = valor con mayor frecuencia").scale(0.6)
        mode_desc = Text("La moda es el valor que aparece con mayor frecuencia en un conjunto de datos.").scale(0.6)

        self.play(Write(mode_title))
        self.wait(2)
        self.play(mode_title.animate.to_edge(UP))
        self.play(Write(mode_eq))
        self.wait(2)
        self.play(mode_eq.animate.shift(UP*2))
        self.play(Write(mode_desc))
        self.wait(3)
        self.play(FadeOut(mode_title), FadeOut(mode_eq), FadeOut(mode_desc))

        # Conclusión
        conclusion = Text(
            "Las medidas de tendencia central incluyen la Media, \n"
            "la Mediana y la Moda, y son esenciales para resumir \n"
            "la distribución de los datos."
        ).scale(0.7)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(FadeOut(conclusion))
