# Ejercicios de la Unidad 4

---

## 📝 Bloque A: Métodos de Demostración Formal

1. Demuestre por **prueba directa** que si \\(a, b \in \mathbb{Z}\\) son enteros impares, entonces su producto \\(a \cdot b\\) es un entero impar.

2. Demuestre por **contraposición** que si \\(3n + 2\\) es un número entero impar, entonces \\(n\\) es un número entero impar.

3. Demuestre por **reducción al absurdo** (contradicción) que \\(\log\_2(3)\\) es un número irracional.

4. Demuestre por **casos exhaustivos** que para todo entero \\(n \in \mathbb{Z}\\), el número \\(n^3 - n\\) es divisible por 3.

---

## 📝 Bloque B: Principio de Inducción Matemática

5. Demuestre por inducción matemática que para todo \\(n \ge 1\\):
 - a) \\(\sum\_{i=1}^n i^2 = 1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}\\)
 - b) \\(\sum\_{i=1}^n i^3 = 1^3 + 2^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2\\)
 - c) \\(\sum\_{i=0}^n 2^i = 1 + 2 + 4 + \dots + 2^n = 2^{n+1} - 1\\)
 - d) \\(n^3 + 2n\\) es divisible por 3 para todo \\(n \in \mathbb{N}\\).
 - e) \\(2^n > n^2\\) para todo entero \\(n \ge 5\\).

---

## 📝 Bloque C: Relaciones de Equivalencia y de Orden

6. Sea \\(R\\) la relación sobre \\(\mathbb{Z} \times (\mathbb{Z} \setminus \\{0\\})\\) definida por:

\\[
(a, b) \, R \, (c, d) \iff a \cdot d = b \cdot c
\\]

 - a) Demuestre que \\(R\\) es una relación de equivalencia (Propiedades Reflexiva, Simétrica y Transitiva).
 - b) Describa la clase de equivalencia \\([(1, 2)]\\). ¿Qué conjunto numérico fundamental se construye mediante este conjunto cociente?

7. Sea \\(A = \\{1, 2, 3, 4, 6, 12\\}\\) ordenado mediante la relación de divisibilidad \\(a \mid b\\).
 - a) Dibuje el diagrama de Hasse correspondiente.
 - b) Identifique los elementos minimales, maximales, el mínimo y el máximo de \\(A\\) (si existen).

---

## 📝 Bloque D: Funciones y Cardinalidad Infinita

8. Para cada una de las siguientes funciones, determine si es inyectiva, sobreyectiva o biyectiva. Si es biyectiva, determine su función inversa \\(f^{-1}\\):
 - a) \\(f: \mathbb{R} \to \mathbb{R}\\), \\(f(x) = 3x - 5\\)
 - b) \\(g: \mathbb{R} \to \mathbb{R}\\), \\(g(x) = x^2 - 1\\)
 - c) \\(h: [0, \infty) \to [0, \infty)\\), \\(h(x) = x^2\\)
 - d) \\(k: \mathbb{Z} \to \mathbb{N}\\), dada por \\(k(n) = 2n\\) si \\(n > 0\\), y \\(k(n) = 2(-n) + 1\\) si \\(n \le 0\\).

9. Demuestre el **Teorema de Cantor**: Para todo conjunto \\(A\\), no existe ninguna función sobreyectiva \\(f: A \to \mathcal{P}(A)\\). 
*(Sugerencia: Considere el conjunto diagonal \\(D = \\{x \in A \mid x \notin f(x)\\} \in \mathcal{P}(A)\\) y suponga que existe \\(d \in A\\) tal que \\(f(d) = D\\))*.

---

## 💡 Soluciones y Guías Seleccionadas

> **Solución al Ejercicio 3 (Irracionalidad de \\(\log\_2(3)\\)):** 
> Supongamos por contradicción que \\(\log\_2(3) \in \mathbb{Q}\\). 
> Como \\(3 > 1\\) y \\(2 > 1\\), \\(\log\_2(3) > 0\\). Por tanto existen enteros positivos \\(p, q \in \mathbb{N}\\) tales que: 
>
> \\[
> \log\_2(3) = \frac{p}{q}
> \\]
>
> Por la definición de logaritmo: 
>
> \\[
> 2^{p/q} = 3 \implies 2^p = 3^q
> \\]
>
> Como \\(p \ge 1\\), el miembro izquierdo \\(2^p\\) es un número entero **par**. 
> Como \\(q \ge 1\\), el miembro derecho \\(3^q\\) es producto de impares y por ende es un número **impar**. 
> Esto genera la contradicción lógica \\(\text{par} = \text{impar}\\) (\\(\bot\\)). 
> Por lo tanto, \\(\log\_2(3)\\) es un número **irracional**. \\(\blacksquare\\)

