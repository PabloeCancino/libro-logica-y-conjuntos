# Ejercicios de la Unidad 3

---

## 📝 Bloque A: Pertenencia, Inclusión y Conjunto Potencia

1. Sean los conjuntos \\(A = \\{1, 2, \\{1, 2\\}, \emptyset\\}\\). Determine el valor de verdad (Verdadero o Falso) de cada una de las siguientes afirmaciones:
 - a) \\(1 \in A\\)
 - b) \\(\\{1\\} \in A\\)
 - c) \\(\\{1\\} \subseteq A\\)
 - d) \\(\\{1, 2\\} \in A\\)
 - e) \\(\\{1, 2\\} \subseteq A\\)
 - f) \\(\emptyset \in A\\)
 - g) \\(\emptyset \subseteq A\\)
 - h) \\(\\{\emptyset\\} \subseteq A\\)

2. Determine el conjunto potencia \\(\mathcal{P}(A)\\) y su cardinalidad para cada uno de los siguientes conjuntos:
 - a) \\(A = \emptyset\\)
 - b) \\(A = \\{a\\}\\)
 - c) \\(A = \\{1, \\{2, 3\\}\\}\\)
 - d) \\(A = \mathcal{P}(\emptyset)\\)

---

## 📝 Bloque B: Álgebra de Conjuntos y Demostraciones de Doble Contención

*Para redactar estas pruebas:* la técnica de doble contención está en la sección 3.2; los esqueletos de redacción y modelos completos se desarrollan en las secciones 4.0 y 4.0.1. Aquí basta con tomar un elemento arbitrario y justificar cada paso.

3. Demuestre rigurosamente mediante el método de **doble contención** las siguientes igualdades conjuntistas:
 - a) \\(A \cap (B \cup C) = (A \cap B) \cup (A \cap C)\\)
 - b) \\(A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)\\)
 - c) \\(A \setminus (B \setminus C) = (A \setminus B) \cup (A \cap C)\\)
 - d) \\(\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)\\)
 - e) ¿Se cumple que \\(\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)\\)? (Demuéstrelo o dé un contraejemplo explícito).

---

## 📝 Bloque C: Cardinalidad, Particiones y Principio de Inclusión-Exclusión

4. Encuentre todas las particiones posibles del conjunto \\(A = \\{a, b, c, d\\}\\). (Verifique que el total coincida con el número de Bell \\(B\_4 = 15\\)).

5. En una encuesta a 200 estudiantes de la UAN:
 - 120 utilizan Python para sus proyectos.
 - 100 utilizan R.
 - 70 utilizan Julia.
 - 50 utilizan Python y R.
 - 30 utilizan Python y Julia.
 - 25 utilizan R y Julia.
 - 15 utilizan los tres lenguajes.
 - Calcule cuántos estudiantes:
 - a) Utilizan al menos uno de los tres lenguajes.
 - b) No utilizan ninguno de estos tres lenguajes.
 - c) Utilizan exclusivamente Python.

---

## 📝 Bloque D: Producto Cartesiano y Familias Indexadas

6. Sean \\(A = \\{1, 2\\}\\), \\(B = \\{a, b\\}\\) y \\(C = \\{x\\}\\).
 - a) Calcule explícitamente \\(A \times B \times C\\).
 - b) Demuestre que \\(A \times (B \cap C) = (A \times B) \cap (A \times C)\\).

7. Para cada \\(n \in \mathbb{N}\\), defínase el intervalo abierto \\(A\_n = \left(-\frac{1}{n}, 1 + \frac{1}{n}\right) \subset \mathbb{R}\\). Calcule:
 - a) \\(\bigcup\_{n=1}^\infty A\_n\\)
 - b) \\(\bigcap\_{n=1}^\infty A\_n\\)

---

## 📝 Bloque E: Demostraciones Básicas con Conjuntos

Este bloque integra las secciones 3.2 a 3.5 y está ordenado de menor a mayor dificultad. La estrategia común es el **elemento arbitrario**: se toma \\(x\\) genérico, se traduce la pertenencia a lógica y se razona con las leyes de la Unidad 1. Los ejercicios 16 y 17 requieren la sección 3.5.

8. Demuestre:
 - a) \\(A \setminus B \subseteq A\\)
 - b) \\((A \setminus B) \cap B = \emptyset\\) (*sugerencia:* ¿puede existir un elemento que esté en ambos conjuntos?)

