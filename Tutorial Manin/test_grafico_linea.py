from manim import *

class LinearRegressionExample(Scene):
    def construct(self):
        # Título de la escena
        title = Text("Ejemplo de Regresión Lineal").scale(1.5)
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        
        # Crear el sistema de coordenadas
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": BLUE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 11, 1),
                "label_direction": DOWN,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 11, 1),
                "label_direction": LEFT,
            },
        )

        labels = axes.get_axis_labels(x_label="X", y_label="Y")
        self.play(Create(axes), Write(labels))
        self.wait(3)
        
        # Datos de ejemplo
        x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y_data = [2, 3, 2.5, 5, 7, 8, 6.5, 9, 9.5, 10]
        
        # Dibujar puntos
        points = [Dot(axes.coords_to_point(x, y), color=YELLOW) for x, y in zip(x_data, y_data)]
        points_group = VGroup(*points)
        self.play(Create(points_group))
        self.wait(3)
        
        # Línea de regresión (y = 0.9x + 1.2)
        regression_line = axes.plot(lambda x: 0.9 * x + 1.2, color=RED)
        regression_label = MathTex(r"y = 0.9x + 1.2", color=RED).next_to(regression_line, UP, buff=0.5)
        
        self.play(Create(regression_line), Write(regression_label))
        self.wait(3)
        
        # Animar la predicción de un nuevo punto
        new_x = 7
        new_y = 0.9 * new_x + 1.2
        new_point = Dot(axes.coords_to_point(new_x, new_y), color=GREEN)
        prediction_line = DashedLine(
            start=axes.coords_to_point(new_x, 0),
            end=axes.coords_to_point(new_x, new_y),
            color=GREEN
        )
        
        self.play(Create(prediction_line), Create(new_point))
        self.wait(3)
        
        # Mostrar ecuación final de regresión
        final_equation = MathTex(r"y = \beta_0 + \beta_1 x + \epsilon", color=BLUE).scale(1.2).to_edge(DOWN)
        self.play(Write(final_equation))
        self.wait(3)
        
        # Finalizar la escena
        self.play(FadeOut(VGroup(axes, labels, points_group, regression_line, regression_label, prediction_line, new_point, final_equation)))

# Para renderizar el video, ejecuta el siguiente comando en tu terminal:
# manim -pql linear_regression_example.py LinearRegressionExample
