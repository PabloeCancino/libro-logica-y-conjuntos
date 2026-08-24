# 3.3 Operaciones Conjuntistas, Álgebra Booleana y Diagramas de Venn

A partir de conjuntos dados dentro de un universo \\(\mathcal{U}\\) se pueden definir nuevas colecciones mediante las **operaciones fundamentales del álgebra de conjuntos**.

---

## 1. Definición Formal de las Cinco Operaciones Fundamentales

Sean \\(A, B \subseteq \mathcal{U}\\):

### A. Unión (A ∪ B)
Reúne todos los elementos que pertenecen a \\(A\\), a \\(B\\) o a ambos:

\\[
A \cup B \;=\; \{x \in \mathcal{U} \mid x \in A \lor x \in B\}
\\]

### B. Intersección (A ∩ B)
Reúne los elementos comunes que pertenecen simultáneamente a \\(A\\) y a \\(B\\):

\\[
A \cap B \;=\; \{x \in \mathcal{U} \mid x \in A \land x \in B\}
\\]

> **Definición (Conjuntos Disjuntos):**  
> Dos conjuntos \\(A\\) y \\(B\\) son **disjuntos** (o ajenos) si no comparten ningún elemento:
> \\[
> A \cap B \;=\; \emptyset
> \\]

### C. Diferencia Relativa (A ∖ B o A - B)
Reúne los elementos de \\(A\\) que **no** pertenecen a \\(B\\):

\\[
A \setminus B \;=\; \{x \in \mathcal{U} \mid x \in A \land x \notin B\}
\\]

### D. Complemento Absoluto (Aᶜ o A')
Reúne todos los elementos del universo \\(\mathcal{U}\\) que no pertenecen a \\(A\\):

\\[
A^c \;=\; \mathcal{U} \setminus A \;=\; \{x \in \mathcal{U} \mid x \notin A\}
\\]

*Propiedad inmediata:* \\(A \setminus B = A \cap B^c\\).

### E. Diferencia Simétrica (A △ B)
Reúne los elementos que pertenecen a \\(A\\) o a \\(B\\), pero **no a ambos** simultáneamente:

\\[
A \Delta B \;=\; (A \setminus B) \cup (B \setminus A) \;=\; (A \cup B) \setminus (A \cap B)
\\]

---

## 2. Diagramas de Venn

Los **diagramas de Venn**, ideados por John Venn en 1880, representan las relaciones lógicas y conjuntistas en el plano:
* Un rectángulo exterior representa el conjunto universal \\(\mathcal{U}\\).
* Círculos o elipses en su interior representan conjuntos individuales.
* El sombreado de regiones denota el resultado específico de una operación.

### Representación de las Operaciones en 2 Conjuntos:```
    ┌─────────────────────────── U ───────────────────────────┐
    │                                                         │
    │         ╭─────────────╮     ╭─────────────╮             │
    │        /               \   /               \            │
    │       /     A \ B       \ /      B \ A      \           │
    │      │                   X                   │          │
    │      │        A         / \        B         │          │
    │       \                /   \                /           │
    │        \              / A∩B \              /            │
    │         ╰─────────────╯     ╰─────────────╯             │
    │                                                         │
    │                  Región Exterior: (A ∪ B)ᶜ              │
    └─────────────────────────────────────────────────────────┘
```

* **Unión \\(A \cup B\\):** Se sombrean las tres regiones interiores: \\(A \setminus B\\), \\(A \cap B\\) y \\(B \setminus A\\).
* **Intersección \\(A \cap B\\):** Se sombrea únicamente la lente central común.
* **Diferencia \\(A \setminus B\\):** Se sombrea la medialuna izquierda de \\(A\\).
* **Diferencia Simétrica \\(A \Delta B\\):** Se sombrean las dos medialunas externas, dejando el centro en blanco.
* **Complemento \\(A^c\\):** Se sombrea todo el rectángulo exterior salvo el círculo \\(A\\).

---

## 3. Leyes del Álgebra de Conjuntos (Estructura Booleana)

Para cualesquiera conjuntos \\(A, B, C \subseteq \mathcal{U}\\), se verifican las siguientes identidades:

### A. Leyes de Idempotencia

\\[
A \cup A = A, \qquad A \cap A = A
\\]

### B. Leyes Conmutativas

\\[
A \cup B = B \cup A, \qquad A \cap B = B \cap A
\\]

### C. Leyes Asociativas

\\[
(A \cup B) \cup C = A \cup (B \cup C), \qquad (A \cap B) \cap C = A \cap (B \cap C)
\\]

### D. Leyes Distributivas

\\[
A \cap (B \cup C) = (A \cap B) \cup (A \cap C)
\\]

\\[
A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
\\]

### E. Leyes de Identidad y Dominación

\\[
A \cup \emptyset = A, \qquad A \cap \mathcal{U} = A \quad \text{(Identidad)}
\\]

\\[
A \cup \mathcal{U} = \mathcal{U}, \qquad A \cap \emptyset = \emptyset \quad \text{(Dominación)}
\\]

### F. Leyes de Complementación e Involución

\\[
A \cup A^c = \mathcal{U}, \qquad A \cap A^c = \emptyset
\\]

\\[
(A^c)^c = A, \qquad \emptyset^c = \mathcal{U}, \qquad \mathcal{U}^c = \emptyset
\\]

### G. Leyes de De Morgan para Conjuntos

\\[
(A \cup B)^c \;=\; A^c \cap B^c
\\]

\\[
(A \cap B)^c \;=\; A^c \cup B^c
\\]

---

## 4. Demostración Formal de la 1ª Ley de De Morgan Conjuntista

> **Teorema 3.2:**  
> \\((A \cup B)^c = A^c \cap B^c\\).

*Demostración por doble contención:*

1. **Parte 1: Probar que \\((A \cup B)^c \subseteq A^c \cap B^c\\):**  
   Sea \\(x \in (A \cup B)^c\\).  
   Por definición de complemento, \\(x \notin (A \cup B)\\).  
   Esto significa que \\(\neg(x \in A \lor x \in B)\\).  
   Por la 1ª Ley de De Morgan lógica, \\(\neg(x \in A) \land \neg(x \in B)\\), lo que equivale a \\(x \notin A \land x \notin B\\).  
   Por definición de complemento, \\(x \in A^c \land x \in B^c\\).  
   Por definición de intersección, \\(x \in A^c \cap B^c\\).  
   Por lo tanto, \\((A \cup B)^c \subseteq A^c \cap B^c\\).

2. **Parte 2: Probar que \\(A^c \cap B^c \subseteq (A \cup B)^c\\):**  
   Sea \\(x \in A^c \cap B^c\\).  
   Entonces \\(x \in A^c \land x \in B^c\\), lo que significa que \\(x \notin A \land x \notin B\\).  
   Equivalentemente, \\(\neg(x \in A) \land \neg(x \in B)\\).  
   Por la equivalencia lógica de De Morgan, \\(\neg(x \in A \lor x \in B)\\).  
   Esto significa que \\(x \notin (A \cup B)\\), y en consecuencia \\(x \in (A \cup B)^c\\).  
   Por lo tanto, \\(A^c \cap B^c \subseteq (A \cup B)^c\\).

**Conclusión:** Al haberse verificado ambas contenciones, se concluye formalmente que \\((A \cup B)^c = A^c \cap B^c\\). \\(\blacksquare\\)