from manim import *

class KurtosisExplanation(Scene):
    def construct(self):
        # Título
        title = Text("Curtosis").scale(0.9)
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

        # Distribuciones con diferentes niveles de curtosis
        gaussian = axes.plot(
            lambda x: np.exp(-x**2 / 2) / np.sqrt(2 * np.pi),
            color=YELLOW
        )

        high_kurtosis = axes.plot(
            lambda x: (np.exp(-x**2 / 0.5) / np.sqrt(0.5 * 2 * np.pi)),
            color=GREEN
        )

        low_kurtosis = axes.plot(
            lambda x: (np.exp(-x**2 / 5) / np.sqrt(5 * 2 * np.pi)),
            color=RED
        )

        # Etiquetas para las distribuciones
        gaussian_label = axes.get_graph_label(gaussian, label="Distribucion Normal", x_val=-3, direction=UP/2)
        high_kurtosis_label = axes.get_graph_label(high_kurtosis, label="Alta Curtosis", x_val=2, direction=UP/2)
        low_kurtosis_label = axes.get_graph_label(low_kurtosis, label="Baja Curtosis", x_val=-2, direction=DOWN/2)

        self.play(Create(gaussian), Write(gaussian_label))
        self.wait(3)
        self.play(Create(high_kurtosis), Write(high_kurtosis_label))
        self.wait(3)
        self.play(Create(low_kurtosis), Write(low_kurtosis_label))
        self.wait(3)

        # Descripción de curtosis
        description_text = Text(
            "La curtosis mide la 'altura' y 'anchura' de la cola de una distribución.\n"
            "Distribuciones con alta curtosis tienen colas más 'pesadas'."
        ).scale(0.7)

        self.play(Write(description_text))
        self.wait(5)
        self.play(FadeOut(description_text), FadeOut(gaussian), FadeOut(high_kurtosis), FadeOut(low_kurtosis), FadeOut(gaussian_label), FadeOut(high_kurtosis_label), FadeOut(low_kurtosis_label), FadeOut(axes), FadeOut(x_label), FadeOut(y_label))

        # Conclusión
        conclusion = Text(
            "La curtosis es una medida importante para entender \n"
            "la forma de una distribución y sus colas."
        ).scale(0.7)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(FadeOut(conclusion))