9. Demuestre que \\(A \subseteq B \iff A \setminus B = \emptyset\\).

10. Demuestre por **cadena de equivalencias** la segunda ley distributiva \\(A \cup (B \cap C) = (A \cup B) \cap (A \cup C)\\), indicando la ley lógica de cada paso.

11. Demuestre que si \\(A \subseteq B\\) y \\(C \subseteq D\\), entonces \\(A \cup C \subseteq B \cup D\\). (*Sugerencia:* proceda por casos sobre \\(x \in A \cup C\\).)

12. Demuestre que \\((A \setminus B) \cup B = A \cup B\\).

13. La sección 3.3 afirma que la diferencia simétrica puede escribirse de dos formas. Demuestre que \\((A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)\\). (*Sugerencia:* reduzca el problema a la equivalencia lógica \\((p \land \neg q) \lor (q \land \neg p) \equiv (p \lor q) \land \neg(p \land q)\\) y verifíquela con una tabla de verdad.)

14. Demuestre que \\(\mathcal{P}(A) \subseteq \mathcal{P}(B) \iff A \subseteq B\\).

15. Decida si la igualdad \\((A \setminus B) \cup (B \setminus C) = A \setminus C\\) es verdadera para todos los conjuntos. Si es falsa, dé un contraejemplo; después determine cuál de las dos inclusiones sí se cumple y demuéstrela.

16. Sea \\(\\{A\_i\\}\_{i \in I}\\) una familia de conjuntos y \\(B\\) un conjunto cualquiera. Demuestre que \\(B \cap \bigcup\_{i \in I} A\_i = \bigcup\_{i \in I} (B \cap A\_i)\\).

17. Demuestre que \\((A \cup B) \times C = (A \times C) \cup (B \times C)\\). (*Sugerencia:* tome un par ordenado arbitrario \\((x, y)\\).)

---

## 💡 Soluciones y Guías Seleccionadas

> **Solución al Ejercicio 3.d:** 
> Probar que \\(\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)\\): 
> * \\(X \in \mathcal{P}(A \cap B) \iff X \subseteq (A \cap B)\\). 
> * Por definición de intersección, \\(X \subseteq (A \cap B) \iff (X \subseteq A \land X \subseteq B)\\). 
> * Por definición de conjunto potencia, esto equivale a \\(X \in \mathcal{P}(A) \land X \in \mathcal{P}(B)\\). 
> * Por definición de intersección, \\(X \in \mathcal{P}(A) \cap \mathcal{P}(B)\\). 
> Al haberse probado la cadena de equivalencias bicondicionales directas (o doble contención), queda demostrado el teorema. \\(\blacksquare\\)

> **Solución al Ejercicio 3.e:** 
> La afirmación es en general **FALSA**. 
> *Contraejemplo:* Sean \\(A = \\{1\\}\\) y \\(B = \\{2\\}\\). 
> Se tiene \\(A \cup B = \\{1, 2\\}\\). 
> El subconjunto \\(\\{1, 2\\} \in \mathcal{P}(A \cup B)\\). 
> Sin embargo, \\(\mathcal{P}(A) = \\{\emptyset, \\{1\\}\\}\\) y \\(\mathcal{P}(B) = \\{\emptyset, \\{2\\}\\}\\), por lo que \\(\mathcal{P}(A) \cup \mathcal{P}(B) = \\{\emptyset, \\{1\\}, \\{2\\}\\}\\). 
> Como \\(\\{1, 2\\} \notin \mathcal{P}(A) \cup \mathcal{P}(B)\\), se concluye que \\(\mathcal{P}(A \cup B) \neq \mathcal{P}(A) \cup \mathcal{P}(B)\\) (en realidad se cumple únicamente la inclusión estricta \\(\mathcal{P}(A) \cup \mathcal{P}(B) \subsetneq \mathcal{P}(A \cup B)\\)). \\(\blacksquare\\)

---

## 💡 Soluciones del Bloque E (Ejercicios 8 a 17)

<details>
<summary><strong>Mostrar / ocultar las soluciones de los Ejercicios 8 a 17</strong></summary>

**Ejercicio 8.**