> **Solución al Ejercicio 9 (Teorema de Cantor):** 
> Sea \\(f: A \to \mathcal{P}(A)\\) una función arbitraria. 
> Definamos el conjunto \\(D = \\{x \in A \mid x \notin f(x)\\}\\). Claramente \\(D \subseteq A\\), luego \\(D \in \mathcal{P}(A)\\). 
> Supongamos por reducción al absurdo que \\(f\\) es sobreyectiva. 
> Entonces debe existir un elemento \\(d \in A\\) tal que \\(f(d) = D\\). 
> Analicemos si \\(d \in D\\): 
> * Si \\(d \in D\\), por la definición de \\(D\\) se tiene que \\(d \notin f(d) = D\\) (Contradicción). 
> * Si \\(d \notin D\\), entonces \\(d \notin f(d)\\), por lo que \\(d\\) cumple la condición para pertenecer a \\(D\\), es decir, \\(d \in D\\) (Contradicción). 
> En ambos casos se arriba a \\(d \in D \iff d \notin D\\) (\\(\bot\\)). 
> Por tanto, \\(f\\) no puede ser sobreyectiva, demostrando que \\(|A| < |\mathcal{P}(A)|\\) para todo conjunto \\(A\\). \\(\blacksquare\\)

---

## 💡 Soluciones de la sección 4.0.1 (seis demostraciones modelo)

<details>
<summary><strong>Mostrar / ocultar las soluciones de los Ejercicios 1 a 10</strong></summary>

Intente cada ejercicio por su cuenta antes de abrir este bloque. Las soluciones siguen la numeración de la sección 4.0.1.

### Nivel básico

**Ejercicio 1.** \\(\neg(p \lor q) \equiv \neg p \land \neg q\\)

| \\(p\\) | \\(q\\) | \\(p \lor q\\) | \\(\neg(p \lor q)\\) | \\(\neg p\\) | \\(\neg q\\) | \\(\neg p \land \neg q\\) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| V | V | V | **F** | F | F | **F** |
| V | F | V | **F** | F | V | **F** |
| F | V | V | **F** | V | F | **F** |
| F | F | F | **V** | V | V | **V** |

Las columnas cuarta y séptima coinciden en las cuatro filas. \\(\blacksquare\\)

**Ejercicio 2.** \\(p \to q \equiv \neg(p \land \neg q)\\)

| Paso | Fórmula | Justificación |
| :---: | :--- | :--- |
| 1 | \\(p \to q\\) | Punto de partida |
| 2 | \\(\neg p \lor q\\) | Definición del condicional |
| 3 | \\(\neg p \lor \neg(\neg q)\\) | Doble negación aplicada a \\(q\\) |
| 4 | \\(\neg(p \land \neg q)\\) | De Morgan: \\(\neg a \lor \neg b \equiv \neg(a \land b)\\), con \\(a = p\\) y \\(b = \neg q\\) |

\\(\blacksquare\\)

**Ejercicio 3.** Tabla de \\(p \to (q \to p)\\):

| \\(p\\) | \\(q\\) | \\(q \to p\\) | \\(p \to (q \to p)\\) |
| :---: | :---: | :---: | :---: |
| V | V | V | **V** |
| V | F | V | **V** |
| F | V | F | **V** |
| F | F | V | **V** |

La última columna es verdadera en las cuatro filas: es una tautología. *Explicación:* si \\(p\\) es verdadera, el consecuente \\(q \to p\\) es verdadero sea cual sea \\(q\\) (su consecuente \\(p\\) es verdadero); si \\(p\\) es falsa, el condicional exterior es verdadero por tener antecedente falso (sección 1.2). \\(\blacksquare\\)

**Ejercicio 4.** \\(A \subseteq A \cup B\\)

Sea \\(x\\) un elemento arbitrario de \\(A\\). Entonces \\(x \in A\\) y, por la regla de adición (\\(p \vdash p \lor q\\)), \\(x \in A \lor x \in B\\). Por definición de unión, \\(x \in A \cup B\\). Como \\(x\\) era arbitrario, \\(A \subseteq A \cup B\\). \\(\blacksquare\\)

### Nivel medio

**Ejercicio 5.** \\((p \to q) \equiv ((p \lor q) \leftrightarrow q)\\)

| \\(p\\) | \\(q\\) | \\(p \to q\\) | \\(p \lor q\\) | \\((p \lor q) \leftrightarrow q\\) |
| :---: | :---: | :---: | :---: | :---: |
| V | V | **V** | V | **V** |
| V | F | **F** | V | **F** |
| F | V | **V** | V | **V** |
| F | F | **V** | F | **V** |

Las columnas tercera y quinta coinciden. *Relación con el Modelo C3:* la igualdad \\(A \cup B = B\\) significa \\((\forall x)(x \in A \lor x \in B \leftrightarrow x \in B)\\). Por esta equivalencia, cada fórmula entre paréntesis es equivalente a \\(x \in A \to x \in B\\), y así \\(A \cup B = B\\) equivale a \\(A \subseteq B\\). El Modelo C3 es, por tanto, la versión cuantificada de este ejercicio. \\(\blacksquare\\)

