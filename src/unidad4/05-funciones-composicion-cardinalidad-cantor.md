# 4.5 Funciones, Composición, Inversa y Cardinalidad de Cantor

Las **funciones** constituyen el tipo especial de relación matemática más utilizado en todas las disciplinas científicas, representando procesos deterministas de transformación, correspondencia y modelación.

---

## 1. Definición Conjuntista Formal de Función

> **Definición 4.4 (Función o Aplicación):**  
> Sean \\(A\\) y \\(B\\) dos conjuntos. Una **función** \\(f\\) de \\(A\\) en \\(B\\), denotada por \\(f: A \to B\\), es una relación binaria \\(f \subseteq A \times B\\) que satisface dos condiciones de existencia y unicidad:
> 1. **Totalidad (Existencia):** Todo elemento del conjunto de partida \\(A\\) tiene asignada una imagen en \\(B\\):
> \\[
> (\forall x \in A)(\exists y \in B) \, [(x, y) \in f]
> \\]
> 2. **Unicidad:** A cada elemento \\(x \in A\\) le corresponde **a lo sumo un único** elemento \\(y \in B\\):
> \\[
> (\forall x \in A)(\forall y_1, y_2 \in B) \, [(x, y_1) \in f \land (x, y_2) \in f \implies y_1 = y_2]
> \\]
> 
> Cuando \\((x, y) \in f\\), escribimos la notación funcional habitual: \\(y = f(x)\\).

* **Dominio:** \\(\text{Dom}(f) = A\\).
* **Codominio:** \\(B\\).
* **Imagen o Recorrido (Rango):** \\(\text{Im}(f) = f(A) = \{f(x) \in B \mid x \in A\} \subseteq B\\).

---

## 2. Clasificación de Funciones: Inyectividad, Sobreyectividad y Biyectividad

### A. Función Inyectiva (Uno a Uno, 1-1)
Una función \\(f: A \to B\\) es **inyectiva** si elementos distintos del dominio tienen imágenes distintas en el codominio:

\\[
(\forall x\_1, x\_2 \in A) \, [x\_1 \neq x\_2 \implies f(x\_1) \neq f(x\_2)]
\\]

> **Criterio Operativo de Demostración (por Contraposición):**  
> Para demostrar que \\(f\\) es inyectiva, se asume que \\(f(x\_1) = f(x\_2)\\) y se demuestra algebraicamente que \\(x\_1 = x\_2\\):
> \\[
> f(x_1) = f(x_2) \implies x_1 = x_2
> \\]

### B. Función Sobreyectiva (Sobre o Suprayectiva)
Una función \\(f: A \to B\\) es **sobreyectiva** si todo elemento del codominio \\(B\\) es imagen de al menos un elemento del dominio \\(A\\):

\\[
(\forall y \in B)(\exists x \in A) \, [f(x) = y] \qquad \text{o equivalentemente} \qquad \text{Im}(f) = B
\\]

### C. Función Biyectiva (Correspondencia Biunívoca)
Una función \\(f: A \to B\\) es **biyectiva** si y sólo si es **simultáneamente inyectiva y sobreyectiva**.

---

## 3. Composición de Funciones y Función Inversa

### A. Composición de Funciones (\\(g \circ f\\))
Dadas \\(f: A \to B\\) y \\(g: B \to C\\), la **función compuesta** \\(g \circ f: A \to C\\) se define por:

\\[
(g \circ f)(x) \;=\; g(f(x)) \quad \text{para todo } x \in A
\\]

* **Propiedades:**
  * Es asociativa: \\(h \circ (g \circ f) = (h \circ g) \circ f\\).
  * **No es conmutativa:** en general, \\(g \circ f \neq f \circ g\\).
  * Si \\(f\\) y \\(g\\) son inyectivas, \\(g \circ f\\) es inyectiva.
  * Si \\(f\\) y \\(g\\) son sobreyectivas, \\(g \circ f\\) es sobreyectiva.
  * Si \\(f\\) y \\(g\\) son biyectivas, \\(g \circ f\\) es biyectiva.

### B. La Función Inversa (\\(f^{-1}\\))
> **Teorema 4.10 (Existencia de la Función Inversa):**  
> Una función \\(f: A \to B\\) admite función inversa \\(f^{-1}: B \to A\\) si y sólo si \\(f\\) es **Biyectiva**.  
> En tal caso, \\(f^{-1}\\) satisface:
> \\[
> f^{-1} \circ f \;=\; \text{id}_A \qquad \text{y} \qquad f \circ f^{-1} \;=\; \text{id}_B
> \\]
> Además, para la composición de biyecciones: \\((g \circ f)^{-1} = f^{-1} \circ g^{-1}\\).

