# 3.2 Contención, Igualdad Extensional, Vacío, Universal y Potencia

Las relaciones de inclusión e igualdad entre conjuntos, junto con la construcción del conjunto de partes, son herramientas indispensables para la fundamentación del análisis y el álgebra.

---

## 1. La Relación de Inclusión o Contención (⊆)

> **Definición 3.2 (Subconjunto):** 
> Sean \\(A\\) y \\(B\\) dos conjuntos en un universo \\(\mathcal{U}\\). Decimos que \\(A\\) es un **subconjunto** de \\(B\\) (o que \\(A\\) está **contenido** en \\(B\\)), y se denota \\(A \subseteq B\\), si y sólo si todo elemento que pertenece a \\(A\\) pertenece también a \\(B\\):
>
> \\[
> A \subseteq B \iff (\forall x) [x \in A \implies x \in B]
> \\]

### Subconjunto Propio (Inclusión Estricta, ⊂ o ⊊)
Decimos que \\(A\\) es un **subconjunto propio** de \\(B\\) si \\(A \subseteq B\\) y además existe al menos un elemento \\(b \in B\\) tal que \\(b \notin A\\) (es decir, \\(A \subseteq B\\) y \\(A \neq B\\)):

\\[
A \subsetneq B \iff (A \subseteq B \land A \neq B)
\\]

### Propiedades de la Inclusión:
1. **Reflexividad:** Para todo conjunto \\(A\\), se cumple que \\(A \subseteq A\\).
2. **Transitividad:** Si \\(A \subseteq B\\) y \\(B \subseteq C\\), entonces \\(A \subseteq C\\).
3. **Antisimetría:** Si \\(A \subseteq B\\) y \\(B \subseteq A\\), entonces \\(A = B\\).

---

## 2. El Axioma de Extensionalidad e Igualdad de Conjuntos

> **Axioma 3.1 (Axioma de Extensionalidad):** 
> Dos conjuntos \\(A\\) y \\(B\\) son **iguales** (denotado \\(A = B\\)) si y sólo si tienen exactamente los mismos elementos.
>
> \\[
> A = B \iff (\forall x) [x \in A \iff x \in B]
> \\]

### Técnica Canónica de Demostración: La Doble Contención
Para demostrar rigurosamente que dos conjuntos \\(A\\) y \\(B\\) son iguales en cualquier rama de la matemática, la estrategia universal consiste en dividir la prueba en dos pasos independientes:
1. **Paso 1 (Probar que \\(A \subseteq B\\)):** Se toma un elemento arbitrario \\(x \in A\\) y, mediante definiciones y propiedades, se deduce que \\(x \in B\\).
2. **Paso 2 (Probar que \\(B \subseteq A\\)):** Se toma un elemento arbitrario \\(y \in B\\) y se deduce que \\(y \in A\\).
3. **Conclusión:** Por el principio de antisimetría y el axioma de extensionalidad, \\(A = B\\).

---

## 3. Conjuntos Notables: El Conjunto Vacío y el Conjunto Universal

### A. El Conjunto Vacío (∅ o {})
Es el único conjunto que **no contiene ningún elemento**:

\\[
\emptyset = \{x \mid x \neq x\} \qquad (\forall x) [x \notin \emptyset]
\\]

> **Teorema 3.1 (Inclusión Vacua del Conjunto Vacío):** 
> Para **cualquier** conjunto \\(A\\), se cumple que el conjunto vacío es subconjunto de \\(A\\):
>
> \\[
> \emptyset \subseteq A
> \\]
>
> *Demostración Formal:* 
> Por definición de subconjunto, \\(\emptyset \subseteq A \iff (\forall x)[x \in \emptyset \implies x \in A]\\). 
> Para cualquier elemento \\(x\\), la proposición \\(x \in \emptyset\\) es **Falsa (\\(F\\))**. 
> Dado que una implicación con antecedente falso es **vacuamente verdadera** (\\(F \to P = V\\)), la afirmación universal es verdadera para todo \\(x\\). Por lo tanto, \\(\emptyset \subseteq A\\). \\(\blacksquare\\)

> **Advertencia de Notación:** 
> Distíngase estrictamente entre \\(\emptyset\\) (conjunto vacío, sin elementos, \\(|\emptyset| = 0\\)) y \\(\{\emptyset\}\\) (conjunto unitario cuyo único elemento es el conjunto vacío, \\(|\{\emptyset\}| = 1\\)).

### B. El Conjunto Universal (U)
Es el conjunto que contiene la totalidad de los objetos bajo estudio en un contexto matemático determinado. Para todo subconjunto \\(A\\) de dicho contexto se cumple:

\\[
\emptyset \subseteq A \subseteq \mathcal{U}
\\]

---

## 4. El Conjunto Potencia (o Conjunto de Partes, 𝒫(A))

> **Definición 3.3 (Conjunto Potencia):** 
> Dado un conjunto \\(A\\), su **conjunto potencia** (o conjunto de partes), denotado por \\(\mathcal{P}(A)\\) o \\(2^A\\), es el conjunto formado por **todos los posibles subconjuntos** de \\(A\\):
>
> \\[
> \mathcal{P}(A) = \{X \mid X \subseteq A\}
> \\]
>
> Por lo tanto, para cualquier conjunto \\(X\\):
>
> \\[
> X \in \mathcal{P}(A) \iff X \subseteq A
> \\]

### Propiedades Fundamentales:
1. Para todo conjunto \\(A\\):

\\[
\emptyset \in \mathcal{P}(A) \qquad \text{y} \qquad A \in \mathcal{P}(A)
\\]

2. **Cardinalidad del Conjunto Potencia Finito:** 
 Si \\(A\\) es un conjunto finito con \\(|A| = n\\) elementos, entonces:

\\[
|\mathcal{P}(A)| = 2^n
\\]

 *Justificación combinatoria:* Para construir un subconjunto de \\(A\\), para cada uno de los \\(n\\) elementos se toma una decisión binaria independiente: o bien se incluye en el subconjunto (1), o bien se excluye (0). El principio de multiplicación arroja \\(2 \times 2 \times \dots \times 2 = 2^n\\) elecciones posibles.

### Ejemplo Detallado:
Sea \\(A = \{1, 2, 3\}\\) (donde \\(|A| = 3\\)). Su conjunto potencia tiene \\(2^3 = 8\\) subconjuntos:

\\[
\mathcal{P}(A) = \Big\{ \emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\} \Big\}
\\]