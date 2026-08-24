# 3.4 Particiones, Cardinalidad y Principio de Inclusión-Exclusión

El análisis cuantitativo de conjuntos finitos y la descomposición estructural de colecciones arbitrarias son fundamentales para la combinatoria, la teoría de la probabilidad y el álgebra moderna.

---

## 1. Particiones de un Conjunto

> **Definición 3.4 (Partición):**  
> Sea \\(A\\) un conjunto no vacío. Una **partición** de \\(A\\) es una colección \\(\mathcal{P} = \{A\_i\}\_{i \in I}\\) de subconjuntos de \\(A\\) (llamados *bloques*, *clases* o *celdas*) que satisfacen simultáneamente tres condiciones axiomáticas:
> 1. **No vacuidad:** Ningún bloque es vacío:
> \\[
> (\forall i \in I) \, [A_i \neq \emptyset]
> \\]
> 2. **Disjunción dos a dos (Mutuamente Excluyentes):** Cualesquiera dos bloques distintos no comparten elementos:
> \\[
> (\forall i, j \in I) \, [i \neq j \implies A_i \cap A_j = \emptyset]
> \\]
> 3. **Cobertura Total (Exhaustividad):** La unión de todos los bloques reconstruye exactamente el conjunto original \\(A\\):
> \\[
> \bigcup_{i \in I} A_i \;=\; A
> \\]

### Ejemplo en un Conjunto Finito:
Sea \\(A = \{1, 2, 3\}\\). Las siguientes son particiones válidas de \\(A\\):
* \\(\mathcal{P}\_1 = \{\{1\}, \{2\}, \{3\}\}\\) (partición discreta).
* \\(\mathcal{P}\_2 = \{\{1, 2\}, \{3\}\}\\).
* \\(\mathcal{P}\_3 = \{\{1, 3\}, \{2\}\}\\).
* \\(\mathcal{P}\_4 = \{\{2, 3\}, \{1\}\}\\).
* \\(\mathcal{P}\_5 = \{\{1, 2, 3\}\}\\) (partición trivial).

El número total de particiones posibles de un conjunto de \\(n\\) elementos viene dado por el **\\(n\\)-ésimo Número de Bell** \\(B\_n\\) (para \\(n=3\\), \\(B\_3 = 5\\); para \\(n=4\\), \\(B\_4 = 15\\)).

---

## 2. Cardinalidad de Conjuntos Finitos

> **Definición 3.5 (Cardinalidad):**  
> La **cardinalidad** de un conjunto finito \\(A\\), denotada por \\(|A|\\) o \\(\#(A)\\), es el número exacto de elementos distintos que contiene.
> * \\(|\emptyset| = 0\\).
> * Si \\(A = \{x\_1, x\_2, \dots, x\_n\}\\) con \\(x\_i \neq x\_j\\) para todo \\(i \neq j\\), entonces \\(|A| = n\\).

### Propiedades Fundamentales del Cardinal:
1. Si \\(A \subseteq B\\), entonces \\(|A| \le |B|\\).
2. Si \\(A \subseteq B\\), entonces \\(|B \setminus A| = |B| - |A|\\).
3. Si \\(A \cap B = \emptyset\\) (conjuntos disjuntos), entonces:

\\[
|A \cup B| \;=\; |A| + |B|
\\]

---

## 3. El Principio de Inclusión-Exclusión (P.I.E.)

Cuando dos o más conjuntos no son disjuntos, sumar sus cardinalidades individuales contaría los elementos compartidos más de una vez. El **Principio de Inclusión-Exclusión** corrige este exceso de manera alternante.

### A. Para Dos Conjuntos:
> **Teorema 3.3 (P.I.E. para 2 Conjuntos):**  
> Para cualesquiera conjuntos finitos \\(A\\) y \\(B\\):
> \\[
> |A \cup B| \;=\; |A| + |B| - |A \cap B|
> \\]

*Demostración:*  
Podemos descomponer \\(A \cup B\\) en tres bloques disjuntos: \\(A \setminus B\\), \\(B \setminus A\\) y \\(A \cap B\\).  
Entonces:

\\[
|A \cup B| = |A \setminus B| + |B \setminus A| + |A \cap B|
\\]

Por otra parte, \\(|A| = |A \setminus B| + |A \cap B|\\) y \\(|B| = |B \setminus A| + |A \cap B|\\).  
Sumando ambas ecuaciones:

\\[
|A| + |B| = |A \setminus B| + |B \setminus A| + 2|A \cap B| = |A \cup B| + |A \cap B|
\\]

Restando \\(|A \cap B|\\) en ambos miembros se obtiene la fórmula. \\(\blacksquare\\)

### B. Para Tres Conjuntos:
> **Teorema 3.4 (P.I.E. para 3 Conjuntos):**  
> Para cualesquiera conjuntos finitos \\(A, B, C\\):
> \\[
> |A \cup B \cup C| \;=\; |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|
> \\]

### C. Forma General para n Conjuntos
> **Teorema 3.5 (P.I.E. General):**  
> Para una familia finita \\(A\_1, A\_2, \dots, A\_n\\):
> \\[
> \left|\bigcup_{i=1}^n A_i\right| \;=\; \sum_{i=1}^n |A_i| - \sum_{1 \le i < j \le n} |A_i \cap A_j| + \sum_{1 \le i < j < k \le n} |A_i \cap A_j \cap A_k| - \dots + (-1)^{n-1} |A_1 \cap \dots \cap A_n|
> \\]

---

## 4. Ejemplo de Aplicación en Conteo

> **Problema:**  
> En una muestra de 100 estudiantes de la Licenciatura en Matemáticas de la UAN:
> * 60 cursan Álgebra Lineal (\\(A\\)).
> * 50 cursan Cálculo Diferencial (\\(B\\)).
> * 40 cursan Lógica y Conjuntos (\\(C\\)).
> * 30 cursan Álgebra y Cálculo (\\(A \cap B\\)).
> * 25 cursan Álgebra y Lógica (\\(A \cap C\\)).
> * 20 cursan Cálculo y Lógica (\\(B \cap C\\)).
> * 10 cursan las tres asignaturas simultáneamente (\\(A \cap B \cap C\\)).
> 
> ¿Cuántos estudiantes cursan **al menos una** de estas tres materias?

*Solución:*  
Aplicando el Teorema 3.4:

\\[
|A \cup B \cup C| = (60 + 50 + 40) - (30 + 25 + 20) + 10 = 150 - 75 + 10 = 85
\\]

Por tanto, 85 estudiantes cursan al menos una materia, y \\(100 - 85 = 15\\) no cursan ninguna de las tres.