# Guía de prompt engineering

Esta guía amplía lo que se ve en las actividades 1 y 2 del taller. Está pensada para leerse en unos 30 minutos y para volver a ella como referencia.

## Contenido

1. [Qué es el prompt engineering](#1-qué-es-el-prompt-engineering)
2. [Lo mínimo que hay que saber de un LLM](#2-lo-mínimo-que-hay-que-saber-de-un-llm)
3. [Principios](#3-principios)
4. [Las seis piezas de un prompt](#4-las-seis-piezas-de-un-prompt)
5. [Técnicas](#5-técnicas)
6. [Trabajar con documentos y contexto largo](#6-trabajar-con-documentos-y-contexto-largo)
7. [Iterar y evaluar un prompt](#7-iterar-y-evaluar-un-prompt)
8. [Errores comunes](#8-errores-comunes)
9. [Recetas para estudiantes](#9-recetas-para-estudiantes)
10. [Del prompt al contexto](#10-del-prompt-al-contexto)
11. [Para seguir aprendiendo](#11-para-seguir-aprendiendo)

---

## 1. Qué es el prompt engineering

El **prompt engineering** es la práctica de diseñar, probar y mejorar las instrucciones que se le dan a un modelo de lenguaje para obtener resultados útiles y consistentes.

La palabra «ingeniería» no es exagerada: un buen prompt se diseña con un objetivo, se prueba contra casos concretos, se mide y se ajusta. Escribir un prompt es más parecido a escribir la especificación de un sistema que a hacer una búsqueda en Google.

No se trata de trucos ni de frases mágicas. Los modelos actuales entienden muy bien el lenguaje natural; lo que no pueden hacer es **adivinar lo que no se les dice**: para quién es el resultado, qué nivel de detalle se espera, qué formato sirve, qué ya se sabe y qué no. La mayor parte del prompt engineering consiste en darle al modelo ese contexto de forma clara.

## 2. Lo mínimo que hay que saber de un LLM

No hace falta entender las matemáticas de un modelo de lenguaje para escribir buenos prompts, pero sí estos siete hechos:

| Hecho | Qué implica para tus prompts |
|---|---|
| **Predice texto.** Un LLM genera la respuesta pieza por pieza, eligiendo lo que es más probable que siga, según lo que aprendió y lo que hay en la conversación. | Si no das contexto, el modelo rellena con lo más típico. Por eso las respuestas sin contexto suenan genéricas. |
| **Trabaja con tokens.** El texto se divide en fragmentos (tokens), que son aproximadamente partes de palabras. Los límites y los costos se miden en tokens. | Un prompt más largo no es mejor por ser largo: cada token compite por la atención del modelo. |
| **Tiene una ventana de contexto.** Solo «ve» lo que cabe en la conversación actual: tus mensajes, sus respuestas, los archivos y las instrucciones del sistema. | Lo que dijiste hace 50 mensajes puede perder peso. Para tareas nuevas, empieza un chat nuevo. |
| **No recuerda entre conversaciones** (salvo funciones de memoria o proyectos que lo hacen explícitamente). | No asumas que sabe lo que le contaste ayer. |
| **Tiene una fecha de corte.** Su conocimiento llega hasta cierta fecha. | Para información reciente, usa la búsqueda web o dale tú la información. |
| **Puede equivocarse con mucha seguridad.** No distingue por sí mismo entre un dato que «sabe» y uno que suena plausible. | Verifica datos, cifras y referencias. Pídele que diga cuando no esté seguro. |
| **Puede usar herramientas** (buscar en la web, ejecutar código, leer archivos) cuando la aplicación se las da. | Si la tarea requiere datos actuales o cálculos exactos, pide que use la herramienta adecuada. |

## 3. Principios

### 3.1 Escribe como si le hablaras a un colega brillante que acaba de llegar

La documentación de Anthropic lo resume así: imagina que tu prompt lo va a leer una persona muy capaz, pero que no sabe nada de tu situación. Si esa persona necesitaría hacerte preguntas para hacer bien el trabajo, al modelo le falta lo mismo.

Prueba rápida: muéstrale tu prompt a un compañero. Si se confunde, el modelo probablemente también.

### 3.2 Explica el porqué

Una instrucción con su razón funciona mejor que una instrucción sola, porque el modelo puede generalizar a casos que no previste.

| Menos efectivo | Más efectivo |
|---|---|
| «No uses fórmulas.» | «No uses fórmulas: el público es de primer semestre y se pierde cuando ve notación antes de entender la idea.» |
| «Responde corto.» | «Responde en máximo tres frases: lo voy a leer en el celular entre clases.» |

### 3.3 Sé específico sobre el resultado

Las palabras vagas («bueno», «completo», «creativo», «profesional») significan cosas distintas para cada persona. Cámbialas por criterios observables:

- «Que sea completo» → «Que cubra definición, un ejemplo resuelto y dos errores comunes.»
- «Que sea creativo» → «Que abra con una analogía de la vida diaria en Bogotá.»
- «Profesional» → «Tono formal, sin tuteo, como un correo a la decanatura.»

### 3.4 Di qué hacer, no solo qué evitar

«No uses viñetas» deja al modelo adivinando qué hacer en su lugar. «Escribe en párrafos de prosa continua» es directo. Las restricciones negativas sirven, pero acompáñalas de la alternativa.

### 3.5 Muestra en lugar de describir

Un ejemplo vale más que un párrafo de instrucciones de estilo. Si tienes algo hecho por ti que muestre el tono, el nivel o la estructura, inclúyelo. Ojo: el modelo copia los ejemplos con bastante fidelidad, así que si das uno solo, puede imitarlo demasiado. Con dos o tres ejemplos variados aprende el patrón sin calcarlo.

### 3.6 Dale permiso para no saber

Frases como «si no estás seguro, dilo» o «si la información no está en el documento, responde que no está» reducen las respuestas inventadas. No las eliminan, pero ayudan.

### 3.7 Separa instrucciones de material

Cuando pegas apuntes, un enunciado o un documento junto con las instrucciones, delimita cada cosa (con etiquetas XML, títulos o comillas triples) para que el modelo no confunda lo que tiene que hacer con el texto que tiene que procesar.

## 4. Las seis piezas de un prompt

| Pieza | Qué responde |
|---|---|
| **Rol** | ¿Quién debe ser el modelo? |
| **Contexto** | ¿Para quién es, para qué sirve, qué información hay? |
| **Tarea** | ¿Qué hay que hacer exactamente? |
| **Formato** | ¿Cómo debe verse la respuesta? |
| **Restricciones** | ¿Qué límites hay? ¿Qué no debe hacer? |
| **Ejemplos** | ¿Cómo se ve algo bien hecho? |

El detalle de cada pieza, los cinco formatos (lenguaje natural, Markdown, XML, JSON y few-shot) y una plantilla están en [`taller/02-anatomia-del-prompt`](../taller/02-anatomia-del-prompt).

Sobre el **rol**: ayuda a fijar el nivel y el enfoque («profesor de primer semestre» explica distinto que «revisor de una revista»), pero por sí solo no hace magia. Un rol sin contexto produce una respuesta genérica con otro tono. Lo que más cambia el resultado suele ser el contexto.

## 5. Técnicas

### 5.1 Zero-shot y few-shot

- **Zero-shot:** pedir la tarea sin ejemplos. Funciona bien para tareas comunes y bien descritas.
- **Few-shot:** incluir de uno a cinco ejemplos de entrada y salida antes del caso real. Útil cuando el formato o el estilo son difíciles de describir. La técnica se popularizó con el artículo de GPT-3, que mostró que los modelos grandes aprenden tareas nuevas a partir de unos pocos ejemplos en el prompt ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)).

Consejos para los ejemplos:

- Que sean **variados** (no tres casi iguales) y que cubran algún caso difícil.
- Que estén **delimitados** (por ejemplo, dentro de etiquetas `<ejemplo>`).
- Que sean **correctos**: el modelo copia también los errores.

### 5.2 Pedir razonamiento antes de la respuesta (chain of thought)

Para problemas con varios pasos (matemáticas, lógica, análisis, depuración), pedirle al modelo que razone antes de responder mejora los resultados. Es la técnica conocida como *chain of thought* ([Wei et al., 2022](https://arxiv.org/abs/2201.11903)); incluso la frase «pensemos paso a paso» produce mejoras en muchos casos ([Kojima et al., 2022](https://arxiv.org/abs/2205.11916)).

```text
Resuelve el ejercicio. Primero, dentro de <razonamiento>, plantea qué se
pide, qué datos hay y qué método aplica. Luego, dentro de <respuesta>,
da solo el resultado final con sus unidades.
```

Muchos modelos actuales tienen un modo de **razonamiento extendido** («thinking») que hace esto internamente. Si lo tienes activado, no hace falta pedirlo; basta con indicar que el problema requiere análisis cuidadoso. En cualquier caso, **el razonamiento escrito no garantiza que la respuesta sea correcta**: revisa los pasos.

### 5.3 Encadenar prompts (prompt chaining)

Una tarea grande se divide en pasos, y la salida de cada paso es la entrada del siguiente. Cada prompt es más simple y cada resultado se puede revisar antes de seguir.

```
1. «Extrae de estos apuntes los conceptos clave y sus definiciones.»
        ↓ (revisas la lista)
2. «Con estos conceptos, propón la estructura de una guía de estudio.»
        ↓ (ajustas la estructura)
3. «Escribe la sección 1 de la guía siguiendo esta estructura.»
```

Es más lento que un solo prompt gigante, pero mucho más controlable. Si repites la misma cadena con frecuencia, conviértela en una [Skill](02-skills.md).

### 5.4 Salidas estructuradas

Cuando la respuesta la va a leer un programa, pide un formato exacto (JSON, CSV, una tabla con columnas fijas) y muestra el esquema. Si usas la API, prefiere las funciones de **salidas estructuradas** que ofrecen los proveedores: el modelo queda obligado a respetar el esquema y no hay que confiar solo en la instrucción.

### 5.5 Autoevaluación y revisión

Pedirle al modelo que revise su propia respuesta con criterios concretos atrapa algunos errores:

```text
Revisa la respuesta anterior con esta lista:
1. ¿Cada afirmación numérica tiene una fuente?
2. ¿Hay alguna palabra absoluta (siempre, nunca, todos) que deba matizarse?
3. ¿Respondiste exactamente lo que pregunté?
Corrige lo que no cumpla y dime qué cambiaste.
```

Funciona mejor en un chat nuevo o con criterios explícitos. No reemplaza la verificación en fuentes externas.

### 5.6 Autoconsistencia

Para preguntas con una respuesta única (un cálculo, una clasificación), generar varias respuestas independientes y quedarse con la más frecuente mejora la precisión ([Wang et al., 2022](https://arxiv.org/abs/2203.11171)). Manualmente: pregunta lo mismo en dos o tres chats nuevos y compara. Si las respuestas no coinciden, es señal de que el modelo no está seguro.

### 5.7 Razonar y actuar (ReAct)

Es el patrón base de los agentes: el modelo alterna entre **pensar** qué hacer, **actuar** con una herramienta (buscar, ejecutar código) y **observar** el resultado, hasta terminar ([Yao et al., 2022](https://arxiv.org/abs/2210.03629)). Lo usas cada vez que una aplicación busca en la web o ejecuta código por ti. Más en la [guía de agentes](03-agentes-especializados.md).

### 5.8 Que el modelo te pregunte

Para tareas con muchas decisiones, invierte el orden:

```text
Quiero preparar un plan de estudio para el parcial de Física II.
Antes de proponer nada, hazme las preguntas que necesites (máximo cinco)
para que el plan se ajuste a mí.
```

Es la idea detrás de Skills populares como [`grill-me`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me), que entrevistan al usuario antes de actuar.

### 5.9 Metaprompting

Puedes pedirle al modelo que te ayude a escribir el prompt: «Quiero que un modelo haga X para Y. Escríbeme el prompt, con las seis piezas, y dime qué información te falta». Anthropic ofrece un [generador de prompts](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/metaprompt.ipynb) basado en esta idea. Úsalo como borrador y ajústalo con lo que sabes de tu caso.

## 6. Trabajar con documentos y contexto largo

Cuando le das al modelo documentos largos (un artículo, un PDF de apuntes, un enunciado extenso):

1. **Pon el documento primero y la pregunta al final.** En prompts largos, las instrucciones al final suelen seguirse mejor.
2. **Delimita cada documento** con etiquetas y metadatos:

   ```xml
   <documentos>
     <documento indice="1">
       <fuente>Apuntes de clase, semana 5</fuente>
       <contenido>…</contenido>
     </documento>
     <documento indice="2">
       <fuente>Capítulo 3 del libro guía</fuente>
       <contenido>…</contenido>
     </documento>
   </documentos>

   Usando solo los documentos anteriores, explica…
   ```

3. **Pide citas textuales** antes del análisis: «Primero extrae, entre `<citas>`, los fragmentos relevantes; luego responde basándote solo en ellos». Así es más fácil comprobar de dónde sale cada afirmación.
4. **Limita la respuesta al material:** «Si algo no está en los documentos, dilo; no completes con conocimiento general».

## 7. Iterar y evaluar un prompt

Un prompt rara vez sale bien al primer intento. Un proceso sencillo:

1. **Define qué es un buen resultado** antes de escribir el prompt. Por ejemplo: «8 diapositivas, máximo 3 viñetas, ningún dato sin fuente, que suene a mí».
2. **Prepara dos o tres casos de prueba** (temas, entradas o preguntas distintas).
3. **Cambia una sola cosa a la vez** y compara con la versión anterior. Si cambias tres cosas y mejora, no sabrás cuál funcionó.
4. **Prueba en chats nuevos** para que la conversación previa no influya.
5. **Guarda las versiones** que funcionan, con una nota de qué cambiaste y por qué. Un archivo de texto o un repositorio sirven.
6. **Cuando un prompt funciona y lo repites**, conviértelo en una plantilla o en una Skill.

## 8. Errores comunes

| Error | Ejemplo | Mejor |
|---|---|---|
| Pedir sin contexto | «Explícame las integrales.» | Decir nivel, para qué, qué ya sabes y qué no entiendes. |
| Varias tareas en un solo prompt | «Resume, traduce, corrige y haz un quiz.» | Encadenar prompts o numerar las tareas y el formato de cada una. |
| Instrucciones contradictorias | «Sé breve pero muy detallado.» | Elegir: «Máximo 200 palabras, priorizando X sobre Y». |
| Palabras vagas | «Hazlo mejor.» | «Reduce a la mitad, quita la jerga y agrega un ejemplo.» |
| Seguir corrigiendo en un chat larguísimo | 40 mensajes de ajustes | Empezar un chat nuevo con un prompt que incluya todo lo aprendido. |
| Confiar en referencias generadas | Copiar la bibliografía que dio el modelo | Verificar cada referencia (ver la [lista de verificación](../taller/05-detective-de-respuestas/lista-de-verificacion.md)). |
| Pegar datos personales | Listas con nombres, documentos y notas | Anonimizar o no hacerlo (ver el [marco normativo](../taller/06-marco-normativo-unal)). |
| Delegar el pensamiento | «Hazme el taller.» | Usar la IA para entender, practicar y revisar; el trabajo entregado debe ser tuyo y declarado. |

## 9. Recetas para estudiantes

Estas plantillas están pensadas para **aprender** con la IA, no para que haga el trabajo por ti. Ajústalas a tu caso.

### Entender un tema

```text
Soy estudiante de [semestre] de [carrera] en la UNAL. Estoy viendo [tema]
en [materia]. Ya entiendo [lo que sí entiendes], pero no entiendo [la duda
concreta].

Explícamelo con un ejemplo cotidiano primero y luego con el formalismo.
Al final, hazme dos preguntas para comprobar si entendí. No me des las
respuestas hasta que yo conteste.
```

### Tutor socrático

```text
Actúa como tutor socrático de [materia]. Quiero resolver este ejercicio
yo mismo: [ejercicio].

No me des la solución. Hazme una pregunta a la vez que me guíe al
siguiente paso. Si me equivoco, señala dónde sin corregirlo por mí.
```

### Practicar para un parcial

```text
Genera 5 preguntas de práctica sobre [temas] con el nivel de un parcial de
[materia] en la UNAL: 2 conceptuales, 2 de ejercicio y 1 de análisis.
Dame solo las preguntas. Cuando te envíe mis respuestas, califícalas con
retroalimentación concreta.
```

### Entender un error de código

```text
Estoy aprendiendo [lenguaje]. Este código debería [qué debería hacer],
pero [qué pasa en realidad, con el mensaje de error completo].

<codigo>
…
</codigo>

Explícame por qué ocurre el error y dame una pista para corregirlo. No me
reescribas todo el código: quiero corregirlo yo.
```

### Recibir retroalimentación sobre un texto propio

```text
Este es el borrador de mi ensayo para [materia]. La rúbrica es:
<rubrica>…</rubrica>

<borrador>…</borrador>

Evalúalo con la rúbrica. Para cada criterio, di qué tan bien lo cumple y
qué cambiaría. No reescribas el texto: señala los problemas y yo los corrijo.
```

### Preparar una exposición

Usa la Skill [`presentaciones-con-mi-voz`](../taller/03-skills/skill-demo/presentaciones-con-mi-voz) o la plantilla de la [Actividad 2](../taller/02-anatomia-del-prompt/plantilla-seis-piezas.md).

### Buscar fuentes (con verificación)

```text
Estoy buscando fuentes sobre [tema] para un informe de [materia].
Sugiéreme términos de búsqueda en español e inglés y tipos de fuente que
debería consultar (bases de datos, autores de referencia, organismos).
No me des referencias específicas a menos que puedas buscarlas en la web;
en ese caso, incluye el enlace.
```

Recuerda declarar el uso de la IA según las reglas de cada curso: [cómo citar y declarar](../taller/06-marco-normativo-unal/como-citar-la-ia.md).

## 10. Del prompt al contexto

A medida que las aplicaciones de IA se vuelven agentes que trabajan varios pasos seguidos, la pregunta deja de ser solo «¿cómo escribo esta instrucción?» y pasa a ser «¿qué información debe tener el modelo en cada momento?». Anthropic llama a esto **context engineering**: decidir qué entra en la ventana de contexto (instrucciones, herramientas, documentos, historial, memoria) para que el modelo tenga lo necesario y nada más ([Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

Las piezas de esta disciplina son las mismas que se ven en el taller:

| Herramienta | Qué resuelve |
|---|---|
| **Prompt** | La instrucción para una tarea concreta. |
| **Instrucciones de proyecto o `CLAUDE.md`** | Contexto que aplica a todas las conversaciones de un proyecto. |
| **Skills** | Conocimiento y procedimientos que se cargan solo cuando la tarea los necesita. [Guía](02-skills.md). |
| **Herramientas y MCP** | Acceso a datos y acciones externas (buscar, leer archivos, consultar una base de datos). |
| **Subagentes** | Contexto aislado para subtareas, para que la conversación principal no se sature. [Guía](03-agentes-especializados.md). |

## 11. Para seguir aprendiendo

**Documentación oficial**

- Anthropic: [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) y [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- OpenAI: [Prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- Google: [Prompt design strategies (Gemini API)](https://ai.google.dev/gemini-api/docs/prompting-strategies)

**Cursos y tutoriales gratuitos**

- Anthropic: [tutorial interactivo de prompt engineering](https://github.com/anthropics/prompt-eng-interactive-tutorial) (cuadernos Jupyter, en inglés)
- Anthropic: [cursos en GitHub](https://github.com/anthropics/courses)
- DAIR.AI: [Prompt Engineering Guide](https://www.promptingguide.ai/es) (disponible en español)

**Artículos de investigación**

- Brown et al. (2020). *Language Models are Few-Shot Learners*. [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)
- Wei et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
- Kojima et al. (2022). *Large Language Models are Zero-Shot Reasoners*. [arXiv:2205.11916](https://arxiv.org/abs/2205.11916)
- Wang et al. (2022). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)
- Yao et al. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
- Schulhoff et al. (2024). *The Prompt Report: A Systematic Survey of Prompting Techniques*. [arXiv:2406.06608](https://arxiv.org/abs/2406.06608)

Más recursos en [`05-recursos.md`](05-recursos.md).
