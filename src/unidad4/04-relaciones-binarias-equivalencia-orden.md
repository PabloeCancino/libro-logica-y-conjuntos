# 4.4 Relaciones Binarias, Relaciones de Equivalencia y de Orden

Las **relaciones** constituyen la formalización conjuntista de los vínculos, asociaciones y jerarquías entre objetos matemáticos.

---

## 1. Definición Formal de Relación Binaria

> **Definición 4.1 (Relación Binaria):** 
> Sean \\(A\\) y \\(B\\) dos conjuntos. Una **relación binaria** \\(R\\) de \\(A\\) en \\(B\\) es cualquier subconjunto del producto cartesiano:
>
> \\[
> R \subseteq A \times B
> \\]
>
> Si \\(A = B\\), decimos que \\(R\\) es una **relación binaria sobre el conjunto \\(A\\)** (\\(R \subseteq A \times A\\)).
> 
> * Notación: Si \\((a, b) \in R\\), se escribe \\(a \, R \, b\\) ("\\(a\\) está relacionado con \\(b\\)").
> * Si \\((a, b) \notin R\\), se escribe \\(a \, \cancel{R} \, b\\).

### Conceptos Asociados:
* **Dominio:** \\(\text{Dom}(R) = \{a \in A \mid (\exists b \in B) [(a, b) \in R]\}\\).
* **Rango (o Imagen):** \\(\text{Ran}(R) = \{b \in B \mid (\exists a \in A) [(a, b) \in R]\}\\).
* **Relación Inversa:** \\(R^{-1} = \{(b, a) \in B \times A \mid (a, b) \in R\}\subseteq B \times A\\).

---

## 2. Propiedades de una Relación sobre un Conjunto A

Dada una relación \\(R \subseteq A \times A\\):

1. **Reflexiva:** Todo elemento está relacionado consigo mismo:

\\[
(\forall x \in A) \, [x \, R \, x]
\\]

2. **Simétrica:** Si un elemento se relaciona con otro, el segundo se relaciona con el primero:

\\[
(\forall x, y \in A) \, [x \, R \, y \implies y \, R \, x]
\\]

3. **Antisimétrica:** Si dos elementos se relacionan mutuamente en ambos sentidos, son necesariamente idénticos:

\\[
(\forall x, y \in A) \, [x \, R \, y \land y \, R \, x \implies x = y]
\\]

4. **Transitiva:** Si \\(x\\) se relaciona con \\(y\\) y este con \\(z\\), entonces \\(x\\) se relaciona con \\(z\\):

\\[
(\forall x, y, z \in A) \, [x \, R \, y \land y \, R \, z \implies x \, R \, z]
\\]

---

## 3. Relaciones de Equivalencia, Clases y Conjunto Cociente

> **Definición 4.2 (Relación de Equivalencia):** 
> Una relación binaria \\(R\\) (usualmente denotada por \\(\sim\\) o \\(\equiv\\)) sobre un conjunto \\(A\\) es una **relación de equivalencia** si y sólo si es **Reflexiva**, **Simétrica** y **Transitiva** (Propiedades RST).

### A. Clases de Equivalencia
Dada una relación de equivalencia \\(\sim\\) sobre \\(A\\) y un elemento \\(a \in A\\), la **clase de equivalencia** de \\(a\\), denotada por \\([a]\\) o \\(\overline{a}\\), es el conjunto de todos los elementos de \\(A\\) que están relacionados con \\(a\\):

\\[
[a] = \{x \in A \mid x \sim a\}
\\]

El elemento \\(a\\) se denomina un **representante** de la clase \\([a]\\).

### B. El Conjunto Cociente (A/∼)
Es el conjunto cuyos elementos son todas las clases de equivalencia inducidas sobre \\(A\\):

\\[
A/\sim = \{[a] \mid a \in A\}
\\]

> **Teorema 4.9 (Teorema Fundamental de las Relaciones de Equivalencia):** 
> Sea \\(\sim\\) una relación de equivalencia sobre un conjunto no vacío \\(A\\). Entonces:
> 1. Para todo \\(a \in A\\), \\(a \in [a]\\) (luego ninguna clase es vacía).
> 2. \\(a \sim b \iff [a] = [b]\\).
> 3. \\(a \not\sim b \iff [a] \cap [b] = \emptyset\\).
> 4. El conjunto cociente \\(A/\sim\\) constituye una **partición de \\(A\\)**.
> 
> *Recíprocamente*, toda partición \\(\mathcal{P}\\) de \\(A\\) define de manera única una relación de equivalencia sobre \\(A\\) mediante: \\(x \sim y \iff x \text{ e } y \text{ pertenecen al mismo bloque de } \mathcal{P}\\).

### Ejemplo Clásico: Congruencia Módulo n en ℤ
Para un entero fijo \\(n \ge 2\\), definimos sobre \\(\mathbb{Z}\\):

\\[
a \equiv b \pmod{n} \iff n \mid (a - b)
\\]

Esta relación es de equivalencia y particiona a \\(\mathbb{Z}\\) en exactamente \\(n\\) clases disjuntas:

\\[
\mathbb{Z}/n\mathbb{Z} = \{[0], [1], [2], \dots, [n-1]\}
\\]

lo que da origen a la **Aritmética Modular** y al anillo de clases residuales \\(\mathbb{Z}\_n\\).

---

## 4. Relaciones de Orden (Posets y Diagramas de Hasse)

> **Definición 4.3 (Orden Parcial):** 
> Una relación binaria \\(R\\) (denotada por \\(\le\\) o \\(\preceq\\)) sobre \\(A\\) es un **orden parcial** si es **Reflexiva**, **Antisimétrica** y **Transitiva**. 
> El par \\((A, \le)\\) se denomina **conjunto parcialmente ordenado** (o *poset*, del inglés *partially ordered set*).

* **Orden Total (o Lineal):** Si además todo par de elementos es comparable:

\\[
(\forall x, y \in A) \, [x \le y \lor y \le x]
\\]

* **Diagrama de Hasse:** Es la representación gráfica minimal de un poset finito, donde se disponen los elementos en niveles verticales y se dibujan aristas orientadas hacia arriba sólo para las relaciones de **cobertura directa**, suprimiendo los lazos reflexivos y las aristas transitivas redundantes.