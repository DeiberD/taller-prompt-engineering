# Guía de Skills

Esta guía amplía la [Actividad 3](../taller/03-skills) del taller: qué son las Skills, cómo funcionan por dentro, cómo se crean y prueban, cómo se instalan en distintas herramientas y cuáles son las más usadas.

## Contenido

1. [Qué es una Skill](#1-qué-es-una-skill)
2. [Cómo funciona: carga progresiva](#2-cómo-funciona-carga-progresiva)
3. [Anatomía de una Skill](#3-anatomía-de-una-skill)
4. [Skills frente a otras herramientas](#4-skills-frente-a-otras-herramientas)
5. [Dónde funcionan y cómo se instalan](#5-dónde-funcionan-y-cómo-se-instalan)
6. [Crear una Skill paso a paso](#6-crear-una-skill-paso-a-paso)
7. [Buenas prácticas](#7-buenas-prácticas)
8. [Probar y mejorar una Skill](#8-probar-y-mejorar-una-skill)
9. [Seguridad](#9-seguridad)
10. [Catálogo de Skills populares](#10-catálogo-de-skills-populares)
11. [Dónde encontrar más](#11-dónde-encontrar-más)

---

## 1. Qué es una Skill

Una **Skill** es una carpeta que contiene instrucciones, y opcionalmente scripts y recursos, que un agente de IA carga cuando la tarea lo necesita. Le enseña al modelo a hacer algo concreto de forma repetible: crear documentos con cierto formato, seguir el procedimiento de un equipo, usar una librería según sus buenas prácticas o aplicar un estilo de escritura.

La idea la presentó Anthropic en octubre de 2025 y luego la publicó como **estándar abierto** en [agentskills.io](https://agentskills.io). Hoy el mismo formato funciona en Claude, Claude Code, Codex y ChatGPT, Gemini CLI, Cursor, GitHub Copilot, VS Code y decenas de agentes más ([lista de clientes](https://agentskills.io/clients)).

La forma más simple de entenderlo:

> Un prompt le dice al modelo qué hacer **ahora**. Una Skill le enseña a hacer algo **cada vez que haga falta**.

## 2. Cómo funciona: carga progresiva

Si cargaras todas las instrucciones de todas tus Skills en cada conversación, llenarías la ventana de contexto antes de empezar. Por eso las Skills se cargan por niveles (*progressive disclosure*):

| Nivel | Qué se carga | Cuándo | Tamaño aproximado |
|---|---|---|---|
| 1. Metadatos | `name` y `description` de **todas** las Skills instaladas | Al iniciar la conversación | ~100 tokens por Skill |
| 2. Instrucciones | El cuerpo completo del `SKILL.md` | Cuando el modelo decide que la Skill aplica | Se recomienda menos de 5.000 tokens |
| 3. Recursos | Archivos de `references/`, `scripts/`, `assets/` | Solo cuando las instrucciones lo piden | Sin límite práctico |

Consecuencias prácticas:

- **La descripción lo es todo** para que la Skill se active. Es lo único que el modelo ve de ella hasta que decide usarla.
- Puedes tener muchas Skills instaladas sin saturar el contexto.
- Los recursos pesados (una guía de estilo larga, una tabla de referencia, una plantilla) van en archivos aparte, no en el `SKILL.md`.
- Los **scripts** se ejecutan sin cargar su código en el contexto: el modelo solo ve el resultado. Son ideales para cálculos, validaciones o conversiones que deben ser exactas.

Más detalle: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (Anthropic).

## 3. Anatomía de una Skill

### Estructura de carpetas

```
nombre-de-la-skill/
├── SKILL.md          Obligatorio: metadatos + instrucciones
├── scripts/          Opcional: código ejecutable (Python, Bash, JavaScript)
├── references/       Opcional: documentación que se lee bajo demanda
└── assets/           Opcional: plantillas, imágenes, datos
```

Los nombres `scripts/`, `references/` y `assets/` son convenciones; puedes usar otros (en el taller usamos `referencias/`), siempre que el `SKILL.md` los mencione con rutas relativas.

### El archivo `SKILL.md`

```markdown
---
name: informe-de-laboratorio
description: Redacta y revisa informes de laboratorio de ingeniería con la
  estructura de la facultad. Úsala cuando pida un informe de laboratorio,
  una práctica, un preinforme o la revisión de uno de ellos.
---

# Informe de laboratorio

## Pasos
1. …

## Reglas
- …

Para el formato de tablas y figuras, lee [references/formato.md](references/formato.md).
```

### Campos del encabezado (estándar abierto)

| Campo | Obligatorio | Reglas |
|---|---|---|
| `name` | Sí | Hasta 64 caracteres. Solo minúsculas, números y guiones. No puede empezar ni terminar con guion ni tener dos guiones seguidos. **Debe coincidir con el nombre de la carpeta.** |
| `description` | Sí | Hasta 1.024 caracteres. Qué hace la Skill **y cuándo usarla**, con palabras clave que el usuario diría. |
| `license` | No | Licencia de la Skill. |
| `compatibility` | No | Requisitos de entorno (por ejemplo, «Requiere Python 3.12 y acceso a internet»). |
| `metadata` | No | Pares clave-valor libres (autor, versión). |
| `allowed-tools` | No | Herramientas preaprobadas (experimental; el soporte varía). |

Fuente: [especificación de Agent Skills](https://agentskills.io/specification).

Algunas herramientas agregan campos propios. Claude Code, por ejemplo, admite `disable-model-invocation: true` (la Skill solo se usa si la invocas con `/nombre`), `argument-hint`, `model` y otros ([documentación](https://code.claude.com/docs/en/skills)).

### Una buena descripción

| Mala | Buena |
|---|---|
| `Ayuda con informes.` | `Redacta y revisa informes de laboratorio de ingeniería con la estructura de la facultad. Úsala cuando pida un informe de laboratorio, una práctica, un preinforme o la revisión de uno de ellos.` |
| `Skill de PDF.` | `Extrae texto y tablas de archivos PDF, llena formularios y une varios PDF. Úsala cuando trabaje con documentos PDF o mencione formularios.` |

Una buena descripción dice **qué hace**, **cuándo usarla** e incluye las **palabras** con las que pedirías la tarea.

## 4. Skills frente a otras herramientas

| Herramienta | Qué es | Cuándo usarla |
|---|---|---|
| **Prompt** | Instrucción para una tarea en una conversación | Tareas únicas |
| **Instrucciones de proyecto** (`CLAUDE.md`, `AGENTS.md`, instrucciones personalizadas) | Contexto que se carga **siempre** en un proyecto | Reglas que aplican a todo: convenciones, estilo general, datos del proyecto |
| **Skill** | Procedimiento o conocimiento que se carga **solo cuando hace falta** | Tareas repetidas y especializadas |
| **MCP** (*Model Context Protocol*) | Conexión a sistemas externos: datos y acciones | Leer un calendario, consultar una base de datos, crear un issue |
| **Subagente** | Agente con contexto propio para una subtarea | Trabajo aislado o en paralelo ([guía](03-agentes-especializados.md)) |
| **Plugin** (Claude Code) | Paquete que agrupa Skills, subagentes, comandos y conexiones MCP | Compartir una configuración completa |

Una forma de recordarlo: **MCP le da acceso al agente; la Skill le enseña qué hacer con ese acceso.** Son complementarios.

## 5. Dónde funcionan y cómo se instalan

### Claude (web, escritorio y móvil)

1. Activa **Settings > Capabilities > Code execution and file creation** (las Skills lo necesitan).
2. Ve a **Customize > Skills**. Ahí puedes activar las Skills de Anthropic que ya vienen incluidas.
3. Para subir una propia: comprime la carpeta en `.zip` y usa **+ > Create skill > Upload a skill**.

Disponible desde el plan gratuito. En Team y Enterprise, quien administra la organización controla si se pueden subir Skills. Referencia: [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

También puedes pedirle a Claude que **cree la Skill contigo**: la Skill integrada [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator) guía el proceso, genera los archivos y la prueba.

### Claude Code

| Alcance | Ruta |
|---|---|
| Personal (todos tus proyectos) | `~/.claude/skills/<nombre>/SKILL.md` |
| Proyecto (se comparte con el repositorio) | `.claude/skills/<nombre>/SKILL.md` |
| Plugin | `<plugin>/skills/<nombre>/SKILL.md` |

Claude Code las detecta solo. Se activan automáticamente según la descripción o manualmente con `/nombre`. Las Skills oficiales de Anthropic se instalan como plugin:

```text
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

Referencia: [Skills en Claude Code](https://code.claude.com/docs/en/skills).

### API de Claude y Agent SDK

Las Skills se pueden subir y usar desde la API ([guía](https://platform.claude.com/docs/en/build-with-claude/skills-guide)) y desde el [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview).

### Cualquier agente compatible: el CLI `skills`

[`skills`](https://github.com/vercel-labs/skills) es una herramienta de línea de comandos (Node.js 22.20 o superior) que instala Skills desde GitHub en más de 75 agentes:

```bash
# Instalar una Skill de un repositorio (pregunta en qué agente)
npx skills add anthropics/skills --skill frontend-design

# Instalarla en un agente específico y para todos los proyectos
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a claude-code -g

# Buscar Skills
npx skills find pdf

# Ver, actualizar o quitar las instaladas
npx skills list
npx skills update
npx skills remove frontend-design
```

## 6. Crear una Skill paso a paso

1. **Elige una tarea que repitas** y que hoy te obligue a escribir siempre el mismo contexto. El [canvas del taller](../taller/03-skills/canvas-skill.md) ayuda a pensarla.
2. **Hazla una vez a mano con el modelo**, corrigiéndolo hasta que el resultado sea bueno. Anota los pasos que funcionaron, las correcciones que hiciste y el formato final.
3. **Crea la carpeta** con un nombre en minúsculas y guiones, y dentro el `SKILL.md`.
4. **Escribe la descripción** (qué hace y cuándo usarla, con las palabras que usarías).
5. **Escribe el cuerpo**: pasos numerados, reglas concretas, el formato de salida y qué hacer cuando falte información. Escribe solo lo que el modelo no sabría sin ti.
6. **Mueve a archivos aparte** lo que sea largo o solo se necesite a veces (ejemplos, guías de estilo, tablas).
7. **Agrega scripts** si hay pasos que deben ser exactos (cálculos, validaciones, conversiones de formato).
8. **Instálala y pruébala** (sección 8).
9. **Ajusta** con lo que veas en las pruebas.

Atajo: en Claude, pide «Ayúdame a crear una Skill para…» y la Skill [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator) hará las preguntas y generará la carpeta. En Claude Code también puedes usar [`writing-skills`](https://github.com/obra/superpowers/tree/main/skills/writing-skills) de Superpowers.

Ejemplos listos en este repositorio:

- [`presentaciones-con-mi-voz`](../taller/03-skills/skill-demo/presentaciones-con-mi-voz): la Skill del taller.
- [`informe-de-laboratorio`](ejemplos-de-skills/informe-de-laboratorio): con referencias y un script de validación.
- [`tutor-socratico`](ejemplos-de-skills/tutor-socratico): una Skill de comportamiento, sin archivos extra.

## 7. Buenas prácticas

Basadas en la [guía de buenas prácticas de agentskills.io](https://agentskills.io/skill-creation/best-practices) y en la experiencia de los repositorios más usados:

- **Parte de experiencia real.** Una Skill generada sin contexto («escríbeme una Skill de informes») produce instrucciones genéricas. Las buenas salen de un trabajo real: tus correcciones, tus plantillas, los errores que ya cometiste.
- **Agrega lo que el modelo no sabe; omite lo que sabe.** No expliques qué es un PDF. Explica qué librería usar, qué caso borde falla y qué formato espera tu profesor.
- **Mantén el `SKILL.md` corto** (menos de 500 líneas). Lo demás va en archivos referenciados.
- **Referencias a un solo nivel.** El `SKILL.md` puede apuntar a `references/x.md`, pero evita cadenas de archivos que apuntan a otros archivos.
- **Una Skill, una unidad de trabajo coherente.** Ni tan pequeña que necesites cinco para una tarea, ni tan grande que se active cuando no debe.
- **Instrucciones con criterio, no solo órdenes.** Explica por qué existe cada regla; el modelo generaliza mejor.
- **Define la salida.** Un formato explícito (plantilla, ejemplo) da resultados consistentes.
- **Prevé qué hacer cuando falte información**: preguntar, marcar el vacío o detenerse.
- **Usa scripts para lo determinista.** Si algo tiene una única respuesta correcta (un cálculo, una validación), que lo haga código.

## 8. Probar y mejorar una Skill

1. **Prueba de activación:** en un chat nuevo, pide la tarea con palabras distintas a las de la descripción. ¿Se activa? Pide algo parecido pero que no debería activarla. ¿Se mantiene quieta?
2. **Prueba comparativa:** haz la misma tarea con la Skill y sin ella. Si no hay diferencia clara, la Skill no está aportando.
3. **Casos difíciles:** prueba con información incompleta, con un pedido ambiguo y con un caso límite.
4. **Lee el proceso, no solo el resultado.** Si el modelo duda, prueba varios caminos o ignora un paso, las instrucciones de ese paso son vagas.
5. **Itera.** Incluso una sola ronda de «probar y corregir» mejora mucho una Skill.

Para evaluaciones más formales (casos de prueba, criterios y comparación de versiones): [Evaluating skills](https://agentskills.io/skill-creation/evaluating-skills) y la Skill [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator), que incluye un flujo de evaluación.

Para validar el formato:

```bash
# Validador de referencia del estándar
# https://github.com/agentskills/agentskills/tree/main/skills-ref
skills-ref validate ./mi-skill
```

## 9. Seguridad

Una Skill puede incluir instrucciones y código que el agente ejecuta con tus permisos. Instalar una Skill es parecido a instalar un programa:

- **Instala solo de fuentes confiables**: repositorios oficiales de empresas (Anthropic, Microsoft, Vercel, Supabase…) o autores conocidos.
- **Lee el `SKILL.md` y los scripts antes de instalar.** Busca instrucciones para descargar o ejecutar cosas externas, enviar datos a otros sitios o leer archivos que no tienen que ver con la tarea.
- **Desconfía de las Skills que piden más permisos de los necesarios.**
- Los directorios abiertos aceptan Skills de cualquier persona. Por eso se han vuelto populares Skills dedicadas a revisar otras Skills antes de instalarlas (por ejemplo, [`skill-vetter`](https://clawhub.ai/spclaudehome/skills/skill-vetter)). Úsalas como apoyo, no como sustituto de tu propia revisión.
- **No pongas contraseñas, tokens ni datos personales dentro de una Skill**, sobre todo si la vas a publicar.

## 10. Catálogo de Skills populares

Las cifras de instalaciones son las de [skills.sh](https://skills.sh), el directorio de Skills más usado, según el corte del **22 de octubre de 2026** publicado por [LinklyAI/best-skills](https://github.com/LinklyAI/best-skills). Cambian todos los días; tómalas como referencia del orden de magnitud.

### 10.1 Skills oficiales de Anthropic

Repositorio: [anthropics/skills](https://github.com/anthropics/skills). Varias ya vienen incluidas en Claude; las de documentos (`docx`, `pdf`, `pptx`, `xlsx`) son las que Claude usa internamente para crear archivos.

| Skill | Para qué sirve | Instalaciones |
|---|---|---|
| [`frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Diseño visual de interfaces con criterio estético, evitando el aspecto genérico | ≈ 1,0 M |
| [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Crear, mejorar y evaluar Skills | ≈ 412 mil |
| [`pptx`](https://github.com/anthropics/skills/tree/main/skills/pptx) | Crear, leer y editar presentaciones de PowerPoint | ≈ 240 mil |
| [`pdf`](https://github.com/anthropics/skills/tree/main/skills/pdf) | Extraer texto y tablas, unir, dividir y llenar formularios PDF | ≈ 215 mil |
| [`docx`](https://github.com/anthropics/skills/tree/main/skills/docx) | Crear y editar documentos de Word, con control de cambios y comentarios | ≈ 205 mil |
| [`xlsx`](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Hojas de cálculo con fórmulas, formato y gráficos | ≈ 186 mil |
| [`webapp-testing`](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | Probar aplicaciones web locales con Playwright | ≈ 184 mil |
| [`mcp-builder`](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | Construir servidores MCP en Python o TypeScript | ≈ 130 mil |
| [`canvas-design`](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | Pósteres y piezas visuales en PNG o PDF | ≈ 120 mil |
| [`web-artifacts-builder`](https://github.com/anthropics/skills/tree/main/skills/web-artifacts-builder) | Artefactos web complejos con React, Tailwind y shadcn/ui | ≈ 111 mil |
| [`doc-coauthoring`](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) | Flujo guiado para coescribir documentos, propuestas y especificaciones | ≈ 93 mil |
| [`algorithmic-art`](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) | Arte generativo con p5.js | ≈ 88 mil |
| [`claude-api`](https://github.com/anthropics/skills/tree/main/skills/claude-api) | Referencia de la API de Claude y sus SDK | ≈ 73 mil |

### 10.2 Las más instaladas de la comunidad

| Skill | Autor | Para qué sirve | Instalaciones |
|---|---|---|---|
| [`find-skills`](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) | Vercel | Busca e instala Skills cuando preguntas «¿hay una Skill para…?» | ≈ 4,0 M |
| [`grill-me`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) | Matt Pocock | Entrevista exhaustiva para afinar un plan o un diseño antes de actuar | ≈ 1,4 M |
| [`agent-browser`](https://skills.sh/vercel-labs/agent-browser/agent-browser) | Vercel | Automatización de navegador para agentes | ≈ 1,2 M |
| [`improve-codebase-architecture`](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) | Matt Pocock | Busca mejoras de arquitectura en un código y las presenta en un informe | ≈ 1,2 M |
| [`hyperframes`](https://skills.sh/heygen-com/hyperframes/hyperframes) | HeyGen | Creación de video y animación con código | ≈ 1,1 M |
| [`tdd`](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) | Matt Pocock | Desarrollo guiado por pruebas (rojo, verde, refactor) | ≈ 1,1 M |
| [`handoff`](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) | Matt Pocock | Resume la conversación en un documento para que otro agente continúe | ≈ 1,0 M |
| [`teach`](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) | Matt Pocock | Enseña un concepto o habilidad nueva paso a paso | ≈ 850 mil |
| [`diagnosing-bugs`](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) | Matt Pocock | Ciclo de diagnóstico para errores difíciles y problemas de rendimiento | ≈ 823 mil |
| [`vercel-react-best-practices`](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) | Vercel | Buenas prácticas de rendimiento en React y Next.js | ≈ 826 mil |
| [`web-design-guidelines`](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | Vercel | Revisa interfaces contra pautas de diseño y accesibilidad | ≈ 768 mil |
| [`remotion-best-practices`](https://skills.sh/remotion-dev/skills/remotion-best-practices) | Remotion | Video programático con React | ≈ 659 mil |
| [`ui-ux-pro-max`](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max) | Next Level Builder | Criterios de diseño UI/UX | ≈ 408 mil |
| [`brainstorming`](https://github.com/obra/superpowers/tree/main/skills/brainstorming) | Jesse Vincent (Superpowers) | Explora el problema y el diseño antes de escribir código | ≈ 401 mil |

### 10.3 Superpowers: una metodología completa

[obra/superpowers](https://github.com/obra/superpowers) es uno de los repositorios de Skills más seguidos de GitHub. No es una Skill suelta sino un conjunto que impone un método de desarrollo: lluvia de ideas, plan, implementación con subagentes, pruebas y revisión.

| Skill | Qué hace |
|---|---|
| [`brainstorming`](https://github.com/obra/superpowers/tree/main/skills/brainstorming) | Refina la idea con preguntas antes de cualquier trabajo creativo |
| [`writing-plans`](https://github.com/obra/superpowers/tree/main/skills/writing-plans) | Convierte requisitos en un plan de implementación detallado |
| [`subagent-driven-development`](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development) | Ejecuta el plan con un subagente por tarea y revisión entre tareas |
| [`test-driven-development`](https://github.com/obra/superpowers/tree/main/skills/test-driven-development) | Obliga a escribir la prueba antes que el código |
| [`systematic-debugging`](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging) | Depuración en fases: reproducir, aislar, diagnosticar, corregir |
| [`verification-before-completion`](https://github.com/obra/superpowers/tree/main/skills/verification-before-completion) | Exige evidencia antes de dar algo por terminado |
| [`dispatching-parallel-agents`](https://github.com/obra/superpowers/tree/main/skills/dispatching-parallel-agents) | Reparte tareas independientes entre agentes en paralelo |
| [`writing-skills`](https://github.com/obra/superpowers/tree/main/skills/writing-skills) | Crear y probar Skills nuevas |

### 10.4 Skills oficiales de empresas de tecnología

Muchas empresas publican Skills para que los agentes usen bien sus productos. Si trabajas con alguna de estas herramientas, conviene instalarlas.

| Empresa | Repositorio | Ejemplos |
|---|---|---|
| Microsoft | [microsoft/azure-skills](https://github.com/microsoft/azure-skills) | `azure-deploy`, `azure-diagnostics`, `azure-ai` (≈ 560 mil cada una) |
| Vercel | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `deploy-to-vercel`, `vercel-composition-patterns`, `vercel-react-native-skills` |
| Supabase | [supabase/agent-skills](https://github.com/supabase/agent-skills) | `supabase-postgres-best-practices` (≈ 455 mil), `supabase` |
| Prisma | [prisma/skills](https://github.com/prisma/skills) | `prisma-client-api`, `prisma-cli`, `prisma-database-setup` |
| Neon | [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) | `neon-postgres` |
| Firebase | [firebase/agent-skills](https://github.com/firebase/agent-skills) | `firebase-basics`, `firebase-auth-basics` |
| Cloudflare | [cloudflare/skills](https://github.com/cloudflare/skills) | `wrangler`, `workers-best-practices` |
| Stripe | [stripe/ai](https://github.com/stripe/ai) | `stripe-best-practices` |
| Remotion | [remotion-dev/skills](https://github.com/remotion-dev/skills) | `remotion-best-practices`, `remotion-render` |

### 10.5 Recomendadas para estudiantes

| Si quieres… | Prueba |
|---|---|
| Trabajar con PDF, Word, Excel o PowerPoint | `pdf`, `docx`, `xlsx`, `pptx` (ya incluidas en Claude) |
| Aprender un tema nuevo con guía | [`teach`](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach) o la Skill [`tutor-socratico`](ejemplos-de-skills/tutor-socratico) de este repositorio |
| Pensar mejor un proyecto antes de empezarlo | [`grill-me`](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) o [`brainstorming`](https://github.com/obra/superpowers/tree/main/skills/brainstorming) |
| Coescribir un documento largo | [`doc-coauthoring`](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) |
| Programar con buenas prácticas | [`tdd`](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd), [`systematic-debugging`](https://github.com/obra/superpowers/tree/main/skills/systematic-debugging) |
| Probar una página web que hiciste | [`webapp-testing`](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) |
| Crear tus propias Skills | [`skill-creator`](https://github.com/anthropics/skills/tree/main/skills/skill-creator) |
| Encontrar una Skill para algo | [`find-skills`](https://github.com/vercel-labs/skills/tree/main/skills/find-skills) |

## 11. Dónde encontrar más

| Directorio o lista | Qué tiene |
|---|---|
| [skills.sh](https://skills.sh) | Directorio y ranking de Skills, con el comando de instalación de cada una |
| [agentskills.io](https://agentskills.io) | Estándar abierto, especificación y guías de creación |
| [anthropics/skills](https://github.com/anthropics/skills) | Skills oficiales de Anthropic y plantilla |
| [LinklyAI/best-skills](https://github.com/LinklyAI/best-skills) | Rankings diarios de varios directorios, con datos abiertos en CSV |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | Lista curada de Skills y recursos |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Lista curada por categorías |
| [openai/skills](https://github.com/openai/skills) | Skills publicadas por OpenAI para Codex |

**Documentación oficial**

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills) (Centro de ayuda de Claude)
- [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Skills en Claude Code](https://code.claude.com/docs/en/skills)
- [Especificación de Agent Skills](https://agentskills.io/specification)
- [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (artículo de ingeniería de Anthropic)
