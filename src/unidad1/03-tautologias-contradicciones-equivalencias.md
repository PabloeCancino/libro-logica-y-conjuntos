# 1.3 Tautologías, Contradicciones, Equivalencias y Leyes de De Morgan

El análisis de las tablas de verdad permite clasificar semánticamente a las fórmulas proposicionales y establecer las leyes algebraicas fundamentales que rigen el cálculo proposicional.

---

## 1. Clasificación Semántica de las Fórmulas Proposicionales

Dada una fórmula proposicional \\(A\\):

1. **Tautología (o Ley Lógica, \\(\top\\)):**  
   Es una fórmula que resulta **verdadera en todas y cada una de sus interpretaciones posibles** (su columna final en la tabla de verdad contiene únicamente el valor \\(V\\)).  
   *Ejemplo fundamental:* El principio de tercio excluso \\(p \lor \neg p\\).

2. **Contradicción (o Absurdo, \\(\bot\\)):**  
   Es una fórmula que resulta **falsa en todas y cada una de sus interpretaciones posibles** (su columna final contiene únicamente el valor \\(F\\)).  
   *Ejemplo fundamental:* \\(p \land \neg p\\).

3. **Contingencia (o Fórmula Sintética):**  
   Es una fórmula que es verdadera bajo al menos una interpretación y falsa bajo al menos otra (su columna final contiene tanto valores \\(V\\) como \\(F\\)).  
   *Ejemplo:* \\(p \to q\\).

---

## 2. Equivalencia Lógica (≡ o ⇔)

> **Definición 1.2 (Equivalencia Lógica):**  
> Dos fórmulas proposicionales \\(A\\) y \\(B\\) son **lógicamente equivalentes** (denotado \\(A \equiv B\\)) si y sólo si tienen exactamente la misma tabla de verdad bajo cualquier asignación de valores de sus variables atómicas.  
> Equivalentemente, \\(A \equiv B\\) si y sólo si la fórmula bicondicional \\(A \leftrightarrow B\\) es una **tautología**.

---

## 3. Leyes del Álgebra de Proposiciones

Las siguientes equivalencias lógicas constituyen las identidades fundamentales del álgebra booleana sobre el cálculo proposicional:

### A. Leyes de Idempotencia

\\[
p \land p \;\equiv\; p, \qquad p \lor p \;\equiv\; p
\\]

### B. Leyes Conmutativas

\\[
p \land q \;\equiv\; q \land p, \qquad p \lor q \;\equiv\; q \lor p
\\]

### C. Leyes Asociativas

\\[
(p \land q) \land r \;\equiv\; p \land (q \land r), \qquad (p \lor q) \lor r \;\equiv\; p \lor (q \lor r)
\\]

### D. Leyes Distributivas

\\[
p \land (q \lor r) \;\equiv\; (p \land q) \lor (p \land r)
\\]

\\[
p \lor (q \land r) \;\equiv\; (p \lor q) \land (p \lor r)
\\]

### E. Leyes de Identidad y Dominación (con ⊤ y ⊥)

\\[
p \land \top \;\equiv\; p, \qquad p \lor \bot \;\equiv\; p \quad \text{(Identidad)}
\\]

\\[
p \lor \top \;\equiv\; \top, \qquad p \land \bot \;\equiv\; \bot \quad \text{(Dominación)}
\\]

### F. Leyes de Complemento y Doble Negación

\\[
p \lor \neg p \;\equiv\; \top, \qquad p \land \neg p \;\equiv\; \bot
\\]

\\[
\neg(\neg p) \;\equiv\; p \quad \text{(Doble Negación o Involución)}
\\]

### G. Leyes de Absorción

\\[
p \lor (p \land q) \;\equiv\; p, \qquad p \land (p \lor q) \;\equiv\; p
\\]

---

## 4. Las Leyes de De Morgan

Nombradas en honor al lógico británico Augustus De Morgan (1806–1871), establecen la dualidad fundamental entre la conjunción y la disyunción bajo la acción del operador de negación:

> **Teorema 1.1 (Leyes de De Morgan):**  
> Para cualesquiera proposiciones \\(p\\) y \\(q\\):
> 1. **Primera Ley:** La negación de una conjunción es equivalente a la disyunción de las negaciones:
> \\[
> \neg(p \land q) \;\equiv\; \neg p \lor \neg q
> \\]
> 2. **Segunda Ley:** La negación de una disyunción es equivalente a la conjunción de las negaciones:
> \\[
> \neg(p \lor q) \;\equiv\; \neg p \land \neg q
> \\]