* **a)** Sea \\(x \in A \setminus B\\). Por definición de diferencia, \\(x \in A\\) y \\(x \notin B\\). En particular, \\(x \in A\\). Por tanto, \\(A \setminus B \subseteq A\\). \\(\blacksquare\\)
* **b)** Suponga que existe \\(x \in (A \setminus B) \cap B\\). Entonces \\(x \in A \setminus B\\) y \\(x \in B\\). De la primera, \\(x \notin B\\); esto contradice \\(x \in B\\). Luego no existe tal \\(x\\) y \\((A \setminus B) \cap B = \emptyset\\). \\(\blacksquare\\)

**Ejercicio 9.**

\\((\Rightarrow)\\) Suponga \\(A \subseteq B\\). Si existiera \\(x \in A \setminus B\\), se tendría \\(x \in A\\) y \\(x \notin B\\); pero \\(x \in A\\) y \\(A \subseteq B\\) dan \\(x \in B\\), una contradicción. Por tanto \\(A \setminus B = \emptyset\\).

\\((\Leftarrow)\\) Suponga \\(A \setminus B = \emptyset\\). Sea \\(x \in A\\). Si fuera \\(x \notin B\\), entonces \\(x \in A \setminus B = \emptyset\\), lo cual es imposible. Luego \\(x \in B\\). Por tanto \\(A \subseteq B\\). \\(\blacksquare\\)

**Ejercicio 10.** Sea \\(x\\) arbitrario.

| Paso | Afirmación | Justificación |
| :---: | :--- | :--- |
| 1 | \\(x \in A \cup (B \cap C)\\) | Punto de partida |
| 2 | \\(\iff x \in A \lor (x \in B \land x \in C)\\) | Definiciones de unión e intersección |
| 3 | \\(\iff (x \in A \lor x \in B) \land (x \in A \lor x \in C)\\) | Distributividad lógica de \\(\lor\\) sobre \\(\land\\) (Ejercicio 6 de la Unidad 1) |
| 4 | \\(\iff x \in A \cup B \land x \in A \cup C\\) | Definición de unión |
| 5 | \\(\iff x \in (A \cup B) \cap (A \cup C)\\) | Definición de intersección |

Por extensionalidad, las dos expresiones son iguales. \\(\blacksquare\\)

**Ejercicio 11.** Sea \\(x \in A \cup C\\). Entonces \\(x \in A\\) o \\(x \in C\\).

* *Caso 1:* \\(x \in A\\). Como \\(A \subseteq B\\), \\(x \in B\\); luego \\(x \in B \cup D\\).
* *Caso 2:* \\(x \in C\\). Como \\(C \subseteq D\\), \\(x \in D\\); luego \\(x \in B \cup D\\).

Los casos son exhaustivos (provienen de la disyunción) y en ambos \\(x \in B \cup D\\). Por tanto \\(A \cup C \subseteq B \cup D\\). \\(\blacksquare\\)

**Ejercicio 12.** Sea \\(x\\) arbitrario. Con \\(a: x \in A\\) y \\(b: x \in B\\):

| Paso | Afirmación | Justificación |
| :---: | :--- | :--- |
| 1 | \\(x \in (A \setminus B) \cup B\\) | Punto de partida |
| 2 | \\(\iff (a \land \neg b) \lor b\\) | Definiciones de diferencia y unión |
| 3 | \\(\iff (a \lor b) \land (\neg b \lor b)\\) | Distributividad de \\(\lor\\) sobre \\(\land\\) |
| 4 | \\(\iff (a \lor b) \land \top\\) | Ley del complemento: \\(\neg b \lor b \equiv \top\\) |
| 5 | \\(\iff a \lor b\\) | Ley de identidad |
| 6 | \\(\iff x \in A \cup B\\) | Definición de unión |

\\(\blacksquare\\)

**Ejercicio 13.** Con \\(p: x \in A\\) y \\(q: x \in B\\), el lado izquierdo equivale a \\((p \land \neg q) \lor (q \land \neg p)\\) y el derecho a \\((p \lor q) \land \neg(p \land q)\\). Se verifica su equivalencia:

| \\(p\\) | \\(q\\) | \\((p \land \neg q) \lor (q \land \neg p)\\) | \\((p \lor q) \land \neg(p \land q)\\) |
| :---: | :---: | :---: | :---: |
| V | V | **F** | **F** |
| V | F | **V** | **V** |
| F | V | **V** | **V** |
| F | F | **F** | **F** |

