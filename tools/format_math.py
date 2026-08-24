import os
import glob
import re

def escape_math_underscores(math_str):
    # Replaces unescaped _ with \_ inside math expressions
    return re.sub(r'(?<!\\)_', r'\\_', math_str)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Split into markdown vs code blocks so we never touch code blocks
    code_block_pattern = re.compile(r'(```.*?```)', re.DOTALL)
    parts = code_block_pattern.split(content)

    for idx in range(len(parts)):
        # If it's a code block, skip
        if parts[idx].startswith('```'):
            continue

        text = parts[idx]
        trailing_newline = '\n' if text.endswith('\n') else ''

        # Step 2: Escape unescaped underscores inside inline math: \\( ... \\)
        def fix_inline(m):
            math_content = m.group(1)
            fixed = escape_math_underscores(math_content)
            return r'\\(' + fixed + r'\\)'

        text = re.sub(r'\\\\\((.*?)\\\\\)', fix_inline, text, flags=re.DOTALL)

        # Step 3: Ensure all display math blocks \\[ ... \\] (including inside blockquotes >) have escaped underscores
        lines = text.splitlines()
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]

            # Case A: Entire display math on single line: \\[ ... \\] or > \\[ ... \\]
            single_match = re.match(r'^(\s*(?:>\s*)?)\\+(\[)(.+?)\\+(\])\s*$', line)
            if single_match:
                prefix = single_match.group(1)
                math_body = single_match.group(3).strip()
                math_body = escape_math_underscores(math_body)

                new_lines.append(f'{prefix}\\\\[')
                new_lines.append(f'{prefix}{math_body}')
                new_lines.append(f'{prefix}\\\\]')
                i += 1
                continue

            # Case B: Opening of multiline display math: \\[ or > \\[
            open_match = re.match(r'^(\s*(?:>\s*)?)\\+(\[)\s*$', line)
            if open_match:
                prefix = open_match.group(1)
                new_lines.append(f'{prefix}\\\\[')
                i += 1
                while i < len(lines):
                    cur_line = lines[i]
                    close_match = re.match(r'^(\s*(?:>\s*)?)\\+(\])\s*$', cur_line)
                    if close_match:
                        new_lines.append(f'{prefix}\\\\]')
                        i += 1
                        break
                    else:
                        escaped_line = escape_math_underscores(cur_line)
                        new_lines.append(escaped_line)
                        i += 1
                continue

            new_lines.append(line)
            i += 1

        parts[idx] = '\n'.join(new_lines) + trailing_newline

    result = ''.join(parts)
    # Fix excess consecutive blank lines or quote lines
    result = re.sub(r'(\n\s*>\s*){2,}\n', '\n>\n', result)
    result = re.sub(r'\n{3,}', '\n\n', result)

    if result != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        return True
    return False

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_dir = os.path.join(base_dir, 'src')
    files = sorted(glob.glob(os.path.join(src_dir, '**', '*.md'), recursive=True) + glob.glob(os.path.join(src_dir, '*.md')))
    modified = 0
    for f in files:
        if process_file(f):
            print(f'Modificado: {os.path.relpath(f, base_dir)}')
            modified += 1
    print(f'Total de archivos formateados: {modified}')