### Demostración Formal mediante Tablas de Verdad

Demostremos la Primera Ley \\(\neg(p \land q) \equiv \neg p \lor \neg q\\):

| \\(p\\) | \\(q\\) | \\(p \land q\\) | \\(\neg(p \land q)\\) | \\(\neg p\\) | \\(\neg q\\) | \\(\neg p \lor \neg q\\) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| \\(V\\) | \\(V\\) | \\(V\\) | **\\(F\\)** | \\(F\\) | \\(F\\) | **\\(F\\)** |
| \\(V\\) | \\(F\\) | \\(F\\) | **\\(V\\)** | \\(F\\) | \\(V\\) | **\\(V\\)** |
| \\(F\\) | \\(V\\) | \\(F\\) | **\\(V\\)** | \\(V\\) | \\(F\\) | **\\(V\\)** |
| \\(F\\) | \\(F\\) | \\(F\\) | **\\(V\\)** | \\(V\\) | \\(V\\) | **\\(V\\)** |

Las columnas de \\(\neg(p \land q)\\) y \\(\neg p \lor \neg q\\) son idénticas en todas sus filas. Por lo tanto, \\(\neg(p \land q) \equiv \neg p \lor \neg q\\). \\(\blacksquare\\)

---

## 5. Equivalencias Fundamentales del Condicional

El condicional material \\(p \to q\\) posee diversas equivalencias de enorme trascendencia para las técnicas de demostración matemática:

### A. Expresión Disyuntiva del Condicional

\\[
p \to q \;\equiv\; \neg p \lor q
\\]

*Demostración:* \\(p \to q\\) es falso solo cuando \\(p=V\\) y \\(q=F\\); en ese mismo caso \\(\neg p=F\\) y \\(q=F\\), por lo que \\(\neg p \lor q = F\\). En los demás casos ambos son \\(V\\).

### B. Negación del Condicional
Aplicando De Morgan a la forma disyuntiva:

\\[
\neg(p \to q) \;\equiv\; \neg(\neg p \lor q) \;\equiv\; \neg(\neg p) \land \neg q \;\equiv\; p \land \neg q
\\]

> **Resultado Clave:**  
> Negar una afirmación condicional "Si \\(p\\), entonces \\(q\\)" **NO** produce otro condicional, sino la conjunción: "\\(p\\) ocurre **y al mismo tiempo no ocurre** \\(q\\)".

### C. La Contrapositiva (o Contraposición)

\\[
p \to q \;\equiv\; \neg q \to \neg p
\\]

* Demostración: \\(\neg q \to \neg p \equiv \neg(\neg q) \lor \neg p \equiv q \lor \neg p \equiv \neg p \lor q \equiv p \to q\\).

### D. Variantes del Condicional y Falacias de Equivalencia
Dada la proposición condicional directa \\(p \to q\\):
* **Directa:** \\(p \to q\\)
* **Contrapositiva:** \\(\neg q \to \neg p\\) $\implies$ **Es equivalente a la directa.**
* **Recíproca (o conversa):** \\(q \to p\\) $\implies$ **NO es equivalente a la directa.**
* **Inversa:** \\(\neg p \to \neg q\\) $\implies$ **NO es equivalente a la directa** (pero sí es equivalente a la recíproca).

| \\(p\\) | \\(q\\) | Directa: \\(p \to q\\) | Contrapositiva: \\(\neg q \to \neg p\\) | Recíproca: \\(q \to p\\) | Inversa: \\(\neg p \to \neg q\\) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| \\(V\\) | \\(V\\) | **\\(V\\)** | **\\(V\\)** | \\(V\\) | \\(V\\) |
| \\(V\\) | \\(F\\) | **\\(F\\)** | **\\(F\\)** | \\(V\\) | \\(V\\) |
| \\(F\\) | \\(V\\) | **\\(V\\)** | **\\(V\\)** | \\(F\\) | \\(F\\) |
| \\(F\\) | \\(F\\) | **\\(V\\)** | **\\(V\\)** | \\(V\\) | \\(V\\) |