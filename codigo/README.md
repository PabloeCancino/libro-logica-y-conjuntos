# 🛠️ Herramientas de Calidad y Formateo Matemático (mdBook)

Este directorio reúne las herramientas de ingeniería y automatización desarrolladas para garantizar la correcta compilación, compatibilidad con **CommonMark (`pulldown-cmark`)** y renderizado impecable de **KaTeX / MathJax** en el libro digital de **Lógica y Conjuntos (CBIMAT-215)**.

---

## 📋 Catálogo de Herramientas

### 1. `format_math.py` (Formateador e Idempotencia KaTeX)
* **Problema que resuelve:**  
  En CommonMark, si en un párrafo o bloque de texto aparecen dos guiones bajos para subíndices (ej. `x_1` y `x_2`, o `\underbrace{...}_{texto}`), el analizador los interpreta erróneamente como etiquetas HTML de cursiva `<em>...</em>`, destruyendo la sintaxis LaTeX interna.
* **Solución aplicada:**  
  1. Protege y respeta bloques de código (```).
  2. Escapa todos los guiones bajos no escapados dentro de fórmulas en línea (`\\( ... \\)`) convirtiéndolos a `\\_`.
  3. Formatea y aísla los bloques display `\\[ ... \\]`, incluyendo aquellos ubicados dentro de citas o definiciones `> \\[ ... \\]`.
* **Ejecución:**
  ```bash
  python codigo/format_math.py
  ```

---

### 2. `check_delimiters.py` (Auditor de Delimitadores de Escape)
* **Problema que resuelve:**  
  En Markdown, una diagonal invertida simple seguida de paréntesis o corchetes (`\(` o `\[`) es consumida por el analizador como el escape de un símbolo literal, mostrando texto plano roto como `(P(x))` o `[ (\forall x) ... ]`.
* **Solución aplicada:**  
  Escanea carácter por carácter todos los archivos Markdown de `src/` y detecta si existe alguna diagonal simple que no esté duplicada (`\\(` o `\\[`).
* **Ejecución:**
  ```bash
  python codigo/check_delimiters.py
  ```

---

### 3. `clean_thick_spaces.py` (Sanitizador de Espacios Manuales LaTeX `\;`)
* **Problema que resuelve:**  
  El uso de la macro manual de espacio grueso `\;` (`\thickspace`) dentro de ecuaciones LaTeX provocaba que, si se desescapaba la diagonal, aparecieran puntos y coma literales en el texto (ej. `∅;⊆;A;⊆;U`).
* **Solución aplicada:**  
  Elimina de forma universal las macros redundantes `\;` y normaliza el espaciado. Los operadores de relación binaria (`=`, `\subseteq`, `\equiv`, `\iff`, `\implies`) ya cuentan con espaciado óptico automático (`\thickmuskip`) en KaTeX/MathJax.
* **Ejecución:**
  ```bash
  python codigo/clean_thick_spaces.py
  ```

---

### 4. `run_all_math_linters.py` (Script Maestro de Calidad)
* **Propósito:**  
  Ejecuta secuencialmente la limpieza de espacios (`clean_thick_spaces.py`), el formateo con idempotencia (`format_math.py`) y la auditoría final (`check_delimiters.py`), arrojando un reporte consolidado.
* **Ejecución:**
  ```bash
  python codigo/run_all_math_linters.py
  ```

---

## 📌 Guía de Buenas Prácticas para Redacción Matemática en mdBook

1. **Fórmulas en línea:** Utilizar siempre `\\( ... \\)` (dos diagonales en Markdown). Evitar el uso de `$ ... $`.
2. **Fórmulas en bloque:** Utilizar siempre `\\[ ... \\]` aisladas en líneas independientes.
3. **Tablas de Verdad:** Utilizar sintaxis Markdown nativa con celdas centradas (`| :---: |`) en lugar de entornos multilínea `\begin{array}`.
4. **Encabezados Markdown (`#`, `##`, `###`):** Utilizar caracteres Unicode limpios (`¬`, `∧`, `∨`, `→`, `↔`, `⊆`, `∪`, `∩`, `√2`, `ℵ₀`) en lugar de fórmulas LaTeX para asegurar anclas HTML y URLs limpias en la barra lateral (TOC).
