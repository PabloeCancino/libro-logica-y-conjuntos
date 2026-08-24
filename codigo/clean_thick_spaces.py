import os
import glob
import re

def clean_file(filepath):
    """
    Elimina las macros manuales de espacio grueso en LaTeX (\\;) que generan
    artefactos de punto y coma literales (ej. '∅;⊆;A;⊆;U') cuando se desescapan
    en el analizador Markdown.
    
    En TeX/KaTeX/MathJax, los operadores de relación binaria (=, \\subseteq, \\equiv,
    \\iff, \\implies) ya incluyen espaciado óptico automático (\\thickmuskip).
    """
    with open(filepath, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Reemplazar \; por un espacio simple estándar
    cleaned = re.sub(r'\\;', ' ', content)
    
    # Colapsar espacios múltiples generados
    cleaned = re.sub(r' {2,}', ' ', cleaned)
    
    if cleaned != content:
        with open(filepath, 'w', encoding='utf-8') as fp:
            fp.write(cleaned)
        return True
    return False

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_dir = os.path.join(base_dir, 'src')
    files = sorted(glob.glob(os.path.join(src_dir, '**', '*.md'), recursive=True) + glob.glob(os.path.join(src_dir, '*.md')))
    count = 0
    for f in files:
        if clean_file(f):
            rel = os.path.relpath(f, base_dir)
            print(f"Limpieza de \\; en: {rel}")
            count += 1
    print(f"Total de archivos procesados: {count}")