---

## 4. Cardinalidad Infinita y la Teoría de Georg Cantor

El concepto de biyección permitió a **Georg Cantor (1874)** extender el concepto de tamaño o cardinalidad a conjuntos infinitos:

> **Definición 4.5 (Equinumerosidad o Coordinabilidad):**  
> Dos conjuntos \\(A\\) y \\(B\\) tienen la **misma cardinalidad** (denotado \\(|A| = |B|\\) o \\(A \approx B\\)) si y sólo si **existe una función biyectiva \\(f: A \to B\\)**.

### A. Conjuntos Numerables (\\(\aleph\_0\\), Álef Cero)
Un conjunto \\(A\\) es **infinito numerable** si tiene la misma cardinalidad que el conjunto de los números naturales: \\(|A| = |\mathbb{N}| = \aleph\_0\\).
* \\(\mathbb{N}\\) es numerable.
* El conjunto de los enteros pares \\(2\mathbb{N}\\) es numerable (biyección \\(f(n) = 2n\\), Paradoja del Hotel de Hilbert).
* \\(\mathbb{Z}\\) es numerable (biyección alternante: \\(0, 1, -1, 2, -2, 3, -3, \dots\\)).
* \\(\mathbb{Q}\\) (los números racionales) es **numerable** (demostrado por Cantor mediante su célebre recorrido diagonal en zigzag sobre la cuadrícula \\(\mathbb{N} \times \mathbb{N}\\)).

### B. Conjuntos No Numerables y el Argumento Diagonal de Cantor
> **Teorema 4.11 (No Numerabilidad de los Reales):**  
> El conjunto de los números reales \\(\mathbb{R}\\) (y el intervalo \\((0, 1)\\)) **NO es numerable**. Su cardinalidad se denota por \\(\mathfrak{c} = 2^{\aleph\_0}\\) (la potencia del continuo).  
> \\[
> |\mathbb{N}| \;<\; |\mathbb{R}| \qquad (\aleph_0 < \mathfrak{c})
> \\]

*Idea de la Demostración Diagonal de Cantor:*  
Si \\((0, 1)\\) fuera numerable, podríamos listar todos sus números reales en una sucesión infinita en desarrollo decimal:

\\[
r\_1 = 0.d\_{11}d\_{12}d\_{13}\dots
\\]

\\[
r\_2 = 0.d\_{21}d\_{22}d\_{23}\dots
\\]

\\[
r\_3 = 0.d\_{31}d\_{32}d\_{33}\dots
\\]

Cantor construye un nuevo número real \\(x = 0.c\_1 c\_2 c\_3 \dots \in (0, 1)\\) eligiendo cada dígito \\(c\_k \neq d\_{kk}\\) (alterando la diagonal). Este número \\(x\\) difiere de \\(r\_1\\) en el primer decimal, de \\(r\_2\\) en el segundo decimal, y en general \\(x \neq r\_n\\) para todo \\(n\\). Por tanto, la lista nunca puede ser completa, lo que prueba que \\(\mathbb{R}\\) es **no numerable**.

### C. El Teorema de Cantor Generalizado
> **Teorema 4.12 (Teorema de Cantor):**  
> Para **cualquier** conjunto \\(A\\) (finito o infinito), la cardinalidad de su conjunto potencia es estrictamente mayor que la del propio conjunto:
> \\[
> |A| \;<\; |\mathcal{P}(A)|
> \\]
> Es decir, **no existe ninguna función sobreyectiva** \\(f: A \to \mathcal{P}(A)\\).

*Consecuencia Filosófica y Matemática:*  
No existe un "infinito supremo". Existe una **jerarquía infinita de infinitos crecientes**:

\\[
|\mathbb{N}| \;<\; |\mathcal{P}(\mathbb{N})| \;<\; |\mathcal{P}(\mathcal{P}(\mathbb{N}))| \;<\; |\mathcal{P}(\mathcal{P}(\mathcal{P}(\mathbb{N})))| \;<\; \dots
\\]

lo que abrió las puertas al fascinante universo de los números transfinitos en la matemática moderna.