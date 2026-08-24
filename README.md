# Lógica y Conjuntos — Un curso para la Licenciatura en Matemáticas

[![Deploy mdBook](https://github.com/PabloeCancino/libro-logica-y-conjuntos/actions/workflows/deploy.yml/badge.svg)](https://github.com/PabloeCancino/libro-logica-y-conjuntos/actions/workflows/deploy.yml)
[![Libro Digital](https://img.shields.io/badge/Leer-Libro%20Digital%20Online-blue?style=for-the-badge&logo=gitbook)](https://pabloecancino.github.io/libro-logica-y-conjuntos/)
[![APK Android](https://img.shields.io/badge/Descargar-APK%20Android-green?style=for-the-badge&logo=android)](https://github.com/PabloeCancino/uan-apk-logica-y-conjuntos/releases)
[![Web App Interactiva](https://img.shields.io/badge/Ver-Web%20App%20Interactiva-orange?style=for-the-badge&logo=githubpages)](https://pabloecancino.github.io/uan-apk-logica-y-conjuntos/)
[![Licencia CC BY-NC-ND 4.0](https://img.shields.io/badge/Licencia-CC%20BY--NC--ND%204.0-lightgrey?style=for-the-badge)](LICENSE.md)

**Autores:** Dr. Pablo Eduardo Cancino Marentes & Dr. Sergio Enrique Yarza Acuña  
**Institución:** Universidad Autónoma de Nayarit (UAN), Unidad Académica de Ciencias Básicas e Ingenierías, Programa Académico de Licenciatura en Matemáticas (PALMAT).  

---

## 📖 Acerca de este Libro

Este repositorio contiene el texto completo y riguroso, en formato [mdBook](https://rust-lang.github.io/mdBook/), del curso de **Lógica y Conjuntos** (clave **CBIMAT-215**, Plan de Estudios 2024 / Actualización 2026) de la Licenciatura en Matemáticas de la Universidad Autónoma de Nayarit.

El libro cubre formalmente las cuatro unidades fundamentales del programa curricular oficial:
1. **Lógica Proposicional y Tablas de Verdad:** Proposiciones atómicas y moleculares, conectivas lógicas, jerarquía de operaciones, semántica de verdad, tautologías, contradicciones, álgebra de proposiciones y leyes de De Morgan, validez formal de argumentos y falacias.
2. **Cuantificadores y Reglas de Inferencia:** Funciones proposicionales y predicados, cuantificador universal ($\forall$), cuantificador existencial ($\exists$), existencia y unicidad ($\exists!$), negación de cuantificadores, cálculo de predicados, deducción natural y las 8 reglas fundamentales de inferencia (m.p.p., m.t.t., m.t.p., silogismo hipotético, etc.).
3. **Teoría de Conjuntos y Álgebra Booleana:** Pertenencia ($\in$), notación extensional y comprensional, paradoja de Russell y axiomas ZFC, contención e igualdad extensional, conjunto vacío ($\emptyset$), universal ($\mathcal{U}$) y potencia ($\mathcal{P}(A)$), operaciones booleanas ($\cup, \cap, \setminus, A^c, \Delta$), diagramas de Venn, particiones, principio de inclusión-exclusión (P.I.E.) y producto cartesiano $A \times B$.
4. **Métodos de Demostración, Relaciones, Funciones e Inducción:** Métodos clásicos de demostración (directa, contrapositiva, reducción al absurdo, casos, existencia constructiva/no constructiva), principio de inducción matemática simple y completa/fuerte, relaciones binarias, relaciones de equivalencia y conjuntos cociente ($A/\sim$), relaciones de orden (posets, diagramas de Hasse), funciones (inyectivas, sobreyectivas, biyectivas), composición, funciones inversas y cardinalidad infinita de Georg Cantor ($\aleph_0, \mathfrak{c}$).
5. **Apéndices:** Catálogo formal de las 14 demostraciones matemáticas paso a paso de la UAN, banco de reactivos institucionales resueltos y comentados (PALMAT 2024), y bibliografía anotada.

---

## 🌐 Lectura en Línea

El libro digital interactivo está disponible para lectura libre en:  
👉 **[https://pabloecancino.github.io/libro-logica-y-conjuntos/](https://pabloecancino.github.io/libro-logica-y-conjuntos/)**

---

## 📱 Aplicación Móvil e Interactiva Complementaria

Este libro cuenta con una aplicación móvil complementaria desarrollada bajo la norma técnica **NTE-UAN-APK-001 v1.3** de la UAN:  
* 🚀 **[Web App Interactiva en Vivo](https://pabloecancino.github.io/uan-apk-logica-y-conjuntos/)**
* 📲 **[Descargar APK Android (100% Offline)](https://github.com/PabloeCancino/uan-apk-logica-y-conjuntos/releases)**
* 💻 **[Repositorio del Proyecto Móvil](https://github.com/PabloeCancino/uan-apk-logica-y-conjuntos)**

---

## 🛠️ Compilación Local

Para compilar y visualizar el libro en tu equipo local:

```bash
# 1. Instalar mdBook (requiere Rust/Cargo)
cargo install mdbook

# 2. Clonar el repositorio
git clone https://github.com/PabloeCancino/libro-logica-y-conjuntos.git
cd libro-logica-y-conjuntos

# 3. Servir localmente con recarga en vivo
mdbook serve --open
```

---

## 📄 Licencia y Cita

Publicado bajo la licencia **[Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)](LICENSE.md)**.

**Cómo citar:**
> Cancino Marentes, P. E., & Yarza Acuña, S. E. (2026). *Lógica y Conjuntos: Un curso para la Licenciatura en Matemáticas*. Universidad Autónoma de Nayarit. Publicación abierta en: https://pabloecancino.github.io/libro-logica-y-conjuntos/
