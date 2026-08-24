import glob
import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Replace \; with a regular space inside math expressions
    # Note: \; in LaTeX was used as manual thick spacing
    cleaned = re.sub(r'\\;', ' ', content)
    
    # Clean any double spaces created
    cleaned = re.sub(r' {2,}', ' ', cleaned)
    
    if cleaned != content:
        with open(filepath, 'w', encoding='utf-8') as fp:
            fp.write(cleaned)
        return True
    return False

if __name__ == '__main__':
    files = sorted(glob.glob('src/**/*.md', recursive=True) + glob.glob('src/*.md'))
    count = 0
    for f in files:
        if clean_file(f):
            print(f"Cleaned \\; in: {f}")
            count += 1
    print(f"Total files cleaned: {count}")
