# Notación y Convenciones

A continuación se resumen los principales símbolos matemáticos, conectivas y notaciones empleadas a lo largo de este libro.

---

### Lógica Proposicional y de Predicados

| Símbolo | Significado | Lectura en Lenguaje Natural |
| :--- | :--- | :--- |
| \\(p, q, r, s\\) | Variables proposicionales | Enunciados atómicos arbitrarios |
| \\(V, F\\) o \\(1, 0\\) | Valores de verdad | Verdadero, Falso |
| \\(\neg p\\) o \\(\sim p\\) | Negación lógica | "No \\(p\\)", "es falso que \\(p\\)" |
| \\(p \land q\\) | Conjunción | "\\(p\\) y \\(q\\)" |
| \\(p \lor q\\) | Disyunción inclusiva | "\\(p\\) o \\(q\\) (o ambos)" |
| \\(p \oplus q\\) | Disyunción exclusiva | "O bien \\(p\\) o bien \\(q\\), pero no ambos" |
| \\(p \to q\\) | Condicional material (implicación) | "Si \\(p\\), entonces \\(q\\)"; "\\(p\\) implica \\(q\\)" |
| \\(p \leftrightarrow q\\) | Bicondicional (doble implicación) | "\\(p\\) si y sólo si \\(q\\)"; "\\(p\\) es equivalente a \\(q\\)" |
| \\(A \equiv B\\) | Equivalencia lógica semántica | "\\(A\\) y \\(B\\) tienen la misma tabla de verdad" |
| \\(\top\\) | Tautología | Fórmula siempre verdadera |
| \\(\bot\\) | Contradicción / Absurdo | Fórmula siempre falsa |
| \\(\vdash\\) | Deducción sintáctica / Derivación | "Se deduce formalmente que..." |
| \\(\models\\) | Consecuencia semántica / Validez | "Implica tautológicamente en todos los modelos" |
| \\(\forall x\\) | Cuantificador universal | "Para todo \\(x\\)", "para cada \\(x\\)" |
| \\(\exists x\\) | Cuantificador existencial | "Existe al menos un \\(x\\)" |
| \\(\exists! x\\) | Cuantificador de existencia única | "Existe un único \\(x\\)" |

---

### Teoría de Conjuntos

| Símbolo | Significado | Lectura en Lenguaje Natural |
| :--- | :--- | :--- |
| \\(\in, \notin\\) | Pertenencia, no pertenencia | "\\(a\\) pertenece a \\(A\\)", "\\(b\\) no pertenece a \\(A\\)" |
| \\(\emptyset\\) o \\(\\{\\}\\) | Conjunto vacío | Conjunto sin elementos |
| \\(\mathcal{U}\\) | Conjunto universal | Universo de discurso contextual |
| \\(\subseteq\\) | Subconjunto (inclusión débil) | "\\(A\\) está contenido en \\(B\\)" |
| \\(\subset\\) o \\(\subsetneq\\) | Subconjunto propio (inclusión estricta) | "\\(A\\) está estrictamente contenido en \\(B\\)" |
| \\(A = B\\) | Igualdad extensional | "\\(A\\) y \\(B\\) tienen exactamente los mismos elementos" |
| \\(A \cup B\\) | Unión de conjuntos | "Elementos en \\(A\\), en \\(B\\) o en ambos" |
| \\(A \cap B\\) | Intersección de conjuntos | "Elementos simultáneamente en \\(A\\) y en \\(B\\)" |
| \\(A \setminus B\\) | Diferencia relativa (complemento relativo) | "Elementos en \\(A\\) que no están en \\(B\\)" |
| \\(A^c\\) o \\(A'\\) o \\(\overline{A}\\) | Complemento absoluto | "\\(\mathcal{U} \setminus A\\)" |
| \\(A \Delta B\\) | Diferencia simétrica | "\\((A \setminus B) \cup (B \setminus A)\\)" |
| \\(\mathcal{P}(A)\\) o \\(2^A\\) | Conjunto potencia (de partes) | Conjunto de todos los subconjuntos de \\(A\\) |
| \\(\|A\|\\) o \\(\\#(A)\\) | Cardinalidad | Número de elementos del conjunto \\(A\\) |
| \\(A \times B\\) | Producto cartesiano | Conjunto de pares ordenados \\(\\{(a, b) \mid a \in A \land b \in B\\}\\) |
| \\(\mathbb{N}\\) | Números naturales | \\(\\{1, 2, 3, \dots\\}\\) (o \\(\\{0, 1, 2, \dots\\}\\) según convención) |
| \\(\mathbb{Z}\\) | Números enteros | \\(\\{\dots, -2, -1, 0, 1, 2, \dots\\}\\) |
| \\(\mathbb{Q}\\) | Números racionales | \\(\\{p/q \mid p, q \in \mathbb{Z}, q \neq 0\\}\\) |
| \\(\mathbb{R}\\) | Números reales | Cuerpo ordenado y completo |
| \\(\mathbb{C}\\) | Números complejos | \\(\\{a + bi \mid a, b \in \mathbb{R}, i^2 = -1\\}\\) |

---

### Relaciones, Funciones y Demostraciones

| Símbolo | Significado | Lectura en Lenguaje Natural |
| :--- | :--- | :--- |
| \\(a R b\\) o \\((a, b) \in R\\) | Relación binaria | "\\(a\\) está relacionado con \\(b\\) bajo \\(R\\)" |
| \\(\sim, \equiv\\) | Relación de equivalencia | Relación reflexiva, simétrica y transitiva |
| \\([a]\\) o \\(\bar{a}\\) | Clase de equivalencia de \\(a\\) | Conjunto de todos los elementos equivalentes a \\(a\\) |
| \\(A/\sim\\) | Conjunto cociente | Conjunto formado por todas las clases de equivalencia |
| \\(\leq, \preceq\\) | Relación de orden parcial | Relación reflexiva, antisimétrica y transitiva |
| \\(f: A \to B\\) | Función o mapeo | Regla unívoca de asignación de \\(A\\) en \\(B\\) |
| \\(\text{Dom}(f), \text{Im}(f)\\) | Dominio e Imagen (Rango) | Conjunto de partida y conjunto de valores alcanzados |
| \\(g \circ f\\) | Composición de funciones | "\\(g\\) compuesta con \\(f\\)": \\((g \circ f)(x) = g(f(x))\\)" |
| \\(f^{-1}\\) | Función inversa / Preimagen | Inversa de una biyección \\(f\\) |
| \\(\blacksquare\\) o Q.E.D. | Fin de la demostración | *Quod erat demonstrandum* ("lo que se quería demostrar") |
| \\(\aleph\_0\\) | Álef cero | Cardinalidad de los números naturales (numerable) |
| \\(\mathfrak{c}\\) o \\(2^{\aleph\_0}\\) | Cardinal del continuo | Cardinalidad de los números reales (no numerable) |