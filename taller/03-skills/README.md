# Actividad 3. Crea tu propia Skill

**Duración:** 30 minutos (concepto 5, demo del problema 5, construcción guiada 15, canvas personal 5) · **Objetivo:** Skills

Una **Skill** es una carpeta con instrucciones (el archivo `SKILL.md`) y recursos opcionales que el modelo carga solo cuando la tarea lo necesita. A diferencia de un prompt suelto, se escribe una vez y se reutiliza. En esta actividad se construye en vivo una Skill que genera presentaciones con la voz del autor.

## Archivos de esta carpeta

| Archivo | Para qué sirve |
|---|---|
| [`skill-demo/presentaciones-con-mi-voz/`](skill-demo/presentaciones-con-mi-voz) | La Skill terminada, lista para adaptar y subir |
| [`canvas-skill.md`](canvas-skill.md) | Canvas para diseñar tu propia Skill |

## 1. Estructura de una Skill

```
presentaciones-con-mi-voz/
├── SKILL.md            <- descripción e instrucciones
└── referencias/
    ├── mi-estilo.md    <- cómo escribo y cómo hablo
    └── ejemplo.md      <- una presentación mía que funcionó
```

El `SKILL.md` empieza con un encabezado (frontmatter YAML) con dos campos obligatorios:

```yaml
---
name: presentaciones-con-mi-voz
description: Genera el contenido de presentaciones académicas con mi estilo
  personal. Úsala cuando pida diapositivas, una exposición, una presentación
  para una clase o el guion de una charla.
---
```

- **`name`**: minúsculas, números y guiones; debe coincidir con el nombre de la carpeta.
- **`description`**: qué hace y **cuándo usarla**. Es lo único que el modelo lee de todas tus Skills al empezar una conversación; con eso decide si la activa. Si es vaga, la Skill no se activa.

## 2. El problema que resuelve

Sin Skill, cada vez que pides una presentación tienes que volver a escribir todo el contexto de la Actividad 2: audiencia, formato, estilo, ejemplo. Y aun así, el estilo cambia de una respuesta a otra. La Skill guarda ese contexto una vez y el modelo lo carga solo cuando hace falta.

## 3. Construcción guiada

1. Descarga la carpeta [`skill-demo/presentaciones-con-mi-voz`](skill-demo/presentaciones-con-mi-voz) o créala desde cero con un editor de texto.
2. Edita [`referencias/mi-estilo.md`](skill-demo/presentaciones-con-mi-voz/referencias/mi-estilo.md) con 5 a 10 rasgos de cómo escribes tú.
3. Reemplaza [`referencias/ejemplo.md`](skill-demo/presentaciones-con-mi-voz/referencias/ejemplo.md) por una presentación tuya que haya funcionado.
4. Si quieres, ajusta los pasos y reglas en [`SKILL.md`](skill-demo/presentaciones-con-mi-voz/SKILL.md).
5. Instálala (ver abajo).
6. **Prueba comparativa:** en un chat nuevo escribe un pedido corto («Hazme la presentación de la exposición de mañana sobre…») y compáralo con lo que obtuviste sin Skill en la Actividad 1.

## 4. Cómo instalarla

### En Claude (web, escritorio o móvil)

1. Activa la ejecución de código: **Settings > Capabilities > Code execution and file creation**. Las Skills la necesitan para funcionar. (En planes Team o Enterprise, quien administra la organización debe habilitarla.)
2. Comprime la carpeta `presentaciones-con-mi-voz` en un archivo `.zip`. El zip debe contener la carpeta, no solo los archivos sueltos.
   - Windows: clic derecho sobre la carpeta > **Enviar a > Carpeta comprimida**.
   - macOS: clic derecho > **Comprimir**.
   - Linux o terminal: `zip -r presentaciones-con-mi-voz.zip presentaciones-con-mi-voz`
3. Ve a **Customize > Skills**, pulsa **+ > Create skill > Upload a skill** y sube el `.zip`.
4. Verifica que la Skill aparezca activada en la lista.

Los nombres de los menús pueden cambiar; la referencia oficial es [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### En Claude Code

Copia la carpeta en una de estas rutas:

- `~/.claude/skills/presentaciones-con-mi-voz/` para tenerla en todos tus proyectos.
- `.claude/skills/presentaciones-con-mi-voz/` dentro de un proyecto para compartirla con quien clone el repositorio.

Claude Code la detecta sola. También puedes invocarla directamente con `/presentaciones-con-mi-voz`.

### En otros agentes

Las Skills siguen un estándar abierto ([agentskills.io](https://agentskills.io)) que también soportan, entre otros, Codex, Gemini CLI, Cursor, GitHub Copilot y VS Code. Con la herramienta de línea de comandos [`skills`](https://github.com/vercel-labs/skills) (requiere Node.js 22.20 o superior) puedes instalarla en el agente que uses. Como la Skill está dentro de subcarpetas, hay que agregar `--full-depth`:

```bash
npx skills add DeiberD/taller-prompt-engineering --full-depth --skill presentaciones-con-mi-voz
```

El comando pregunta en qué agente instalarla. Agrega `-g` para que quede disponible en todos tus proyectos.

## 5. Canvas personal

Llena el [canvas](canvas-skill.md) para una Skill tuya, pensada para una tarea que repitas al menos una vez por semana.

## Notas para el moderador

- Tener esta carpeta lista como respaldo por si falla la conexión o la subida del archivo.
- Insistir en la **descripción**: es la causa más común de que una Skill no se active.
- Para profundizar: [guía de Skills](../../guias/02-skills.md).
