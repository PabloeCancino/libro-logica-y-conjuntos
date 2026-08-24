# Ejercicios de la Unidad 3

---

## 📝 Bloque A: Pertenencia, Inclusión y Conjunto Potencia

1. Sean los conjuntos \\(A = \{1, 2, \{1, 2\}, \emptyset\}\\). Determine el valor de verdad (Verdadero o Falso) de cada una de las siguientes afirmaciones:
 - a) \\(1 \in A\\)
 - b) \\(\{1\} \in A\\)
 - c) \\(\{1\} \subseteq A\\)
 - d) \\(\{1, 2\} \in A\\)
 - e) \\(\{1, 2\} \subseteq A\\)
 - f) \\(\emptyset \in A\\)
 - g) \\(\emptyset \subseteq A\\)
 - h) \\(\{\emptyset\} \subseteq A\\)

2. Determine el conjunto potencia \\(\mathcal{P}(A)\\) y su cardinalidad para cada uno de los siguientes conjuntos:
 - a) \\(A = \emptyset\\)
 - b) \\(A = \{a\}\\)
 - c) \\(A = \{1, \{2, 3\}\}\\)
 - d) \\(A = \mathcal{P}(\emptyset)\\)

---

## 📝 Bloque B: Álgebra de Conjuntos y Demostraciones de Doble Contención

3. Demuestre rigurosamente mediante el método de **doble contención** las siguientes igualdades conjuntistas:
 - a) \\(A \cap (B \cup C) = (A \cap B) \cup (A \cap C)\\)
 - b) \\(A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)\\)
 - c) \\(A \setminus (B \setminus C) = (A \setminus B) \cup (A \cap C)\\)
 - d) \\(\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)\\)
 - e) ¿Se cumple que \\(\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)\\)? (Demuéstrelo o dé un contraejemplo explícito).

---

## 📝 Bloque C: Cardinalidad, Particiones y Principio de Inclusión-Exclusión

4. Encuentre todas las particiones posibles del conjunto \\(A = \{a, b, c, d\}\\). (Verifique que el total coincida con el número de Bell \\(B\_4 = 15\\)).

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

6. Sean \\(A = \{1, 2\}\\), \\(B = \{a, b\}\\) y \\(C = \{x\}\\).
 - a) Calcule explícitamente \\(A \times B \times C\\).
 - b) Demuestre que \\(A \times (B \cap C) = (A \times B) \cap (A \times C)\\).

7. Para cada \\(n \in \mathbb{N}\\), defínase el intervalo abierto \\(A\_n = \left(-\frac{1}{n}, 1 + \frac{1}{n}\right) \subset \mathbb{R}\\). Calcule:
 - a) \\(\bigcup\_{n=1}^\infty A\_n\\)
 - b) \\(\bigcap\_{n=1}^\infty A\_n\\)

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
> *Contraejemplo:* Sean \\(A = \{1\}\\) y \\(B = \{2\}\\). 
> Se tiene \\(A \cup B = \{1, 2\}\\). 
> El subconjunto \\(\{1, 2\} \in \mathcal{P}(A \cup B)\\). 
> Sin embargo, \\(\mathcal{P}(A) = \{\emptyset, \{1\}\}\\) y \\(\mathcal{P}(B) = \{\emptyset, \{2\}\}\\), por lo que \\(\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}, \{2\}\}\\). 
> Como \\(\{1, 2\} \notin \mathcal{P}(A) \cup \mathcal{P}(B)\\), se concluye que \\(\mathcal{P}(A \cup B) \neq \mathcal{P}(A) \cup \mathcal{P}(B)\\) (en realidad se cumple únicamente la inclusión estricta \\(\mathcal{P}(A) \cup \mathcal{P}(B) \subsetneq \mathcal{P}(A \cup B)\\)). \\(\blacksquare\\)