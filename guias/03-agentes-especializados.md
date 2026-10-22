# Guía de agentes especializados

Esta guía amplía la [Actividad 4](../taller/04-agentes) del taller: qué es un agente, cuándo conviene usarlo, cómo se diseña un agente especializado y cómo se despliega como subagente en Claude Code o con código.

## Contenido

1. [Qué es un agente](#1-qué-es-un-agente)
2. [Workflows y agentes: los patrones básicos](#2-workflows-y-agentes-los-patrones-básicos)
3. [Cuándo usar un agente y cuándo no](#3-cuándo-usar-un-agente-y-cuándo-no)
4. [Agentes especializados y subagentes](#4-agentes-especializados-y-subagentes)
5. [Diseñar un agente especializado](#5-diseñar-un-agente-especializado)
6. [Subagentes en Claude Code](#6-subagentes-en-claude-code)
7. [Agentes con código](#7-agentes-con-código)
8. [Conectar herramientas: MCP](#8-conectar-herramientas-mcp)
9. [Riesgos y buenas prácticas](#9-riesgos-y-buenas-prácticas)
10. [Ejercicio: diseña tu agente](#10-ejercicio-diseña-tu-agente)
11. [Para seguir aprendiendo](#11-para-seguir-aprendiendo)

---

## 1. Qué es un agente

Un **agente** es un modelo de lenguaje que recibe un objetivo y trabaja en un ciclo: decide qué hacer, usa una herramienta, observa el resultado y vuelve a decidir, hasta terminar o hasta que necesita ayuda.

```
        ┌──────────────────────────────────┐
        │             Objetivo             │
        └────────────────┬─────────────────┘
                         ▼
   ┌───────────► Pensar: ¿qué hago ahora? ─────────┐
   │                                               ▼
Observar el resultado                  Actuar con una herramienta
   ▲                                  (buscar, leer, ejecutar código)
   └───────────────────────────────────────────────┘
                         │
                         ▼ (cuando el objetivo se cumple)
                   Respuesta final
```

Un agente tiene cuatro componentes:

| Componente | Qué es | Ejemplo |
|---|---|---|
| **Modelo** | El LLM que razona y decide | Claude, GPT, Gemini |
| **Instrucciones** | El prompt de sistema: rol, objetivo, reglas, formato de salida | «Eres un revisor de fuentes académicas…» |
| **Herramientas** | Lo que puede hacer en el mundo | Buscar en la web, leer y escribir archivos, ejecutar código, consultar una base de datos |
| **Ciclo** | El programa que repite pensar, actuar y observar | Claude Code, el Agent SDK, ChatGPT con herramientas |

Cuando Claude busca en la web antes de responderte o Claude Code corre las pruebas de tu proyecto, estás usando un agente.

## 2. Workflows y agentes: los patrones básicos

Anthropic distingue dos tipos de sistemas ([Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)):

- **Workflows:** el camino lo define una persona en código. El modelo ejecuta cada paso, pero no decide el orden.
- **Agentes:** el modelo decide dinámicamente el camino y qué herramientas usar.

Antes de construir un agente, conviene conocer los patrones de workflow, porque muchas tareas se resuelven con ellos de forma más barata y predecible:

| Patrón | Cómo funciona | Ejemplo para estudiantes |
|---|---|---|
| **Encadenamiento** (*prompt chaining*) | Una secuencia fija de pasos; la salida de uno es la entrada del siguiente | Apuntes → conceptos clave → guía de estudio → preguntas de práctica |
| **Enrutamiento** (*routing*) | Un primer paso clasifica la entrada y la envía al proceso especializado | Clasificar una pregunta como de Cálculo, Física o Programación y responder con el tutor de esa materia |
| **Paralelización** | Varias llamadas a la vez: secciones distintas (*sectioning*) o la misma tarea varias veces para comparar (*voting*) | Revisar un informe en paralelo: un revisor de formato, otro de análisis y otro de referencias |
| **Orquestador y trabajadores** | Un modelo central divide la tarea, reparte subtareas que no conocía de antemano y combina los resultados | Investigar un tema: el orquestador decide qué subtemas buscar y lanza un trabajador por subtema |
| **Evaluador y optimizador** | Un modelo genera y otro evalúa con criterios, en ciclo, hasta cumplirlos | Un modelo escribe un resumen y otro lo evalúa con la rúbrica hasta que la cumple |

Y el **agente** propiamente dicho: un ciclo abierto en el que el modelo decide todo el camino, útil cuando no se pueden prever los pasos.

## 3. Cuándo usar un agente y cuándo no

Regla del taller: **la solución más simple que funcione es la mejor.**

| Situación | Lo adecuado |
|---|---|
| Tarea única, corta y bien definida | Un prompt |
| Tarea que se repite igual | Una [Skill](02-skills.md) |
| Pasos conocidos de antemano | Un workflow (o una Skill con los pasos) |
| Pasos que dependen de lo que se va encontrando, con herramientas | Un agente |
| Partes grandes e independientes, o subtareas que saturarían el contexto | Un agente que delega en subagentes |

Los agentes tienen costos reales:

- **Más tokens.** En el sistema de investigación de Anthropic, los agentes usaron unas 4 veces más tokens que una conversación normal, y los sistemas multiagente unas 15 veces más ([How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)).
- **Más tiempo** y más puntos donde algo puede fallar.
- **Más difícil de verificar**: hay que revisar no solo el resultado sino lo que hizo para llegar a él.

A cambio, cuando la tarea lo amerita, la mejora puede ser grande: en el mismo estudio, el sistema multiagente superó al agente individual por un amplio margen en tareas de investigación que se podían dividir.

## 4. Agentes especializados y subagentes

Un **agente especializado** es un agente con un trabajo acotado: revisar fuentes, revisar código, analizar datos, investigar un tema. Un **subagente** es un agente especializado que otro agente (el principal) invoca para una subtarea.

Por qué especializar:

| Ventaja | Explicación |
|---|---|
| **Contexto limpio** | El subagente empieza sin el historial de la conversación principal. Lee lo que necesita, trabaja y devuelve solo el resultado. La conversación principal no se llena de páginas leídas o de salidas de comandos. |
| **Instrucciones enfocadas** | Un prompt de sistema que hace una sola cosa bien es más fácil de escribir y de probar que uno que lo hace todo. |
| **Permisos mínimos** | Un revisor no necesita poder borrar archivos. Cada subagente recibe solo las herramientas que su trabajo requiere. |
| **Paralelismo** | Varias subtareas independientes pueden avanzar a la vez. |
| **Modelo adecuado** | Una tarea acotada puede usar un modelo más rápido y barato. |
| **Reutilización** | El mismo subagente sirve en muchos proyectos. |

Diferencia con una Skill: una **Skill** le enseña al agente actual a hacer algo, dentro de su misma conversación. Un **subagente** es otro agente, con su propio contexto, que hace el trabajo aparte y devuelve el resultado. Pueden combinarse: un subagente puede usar Skills.

## 5. Diseñar un agente especializado

Antes de escribir el archivo, responde estas preguntas. Son el equivalente al canvas de Skills de la Actividad 3.

| Elemento | Pregunta | Ejemplo: revisor de fuentes |
|---|---|---|
| **Misión** | ¿Qué hace, en una frase? | Verifica que las referencias de un documento existan y respalden lo que se les atribuye. |
| **Cuándo se usa** (descripción) | ¿En qué situaciones debe delegarse a este agente? | Antes de entregar un informe, artículo o presentación con bibliografía. |
| **Alcance** | ¿Qué hace y, sobre todo, qué **no** hace? | Verifica; no reescribe el documento ni agrega referencias nuevas. |
| **Entradas** | ¿Qué recibe? | Ruta del documento. |
| **Herramientas** | ¿Qué necesita, como mínimo? | Leer archivos, buscar y abrir páginas web. **No** escribir ni ejecutar comandos. |
| **Proceso** | ¿Qué pasos sigue? | Buscar cada referencia, confirmar datos, contrastar la afirmación. |
| **Salida** | ¿Qué devuelve exactamente? (el «contrato») | Una tabla con columnas fijas y una lista de correcciones. |
| **Criterio de parada** | ¿Cuándo termina? ¿Qué hace si no puede? | Al revisar todas las referencias; marca «no verificable» si no accede a la fuente. |
| **Modelo** | ¿Necesita el más capaz o basta uno rápido? | Uno intermedio (búsqueda y comparación). |
| **Evaluación** | ¿Cómo sé que funciona? | Probarlo con un documento con errores conocidos ([`informe-de-prueba.md`](../taller/04-agentes/informe-de-prueba.md)). |

Consejos para el prompt de sistema del agente:

- **Define la salida con precisión.** El agente principal (o tú) va a usar ese resultado; un formato fijo hace que sea fácil de leer y comparar.
- **Dile qué hacer cuando no pueda.** «Si no puedes acceder a la fuente, márcalo como no verificable» evita que invente.
- **Escribe el proceso, no solo el objetivo.** Los pasos guían el uso de herramientas.
- **Que la descripción diga cuándo usarlo**, igual que en las Skills.

## 6. Subagentes en Claude Code

### Dónde se guardan

| Ubicación | Alcance |
|---|---|
| `.claude/agents/` dentro del proyecto | Solo ese proyecto; se comparte con quien clone el repositorio |
| `~/.claude/agents/` | Todos tus proyectos |
| Carpeta `agents/` de un plugin | Donde el plugin esté activo |

### Formato

Un archivo Markdown con encabezado YAML. El cuerpo es el prompt de sistema del subagente.

```markdown
---
name: revisor-de-codigo
description: Revisa cambios de código buscando errores, problemas de
  seguridad y falta de pruebas. Úsalo después de escribir o modificar código.
tools: Read, Grep, Glob, Bash
model: sonnet
---

Eres un revisor de código para proyectos universitarios…
```

| Campo | Obligatorio | Para qué |
|---|---|---|
| `name` | Sí | Identificador único (minúsculas y guiones) |
| `description` | Sí | Cuándo debe delegarse a este subagente |
| `tools` | No | Lista de herramientas permitidas; si se omite, hereda todas |
| `disallowedTools` | No | Herramientas prohibidas |
| `model` | No | `sonnet`, `opus`, `haiku`, `inherit` o un identificador completo |
| `permissionMode` | No | Cómo maneja los permisos (por ejemplo, `plan` para solo lectura) |
| `maxTurns` | No | Máximo de turnos antes de detenerse |
| `skills` | No | Skills que el subagente carga desde el inicio |

Lista completa en la [documentación de subagentes](https://code.claude.com/docs/en/sub-agents).

### Crear y usar

1. Escribe `/agents` en Claude Code para ver, crear o editar subagentes con un asistente, o crea el archivo a mano.
2. Para invocarlo:
   - **Automático:** Claude delega cuando la tarea coincide con la descripción.
   - **Explícito:** «Usa el subagente revisor-de-codigo para revisar mis cambios».
   - **Mención:** escribe `@` y elige el subagente.
3. Para paralelizar, pide varias tareas independientes a la vez: «Usa un subagente por universidad para resumir estos cinco planes de estudio».

Ejemplos listos para copiar en [`ejemplos-de-agentes/`](ejemplos-de-agentes).

## 7. Agentes con código

Cuando quieres un agente dentro de tu propia aplicación (un bot, un script, un servicio), usas un SDK.

### Claude Agent SDK

Es el mismo motor de Claude Code, como librería para Python y TypeScript ([documentación](https://platform.claude.com/docs/en/agent-sdk/overview)). Trae las herramientas de Claude Code (leer, escribir, ejecutar comandos, buscar en la web), manejo de contexto y subagentes.

```bash
pip install claude-agent-sdk
```

```python
import anyio
from claude_agent_sdk import (
    AgentDefinition,
    AssistantMessage,
    ClaudeAgentOptions,
    TextBlock,
    query,
)

opciones = ClaudeAgentOptions(
    system_prompt="Eres un asistente que ayuda a estudiantes a revisar sus informes.",
    disallowed_tools=["Write", "Edit", "Bash"],  # solo lectura
    agents={
        "revisor-de-fuentes": AgentDefinition(
            description="Verifica que las referencias existan y respalden lo que se afirma.",
            prompt="Eres un revisor de fuentes académicas. Devuelve una tabla con "
                   "referencia, ¿existe?, ¿respalda la afirmación? y observaciones.",
            tools=["Read", "WebSearch", "WebFetch"],
            model="sonnet",
        ),
    },
)


async def main():
    async for mensaje in query(
        prompt="Usa el revisor-de-fuentes para revisar las referencias de informe.md",
        options=opciones,
    ):
        if isinstance(mensaje, AssistantMessage):
            for bloque in mensaje.content:
                if isinstance(bloque, TextBlock):
                    print(bloque.text)


anyio.run(main)
```

Necesitas una clave de la API de Anthropic en la variable de entorno `ANTHROPIC_API_KEY`. El archivo completo está en [`ejemplos-de-agentes/agente_sdk.py`](ejemplos-de-agentes/agente_sdk.py).

### OpenAI Agents SDK

Librería de OpenAI para agentes con herramientas y **traspasos** (*handoffs*) entre agentes ([documentación](https://openai.github.io/openai-agents-python/)):

```python
from agents import Agent, Runner

tutor_calculo = Agent(
    name="Tutor de Cálculo",
    handoff_description="Especialista en preguntas de cálculo",
    instructions="Explica paso a paso, con un ejemplo cotidiano antes de la fórmula.",
)

tutor_programacion = Agent(
    name="Tutor de Programación",
    handoff_description="Especialista en preguntas de programación",
    instructions="Da pistas para corregir el código; no lo reescribas completo.",
)

clasificador = Agent(
    name="Clasificador",
    instructions="Decide qué tutor debe responder la pregunta del estudiante.",
    handoffs=[tutor_calculo, tutor_programacion],
)

resultado = Runner.run_sync(clasificador, "¿Por qué mi ciclo for nunca termina?")
print(resultado.final_output)
```

Este ejemplo es el patrón de **enrutamiento** de la sección 2.

### Otros frameworks

| Framework | De quién | Enfoque | Enlace |
|---|---|---|---|
| Claude Agent SDK | Anthropic | Agentes con las herramientas de Claude Code | [Python](https://github.com/anthropics/claude-agent-sdk-python), [TypeScript](https://github.com/anthropics/claude-agent-sdk-typescript) |
| OpenAI Agents SDK | OpenAI | Agentes ligeros con handoffs y guardrails | [GitHub](https://github.com/openai/openai-agents-python) |
| Agent Development Kit (ADK) | Google | Agentes y sistemas multiagente, integrado con Gemini y Google Cloud | [Documentación](https://google.github.io/adk-docs/), [GitHub](https://github.com/google/adk-python) |
| LangGraph | LangChain | Agentes como grafos de estados, con control fino del flujo | [GitHub](https://github.com/langchain-ai/langgraph) |
| CrewAI | CrewAI | Equipos de agentes con roles | [GitHub](https://github.com/crewAIInc/crewAI) |

Para aprender, empieza por subagentes en Claude Code (sin código) y pasa a un SDK cuando necesites integrarlo en un programa.

## 8. Conectar herramientas: MCP

El **Model Context Protocol (MCP)** es un estándar abierto para conectar agentes con sistemas externos: bases de datos, calendarios, repositorios, APIs. Un **servidor MCP** expone herramientas y datos; cualquier agente compatible (Claude, Claude Code, ChatGPT, Cursor, VS Code y otros) puede usarlas.

- Sitio oficial: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- Servidores de referencia: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- Para construir uno: la Skill [`mcp-builder`](https://github.com/anthropics/skills/tree/main/skills/mcp-builder)

Recuerda: **MCP le da acceso al agente; la Skill le enseña qué hacer con ese acceso; el subagente aísla el trabajo.**

## 9. Riesgos y buenas prácticas

| Riesgo | Qué hacer |
|---|---|
| **Permisos excesivos** | Dale a cada agente solo las herramientas que necesita. Empieza en modo de solo lectura o con aprobación de cada acción. |
| **Inyección de instrucciones** (*prompt injection*) | Una página web, un PDF o un correo pueden contener texto que intenta darle órdenes al agente. Trata el contenido externo como datos, no como instrucciones, y no le des a un agente que lee la web permisos para acciones irreversibles. |
| **Acciones irreversibles** | Exige confirmación humana antes de borrar, enviar, publicar o pagar. |
| **Costos que se disparan** | Limita turnos (`maxTurns`) y presupuesto. Revisa el consumo. |
| **Resultados que parecen correctos** | Verifica. Pide al agente evidencia (pruebas que pasan, enlaces a fuentes) y revísala. |
| **Datos personales** | Las mismas reglas del [marco normativo](../taller/06-marco-normativo-unal): no expongas datos de otras personas. |
| **Demasiados agentes** | Más agentes no es mejor. Agrega uno solo cuando el anterior no alcanza. |

## 10. Ejercicio: diseña tu agente

1. Elige una tarea de tu carrera que tenga varios pasos y requiera herramientas (no solo escribir texto).
2. Llena la tabla de la sección 5.
3. Escribe el archivo del subagente con base en los [ejemplos](ejemplos-de-agentes).
4. Pruébalo en Claude Code con un caso donde conozcas la respuesta correcta.
5. Ajusta la descripción si no se activa cuando debe, y el proceso si el resultado no es el esperado.

## 11. Para seguir aprendiendo

**Artículos de ingeniería de Anthropic**

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): patrones de workflows y agentes.
- [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system): lecciones de un sistema multiagente real.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): qué información darle al agente en cada momento.
- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents): cómo diseñar las herramientas que usa un agente.

**Documentación**

- [Subagentes en Claude Code](https://code.claude.com/docs/en/sub-agents)
- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [Google Agent Development Kit](https://google.github.io/adk-docs/)
- [Model Context Protocol](https://modelcontextprotocol.io)

**Colecciones de subagentes de la comunidad**

- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)
- [wshobson/agents](https://github.com/wshobson/agents)

Revisa cualquier agente de terceros antes de usarlo, igual que con las Skills.

**Investigación**

- Yao et al. (2022). *ReAct: Synergizing Reasoning and Acting in Language Models*. [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)
