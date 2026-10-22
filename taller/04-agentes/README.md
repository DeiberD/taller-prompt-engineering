# Actividad 4. ¿Prompt, Skill, agente o subagentes?

**Duración:** 15 minutos (concepto 5, demo 5, clasificación en parejas 5) · **Objetivo:** agentes y subagentes

Se distinguen cuatro formas de trabajar con la IA, se ve un ejemplo de despliegue de un subagente y, en parejas, se clasifican seis tareas reales según lo que necesitan. La idea central: **la solución más simple que funcione es la mejor.**

## Archivos de esta carpeta

| Archivo | Para qué sirve |
|---|---|
| [`.claude/agents/revisor-de-fuentes.md`](.claude/agents/revisor-de-fuentes.md) | Subagente de la demo, listo para Claude Code |
| [`informe-de-prueba.md`](informe-de-prueba.md) | Informe con referencias problemáticas para la demo |
| [`tareas-para-clasificar.md`](tareas-para-clasificar.md) | Hoja de trabajo en parejas |
| [`respuestas.md`](respuestas.md) | Respuestas y discusión (abrir al final) |

## 1. Cuatro formas de trabajar con la IA

| Opción | Qué es | Quién decide el camino |
|---|---|---|
| **Chat o prompt** | Una pregunta, una respuesta. La persona hace todo lo demás. | La persona |
| **Workflow** | Una secuencia de pasos definida de antemano por una persona (primero resume, luego traduce, luego da formato). | La persona, al diseñar el flujo |
| **Agente** | Un modelo que recibe un objetivo y decide qué herramientas usar y en qué orden (buscar, leer archivos, ejecutar código), en un ciclo, hasta terminar. | El modelo |
| **Subagentes** | Agentes que el agente principal lanza para subtareas independientes. Cada uno trabaja con su propio contexto limpio y devuelve solo el resultado. | El agente principal reparte; cada subagente resuelve su parte |

```
Agente principal
 ├── recibe el objetivo
 ├── decide que hay partes independientes
 ├──> Subagente A (contexto propio) ──> resultado A ──┐
 ├──> Subagente B (contexto propio) ──> resultado B ──┤
 └── combina los resultados <─────────────────────────┘
```

## 2. Demo: desplegar un subagente en Claude Code

En Claude Code, un subagente es un archivo Markdown con un encabezado YAML dentro de la carpeta `.claude/agents/` del proyecto (o en `~/.claude/agents/` para usarlo en todos tus proyectos):

```markdown
---
name: revisor-de-fuentes
description: Verifica que las referencias de un documento existan y digan
  lo que se les atribuye. Úsalo cuando haya que revisar la bibliografía.
tools: Read, Grep, Glob, WebSearch, WebFetch
model: sonnet
---

Eres un revisor de fuentes académicas. Para cada referencia, confirma que
exista, que autores y año coincidan y que respalde la afirmación.
Devuelve una tabla: referencia, ¿existe?, ¿respalda la afirmación?,
observaciones.
```

- **`name`** y **`description`** son obligatorios. La descripción le dice al agente principal cuándo delegar.
- **`tools`** limita las herramientas del subagente (si se omite, hereda todas). Un revisor no necesita poder editar archivos.
- **`model`** permite usar un modelo más rápido o más barato para tareas acotadas.
- El cuerpo del archivo es el prompt de sistema del subagente.

Para reproducir la demo:

1. Instala [Claude Code](https://code.claude.com/docs/en/overview).
2. Abre una terminal en esta carpeta (`taller/04-agentes`) y ejecuta `claude`.
3. Escribe `/agents` para ver que `revisor-de-fuentes` aparece en la lista.
4. Pide: «Usa el subagente revisor-de-fuentes para revisar las referencias de informe-de-prueba.md».
5. Observa que el subagente trabaja aparte y el agente principal solo recibe la tabla.

La solución esperada está al final de [`informe-de-prueba.md`](informe-de-prueba.md).

## 3. Clasificación en parejas

Abre [`tareas-para-clasificar.md`](tareas-para-clasificar.md). Cuando terminen, revisen [`respuestas.md`](respuestas.md).

## Notas para el moderador

- Si no hay Claude Code disponible, la demo puede mostrarse con capturas de pantalla.
- Insistir en que más agentes no es mejor: cuestan más, tardan más y sus resultados son más difíciles de verificar.
- Para profundizar: [guía de agentes especializados](../../guias/03-agentes-especializados.md).
