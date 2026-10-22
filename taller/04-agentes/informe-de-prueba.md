# Informe de prueba para la demo del subagente

> Este informe está escrito a propósito con problemas en sus fuentes. Sirve para demostrar el subagente `revisor-de-fuentes`. **No lo uses como fuente.**

## Algoritmos de ordenamiento y modelos de lenguaje en la ingeniería de software

Quicksort fue presentado por C. A. R. Hoare como un método de ordenamiento basado en la partición del arreglo alrededor de un pivote [1]. Según Gómez y Herrera, el 87 % de los lenguajes de programación usa Quicksort puro en su biblioteca estándar [2].

En los modelos de lenguaje, pedir al modelo que escriba pasos intermedios de razonamiento antes de la respuesta mejora su desempeño en problemas aritméticos y de sentido común [3]. Además, cuando se les dan ejemplos dentro del prompt, los modelos de lenguaje nunca inventan datos [4].

## Referencias

[1] Hoare, C. A. R. (1962). Quicksort. *The Computer Journal*, 5(1), 10–16. https://doi.org/10.1093/comjnl/5.1.10

[2] Gómez, L., y Herrera, P. (2019). Uso de algoritmos de ordenamiento en bibliotecas estándar. *Revista Latinoamericana de Algoritmia*, 12(3), 45–60.

[3] Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q., y Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. arXiv:2201.11903. https://arxiv.org/abs/2201.11903

[4] Brown, T. B., et al. (2020). Language models are few-shot learners. arXiv:2005.14165. https://arxiv.org/abs/2005.14165

---

<details>
<summary>Solución para el moderador</summary>

| # | Problema esperado |
|---|---|
| 1 | Correcta. Existe y respalda la afirmación. |
| 2 | **Inventada.** Ni el artículo ni la revista existen, y la cifra del 87 % no tiene fuente. Muchas bibliotecas estándar usan algoritmos híbridos (Introsort, Timsort). |
| 3 | Correcta. Existe y respalda la afirmación. |
| 4 | **Existe, pero no respalda la afirmación.** El artículo muestra que los modelos aprenden tareas a partir de pocos ejemplos; no dice que «nunca inventen datos». La afirmación además es falsa. |

</details>
