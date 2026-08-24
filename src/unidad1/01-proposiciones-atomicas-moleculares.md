# 1.1 Proposiciones Atómicas y Moleculares

El punto de partida del análisis lógico formal es el concepto de **proposición**. En el lenguaje ordinario utilizamos oraciones para diversos propósitos: formular preguntas, impartir órdenes, expresar emociones o hacer declaraciones. Sin embargo, la lógica matemática se restringe rigurosamente a aquellos enunciados de los cuales tiene sentido predicar su verdad o falsedad.

---

## 1. Definición Formal de Proposición

> **Definición 1.1 (Proposición Lógica):**  
> Una **proposición** es cualquier enunciado declarativo del cual se puede afirmar inequívocamente su valor de verdad: o bien es **verdadero (\\(V\\))**, o bien es **falso (\\(F\\))**, pero no ambos simultáneamente.

A este principio fundamental de la lógica clásica se le conoce como el **Principio de Bivalencia**:
1. **Principio del Tercio Excluso:** Todo enunciado es verdadero o es falso; no existe una tercera posibilidad intermedia.
2. **Principio de No Contradicción:** Ningún enunciado puede ser simultáneamente verdadero y falso bajo la misma interpretación y en el mismo contexto.

### Ejemplos de Proposiciones Matemáticas
* \\(p\\): "El número 17 es un número primo." \\(\to\\) Es una proposición con valor de verdad **Verdadero (\\(V\\))**.
* \\(q\\): "\\(2 + 3 = 7\\)." \\(\to\\) Es una proposición con valor de verdad **Falso (\\(F\\))**.
* \\(r\\): "Para todo número real \\(x\\), se cumple que \\(x^2 \ge 0\\)." \\(\to\\) Es una proposición con valor de verdad **Verdadero (\\(V\\))**.

### Enunciados que NO son Proposiciones
* "¿Cuál es el valor de \\(x\\)?" (Oración interrogativa).
* "¡Calcula la derivada de la función!" (Oración imperativa).
* "\\(x + 5 = 12\\)" (Enunciado abierto o función proposicional; su valor de verdad no puede determinarse hasta que se especifique el valor de la variable libre \\(x\\)).
* "Esta afirmación es falsa" (Paradoja del mentiroso; viola el principio de no contradicción).

---

## 2. Clasificación: Proposiciones Atómicas y Moleculares

Las proposiciones se clasifican estructuralmente según su grado de complejidad sintáctica:

### A. Proposiciones Atómicas (o Simples)
Son aquellas que expresan una única propiedad o relación directa y no contienen conectivas lógicas ni pueden descomponerse en proposiciones más elementales. Se representan simbólicamente mediante letras proposicionales minúsculas:

\\[
p, \quad q, \quad r, \quad s, \quad t, \quad \dots
\\]

**Ejemplos:**
* \\(p\\): "El triángulo equilátero tiene sus tres lados de igual longitud."
* \\(q\\): "El número \\(\pi\\) es irracional."

### B. Proposiciones Moleculares (o Compuestas)
Son enunciados formados por la combinación de una o más proposiciones atómicas mediante operadores sintácticos denominados **conectivas lógicas** (como la negación \\(\neg\\), la conjunción \\(\land\\), la disyunción \\(\lor\\), el condicional \\(\to\\) y el bicondicional \\(\leftrightarrow\\)).

El valor de verdad de una proposición molecular queda **completamente determinado** por:
1. Los valores de verdad individuales de las proposiciones atómicas que la constituyen.
2. La definición semántica formal de las conectivas empleadas.

**Ejemplos:**
* \\(p \land q\\): "El número 7 es primo **y** el número 8 es par."
* \\(\neg r\\): "**No** es cierto que \\(\sqrt{2}\\) sea un número racional."
* \\(p \to q\\): "**Si** un cuadrilátero es un cuadrado, **entonces** es un paralelogramo."

---

## 3. Clasificación Semántica de Enunciados

| Tipo de Enunciado | Estructura Sintáctica | Ejemplo Matemático | Valor de Verdad |
| :--- | :--- | :--- | :--- |
| **Atómica** | No descomponible (un solo predicado) | \\(p\\): "\\(2^3 = 8\\)" | \\(V\\) |
| **Atómica** | No descomponible | \\(q\\): "\\(5 < 3\\)" | \\(F\\) |
| **Molecular** | Unión por conectiva \\(\land\\) | \\(p \land q\\): "\\(2^3 = 8\\) y \\(5 < 3\\)" | \\(F\\) |
| **Molecular** | Unión por conectiva \\(\lor\\) | \\(p \lor q\\): "\\(2^3 = 8\\) o \\(5 < 3\\)" | \\(V\\) |
| **No Proposición** | Enunciado abierto | "\\(x^2 - 1 = 0\\)" | Indeterminado (depende de \\(x\\)) |
| **No Proposición** | Directiva / Exclamación | "¡Demuestra el teorema!" | Sin valor de verdad |

---

## 4. Formalización y Simbolización del Lenguaje Natural

El proceso de formalización consiste en traducir afirmaciones expresadas en lenguaje natural a fórmulas bien formadas (FBF) del cálculo proposicional, eliminando ambigüedades semánticas.

### Procedimiento de Formalización:
1. **Identificar las proposiciones atómicas:** Aislar cada componente declarativo simple y asignarle una letra proposicional fija.
2. **Identificar las conectivas lógicas:** Reconocer términos de enlace como "y", "o", "si... entonces", "no", "si y sólo si".
3. **Determinar la jerarquía y el alcance:** Utilizar paréntesis para indicar con exactitud el orden de evaluación sintáctica.

> **Ejemplo de Formalización:**  
> Consideremos el enunciado: *"Si la función \\(f\\) es diferenciable en \\(x\_0\\), entonces \\(f\\) es continua en \\(x\_0\\); sin embargo, si \\(f\\) es continua en \\(x\_0\\), no necesariamente \\(f\\) es diferenciable en \\(x\_0\\)."*
> 
> * Sean las atómicas:
>   * \\(p\\): "La función \\(f\\) es diferenciable en \\(x\_0\\)."
>   * \\(q\\): "La función \\(f\\) es continua en \\(x\_0\\)."
> * La estructura lógica formal es:
> \\[
> (p \to q) \land \neg(q \to p)
> \\]