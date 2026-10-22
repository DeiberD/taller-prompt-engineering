# Canvas de diseño de Skill

Llénalo para una tarea que repitas **al menos una vez por semana**. Si no puedes responder alguna casilla, todavía no es momento de convertir esa tarea en Skill.

| Casilla | Pregunta | Tu respuesta |
|---|---|---|
| **Tarea** | ¿Qué tarea repito con frecuencia? | |
| **Descripción** | ¿Con qué palabras la pido? (Esto define cuándo se activa la Skill.) | |
| **Nombre** | Nombre corto en minúsculas y con guiones (por ejemplo, `informe-de-laboratorio`) | |
| **Pasos** | ¿Qué pasos sigo siempre, en orden? | |
| **Reglas** | ¿Qué reglas de estilo o de calidad aplico? | |
| **Referencias** | ¿Qué archivo de ejemplo, plantilla o guía de estilo adjuntaría? | |
| **Scripts** | ¿Hay algún cálculo o conversión que debería hacer un programa y no el modelo? | |
| **Prueba** | ¿Cómo sabré que la Skill funcionó mejor que un prompt suelto? | |

## Ideas de Skills para estudiantes de ingeniería

- `informe-de-laboratorio`: estructura de informe con el formato que pide tu facultad (ver el ejemplo en [`guias/ejemplos-de-skills`](../../guias/ejemplos-de-skills)).
- `tutor-socratico`: explica un tema con preguntas, sin dar la respuesta de inmediato.
- `acta-de-reunion`: convierte notas sueltas de una reunión del grupo de estudio en un acta con decisiones y responsables.
- `revision-de-codigo`: revisa tu código con los criterios del curso de programación.
- `resumen-de-lectura`: resume artículos con la estructura que usa tu profesor (pregunta, método, resultados, crítica).
- `correo-formal`: redacta correos a profesores o dependencias con el tono adecuado.

## De canvas a Skill

```
nombre-de-tu-skill/
├── SKILL.md            <- casillas Descripción, Pasos y Reglas
├── referencias/        <- casilla Referencias
│   └── ejemplo.md
└── scripts/            <- casilla Scripts (opcional)
```

Guía completa: [`guias/02-skills.md`](../../guias/02-skills.md).
