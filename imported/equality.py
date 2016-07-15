import re
with open('equality.txt') as f:
    txt = f.read()
    pattern = '[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
    all = re.findall(pattern, txt)
    print(''.join(all))