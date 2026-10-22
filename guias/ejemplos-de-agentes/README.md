# Ejemplos de agentes especializados

Subagentes listos para copiar en Claude Code y un ejemplo con el Claude Agent SDK.

| Archivo | Qué hace | Herramientas |
|---|---|---|
| [`revisor-de-codigo.md`](revisor-de-codigo.md) | Revisa cambios de código, ejecuta las pruebas y da pistas sin reescribir | Read, Grep, Glob, Bash |
| [`analista-de-datos.md`](analista-de-datos.md) | Explora datos con Python y deja un script reproducible | Read, Write, Bash, Glob |
| [`investigador.md`](investigador.md) | Investiga un subtema en la web y devuelve hallazgos con fuentes | WebSearch, WebFetch, Read |
| [`../../taller/04-agentes/.claude/agents/revisor-de-fuentes.md`](../../taller/04-agentes/.claude/agents/revisor-de-fuentes.md) | Verifica referencias bibliográficas (el de la demo del taller) | Read, Grep, Glob, WebSearch, WebFetch |
| [`agente_sdk.py`](agente_sdk.py) | Agente en Python con un subagente revisor de fuentes | SDK |

## Usar los subagentes en Claude Code

1. Copia el archivo `.md` en una de estas carpetas:
   - `.claude/agents/` dentro de tu proyecto (solo ese proyecto).
   - `~/.claude/agents/` (todos tus proyectos).
2. Abre Claude Code y escribe `/agents` para confirmar que aparece.
3. Pídelo por su nombre («Usa el investigador para…») o deja que Claude lo elija según la descripción.

## Patrón de ejemplo: investigación en paralelo

Con el subagente `investigador` instalado:

```text
Quiero comparar tres lenguajes para un proyecto de análisis de datos:
Python, R y Julia. Lanza un subagente investigador por lenguaje, en
paralelo, con la pregunta «¿cuáles son sus fortalezas y limitaciones para
análisis de datos en 2026?». Cuando terminen, arma una tabla comparativa
con las fuentes de cada fila.
```

El agente principal reparte el trabajo (patrón orquestador y trabajadores), cada investigador lee sus fuentes con su propio contexto y el principal solo combina los resúmenes.

## Ejecutar el ejemplo del SDK

```bash
pip install claude-agent-sdk
export ANTHROPIC_API_KEY="tu-clave"   # en Windows PowerShell: $env:ANTHROPIC_API_KEY="tu-clave"
python agente_sdk.py ../../taller/04-agentes/informe-de-prueba.md
```

El uso de la API tiene costo. El script imprime el costo aproximado al final.

## Antes de usar agentes de terceros

Lee el archivo completo. Fíjate en qué herramientas pide y si las instrucciones hacen algo distinto de lo que dice la descripción. Más en la [guía de agentes](../03-agentes-especializados.md#9-riesgos-y-buenas-prácticas).