**Ejercicio 6.** \\((A \cap B)^c = A^c \cup B^c\\)

Sea \\(x \in \mathcal{U}\\) arbitrario.

| Paso | Afirmación | Justificación |
| :---: | :--- | :--- |
| 1 | \\(x \in (A \cap B)^c\\) | Punto de partida |
| 2 | \\(\iff x \notin A \cap B\\) | Definición de complemento |
| 3 | \\(\iff \neg(x \in A \land x \in B)\\) | Definición de intersección |
| 4 | \\(\iff x \notin A \lor x \notin B\\) | De Morgan lógico (Modelo L1) |
| 5 | \\(\iff x \in A^c \lor x \in B^c\\) | Definición de complemento |
| 6 | \\(\iff x \in A^c \cup B^c\\) | Definición de unión |

Como \\(x\\) era arbitrario, por extensionalidad \\((A \cap B)^c = A^c \cup B^c\\). \\(\blacksquare\\)

**Ejercicio 7.** \\(A \subseteq B \iff A \cap B = A\\)

\\((\Rightarrow)\\) Suponga \\(A \subseteq B\\). Por doble contención:

* \\(A \cap B \subseteq A\\) es el Modelo C1.
* \\(A \subseteq A \cap B\\): sea \\(x \in A\\). Por hipótesis, \\(x \in B\\). Luego \\(x \in A\\) y \\(x \in B\\), es decir, \\(x \in A \cap B\\).

Por tanto \\(A \cap B = A\\).

\\((\Leftarrow)\\) Suponga \\(A \cap B = A\\). Sea \\(x \in A\\). Como \\(A = A \cap B\\), se tiene \\(x \in A \cap B\\), y por simplificación \\(x \in B\\). Por tanto \\(A \subseteq B\\). \\(\blacksquare\\)

**Ejercicio 8.** De \\(p \to q\\) y \\(p \to r\\) se deduce \\(p \to (q \land r)\\).

| N.º | Fórmula | Justificación |
| :---: | :--- | :--- |
| 1 | \\(p \to q\\) | Premisa |
| 2 | \\(p \to r\\) | Premisa |
| 3 | \\(p\\) | Supuesto (para la prueba condicional) |
| 4 | \\(q\\) | Modus ponens, de 1 y 3 |
| 5 | \\(r\\) | Modus ponens, de 2 y 3 |
| 6 | \\(q \land r\\) | Introducción de la conjunción, de 4 y 5 |
| 7 | \\(p \to (q \land r)\\) | Prueba condicional, líneas 3 a 6 (se descarga el supuesto 3) |

\\(\blacksquare\\)

### Nivel de reto

**Ejercicio 9.** Si \\(A \subseteq B\\), entonces \\(B^c \subseteq A^c\\).

La hipótesis dice que, para todo \\(x \in \mathcal{U}\\), \\(x \in A \to x \in B\\). Por la contrapositiva (Modelo L2), para cada \\(x\\) esta condicional es equivalente a \\(x \notin B \to x \notin A\\), es decir, a \\(x \in B^c \to x \in A^c\\). Como esto vale para todo \\(x \in \mathcal{U}\\), se concluye que \\(B^c \subseteq A^c\\). \\(\blacksquare\\)

**Ejercicio 10.** La afirmación «Si \\(A \cup B \subseteq A \cup C\\), entonces \\(B \subseteq C\\)» es **falsa**.

*Contraejemplo:* sean \\(A = \\{1\\}\\), \\(B = \\{1\\}\\) y \\(C = \emptyset\\). Entonces \\(A \cup B = \\{1\\}\\) y \\(A \cup C = \\{1\\}\\), de modo que \\(A \cup B \subseteq A \cup C\\). Pero \\(B = \\{1\\} \not\subseteq \emptyset = C\\).

*Diagnóstico:* los elementos de \\(B\\) pueden quedar «cubiertos» por \\(A\\) en ambos lados, de modo que la hipótesis no dice nada sobre ellos. Esto es el mismo error de «cancelar \\(A\\)» que se analizó en la sección 4.0.

*Versión corregida (verdadera):* si \\(A \cup B \subseteq A \cup C\\) y \\(A \cap B = \emptyset\\), entonces \\(B \subseteq C\\). En efecto, sea \\(x \in B\\). Entonces \\(x \in A \cup B\\) y, por hipótesis, \\(x \in A \cup C\\). Como \\(A \cap B = \emptyset\\) y \\(x \in B\\), se tiene \\(x \notin A\\). Por tanto, \\(x \in C\\). \\(\blacksquare\\)

</details>