Las dos columnas coinciden. Como esto vale para todo \\(x\\), ambos conjuntos tienen los mismos elementos y son iguales. \\(\blacksquare\\)

**Ejercicio 14.**

\\((\Rightarrow)\\) Suponga \\(\mathcal{P}(A) \subseteq \mathcal{P}(B)\\). Como \\(A \subseteq A\\), se tiene \\(A \in \mathcal{P}(A)\\), y por hipótesis \\(A \in \mathcal{P}(B)\\), es decir, \\(A \subseteq B\\).

\\((\Leftarrow)\\) Suponga \\(A \subseteq B\\). Sea \\(X \in \mathcal{P}(A)\\), es decir, \\(X \subseteq A\\). Como \\(X \subseteq A\\) y \\(A \subseteq B\\), por transitividad \\(X \subseteq B\\), esto es, \\(X \in \mathcal{P}(B)\\). Por tanto \\(\mathcal{P}(A) \subseteq \mathcal{P}(B)\\). \\(\blacksquare\\)

**Ejercicio 15.** La igualdad es **falsa**.

*Contraejemplo:* sean \\(A = \emptyset\\), \\(B = \\{1\\}\\) y \\(C = \emptyset\\). Entonces \\((A \setminus B) \cup (B \setminus C) = \emptyset \cup \\{1\\} = \\{1\\}\\), mientras que \\(A \setminus C = \emptyset\\). Como \\(\\{1\\} \neq \emptyset\\), la igualdad falla.

*La inclusión que sí se cumple* es \\(A \setminus C \subseteq (A \setminus B) \cup (B \setminus C)\\). En efecto, sea \\(x \in A \setminus C\\), es decir, \\(x \in A\\) y \\(x \notin C\\). Hay dos casos:

* *Caso 1:* \\(x \notin B\\). Entonces \\(x \in A \setminus B\\).
* *Caso 2:* \\(x \in B\\). Como \\(x \notin C\\), \\(x \in B \setminus C\\).

En ambos casos \\(x\\) pertenece a la unión. \\(\blacksquare\\) (La inclusión contraria falla justamente en el contraejemplo anterior: \\(1 \in B \setminus C\\) pero \\(1 \notin A \setminus C\\).)

**Ejercicio 16.** Sea \\(x\\) arbitrario.

| Paso | Afirmación | Justificación |
| :---: | :--- | :--- |
| 1 | \\(x \in B \cap \bigcup\_{i \in I} A\_i\\) | Punto de partida |
| 2 | \\(\iff x \in B \land (\exists i \in I)(x \in A\_i)\\) | Definiciones de intersección y de unión generalizada |
| 3 | \\(\iff (\exists i \in I)(x \in B \land x \in A\_i)\\) | Una proposición que no depende de \\(i\\) entra y sale del alcance de \\(\exists i\\) |
| 4 | \\(\iff (\exists i \in I)(x \in B \cap A\_i)\\) | Definición de intersección |
| 5 | \\(\iff x \in \bigcup\_{i \in I} (B \cap A\_i)\\) | Definición de unión generalizada |

\\(\blacksquare\\) *Observación:* el paso 3 es válido incluso si \\(I = \emptyset\\): ambos lados son falsos.

**Ejercicio 17.** Sea \\((x, y)\\) un par ordenado arbitrario.

| Paso | Afirmación | Justificación |
| :---: | :--- | :--- |
| 1 | \\((x, y) \in (A \cup B) \times C\\) | Punto de partida |
| 2 | \\(\iff x \in A \cup B \land y \in C\\) | Definición de producto cartesiano |
| 3 | \\(\iff (x \in A \lor x \in B) \land y \in C\\) | Definición de unión |
| 4 | \\(\iff (x \in A \land y \in C) \lor (x \in B \land y \in C)\\) | Distributividad de \\(\land\\) sobre \\(\lor\\) |
| 5 | \\(\iff (x, y) \in A \times C \lor (x, y) \in B \times C\\) | Definición de producto cartesiano |
| 6 | \\(\iff (x, y) \in (A \times C) \cup (B \times C)\\) | Definición de unión |

Como todo elemento de ambos conjuntos es un par ordenado, las dos expresiones son iguales. \\(\blacksquare\\)

</details>
