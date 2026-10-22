# El mismo pedido en cinco formatos

El pedido de base es siempre el mismo: **el contenido de una presentación de 8 diapositivas sobre la regla de la cadena, para compañeros de primer semestre.** Lo único que cambia es la forma de escribirlo.

## 1. Lenguaje natural

Útil para pedidos cortos o cuando conversas con el modelo.

```text
Actúa como monitor de Cálculo Diferencial. Voy a exponer 10 minutos ante
compañeros de primer semestre que no han visto la regla de la cadena.
Escríbeme el contenido de 8 diapositivas: para cada una, un título, máximo
3 viñetas de no más de 15 palabras y una nota corta para mí como expositor.
No uses demostraciones formales y, si no estás seguro de algo, dímelo.
Empieza con una pregunta o un ejemplo cotidiano, como hago yo.
```

## 2. Markdown

Útil cuando el prompt es largo y quieres que cada parte se lea por separado.

```markdown
# Rol
Monitor de Cálculo Diferencial de la UNAL.

# Contexto
- Exposición de 10 minutos en clase.
- Público: compañeros de primer semestre que no han visto el tema.

# Tarea
Escribe el contenido de 8 diapositivas sobre la regla de la cadena.

# Formato
Para cada diapositiva:
1. Título
2. Máximo 3 viñetas (15 palabras por viñeta como máximo)
3. Nota para el expositor (1 o 2 frases)

# Restricciones
- Sin demostraciones formales.
- Si no estás seguro de un dato, dilo.
```

## 3. Etiquetas XML

Útil cuando el prompt mezcla instrucciones con material (apuntes, un enunciado, un documento). Las etiquetas le dicen al modelo qué es instrucción y qué es dato. Los nombres de las etiquetas son libres; lo importante es usarlos de forma consistente.

```xml
<rol>Monitor de Cálculo Diferencial de la UNAL.</rol>

<contexto>
Exposición de 10 minutos para compañeros de primer semestre
que no han visto el tema.
</contexto>

<apuntes>
(Aquí se pegan los apuntes de clase sobre la regla de la cadena.)
</apuntes>

<tarea>
Usando solo lo que está en <apuntes>, escribe el contenido de
8 diapositivas sobre la regla de la cadena.
</tarea>

<formato>
Por diapositiva: título, máximo 3 viñetas y una nota para el expositor.
</formato>

<restricciones>
Sin demostraciones formales. Si algo no está en los apuntes, avísame.
</restricciones>
```

## 4. JSON

Útil cuando la salida la va a procesar un programa (por ejemplo, un script que genera las diapositivas) o necesitas una estructura exacta.

```text
Escribe el contenido de 8 diapositivas sobre la regla de la cadena para
compañeros de primer semestre. Responde SOLO con un JSON válido que siga
exactamente este esquema, sin texto antes ni después:

{
  "titulo_presentacion": "string",
  "diapositivas": [
    {
      "numero": 1,
      "titulo": "string",
      "vinetas": ["string", "string", "string"],
      "nota_expositor": "string"
    }
  ]
}

Reglas: máximo 3 viñetas por diapositiva, máximo 15 palabras por viñeta,
sin demostraciones formales.
```

Si usas la API, varios proveedores ofrecen **salidas estructuradas**: le pasas un esquema JSON y el modelo queda obligado a respetarlo. Es más confiable que pedirlo solo con palabras.

## 5. Few-shot (con ejemplos)

Útil cuando el estilo es difícil de describir pero fácil de mostrar. Se dan uno a tres ejemplos de entrada y salida y luego el caso nuevo.

```text
Escribe diapositivas con el estilo de estos ejemplos.

Ejemplo 1
Tema: derivada
Diapositiva:
  Título: ¿Qué tan rápido cambia algo?
  - Velocidad de un bus: cuánto avanza por cada segundo.
  - La derivada mide eso mismo, en cualquier función.
  Nota: pregunta al público cuánto se demora el bus a la U.

Ejemplo 2
Tema: límite
Diapositiva:
  Título: Acercarse sin tocar
  - Caminar hacia una pared dando pasos cada vez más cortos.
  - El límite es a dónde llegas, aunque nunca la toques.
  Nota: haz el gesto de los pasos con la mano.

Ahora tú
Tema: regla de la cadena
Diapositiva:
```

Fíjate en que los ejemplos no explican el estilo: lo muestran. El modelo imita la estructura, el tono (preguntas, ejemplos cotidianos) y la longitud.

## Cómo elegir

- ¿Es corto y lo vas a conversar? **Lenguaje natural.**
- ¿Es largo y tiene varias partes? **Markdown.**
- ¿Pegas documentos, datos o código junto con las instrucciones? **XML.**
- ¿Lo va a leer un programa? **JSON** (y, si puedes, salidas estructuradas).
- ¿Te cuesta describir el estilo? **Few-shot.**

Los formatos se combinan: un prompt en XML puede incluir ejemplos few-shot dentro de una etiqueta `<ejemplos>`.
