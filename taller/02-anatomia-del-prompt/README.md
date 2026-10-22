# Actividad 2. Anatomía del prompt

**Duración:** 25 minutos (teoría 8, laboratorio 12, comparación en parejas 5) · **Objetivo:** estructura y formatos del prompt

Se presentan las seis piezas que componen un buen prompt y cinco formatos para escribirlo. Luego, en laboratorio, cada asistente reescribe el prompt de la [Actividad 1](../01-el-mismo-pedido) en tres versiones, cambiando una sola variable a la vez, para ver qué aporta cada pieza al resultado.

## Archivos de esta carpeta

| Archivo | Para qué sirve |
|---|---|
| [`plantilla-seis-piezas.md`](plantilla-seis-piezas.md) | Plantilla para copiar y llenar con tu propio pedido |
| [`ejemplos-por-formato.md`](ejemplos-por-formato.md) | El mismo pedido escrito en los cinco formatos |
| [`laboratorio.md`](laboratorio.md) | Hoja de trabajo del laboratorio y preguntas para la comparación en parejas |

## Las seis piezas

| Pieza | Qué responde | Ejemplo |
|---|---|---|
| **Rol** | ¿Quién debe ser el modelo? | «Actúa como monitor de Cálculo Diferencial con experiencia explicando a estudiantes de primer semestre.» |
| **Contexto** | ¿Para quién es, para qué sirve, con qué información se cuenta? | «Es para una exposición de 10 minutos en clase; el público son compañeros que no han visto el tema.» |
| **Tarea** | ¿Qué hay que hacer exactamente? (verbo + entregable) | «Escribe el contenido de 8 diapositivas sobre la regla de la cadena.» |
| **Formato** | ¿Cómo debe verse la respuesta? | «Por cada diapositiva: título, máximo 3 viñetas y una nota para el expositor.» |
| **Restricciones** | ¿Qué límites hay y qué no debe hacer? | «Sin demostraciones formales; máximo 15 palabras por viñeta; si no estás seguro de un dato, dilo.» |
| **Ejemplos** | ¿Cómo se ve algo bien hecho? | Una diapositiva escrita por ti, con tu voz. |

No todos los prompts necesitan las seis piezas. Una pregunta rápida funciona bien en una línea. Pero cuando el resultado importa (algo que vas a entregar, exponer o reutilizar), cada pieza que falta es una decisión que el modelo toma por ti.

## Los cinco formatos

| Formato | Cuándo conviene |
|---|---|
| **Lenguaje natural** | Pedidos cortos y conversacionales |
| **Markdown** (títulos y viñetas) | Prompts largos que se quieren ordenar por secciones |
| **Etiquetas XML** (`<contexto>`, `<tarea>`, `<ejemplo>`) | Cuando se mezclan instrucciones con documentos o datos, para que el modelo no los confunda |
| **JSON** | Cuando la salida la va a leer un programa o se necesita una estructura exacta |
| **Few-shot** | Cuando es más fácil mostrar que explicar: se dan de uno a tres ejemplos de entrada y salida |

Los cinco formatos aplicados al mismo pedido están en [`ejemplos-por-formato.md`](ejemplos-por-formato.md).

## Antes y después

**Antes:**

```text
Hazme una presentación sobre la regla de la cadena.
```

**Después (con etiquetas XML):**

```xml
<rol>Monitor de Cálculo Diferencial de la UNAL.</rol>

<contexto>
Exposición de 10 minutos para compañeros de primer semestre
que no han visto el tema.
</contexto>

<tarea>Escribe el contenido de 8 diapositivas sobre la regla de la cadena.</tarea>

<formato>
Por diapositiva: título, máximo 3 viñetas y una nota para el expositor.
</formato>

<restricciones>
Sin demostraciones formales. Máximo 15 palabras por viñeta.
Si no estás seguro de un dato, dilo.
</restricciones>

<ejemplo>
Diapositiva 1: «¿Funciones dentro de funciones?»
- Piensa en una muñeca rusa: una función guarda a otra.
</ejemplo>
```

## Pasos del laboratorio

1. Abre [`laboratorio.md`](laboratorio.md).
2. Reescribe tu prompt de la Actividad 1 en tres versiones, **cada una en un chat nuevo** para que el contexto anterior no influya:
   - **Versión 1:** el mismo pedido en lenguaje natural, pero con las seis piezas.
   - **Versión 2:** la misma información de la versión 1, organizada con etiquetas XML o Markdown (solo cambia el formato).
   - **Versión 3:** la versión 2 más un ejemplo propio.
3. Anota en una línea qué cambió en el resultado entre una versión y la siguiente.
4. En parejas, comparen resultados con las preguntas guía del laboratorio.

## Notas para el moderador

- Pedir que cambien **una sola variable por vez** para que puedan atribuir cada mejora a una pieza concreta.
- Al cerrar, conectar con la Actividad 3: si cada vez hay que repetir todo este contexto, conviene guardarlo en una Skill.
- Para profundizar: [guía de prompt engineering](../../guias/01-prompt-engineering.md).
