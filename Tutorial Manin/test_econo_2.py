from manim import *

class EconometricsVideo(Scene):
    def construct(self):
        # Intro
        title = Text("¿Qué es la econometría?").scale(1.5)
        self.play(Write(title))
        self.wait(3)
        
        econometrics_text = Text("""
        La econometría es un subdominio de la economía que aplica \n
        modelos matemáticos y estadísticos junto con teorías económicas \n
        para entender, explicar y medir la causalidad en los sistemas económicos.
        """, t2c={"econometría": BLUE, "modelos matemáticos": YELLOW, "estadísticos": YELLOW}).scale(0.5)
        
        self.play(ReplacementTransform(title, econometrics_text))
        self.wait(3)
        
        hypothesis_text = Text("""
        Con la econometría, uno puede plantear una hipótesis \n
        de que la duración de la educación tiene un impacto \n
        positivo en las tasas salariales; luego calificar esta \n
        relación con la teoría económica; y finalmente formalizar esa relación cuantitativamente.
        """, t2c={"hipótesis": BLUE, "teoría económica": YELLOW, "cuantitativamente": YELLOW}).scale(0.5)
        
        self.play(ReplacementTransform(econometrics_text, hypothesis_text))
        self.wait(3)
        
        self.play(FadeOut(hypothesis_text))
        
        # Métodos de Econometría
        title = Text("Métodos de Econometría").scale(1.5)
        self.play(Write(title))
        self.wait(3)
        
        methods_text = Text("""
        Agrupé los métodos de econometría en cuatro categorías: estadísticas descriptivas, pruebas de hipótesis, regresión y pronósticos.
        """, t2c={"estadísticas descriptivas": BLUE, "pruebas de hipótesis": YELLOW, "regresión": GREEN, "pronósticos": RED}).scale(0.7)
        
        self.play(ReplacementTransform(title, methods_text))
        self.wait(3)
        
        self.play(FadeOut(methods_text))
        
        # Estadísticas Descriptivas
        title = Text("Estadísticas Descriptivas").scale(1.5)
        self.play(Write(title))
        self.wait(3)
        
        desc_stats_text = Tex(r"which means that", r"$\frac{\pi}{2}\thickapprox 1.5707$", color=RED).scale(0.7)
        
        self.play(ReplacementTransform(title, desc_stats_text))
        self.wait(3)
        
        self.play(FadeOut(desc_stats_text))
        
        # Pruebas de Hipótesis
        title = Text("Pruebas de Hipótesis").scale(1.5)
        self.play(Write(title))
        self.wait(3)
        
        hypothesis_text = Text("""
        Las pruebas de hipótesis se utilizan para determinar si existe suficiente evidencia en una muestra de datos para inferir que una condición es verdadera para toda la población.
        """, t2c={"pruebas de hipótesis": BLUE, "evidencia": YELLOW, "muestra de datos": GREEN, "población": RED}).scale(0.7)
        
        self.play(ReplacementTransform(title, hypothesis_text))
        self.wait(3)
        
        self.play(FadeOut(hypothesis_text))
        
        # Regresión
        title = Text("Regresión").scale(1.5)
        self.play(Write(title))
        self.wait(3)
        
        regression_text = Text("""
        La regresión es una técnica estadística que se utiliza para modelar y analizar la relación entre una variable dependiente y una o más variables independientes.
        """, t2c={"regresión": BLUE, "variable dependiente": YELLOW, "variables independientes": GREEN}).scale(0.7)
        
        self.play(ReplacementTransform(title, regression_text))
        self.wait(3)
        
        regression_eq = MathTex(r"y = \beta_0 + \beta_1 x + \epsilon")
        self.play(ReplacementTransform(regression_text, regression_eq))
        self.wait(3)
        
        self.play(FadeOut(regression_eq))
        
        # Pronósticos
        title = Text("Pronósticos").scale(1.5)
        self.play(Write(title))
        self.wait(3)
        
        forecast_text = Text("""
        Los pronósticos implican el uso de modelos estadísticos para predecir futuros valores de una variable basada en sus valores históricos.
        """, t2c={"pronósticos": BLUE, "modelos estadísticos": YELLOW, "valores históricos": GREEN}).scale(0.7)
        
        self.play(ReplacementTransform(title, forecast_text))
        self.wait(3)
        
        self.play(FadeOut(forecast_text))

# To render the video, run the following command in your terminal:
# manim -pql econometrics_video.py EconometricsVideo
