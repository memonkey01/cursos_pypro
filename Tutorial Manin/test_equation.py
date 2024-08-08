from manim import *

class displayEquations(Scene):
    def construct(self):
        # Create Tex objects
        first_line = Text('Manim also allows you')
        second_line = Text('to show beautiful math equations')
        equation = Tex('\( x_1, x_2, \ldots, x_n \)')
        equation2 = MathTex(r'\text{Media} (\overline{x}) = \frac{1}{n} \sum_{i=1}^{n} x_i')
        
        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text and equation
        self.play(Write(first_line), Write(second_line))
        self.wait(2)
        self.play(ReplacementTransform(first_line, equation), FadeOut(second_line))
        self.wait(3)
        self.play(ReplacementTransform(equation, equation2))
        self.wait(3)

"""
Las medidas de tendencia central son valores que representan un punto central o típico de un conjunto de datos. Estas medidas son fundamentales en estadística y econometría, ya que proporcionan una idea general de dónde se encuentran los datos. Las principales medidas de tendencia central son la media, la mediana y la moda. A continuación, se explica cada una de ellas en detalle:

### Media (Promedio)

#### Definición:
La media aritmética de un conjunto de datos es el valor que se obtiene sumando todos los datos y dividiéndolos entre el número total de datos.

#### Fórmula:
Para un conjunto de datos \( x_1, x_2, \ldots, x_n \):
\[ \text{Media} (\overline{x}) = \frac{1}{n} \sum_{i=1}^{n} x_i \]

#### Ejemplo:
Si tienes los datos: 2, 4, 6, 8, 10
\[ \overline{x} = \frac{2 + 4 + 6 + 8 + 10}{5} = \frac{30}{5} = 6 \]

#### Propiedades:
- La media es sensible a valores extremos (outliers). Un valor extremadamente alto o bajo puede distorsionar significativamente la media.
- Se utiliza para datos cuantitativos.

### Mediana

#### Definición:
La mediana es el valor que divide el conjunto de datos en dos partes iguales, es decir, el 50% de los datos están por debajo de la mediana y el 50% están por encima.

#### Método de Cálculo:
1. Ordenar los datos de menor a mayor.
2. Si el número de datos \( n \) es impar, la mediana es el valor central.
3. Si el número de datos \( n \) es par, la mediana es el promedio de los dos valores centrales.

#### Ejemplo:
Para los datos ordenados 2, 4, 6, 8, 10:
- Como hay 5 datos (impar), la mediana es el tercer valor: 6.
Para los datos ordenados 2, 4, 6, 8:
- Como hay 4 datos (par), la mediana es el promedio de los dos valores centrales: \( \frac{4 + 6}{2} = 5 \).

#### Propiedades:
- La mediana no es afectada por valores extremos, lo que la hace una medida robusta.
- Es útil para datos ordinales y cuantitativos.

### Moda

#### Definición:
La moda es el valor que aparece con mayor frecuencia en un conjunto de datos.

#### Ejemplo:
Para los datos 2, 4, 4, 6, 8:
- La moda es 4, ya que aparece dos veces, más que cualquier otro valor.

#### Propiedades:
- Puede haber más de una moda (bimodal, multimodal) o ninguna moda (si todos los valores son únicos).
- Es útil para datos cualitativos y cuantitativos.

### Comparación y Uso

- **Media**: Es la medida más comúnmente utilizada y es ideal cuando los datos no tienen outliers significativos. Se utiliza en cálculos posteriores y en la inferencia estadística.
- **Mediana**: Es útil cuando los datos tienen outliers o están sesgados, ya que proporciona una medida más representativa del centro de los datos en estos casos.
- **Moda**: Se utiliza principalmente para datos categóricos para identificar la categoría más frecuente, y en datos cuantitativos cuando se desea conocer el valor más común.

### Ejemplo Comparativo

Supongamos que tenemos el siguiente conjunto de datos que representa las notas de un examen: 55, 60, 65, 70, 75, 80, 85, 90, 95, 100.

- **Media**:
  \[ \overline{x} = \frac{55 + 60 + 65 + 70 + 75 + 80 + 85 + 90 + 95 + 100}{10} = \frac{775}{10} = 77.5 \]

- **Mediana**:
  - Ordenando los datos (ya están ordenados).
  - Número de datos \( n = 10 \) (par), la mediana es el promedio de los dos valores centrales (75 y 80):
  \[ \text{Mediana} = \frac{75 + 80}{2} = 77.5 \]

- **Moda**:
  - No hay ningún valor que se repita, por lo que no hay moda.

Supongamos ahora que añadimos un valor extremo, por ejemplo, 500:

- **Media**:
  \[ \overline{x} = \frac{55 + 60 + 65 + 70 + 75 + 80 + 85 + 90 + 95 + 100 + 500}{11} = \frac{1275}{11} \approx 115.91 \]

- **Mediana**:
  - Ordenando los datos: 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 500.
  - Número de datos \( n = 11 \) (impar), la mediana es el sexto valor:
  \[ \text{Mediana} = 80 \]

- **Moda**:
  - Sigue sin haber ningún valor que se repita, por lo que no hay moda.

En este caso, se puede observar cómo la media se ve afectada por el valor extremo, mientras que la mediana permanece más representativa del conjunto central de los datos.
"""