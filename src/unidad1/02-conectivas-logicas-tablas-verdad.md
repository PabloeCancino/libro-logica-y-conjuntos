# 1.2 Conectivas Lógicas y Evaluación de Tablas de Verdad

Las **conectivas lógicas** son operadores formales (funciones de verdad) que toman uno o más valores de verdad del conjunto \\(\mathbb{B} = \{V, F\}\\) y devuelven un único valor de verdad resultante.

---

## 1. Las Cinco Conectivas Lógicas Fundamentales

### A. La Negación (¬ o ~)
Es el único operador **unario**. Invierte el valor de verdad de la proposición sobre la cual opera.

| \\(p\\) | \\(\neg p\\) |
| :---: | :---: |
| \\(V\\) | \\(F\\) |
| \\(F\\) | \\(V\\) |

---

### B. La Conjunción (∧)
Es un operador binario que representa la unión copulativa ("y"). La proposición \\(p \land q\\) es **verdadera únicamente cuando ambas componentes son verdaderas** de manera simultánea; en cualquier otro caso es falsa.

| \\(p\\) | \\(q\\) | \\(p \land q\\) |
| :---: | :---: | :---: |
| \\(V\\) | \\(V\\) | \\(V\\) |
| \\(V\\) | \\(F\\) | \\(F\\) |
| \\(F\\) | \\(V\\) | \\(F\\) |
| \\(F\\) | \\(F\\) | \\(F\\) |

---

### C. La Disyunción Inclusiva (∨)
Representa la unión distributiva ("o"). La proposición \\(p \lor q\\) es **falsa únicamente cuando ambas componentes son falsas**; basta con que una de ellas sea verdadera para que toda la disyunción sea verdadera.

| \\(p\\) | \\(q\\) | \\(p \lor q\\) |
| :---: | :---: | :---: |
| \\(V\\) | \\(V\\) | \\(V\\) |
| \\(V\\) | \\(F\\) | \\(V\\) |
| \\(F\\) | \\(V\\) | \\(V\\) |
| \\(F\\) | \\(F\\) | \\(F\\) |

> **Nota sobre la Disyunción Exclusiva (\\(\oplus\\) o \\(\underline{\lor}\\)):**  
> La disyunción exclusiva \\(p \oplus q\\) es verdadera si y sólo si exactamente una de las componentes es verdadera (pero no ambas). Se define formalmente como \\(p \oplus q \equiv (p \lor q) \land \neg(p \land q)\\).

---

### D. El Condicional Material (→)
El condicional \\(p \to q\\) (leído "Si \\(p\\), entonces \\(q\\)") establece una relación de implicación donde \\(p\\) es el **antecedente** (o hipótesis) y \\(q\\) es el **consecuente** (o conclusión o tesis).

> **Caso Crítico del Condicional:**  
> \\(p \to q\\) es **FALSO en un único escenario**: cuando el antecedente \\(p\\) es VERDADERO y el consecuente \\(q\\) es FALSO (\\(V \to F = F\\)).  
> Cuando el antecedente \\(p\\) es falso, el condicional es **vacuamente verdadero** (\\(F \to V = V\\) y \\(F \to F = V\\)).

| \\(p\\) | \\(q\\) | \\(p \to q\\) |
| :---: | :---: | :---: |
| \\(V\\) | \\(V\\) | \\(V\\) |
| \\(V\\) | \\(F\\) | \\(F\\) |
| \\(F\\) | \\(V\\) | \\(V\\) |
| \\(F\\) | \\(F\\) | \\(V\\) |

---

### E. El Bicondicional (↔)
El bicondicional \\(p \leftrightarrow q\\) (leído "\\(p\\) si y sólo si \\(q\\)") afirma que ambas proposiciones tienen el **mismo valor de verdad**. Es verdadero si ambas son verdaderas o ambas son falsas.

| \\(p\\) | \\(q\\) | \\(p \leftrightarrow q\\) |
| :---: | :---: | :---: |
| \\(V\\) | \\(V\\) | \\(V\\) |
| \\(V\\) | \\(F\\) | \\(F\\) |
| \\(F\\) | \\(V\\) | \\(F\\) |
| \\(F\\) | \\(F\\) | \\(V\\) |

