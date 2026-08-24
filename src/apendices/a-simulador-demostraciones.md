# Apéndice A. Simulador de Demostraciones Matemáticas Formales

Este apéndice reúne las **14 demostraciones matemáticas formales paso a paso** desarrolladas para el proyecto curricular de **Lógica y Conjuntos (CBIMAT-215)** de la Universidad Autónoma de Nayarit, estructuradas con justificaciones axiomáticas rigurosas.

---

## 1. Demostraciones de la Unidad 1: Lógica Proposicional

### Demostración 1: 1ª Ley de De Morgan Proposicional

\\[
\neg(p \land q) \;\equiv\; \neg p \lor \neg q
\\]

1. **Objetivo:** Demostrar que la negación de una conjunción \\(\neg(p \land q)\\) es lógicamente equivalente a la disyunción de las negaciones \\(\neg p \lor \neg q\\).
2. **Método:** Tablas de verdad exhaustivas para las cuatro combinaciones de \\((p, q) \in \{V, F\}^2\\).
3. **Fila \\((V, V)\\):** \\(p \land q = V \implies \neg(p \land q) = F\\). Por la derecha: \\(\neg p \lor \neg q = F \lor F = F\\). Coinciden en \\(F\\).
4. **Fila \\((V, F)\\):** \\(p \land q = F \implies \neg(p \land q) = V\\). Por la derecha: \\(\neg p \lor \neg q = F \lor V = V\\). Coinciden en \\(V\\).
5. **Fila \\((F, V)\\):** \\(p \land q = F \implies \neg(p \land q) = V\\). Por la derecha: \\(\neg p \lor \neg q = V \lor F = V\\). Coinciden en \\(V\\).
6. **Fila \\((F, F)\\):** \\(p \land q = F \implies \neg(p \land q) = V\\). Por la derecha: \\(\neg p \lor \neg q = V \lor V = V\\). Coinciden en \\(V\\).
7. **Conclusión:** Las columnas son idénticas en todas las interpretaciones. Por tanto, \\(\neg(p \land q) \equiv \neg p \lor \neg q\\). \\(\blacksquare\\)

---

### Demostración 2: Silogismo Hipotético

\\[
[(p \to q) \land (q \to r)] \;\implies\; (p \to r)
\\]

1. **Premisa 1:** \\(p \to q\\).
2. **Premisa 2:** \\(q \to r\\).
3. **Suposición:** Asumimos que el antecedente \\(p\\) es verdadero.
4. De \\(p\\) y \\(p \to q\\), por *Modus Ponendo Ponens* obtenemos \\(q\\).
5. De \\(q\\) y \\(q \to r\\), por *Modus Ponendo Ponens* obtenemos \\(r\\).
6. Habiendo deducido \\(r\\) bajo la hipótesis \\(p\\), por el Teorema de la Deducción se concluye \\(p \to r\\). \\(\blacksquare\\)

---

### Demostración 3: Equivalencia Disyuntiva del Condicional

\\[
(p \to q) \;\equiv\; (\neg p \lor q)
\\]

1. El condicional \\(p \to q\\) es falso únicamente cuando \\(p = V\\) y \\(q = F\\).
2. La disyunción \\(\neg p \lor q\\) es falsa únicamente cuando \\(\neg p = F\\) (es decir, \\(p = V\\)) y \\(q = F\\).
3. En los tres casos restantes (\\(V-V\\), \\(F-V\\), \\(F-F\\)), ambas fórmulas evalúan a Verdadero (\\(V\\)).
4. Al tener exactamente la misma tabla de verdad, \\((p \to q) \equiv (\neg p \lor q)\\). \\(\blacksquare\\)

---

## 2. Demostraciones de la Unidad 2: Cuantificadores e Inferencia

### Demostración 4: Negación del Cuantificador Universal

\\[
\neg(\forall x \in A)\, p(x) \;\equiv\; (\exists x \in A)\, \neg p(x)
\\]

1. Supongamos que \\(\neg(\forall x \in A) p(x)\\) es verdadera.
2. Por definición de negación, la afirmación universal \\((\forall x \in A) p(x)\\) es falsa.
3. Para que un enunciado universal sea falso en el universo \\(A\\), no todos los elementos verifican el predicado \\(p(x)\\).
4. Por tanto, existe al menos un elemento testigo \\(x\_0 \in A\\) tal que \\(p(x\_0)\\) es falso.
5. Que \\(p(x\_0)\\) sea falso equivale a que su negación \\(\neg p(x\_0)\\) sea verdadera.
6. La existencia de dicho testigo demuestra que \\((\exists x \in A) \neg p(x)\\) es verdadera. \\(\blacksquare\\)

---

### Demostración 5: Regla Modus Tollendo Tollens

