# Respuestas: ¿prompt, Skill, agente o subagentes?

| | Tarea | Respuesta | Razón |
|---|---|---|---|
| a | Traducir el resumen de un artículo | **Prompt** | Tarea única y corta. Basta con un buen prompt con contexto (para qué curso, qué registro). |
| b | Acta semanal con el mismo formato | **Skill** | Se repite y tiene formato fijo. La Skill guarda la plantilla y las reglas una sola vez. |
| c | Encontrar por qué falla el proyecto | **Agente** | Hay que leer código, ejecutar pruebas, interpretar resultados y decidir el siguiente paso. Son varios pasos con herramientas y decisiones sobre la marcha. |
| d | Comparar cinco planes de estudio largos | **Subagentes** | Son cinco partes grandes e independientes. Un subagente por universidad lee su plan con contexto limpio y devuelve un resumen; el agente principal solo compara los resúmenes. |
| e | Correo de prórroga | **Prompt** | Tarea única y corta. |
| f | Exposiciones del semestre con el mismo estilo | **Skill** | Se repite con un estilo fijo. Es justamente la Skill de la [Actividad 3](../03-skills). |

## Discusión frecuente

- **«¿La c no podría ser con subagentes?»** Podría, si el proyecto es grande y hay partes independientes (por ejemplo, un subagente que revise el backend y otro el frontend). Pero para un error concreto, un solo agente que sigue el hilo suele ser más eficiente: el diagnóstico depende de lo que va encontrando.
- **«¿La d no se puede hacer con un prompt?»** Se puede pegar todo en un chat, pero cinco documentos largos saturan el contexto y el modelo empieza a mezclar o a olvidar detalles. Los subagentes evitan eso porque cada uno trabaja aparte.
- **«¿Y si combino?»** Es lo normal: un agente puede usar Skills y lanzar subagentes. La pregunta del ejercicio es cuál es la pieza mínima que resuelve la tarea.

## Regla para recordar

**La solución más simple que funcione es la mejor.** Más agentes no es mejor: cuestan más (cada uno consume tokens), tardan más y sus resultados son más difíciles de verificar.
