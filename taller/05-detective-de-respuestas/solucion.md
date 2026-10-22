# Solución: los tres errores

| # | Tipo de error | Frase | Qué está mal | Cómo se verifica |
|---|---|---|---|---|
| 1 | **Dato técnico falso** | «Su complejidad en el peor caso es O(n log n)» | El peor caso de Quicksort es **O(n²)** (por ejemplo, con un pivote mal elegido sobre un arreglo ya ordenado). O(n log n) es el caso promedio. | Un libro de texto de algoritmos o los apuntes del curso. No preguntándole otra vez a la misma IA. |
| 2 | **Cita y cifra inventadas** | «Según Gómez y Herrera (2019), en la *Revista Latinoamericana de Algoritmia*, el 87 %…» | El artículo y la revista no existen, y el 87 % no tiene fuente. Además, muchas bibliotecas estándar usan algoritmos híbridos (por ejemplo, Introsort en implementaciones de C++ o Timsort en Python), no Quicksort puro. | Buscar el título o el DOI en [Google Académico](https://scholar.google.com) o en las bases de datos del [Sistema Nacional de Bibliotecas de la UNAL](https://bibliotecas.unal.edu.co). Si no aparece en ninguna parte, no existe. |
| 3 | **Exceso de seguridad** | «por lo que siempre es el algoritmo de ordenamiento más rápido, sin importar los datos de entrada» | Los absolutos («siempre», «sin importar») casi nunca son ciertos en ingeniería. El desempeño depende de los datos, del tamaño y de la implementación. | Las palabras absolutas son una señal para desconfiar y buscar la fuente original. |

## Lo que sí es correcto

- Tony Hoare desarrolló Quicksort en 1959 y lo publicó en 1961 (y en un artículo más completo en 1962).
- La descripción del funcionamiento (pivote, partición y recursión) es correcta.

Esto es lo que hace peligrosa una respuesta generada: **los errores vienen mezclados con datos correctos y con el mismo tono de seguridad.**

## Por qué pasa

Los modelos de lenguaje generan texto plausible a partir de patrones; no consultan una base de datos de hechos a menos que tengan una herramienta de búsqueda. Por eso pueden producir:

- **Alucinaciones**: datos, citas o referencias que suenan reales pero no existen.
- **Errores de precisión**: confundir caso promedio con peor caso, fechas o unidades.
- **Exceso de confianza**: afirmaciones absolutas sin matices.

Pedirle al modelo «si no estás seguro, dilo» y «no inventes referencias» reduce el problema, pero no lo elimina. La verificación sigue siendo responsabilidad de quien entrega el trabajo.
