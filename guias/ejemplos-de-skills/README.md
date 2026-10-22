# Ejemplos de Skills para estudiantes

Skills listas para usar o adaptar. Cada carpeta es una Skill completa que cumple la [especificación de Agent Skills](https://agentskills.io/specification).

| Skill | Qué hace | Qué muestra como ejemplo |
|---|---|---|
| [`informe-de-laboratorio`](informe-de-laboratorio) | Estructura, redacta por secciones y revisa informes de laboratorio | Uso de `references/` para material largo y de `scripts/` para una validación exacta |
| [`tutor-socratico`](tutor-socratico) | Guía con preguntas y pistas en lugar de dar respuestas | Una Skill de comportamiento: solo instrucciones, sin archivos extra |

La Skill del taller, [`presentaciones-con-mi-voz`](../../taller/03-skills/skill-demo/presentaciones-con-mi-voz), muestra el uso de referencias de estilo y ejemplos.

## Cómo instalarlas

**En Claude:** comprime la carpeta de la Skill (no su contenido suelto) en un `.zip` y súbela en **Customize > Skills > + > Create skill > Upload a skill**.

**En Claude Code:** copia la carpeta en `~/.claude/skills/` o en `.claude/skills/` de tu proyecto.

**En cualquier agente compatible:**

```bash
npx skills add DeiberD/taller-prompt-engineering --full-depth --skill tutor-socratico
npx skills add DeiberD/taller-prompt-engineering --full-depth --skill informe-de-laboratorio
```

## Probar el script de validación

```bash
cd informe-de-laboratorio
python scripts/validar_informe.py ruta/a/tu-informe.md
```

Más información en la [guía de Skills](../02-skills.md).
