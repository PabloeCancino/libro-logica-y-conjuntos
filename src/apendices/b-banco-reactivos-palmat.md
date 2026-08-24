# Apéndice B. Banco de Reactivos Institucionales Resueltos (PALMAT 2024)

Este apéndice presenta una selección representativa y comentada del banco curricular de **200 reactivos de opción múltiple** de la asignatura **Lógica y Conjuntos (CBIMAT-215)**, alineados a los estándares de evaluación del **PALMAT 2024** de la Universidad Autónoma de Nayarit.

---

## 📌 Unidad 1: Lógica Proposicional y Tablas de Verdad

### Reactivo 1.1: Semántica del Condicional Material
**Pregunta:** ¿Cuál es el valor de verdad del condicional \\(p \to q\\) cuando el antecedente \\(p\\) es VERDADERO y el consecuente \\(q\\) es FALSO? 
- A) Verdadero 
- B) **Falso (Correcta)** 
- C) Indeterminado 
- D) Tautológico 

> **Retroalimentación Formativa:** En la semántica de la lógica clásica proposicional, el condicional material \\(p \to q\\) resulta Falso en un único escenario: cuando la hipótesis antecedente \\(p\\) es Verdadera y la conclusión consecuente \\(q\\) es Falsa. En todos los demás casos resulta Verdadero.

---

### Reactivo 1.2: Negación de una Conjunción
**Pregunta:** ¿Cuál de las siguientes fórmulas es lógicamente equivalente a la negación de la conjunción \\(\neg(p \land q)\\)? 
- A) \\(\neg p \land \neg q\\) 
- B) **\\(\neg p \lor \neg q\\) (Correcta)** 
- C) \\(p \lor q\\) 
- D) \\(p \to \neg q\\) 

> **Retroalimentación Formativa:** Por la 1ª Ley de De Morgan para la lógica proposicional, la negación de una conjunción copulativa equivale estrictamente a la disyunción de las componentes negadas individualmente: \\(\neg(p \land q) \equiv \neg p \lor \neg q\\).

---

### Reactivo 1.3: Definición de Tautología
**Pregunta:** Una fórmula proposicional cuya columna final en la tabla de verdad resulta ser VERDADERA para todas y cada una de sus interpretaciones se define como: 
- A) Contingencia 
- B) Contradicción 
- C) **Tautología (Correcta)** 
- D) Falacia formal 

> **Retroalimentación Formativa:** Una fórmula bien formada que resulta verdadera bajo cualquier asignación de verdad de sus variables atómicas es una Tautología (por ejemplo, el principio de tercio excluso \\(p \lor \neg p\\)).

---

## 📌 Unidad 2: Cuantificadores y Reglas de Inferencia

### Reactivo 2.1: Negación de una Proposición Universal
**Pregunta:** La negación formal del enunciado cuantificado \\((\forall x \in \mathbb{R}) (x^2 \ge 0)\\) corresponde a: 
- A) \\((\forall x \in \mathbb{R}) (x^2 < 0)\\) 
- B) **\\((\exists x \in \mathbb{R}) (x^2 < 0)\\) (Correcta)** 
- C) \\((\exists x \in \mathbb{R}) (x^2 \ge 0)\\) 
- D) \\((\forall x \in \mathbb{R}) (x^2 \le 0)\\) 

> **Retroalimentación Formativa:** Por la ley de dualidad de cuantificadores, negar un cuantificador universal transforma el operador en existencial e invierte el predicado estricto: \\(\neg[(\forall x) P(x)] \equiv (\exists x) \neg P(x)\\). La negación de \\(x^2 \ge 0\\) es \\(x^2 < 0\\).

---

### Reactivo 2.2: Regla Modus Tollendo Tollens
**Pregunta:** Dadas las premisas \\(p \to q\\) y \\(\neg q\\), ¿cuál es la conclusión válida que se deriva por Modus Tollens? 
- A) \\(p\\) 
- B) **\\(\neg p\\) (Correcta)** 
- C) \\(q\\) 
- D) \\(p \land q\\) 

> **Retroalimentación Formativa:** La regla de inferencia *Modus Tollendo Tollens* (m.t.t.) establece que al negar el consecuente de una implicación se deduce necesariamente la negación del antecedente, preservando la validez deductiva formal.

---

## 📌 Unidad 3: Teoría de Conjuntos y Álgebra Booleana

### Reactivo 3.1: Cardinalidad del Conjunto Potencia
**Pregunta:** Si un conjunto \\(A\\) tiene cardinalidad \\(|A| = 5\\), ¿cuántos elementos contiene su conjunto potencia \\(\mathcal{P}(A)\\)? 
- A) 10 
- B) 25 
- C) **32 (Correcta)** 
- D) 64 

> **Retroalimentación Formativa:** El número de subconjuntos de un conjunto finito con \\(n\\) elementos viene dado por la fórmula exponencial \\(|\mathcal{P}(A)| = 2^n\\). Para \\(n=5\\), se tiene \\(2^5 = 32\\) subconjuntos posibles.

---

### Reactivo 3.2: Pertenencia del Conjunto Vacío
**Pregunta:** Para cualquier conjunto \\(A\\), ¿cuál de las siguientes afirmaciones es SIEMPRE verdadera? 
- A) \\(A \in \mathcal{P}(A)\\) y \\(\emptyset \subseteq A\\) 
- B) \\(\emptyset \in A\\) 
- C) **Tanto \\(A \in \mathcal{P}(A)\\) como \\(\emptyset \subseteq A\\) son siempre verdaderas (Correcta)** 
- D) \\(|A \cup A^c| = 0\\) 

> **Retroalimentación Formativa:** Por definición del conjunto potencia, \\(X \in \mathcal{P}(A) \iff X \subseteq A\\). Dado que \\(A \subseteq A\\) y \\(\emptyset \subseteq A\\) para cualquier conjunto, se tiene que \\(\emptyset \in \mathcal{P}(A)\\) y \\(A \in \mathcal{P}(A)\\).

---

## 📌 Unidad 4: Métodos de Demostración, Relaciones y Funciones

### Reactivo 4.1: Estructura de la Prueba por Contraposición
**Pregunta:** Para demostrar la implicación \\(P \implies Q\\) mediante el método por contraposición, la hipótesis de trabajo asumida al inicio es: 
- A) \\(P\\) es verdadera 
- B) **\\(Q\\) es falsa (\\(\neg Q\\) es verdadera) (Correcta)** 
- C) \\(P \land Q\\) es verdadera 
- D) \\(\neg P\\) es verdadera 

> **Retroalimentación Formativa:** El método de contraposición se fundamenta en la equivalencia \\((P \implies Q) \equiv (\neg Q \implies \neg P)\\). Se inicia asumiendo \\(\neg Q\\) como hipótesis para deducir directamente \\(\neg P\\).

---

### Reactivo 4.2: Relaciones de Equivalencia
**Pregunta:** Una relación binaria \\(R\\) sobre un conjunto \\(A\\) es de equivalencia si y sólo si cumple las propiedades: 
- A) Reflexiva, Antisimétrica y Transitiva 
- B) **Reflexiva, Simétrica y Transitiva (Correcta)** 
- C) Irreflexiva, Asimétrica y Transitiva 
- D) Total, Inyectiva y Biyectiva 

> **Retroalimentación Formativa:** Por definición fundamental, una relación de equivalencia debe satisfacer simultáneamente la reflexividad, la simetría y la transitividad (Propiedades RST), lo que garantiza la inducción de una partición canónica en el conjunto cociente \\(A/R\\).