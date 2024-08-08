from manim import *

class MedidasTendenciaCentral(Scene):
    def construct(self):
        # Título
        titulo = Text("Medidas de Tendencia Central").scale(1.2)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Media
        media_titulo = Text("Media (Promedio)").to_edge(UP)
        self.play(Write(media_titulo))
        
        media_def = Text(
            "Definición:\nLa media aritmética de un conjunto de datos es el valor que se obtiene\n"
            "sumando todos los datos y dividiéndolos entre el número total de datos.",
            t2c={"Definición:": YELLOW}
        ).scale(0.6).next_to(media_titulo, DOWN)
        self.play(Write(media_def))
        
        media_formula = MathTex(
            r"\text{Media} (\overline{x}) = \frac{1}{n} \sum_{i=1}^{n} x_i"
        ).scale(0.8).next_to(media_def, DOWN)
        self.play(Write(media_formula))
        
        media_ejemplo = MathTex(
            "Ejemplo:\nSi tienes los datos: 2, 4, 6, 8, 10\n"
            r"\[ \overline{x} = \frac{2 + 4 + 6 + 8 + 10}{5} = \frac{30}{5} = 6 \]",
            t2c={"Ejemplo:": YELLOW}
        ).scale(0.6).next_to(media_formula, DOWN)
        self.play(Write(media_ejemplo))
        
        media_prop = Text(
            "Propiedades:\n- La media es sensible a valores extremos (outliers).\n"
            "- Se utiliza para datos cuantitativos.",
            t2c={"Propiedades:": YELLOW}
        ).scale(0.6).next_to(media_ejemplo, DOWN)
        self.play(Write(media_prop))
        
        self.wait(4)
        self.play(FadeOut(media_titulo, media_def, media_formula, media_ejemplo, media_prop))

        # Mediana
        mediana_titulo = Text("Mediana").to_edge(UP)
        self.play(Write(mediana_titulo))
        
        mediana_def = Text(
            "Definición:\nLa mediana es el valor que divide el conjunto de datos en dos partes iguales,\n"
            "es decir, el 50% de los datos están por debajo de la mediana y el 50% están por encima.",
            t2c={"Definición:": YELLOW}
        ).scale(0.4).next_to(mediana_titulo, DOWN)
        self.play(Write(mediana_def))
        
        mediana_calc = Text(
            "Método de Cálculo:\n1. Ordenar los datos de menor a mayor.\n"
            "2. Si el número de datos \( n \) es impar, la mediana es el valor central.\n"
            "3. Si el número de datos \( n \) es par, la mediana es el promedio de los dos valores centrales.",
            t2c={"Método de Cálculo:": YELLOW}
        ).scale(0.3).next_to(mediana_def, DOWN)
        self.play(Write(mediana_calc))
        
        mediana_ejemplo = Text(
            "Ejemplo:\nPara los datos ordenados 2, 4, 6, 8, 10:\n"
            "- Como hay 5 datos (impar), la mediana es el tercer valor: 6.\n"
            "Para los datos ordenados 2, 4, 6, 8:\n"
            "- Como hay 4 datos (par), la mediana es el promedio de los dos valores centrales: \( \\frac{4 + 6}{2} = 5 \).",
            t2c={"Ejemplo:": YELLOW}
        ).scale(0.3).next_to(mediana_calc, DOWN)
        self.play(Write(mediana_ejemplo))
        
        mediana_prop = Text(
            "Propiedades:\n- La mediana no es afectada por valores extremos.\n"
            "- Es útil para datos ordinales y cuantitativos.",
            t2c={"Propiedades:": YELLOW}
        ).scale(0.6).next_to(mediana_ejemplo, DOWN)
        self.play(Write(mediana_prop))
        
        self.wait(4)
        self.play(FadeOut(mediana_titulo, mediana_def, mediana_calc, mediana_ejemplo, mediana_prop))

        # Moda
        moda_titulo = Text("Moda").to_edge(UP)
        self.play(Write(moda_titulo))
        
        moda_def = Text(
            "Definición:\nLa moda es el valor que aparece con mayor frecuencia en un conjunto de datos.",
            t2c={"Definición:": YELLOW}
        ).scale(0.6).next_to(moda_titulo, DOWN)
        self.play(Write(moda_def))
        
        moda_ejemplo = Text(
            "Ejemplo:\nPara los datos 2, 4, 4, 6, 8:\n- La moda es 4, ya que aparece dos veces, más que cualquier otro valor.",
            t2c={"Ejemplo:": YELLOW}
        ).scale(0.6).next_to(moda_def, DOWN)
        self.play(Write(moda_ejemplo))
        
        moda_prop = Text(
            "Propiedades:\n- Puede haber más de una moda (bimodal, multimodal) o ninguna moda.\n"
            "- Es útil para datos cualitativos y cuantitativos.",
            t2c={"Propiedades:": YELLOW}
        ).scale(0.6).next_to(moda_ejemplo, DOWN)
        self.play(Write(moda_prop))
        
        self.wait(4)
        self.play(FadeOut(moda_titulo, moda_def, moda_ejemplo, moda_prop))

        # Comparación y Uso
        comparacion_titulo = Text("Comparación y Uso").to_edge(UP)
        self.play(Write(comparacion_titulo))
        
        comparacion_text = Text(
            "- Media: Ideal cuando los datos no tienen outliers significativos.\n"
            "- Mediana: Útil cuando los datos tienen outliers o están sesgados.\n"
            "- Moda: Principalmente para datos categóricos para identificar la categoría más frecuente.",
            t2c={"Media:": YELLOW, "Mediana:": YELLOW, "Moda:": YELLOW}
        ).scale(0.6).next_to(comparacion_titulo, DOWN)
        self.play(Write(comparacion_text))
        
        self.wait(4)
        self.play(FadeOut(comparacion_titulo, comparacion_text))

        # Ejemplo Comparativo
        ejemplo_titulo = Text("Ejemplo Comparativo").to_edge(UP)
        self.play(Write(ejemplo_titulo))
        
        ejemplo_text = Text(
            "Supongamos que tenemos el siguiente conjunto de datos que representa las notas de un examen: 55, 60, 65, 70, 75, 80, 85, 90, 95, 100.",
            t2c={"Supongamos": YELLOW}
        ).scale(0.6).next_to(ejemplo_titulo, DOWN)
        self.play(Write(ejemplo_text))
        
        media_ejemplo = MathTex(
            r"\overline{x} = \frac{55 + 60 + 65 + 70 + 75 + 80 + 85 + 90 + 95 + 100}{10} = \frac{775}{10} = 77.5"
        ).scale(0.8).next_to(ejemplo_text, DOWN)
        self.play(Write(media_ejemplo))
        
        mediana_ejemplo = Text(
            "Mediana:\n- Número de datos \( n = 10 \) (par), la mediana es el promedio de los dos valores centrales (75 y 80):\n"
            r"\[ \text{Mediana} = \frac{75 + 80}{2} = 77.5 \]",
            t2c={"Mediana:": YELLOW}
        ).scale(0.6).next_to(media_ejemplo, DOWN)
        self.play(Write(mediana_ejemplo))
        
        moda_ejemplo = Text(
            "Moda:\n- No hay ningún valor que se repita, por lo que no hay moda.",
            t2c={"Moda:": YELLOW}
        ).scale(0.6).next_to(mediana_ejemplo, DOWN)
        self.play(Write(moda_ejemplo))
        
        self.wait(4)
        self.play(FadeOut(ejemplo_titulo, ejemplo_text, media_ejemplo, mediana_ejemplo, moda_ejemplo))
        
        # Ejemplo con Valor Extremo
        ejemplo_extremo_titulo = Text("Ejemplo con Valor Extremo").to_edge(UP)
        self.play(Write(ejemplo_extremo_titulo))
        
        ejemplo_extremo_text = Text(
            "Supongamos ahora que añadimos un valor extremo, por ejemplo, 500.",
            t2c={"Supongamos": YELLOW}
        ).scale(0.6).next_to(ejemplo_extremo_titulo, DOWN)
        self.play(Write(ejemplo_extremo_text))
        
        media_extremo = MathTex(
            r"\overline{x} = \frac{55 + 60 + 65 + 70 + 75 + 80 + 85 + 90 + 95 + 100 + 500}{11} = \frac{1275}{11} \approx 115.91"
        ).scale(0.8).next_to(ejemplo_extremo_text, DOWN)
        self.play(Write(media_extremo))
        
        mediana_extremo = Text(
            "Mediana:\n- Ordenando los datos: 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 500.\n"
            "- Número de datos \( n = 11 \) (impar), la mediana es el sexto valor: 80.",
            t2c={"Mediana:": YELLOW}
        ).scale(0.6).next_to(media_extremo, DOWN)
        self.play(Write(mediana_extremo))
        
        moda_extremo = Text(
            "Moda:\n- Sigue sin haber ningún valor que se repita, por lo que no hay moda.",
            t2c={"Moda:": YELLOW}
        ).scale(0.6).next_to(mediana_extremo, DOWN)
        self.play(Write(moda_extremo))
        
        self.wait(4)
        self.play(FadeOut(ejemplo_extremo_titulo, ejemplo_extremo_text, media_extremo, mediana_extremo, moda_extremo))
        
        conclusion_text = Text(
            "En este caso, se puede observar cómo la media se ve afectada por el valor extremo, mientras que la mediana permanece más representativa del conjunto central de los datos.",
            #t2c={"media": YELLOW, "mediana": YELLOW}
        ).scale(0.6).to_edge(DOWN)
        self.play(Write(conclusion_text))
        self.wait(4)