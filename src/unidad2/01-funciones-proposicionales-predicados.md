# 2.1 Funciones Proposicionales, Predicados y Conjuntos de Verdad

El cálculo proposicional analizado en la Unidad 1 resulta insuficiente para expresar la estructura interna de muchas afirmaciones matemáticas. Por ejemplo, el enunciado *"Todo número primo mayor que 2 es impar"* no puede descomponerse adecuadamente utilizando únicamente variables proposicionales simples \\(p, q\\). Para superar esta limitación se introduce el **Cálculo de Predicados de Primer Orden**.

---

## 1. Definición de Predicado o Función Proposicional

> **Definición 2.1 (Función Proposicional):**  
> Sea \\(U\\) un conjunto no vacío denominado **universo de discurso** (o dominio de referencia). Una **función proposicional** (o *predicado*) de una variable, denotada por \\(P(x)\\), es una expresión lingüística o matemática que contiene una variable libre \\(x \in U\\) tal que:
> 1. \\(P(x)\\) **no es una proposición** mientras \\(x\\) permanezca como variable libre (no posee un valor de verdad definido).
> 2. Al sustituir la variable \\(x\\) por un elemento específico y concreto \\(a \in U\\), la expresión resultante \\(P(a)\\) se convierte en una **proposición lógica** con valor de verdad bien definido (Verdadero o Falso).

### Ejemplos en Distintos Universos
* Sea \\(U = \mathbb{Z}\\) y el predicado \\(P(x)\\): *"\\(x\\) es un número par"*:
  * \\(P(4)\\): "4 es par" \\(\implies\\) Proposición **Verdadera (\\(V\\))**.
  * \\(P(7)\\): "7 es par" \\(\implies\\) Proposición **Falsa (\\(F\\))**.
* Sea \\(U = \mathbb{R}\\) y el predicado \\(Q(x)\\): *"\\(x^2 - 4 = 0\\)"*:
  * \\(Q(2)\\): "\\(2^2 - 4 = 0\\)" \\(\implies\\) Proposición **Verdadera (\\(V\\))**.
  * \\(Q(3)\\): "\\(3^2 - 4 = 0\\)" \\(\implies\\) Proposición **Falsa (\\(F\\))**.

---

## 2. Predicados Multivariables (Relaciones n-arias)

El concepto se generaliza de forma natural a funciones proposicionales de varias variables \\(P(x\_1, x\_2, \dots, x\_n)\\) sobre el producto cartesiano de dominios \\(U\_1 \times U\_2 \times \dots \times U\_n\\):

* **Predicados binarios \\(P(x, y)\\):**
  * Sea \\(U = \mathbb{N}\\) y \\(L(x, y)\\): *"\\(x < y\\)"*.
  * \\(L(2, 5)\\): "\\(2 < 5\\)" \\(\implies\\) **\\(V\\)**.
  * \\(L(5, 2)\\): "\\(5 < 2\\)" \\(\implies\\) **\\(F\\)**.
* **Predicados algebraicos:**
  * Sea \\(U = \mathbb{R}\\) y \\(E(x, y, z)\\): *"\\(x^2 + y^2 = z^2\\)"*.
  * \\(E(3, 4, 5)\\): "\\(3^2 + 4^2 = 5^2\\)" \\(\implies\\) **\\(V\\)** (Terna pitagórica).

---

## 3. Conjunto de Verdad de una Función Proposicional

> **Definición 2.2 (Conjunto de Verdad):**  
> Dado un universo de discurso \\(U\\) y una función proposicional \\(P(x)\\), el **conjunto de verdad** de \\(P(x)\\), denotado por \\(T\_P\\) (o \\(V\_P\\)), es el subconjunto de \\(U\\) formado por todos aquellos elementos que hacen verdadera la proposición \\(P(x)\\):
> \\[
> T_P \;=\; \{x \in U \mid P(x) \text{ es verdadero}\}
> \\]

### Conexión Directa entre Lógica y Teoría de Conjuntos

Existe un isomorfismo conceptual estricto entre los operadores lógicos aplicados a predicados y las operaciones entre sus conjuntos de verdad:

| Operación Lógica sobre Predicados | Notación Lógica | Operación Conjuntista | Conjunto de Verdad Resultante |
| :--- | :---: | :---: | :---: |
| **Negación** | \\(\neg P(x)\\) | Complemento | \\(T\_{\neg P} = (T\_P)^c = U \setminus T\_P\\) |
| **Conjunción** | \\(P(x) \land Q(x)\\) | Intersección | \\(T\_{P \land Q} = T\_P \cap T\_Q\\) |
| **Disyunción** | \\(P(x) \lor Q(x)\\) | Unión | \\(T\_{P \lor Q} = T\_P \cup T\_Q\\) |
| **Condicional** | \\(P(x) \to Q(x)\\) | Inclusión | \\(T\_{P \to Q} = (T\_P)^c \cup T\_Q\\) |
| **Implicación Universal** | \\(P(x) \implies Q(x)\\) | Contención | \\(T\_P \subseteq T\_Q\\) |
| **Equivalencia Universal** | \\(P(x) \iff Q(x)\\) | Igualdad | \\(T\_P = T\_Q\\) |

> **Observación Fundamental:**  
> Afirmar que \\(P(x) \implies Q(x)\\) de manera universal en \\(U\\) equivale exactamente a decir que **todo elemento que satisface \\(P\\) también satisface \\(Q\\)**, lo cual es la definición matemática estricta de la inclusión de conjuntos \\(T\_P \subseteq T\_Q\\).