\\[
[(p \to q) \land \neg q] \;\implies\; \neg p
\\]

1. **Premisas:** \\(p \to q\\) y \\(\neg q\\).
2. Supongamos por reducción al absurdo que \\(\neg p\\) es falsa; por tanto, \\(p\\) es verdadera.
3. Aplicando *Modus Ponens* con \\(p\\) y \\(p \to q\\), deducimos \\(q\\).
4. Sin embargo, por la Premisa 2 tenemos \\(\neg q\\). Esto genera una contradicción directa \\(q \land \neg q\\) (\\(\bot\\)).
5. La suposición de que \\(p\\) era verdadera es insostenible. Concluimos \\(\neg p\\). \\(\blacksquare\\)

---

## 3. Demostraciones de la Unidad 3: Teoría de Conjuntos

### Demostración 6: De Morgan Conjuntista

\\[
(A \cup B)^c \;=\; A^c \cap B^c
\\]

1. \\(x \in (A \cup B)^c \iff x \notin (A \cup B)\\) (Definición de complemento).
2. \\(\iff \neg(x \in A \lor x \in B)\\) (Definición de unión).
3. \\(\iff x \notin A \land x \notin B\\) (1ª Ley de De Morgan lógica).
4. \\(\iff x \in A^c \land x \in B^c\\) (Definición de complementos individuales).
5. \\(\iff x \in A^c \cap B^c\\) (Definición de intersección).
6. Dado que cada paso es un bicondicional, queda demostrada la igualdad \\((A \cup B)^c = A^c \cap B^c\\). \\(\blacksquare\\)

---

### Demostración 7: Descomposición Ortogonal de un Conjunto

\\[
A \;=\; (A \cap B) \cup (A \setminus B)
\\]

1. Reescribimos la diferencia relativa como \\(A \setminus B = A \cap B^c\\).
2. La expresión se convierte en \\((A \cap B) \cup (A \cap B^c)\\).
3. Aplicamos distributividad de \\(\cap\\) sobre \\(\cup\\): \\(= A \cap (B \cup B^c)\\).
4. Por la propiedad del complemento universal, \\(B \cup B^c = \mathcal{U}\\).
5. Sustituyendo: \\(= A \cap \mathcal{U} = A\\). Por tanto, \\(A = (A \cap B) \cup (A \setminus B)\\). \\(\blacksquare\\)

---

### Demostración 8: Distributividad de la Intersección sobre la Unión

\\[
A \cap (B \cup C) \;=\; (A \cap B) \cup (A \cap C)
\\]

1. Sea \\(x \in \mathcal{U}\\).
2. \\(x \in A \cap (B \cup C) \iff x \in A \land x \in (B \cup C)\\).
3. \\(\iff x \in A \land (x \in B \lor x \in C)\\).
4. \\(\iff (x \in A \land x \in B) \lor (x \in A \land x \in C)\\) (Distributividad lógica de \\(\land\\) sobre \\(\lor\\)).
5. \\(\iff x \in (A \cap B) \lor x \in (A \cap C)\\).
6. \\(\iff x \in (A \cap B) \cup (A \cap C)\\). \\(\blacksquare\\)

---

## 4. Demostraciones de la Unidad 4: Métodos de Demostración e Inducción

### Demostración 9: Irracionalidad de \\(\sqrt{2}\\)

\\[
\sqrt{2} \;\notin\; \mathbb{Q}
\\]

1. Supongamos por contradicción que \\(\sqrt{2} \in \mathbb{Q}\\).
2. Existen enteros positivos coprimos \\(a, b \in \mathbb{Z}^+\\) con \\(\gcd(a, b) = 1\\) tales que \\(\sqrt{2} = \frac{a}{b}\\).
3. Elevando al cuadrado: \\(2 = \frac{a^2}{b^2} \implies a^2 = 2b^2\\).
4. Como \\(a^2\\) es par, se deduce que \\(a\\) es par (\\(a = 2k\\)).
5. Sustituyendo: \\((2k)^2 = 2b^2 \implies 4k^2 = 2b^2 \implies b^2 = 2k^2\\).
6. Por ende \\(b^2\\) es par y \\(b\\) también es par.
7. Si \\(a\\) y \\(b\\) son pares, \\(2 \mid \gcd(a, b)\\), contradiciendo que \\(\gcd(a, b) = 1\\). ∴ \\(\sqrt{2} \notin \mathbb{Q}\\). \\(\blacksquare\\)

---

### Demostración 10: Infinitud de los Números Primos (Euclides)

\\[
|\mathbb{P}| \;=\; \infty
\\]

