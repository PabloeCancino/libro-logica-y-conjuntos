import glob

for f in sorted(glob.glob('src/**/*.md', recursive=True) + glob.glob('src/*.md')):
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    bad = []
    i = 0
    while i < len(content):
        if content[i] == '\\':
            # Check if this is part of \\
            if i + 1 < len(content) and content[i+1] == '\\':
                # This is \\, skip both
                i += 2
                continue
            else:
                # Single \
                if i + 1 < len(content) and content[i+1] in '()[]':
                    bad.append((content[i+1], content[max(0, i-15):min(len(content), i+25)]))
                i += 1
        else:
            i += 1
    if bad:
        print(f"=== {f} === (total {len(bad)} issues)")
        for b in bad:
            print("  ", repr(b[1]))
