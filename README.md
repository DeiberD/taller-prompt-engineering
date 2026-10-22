# Taller de Prompt Engineering

Material del taller **Prompt Engineering** para estudiantes de pregrado de la Universidad Nacional de Colombia, sede Bogotá, que usan Claude u otros modelos de lenguaje (LLM).

El repositorio tiene dos partes:

- **`taller/`**: todo lo que se usa durante las dos horas del taller, actividad por actividad (plantillas, ejemplos, la Skill de demostración, los subagentes y los casos).
- **`guias/`**: material de estudio para después del taller. Explica con más profundidad qué es el prompt engineering, cómo funcionan y se crean las Skills (con un catálogo de las más usadas) y cómo diseñar agentes especializados.

Propuesto y moderado por **Deiber David Gongora Hurtado**, Grupos de Estudio Autónomo (GEA), Facultad de Ingeniería.

## Datos del taller

| | |
|---|---|
| **Dirigido a** | Estudiantes de la sede Bogotá de la UNAL que usen Claude u otros LLM |
| **Duración** | 1 h 45 min de taller + 15 min de preguntas (2 horas en total) |
| **Modalidad** | Virtual y práctica |
| **Requisitos** | Computador con acceso a Claude (sirve el plan gratuito) u otro LLM |

## Objetivos

Al terminar el taller, cada asistente podrá:

1. **Estructura y formatos del prompt.** Reescribir un prompt vago con las seis piezas (rol, contexto, tarea, formato, restricciones y ejemplos) y elegir el formato adecuado (lenguaje natural, Markdown, etiquetas XML, JSON o few-shot).
2. **Skills.** Explicar qué es una Skill y en qué se diferencia de un prompt suelto, crear una desde cero (carpeta, `SKILL.md`, descripción y referencias) y comprobar con una prueba comparativa que mejora el resultado.
3. **Agentes y subagentes.** Distinguir un chat, un workflow y un agente; decidir si una tarea necesita un prompt, una Skill, un agente o subagentes, y describir cómo se despliega un subagente.
4. **Uso consciente.** Detectar errores típicos de una respuesta generada (datos falsos, citas y cifras inventadas, exceso de seguridad) y verificarlos.
5. **Marco normativo.** Conocer las normas de la UNAL y de Colombia que aplican al uso de la IA, y citar y declarar ese uso.

## Agenda

| Momento | Actividad | Duración | Material |
|---|---|---|---|
| 0:00–0:10 | 1. El mismo pedido, dos prompts (rompehielos) | 10 min | [`taller/01-el-mismo-pedido`](taller/01-el-mismo-pedido) |
| 0:10–0:35 | 2. Anatomía del prompt (estructura y formatos) | 25 min | [`taller/02-anatomia-del-prompt`](taller/02-anatomia-del-prompt) |
| 0:35–1:05 | 3. Crea tu propia Skill | 30 min | [`taller/03-skills`](taller/03-skills) |
| 1:05–1:20 | 4. ¿Prompt, Skill, agente o subagentes? | 15 min | [`taller/04-agentes`](taller/04-agentes) |
| 1:20–1:30 | 5. Detective de respuestas (uso consciente) | 10 min | [`taller/05-detective-de-respuestas`](taller/05-detective-de-respuestas) |
| 1:30–1:45 | 6. La IA y las reglas de juego en la UNAL | 15 min | [`taller/06-marco-normativo-unal`](taller/06-marco-normativo-unal) |
| 1:45–2:00 | Preguntas y respuestas | 15 min | |

## Estructura del repositorio

```
taller-prompt-engineering/
├── README.md
├── taller/
│   ├── 01-el-mismo-pedido/          Rompehielos: el prompt sin contexto
│   ├── 02-anatomia-del-prompt/      Seis piezas, cinco formatos y laboratorio
│   ├── 03-skills/                   Skill de demostración lista para subir y canvas
│   ├── 04-agentes/                  Subagentes de ejemplo y tareas para clasificar
│   ├── 05-detective-de-respuestas/  Respuesta con errores plantados
│   └── 06-marco-normativo-unal/     Normas, casos, citación y compromiso
└── guias/
    ├── 01-prompt-engineering.md     Guía completa de prompt engineering
    ├── 02-skills.md                 Qué son, cómo se crean y catálogo de las más usadas
    ├── 03-agentes-especializados.md Cómo diseñar y desplegar agentes y subagentes
    ├── 04-glosario.md
    ├── 05-recursos.md               Documentación, cursos, artículos y repositorios
    ├── ejemplos-de-skills/          Skills adicionales para estudiantes
    └── ejemplos-de-agentes/         Subagentes adicionales para estudiantes
```

## Cómo usar este repositorio

**Si vas a asistir al taller:** no necesitas descargar nada antes. Durante cada actividad el moderador te indicará qué carpeta abrir.

**Si quieres repasar después:** empieza por [`guias/01-prompt-engineering.md`](guias/01-prompt-engineering.md) y sigue en orden. Cada guía termina con enlaces a fuentes oficiales.

**Si quieres usar la Skill de demostración:** sigue las instrucciones de [`taller/03-skills/README.md`](taller/03-skills/README.md). Puedes descargar el repositorio con el botón **Code > Download ZIP** de GitHub o con:

```bash
git clone https://github.com/DeiberD/taller-prompt-engineering.git
```

## Uso responsable

Todo lo que entrega una IA se verifica, se cita y se declara. Antes de usar IA en un curso, revisa las reglas del programa de la asignatura y las indicaciones del profesor. La sección [`taller/06-marco-normativo-unal`](taller/06-marco-normativo-unal) resume la normativa vigente; es una orientación y no constituye asesoría jurídica.

## Contribuciones

Si encuentras un error, un enlace roto o una norma desactualizada, abre un *issue* o un *pull request*.