---

## 2. Resumen Semántico: Condiciones Críticas de Falsedad

| Conectiva | Símbolo | Notación | Es FALSA cuando... |
| :--- | :---: | :---: | :--- |
| **Negación** | \\(\neg\\) | \\(\neg p\\) | \\(p\\) es Verdadero |
| **Conjunción** | \\(\land\\) | \\(p \land q\\) | Al menos una componente es Falsa |
| **Disyunción** | \\(\lor\\) | \\(p \lor q\\) | Ambas componentes son Falsas |
| **Condicional** | \\(\to\\) | \\(p \to q\\) | **\\(p = V\\) y \\(q = F\\)** (único caso) |
| **Bicondicional** | \\(\leftrightarrow\\) | \\(p \leftrightarrow q\\) | \\(p\\) y \\(q\\) tienen distinto valor de verdad |
| **Disyunción Exclusiva** | \\(\oplus\\) | \\(p \oplus q\\) | \\(p\\) y \\(q\\) tienen idéntico valor de verdad |

---

## 3. Jerarquía y Precedencia de Operadores

Para evaluar expresiones sin ambigüedad cuando se omiten paréntesis, la lógica matemática adopta la siguiente convención estándar de precedencia (de mayor a menor fuerza vinculante):

1. **Paréntesis:** \\(( \dots )\\) (fuerza vinculante máxima, alteran cualquier orden).
2. **Negación:** \\(\neg\\) (operador unario de mayor prioridad).
3. **Conjunción y Disyunción:** \\(\land\\) y \\(\lor\\) (mismo nivel de precedencia; en caso de duda se exige el uso de paréntesis).
4. **Condicional:** \\(\to\\).
5. **Bicondicional:** \\(\leftrightarrow\\) (menor prioridad).

Por ejemplo:

\\[
\neg p \land q \to r \quad \text{se interpreta estrictamente como} \quad ((\neg p) \land q) \to r
\\]

---

## 4. Construcción Sistemática de Tablas de Verdad

Para evaluar una fórmula molecular con \\(n\\) variables proposicionales atómicas distintas:
1. El número total de combinaciones posibles (filas de la tabla) es **\\(2^n\\)**.
2. Se asignan las columnas base alternando valores: para la primera variable bloques de \\(2^{n-1}\\) valores \\(V\\) y \\(F\\); para la siguiente bloques de \\(2^{n-2}\\), y así sucesivamente hasta alternar \\(V\\) y \\(F\\) de uno en uno.
3. Se añaden columnas intermedias para cada subfórmula, evaluando de adentro hacia afuera según la estructura sintáctica.
4. La columna final representa el valor de verdad global de la fórmula.

### Ejemplo Completo de Evaluación de Tautología

Evaluemos la equivalencia del bicondicional: \\((p \to q) \land (q \to p) \leftrightarrow (p \leftrightarrow q)\\):

| \\(p\\) | \\(q\\) | \\(p \to q\\) | \\(q \to p\\) | \\((p \to q) \land (q \to p)\\) | \\(p \leftrightarrow q\\) | Fórmula Final |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| \\(V\\) | \\(V\\) | \\(V\\) | \\(V\\) | \\(V\\) | \\(V\\) | **\\(V\\)** |
| \\(V\\) | \\(F\\) | \\(F\\) | \\(V\\) | \\(F\\) | \\(F\\) | **\\(V\\)** |
| \\(F\\) | \\(V\\) | \\(V\\) | \\(F\\) | \\(F\\) | \\(F\\) | **\\(V\\)** |
| \\(F\\) | \\(F\\) | \\(V\\) | \\(V\\) | \\(V\\) | \\(V\\) | **\\(V\\)** |

Como la columna final contiene exclusivamente valores **\\(V\\)**, esta fórmula es una **Tautología**, demostrando formalmente que el bicondicional equivale a la conjunción de los dos condicionales recíprocos.