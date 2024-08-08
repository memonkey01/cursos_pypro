from manim import *

class GaussianDistribution(Scene):
    def construct(self):
        # Título
        title = Text("Distribución Gaussiana").scale(0.9)
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

        # Crear ejes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(-4, 5, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 0.6, 0.1)},
        )

        # Etiquetas de los ejes
        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("f(x)"))

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(3)

        # Función de distribución gaussiana
        gaussian = axes.plot(
            lambda x: np.exp(-x**2 / 2) / np.sqrt(2 * np.pi),
            color=YELLOW
        )

        gaussian_label = axes.get_graph_label(gaussian, label="f(x) = \\frac{1}{\\sqrt{2\\pi}} e^{-\\frac{x^2}{2}}", x_val=-2, direction=UP/2)

        self.play(Create(gaussian), Write(gaussian_label))
        self.wait(3)

        # Mostrar desviaciones estándar
        sigma_lines = VGroup(
            DashedLine(start=axes.c2p(1, 0), end=axes.c2p(1, np.exp(-1 / 2) / np.sqrt(2 * np.pi)), color=RED),
            DashedLine(start=axes.c2p(-1, 0), end=axes.c2p(-1, np.exp(-1 / 2) / np.sqrt(2 * np.pi)), color=RED)
        )

        sigma_labels = VGroup(
            Tex("$\\sigma = 1$").next_to(sigma_lines[0], DOWN),
            Tex("$-\\sigma = -1$").next_to(sigma_lines[1], DOWN)
        )

        self.play(Create(sigma_lines), Write(sigma_labels))
        self.wait(3)

        # Desvanecer todo
        self.play(FadeOut(gaussian), FadeOut(gaussian_label), FadeOut(sigma_lines), FadeOut(sigma_labels), FadeOut(axes), FadeOut(x_label), FadeOut(y_label))

        # Conclusión
        conclusion = Text(
            "La distribución gaussiana es una de las distribuciones \n"
            "más importantes en estadística y econometría."
        ).scale(0.7)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(FadeOut(conclusion))
