# Glosario

Términos que aparecen en el taller y en las guías, en orden alfabético.

| Término | Definición |
|---|---|
| **Agente** | Modelo de lenguaje que, en un ciclo, decide qué hacer, usa herramientas, observa el resultado y continúa hasta cumplir un objetivo. Ver la [guía de agentes](03-agentes-especializados.md). |
| **Agent Skills** | Estándar abierto para empaquetar Skills, publicado en [agentskills.io](https://agentskills.io). |
| **Alucinación** | Respuesta que suena plausible pero es falsa o inventada: un dato, una cita o una referencia que no existe. |
| **API** | Interfaz para usar un modelo desde un programa, en lugar de desde una aplicación de chat. Se paga por uso (tokens). |
| **Carga progresiva** (*progressive disclosure*) | Forma en que se cargan las Skills: primero solo el nombre y la descripción; las instrucciones y los recursos, solo cuando hacen falta. |
| **Chain of thought** (cadena de pensamiento) | Técnica de pedir al modelo que escriba su razonamiento paso a paso antes de la respuesta. |
| **`CLAUDE.md` / `AGENTS.md`** | Archivo de instrucciones que el agente carga siempre al trabajar en un proyecto. |
| **Context engineering** | Diseño de toda la información que recibe el modelo en cada momento: instrucciones, herramientas, documentos, historial y memoria. |
| **Fecha de corte** | Fecha hasta la que llega el conocimiento con el que se entrenó el modelo. |
| **Few-shot** | Prompt que incluye unos pocos ejemplos de entrada y salida. |
| **Frontmatter** | Encabezado en formato YAML, entre líneas `---`, al inicio de un archivo Markdown. En las Skills y los subagentes contiene `name` y `description`. |
| **Handoff** (traspaso) | Cuando un agente pasa la conversación a otro agente más especializado. |
| **Herramienta** (*tool*) | Función que el modelo puede invocar: buscar en la web, leer un archivo, ejecutar código, consultar una API. |
| **Inyección de instrucciones** (*prompt injection*) | Ataque en el que un contenido externo (una página, un documento) incluye texto que intenta darle órdenes al modelo. |
| **LLM** (*large language model*) | Modelo de lenguaje de gran tamaño, como Claude, GPT o Gemini. |
| **Markdown** | Formato de texto con marcas simples (`#` para títulos, `-` para listas). Es el formato de los archivos `.md` de este repositorio. |
| **MCP** (*Model Context Protocol*) | Estándar abierto para conectar agentes con sistemas externos (bases de datos, calendarios, APIs). Ver [modelcontextprotocol.io](https://modelcontextprotocol.io). |
| **Modelo de razonamiento** / **razonamiento extendido** | Modo en el que el modelo «piensa» internamente antes de responder, útil en problemas de varios pasos. |
| **Orquestador** | Agente que divide una tarea, la reparte entre otros agentes y combina los resultados. |
| **Plugin** | En Claude Code, paquete que agrupa Skills, subagentes, comandos y conexiones MCP para instalarlos juntos. |
| **Prompt** | Instrucción o mensaje que se le da a un modelo. |
| **Prompt de sistema** (*system prompt*) | Instrucciones de fondo que definen el comportamiento del modelo en toda una conversación o de un agente. |
| **Prompt chaining** (encadenamiento) | Dividir una tarea en varios prompts en secuencia, donde la salida de uno alimenta al siguiente. |
| **ReAct** | Patrón en el que el modelo alterna razonar y actuar con herramientas. Es la base de los agentes. |
| **Rol** | Pieza del prompt que indica quién debe ser el modelo («actúa como…»). |
| **Salidas estructuradas** | Función de algunas API que obliga al modelo a responder con un esquema JSON definido. |
| **Skill** | Carpeta con instrucciones (`SKILL.md`) y recursos opcionales que el agente carga cuando la tarea lo necesita. Ver la [guía de Skills](02-skills.md). |
| **`SKILL.md`** | Archivo principal de una Skill: encabezado con nombre y descripción, y cuerpo con las instrucciones. |
| **Subagente** | Agente especializado, con contexto propio, que otro agente invoca para una subtarea y que devuelve solo el resultado. |
| **Temperatura** | Parámetro que controla qué tan variadas son las respuestas. Más baja, más predecible; más alta, más diversa. |
| **Token** | Unidad en que el modelo divide el texto (aproximadamente, partes de palabras). Los límites y los costos se miden en tokens. |
| **Ventana de contexto** | Cantidad máxima de texto (en tokens) que el modelo puede considerar a la vez: instrucciones, conversación y archivos. |
| **Workflow** | Secuencia de pasos con modelos definida de antemano por una persona, a diferencia de un agente, que decide el camino. |
| **XML (etiquetas)** | Marcas como `<contexto>…</contexto>` que se usan en los prompts para separar instrucciones, datos y ejemplos. |
| **Zero-shot** | Prompt sin ejemplos, solo con la instrucción. |