1. Supongamos por contradicción que el conjunto de primos es finito: \\(\mathbb{P} = \{p\_1, p\_2, \dots, p\_n\}\\).
2. Construimos el entero \\(N = (p\_1 \cdot p\_2 \cdot \dots \cdot p\_n) + 1\\).
3. Como \\(N > 1\\), por el Teorema Fundamental de la Aritmética, \\(N\\) tiene un divisor primo \\(q\\).
4. Por la suposición de finitud, \\(q\\) debe ser igual a algún \\(p\_i\\) de la lista.
5. Luego \\(q \mid (p\_1 \dots p\_n)\\).
6. Como \\(q \mid N\\) y \\(q \mid (p\_1 \dots p\_n)\\), debe dividir a su diferencia: \\(q \mid [N - (p\_1 \dots p\_n)] = 1\\).
7. Pero ningún primo divide a 1. Esta contradicción prueba que existen infinitos primos. \\(\blacksquare\\)

---

### Demostración 11: Suma de los Primeros \\(n\\) Naturales

\\[
\sum\_{i=1}^n i \;=\; \frac{n(n+1)}{2}
\\]

1. **Base (\\(n=1\\)):** \\(1 = \frac{1(2)}{2} = 1\\) (Verdadero).
2. **Hipótesis Inductiva:** Asumimos \\(1 + 2 + \dots + k = \frac{k(k+1)}{2}\\).
3. **Paso Inductivo:**

\\[
[1 + 2 + \dots + k] + (k+1) = \frac{k(k+1)}{2} + (k+1) = (k+1)\left[\frac{k}{2} + 1\right] = \frac{(k+1)(k+2)}{2}
\\]

4. Queda demostrado para todo \\(n \in \mathbb{N}\\). \\(\blacksquare\\)

---

### Demostración 12: Cardinalidad del Conjunto Potencia

\\[
|\mathcal{P}(A)| \;=\; 2^n \quad (\text{para } |A| = n)
\\]

1. **Base (\\(n=0\\)):** \\(A = \emptyset \implies \mathcal{P}(\emptyset) = \{\emptyset\}\\), \\(|\mathcal{P}(\emptyset)| = 1 = 2^0\\).
2. **Hipótesis Inductiva:** Todo conjunto con \\(k\\) elementos posee \\(2^k\\) subconjuntos.
3. Sea \\(B = A \cup \{x\_{k+1}\}\\) con \\(|A| = k\\) y \\(x\_{k+1} \notin A\\).
4. Los subconjuntos de \\(B\\) se dividen en dos clases disjuntas: los que no contienen a \\(x\_{k+1}\\) (que son los \\(2^k\\) subconjuntos de \\(A\\)) y los que sí lo contienen (formados agregando \\(x\_{k+1}\\) a cada uno de los anteriores, otros \\(2^k\\)).
5. Total: \\(2^k + 2^k = 2^{k+1}\\). Por inducción, \\(|\mathcal{P}(A)| = 2^n\\) para todo \\(n \ge 0\\). \\(\blacksquare\\)

---

### Demostración 13: Prueba por Contraposición de la Paridad

\\[
n^2 \text{ es par} \;\implies\; n \text{ es par}
\\]

1. Demostraremos la contrapositiva equivalente: *"Si \\(n\\) es impar, entonces \\(n^2\\) es impar"*.
2. Asumimos \\(n = 2k + 1\\) con \\(k \in \mathbb{Z}\\).
3. \\(n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1\\).
4. Definiendo \\(m = 2k^2 + 2k \in \mathbb{Z}\\), se tiene \\(n^2 = 2m + 1\\), lo que prueba que \\(n^2\\) es impar.
5. Por contraposición, si \\(n^2\\) es par, \\(n\\) es par. \\(\blacksquare\\)

---

### Demostración 14: Desigualdad de Bernoulli

\\[
(1 + x)^n \;\ge\; 1 + nx \quad (\forall x > -1, \; n \in \mathbb{N})
\\]

1. **Base (\\(n=1\\)):** \\((1 + x)^1 = 1 + x \ge 1 + 1\cdot x\\) (Verdadero).
2. **Hipótesis Inductiva:** \\((1 + x)^k \ge 1 + kx\\) para \\(k \ge 1\\).
3. Como \\(x > -1\\), \\(1 + x > 0\\). Multiplicando ambos lados:

\\[
(1 + x)^{k+1} \ge (1 + kx)(1 + x) = 1 + x + kx + kx^2 = 1 + (k+1)x + kx^2
\\]

4. Como \\(kx^2 \ge 0\\), se deduce \\(1 + (k+1)x + kx^2 \ge 1 + (k+1)x\\).
5. Por transitividad: \\((1 + x)^{k+1} \ge 1 + (k+1)x\\). Queda demostrado para todo \\(n \in \mathbb{N}\\). \\(\blacksquare\\)