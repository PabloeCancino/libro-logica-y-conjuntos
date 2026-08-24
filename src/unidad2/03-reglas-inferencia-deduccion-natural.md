# 2.3 Reglas de Inferencia y Deducción Natural

En lugar de recurrir a tablas de verdad exponenciales (que para \\(n\\) variables requieren \\(2^n\\) filas), las demostraciones en matemáticas formales se efectúan mediante el método de **Deducción Natural**, aplicando una secuencia finita de **reglas de inferencia** que preservan tautológicamente la verdad de las premisas hacia la conclusión.

---

## 1. Las Reglas de Inferencia Fundamentales del Cálculo Proposicional

A continuación se resumen las reglas de derivación elementales más importantes:

### A. Modus Ponendo Ponens (m.p.p. o Modus Ponens)
"El método que afirmando el antecedente, afirma el consecuente".

\\[
\frac{p \to q, \quad p}{\therefore q}
\\]

### B. Modus Tollendo Tollens (m.t.t. o Modus Tollens)
"El método que negando el consecuente, niega el antecedente".

\\[
\frac{p \to q, \quad \neg q}{\therefore \neg p}
\\]

### C. Modus Tollendo Ponens (m.t.p. o Silogismo Disyuntivo)
"El método que negando una alternativa de la disyunción, afirma la otra".

\\[
\frac{p \lor q, \quad \neg p}{\therefore q} \qquad \text{o bien} \qquad \frac{p \lor q, \quad \neg q}{\therefore p}
\\]

### D. Ley del Silogismo Hipotético (Transitividad de la Implicación)

\\[
\frac{p \to q, \quad q \to r}{\therefore p \to r}
\\]

### E. Ley del Dilema Constructivo

\\[
\frac{(p \to q) \land (r \to s), \quad p \lor r}{\therefore q \lor s}
\\]

### F. Ley de Simplificación Conjuntiva

\\[
\frac{p \land q}{\therefore p} \qquad \text{y} \qquad \frac{p \land q}{\therefore q}
\\]

### G. Ley de Adición Disyuntiva

\\[
\frac{p}{\therefore p \lor q}
\\]

### H. Ley de Conjunción (o Introducción del ∧)

\\[
\frac{p, \quad q}{\therefore p \land q}
\\]

---

## 2. Reglas de Inferencia para Cuantificadores

Para conectar el cálculo de predicados con el cálculo proposicional se introducen cuatro reglas de manipulación de cuantificadores:

### A. Ejemplificación Universal (E.U. o Eliminación de ∀)
Si una propiedad se cumple para absolutamente todo elemento del universo \\(U\\), se cumple en particular para cualquier elemento específico \\(c \in U\\):

\\[
\frac{(\forall x) P(x)}{\therefore P(c)} \quad (\text{para cualquier } c \in U)
\\]

### B. Generalización Universal (G.U. o Introducción de ∀)
Si se demuestra que \\(P(c)\\) es verdadero para un elemento **arbitrario y genérico** \\(c \in U\\) (sin suposiciones adicionales sobre \\(c\\)):

\\[
\frac{P(c) \quad (c \text{ arbitrario})}{\therefore (\forall x) P(x)}
\\]

### C. Ejemplificación Existencial (E.E. o Eliminación de ∃)
Si se sabe que existe al menos un elemento que cumple \\(P\\), podemos asignarle un nombre o etiqueta nueva \\(c\\) (que no haya aparecido previamente en la deducción):

\\[
\frac{(\exists x) P(x)}{\therefore P(c) \quad (c \text{ nuevo elemento testigo})}
\\]

### D. Generalización Existencial (G.E. o Introducción de ∃)
Si se exhibe un elemento concreto \\(c\\) que cumple \\(P(c)\\), se concluye inmediatamente que existe al menos uno:

\\[
\frac{P(c)}{\therefore (\exists x) P(x)}
\\]

---

## 3. Ejemplo de Deducción Formal Paso a Paso

Demostremos la validez del siguiente argumento:
* Premisa 1: \\(p \to q\\)
* Premisa 2: \\(q \to \neg r\\)
* Premisa 3: \\(r \lor s\\)
* Premisa 4: \\(p\\)
* **Conclusión:** \\(s\\)

### Cuadro de Derivación Formal:

| Paso | Expresión Lógica | Justificación / Regla Utilizada |
| :---: | :--- | :--- |
| **(1)** | \\(p \to q\\) | Premisa 1 |
| **(2)** | \\(q \to \neg r\\) | Premisa 2 |
| **(3)** | \\(r \lor s\\) | Premisa 3 |
| **(4)** | \\(p\\) | Premisa 4 |
| **(5)** | \\(q\\) | Modus Ponens (m.p.p.) entre (1) y (4) |
| **(6)** | \\(\neg r\\) | Modus Ponens (m.p.p.) entre (2) y (5) |
| **(7)** | \\(s\\) | Silogismo Disyuntivo (m.t.p.) entre (3) y (6) |

**Conclusión:** La derivación ha culminado formalmente en el paso (7) deduciendo \\(s\\). El argumento es estrictamente **VÁLIDO**. \\(\blacksquare\\)