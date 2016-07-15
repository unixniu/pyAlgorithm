import string

m = {}

with open('ocr_src.txt') as f:
    for l in f:
        for c in l:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1

with open('result', 'w') as f:
    for c, n in m.items():
        f.write('{}: {}\n'.format(c, n))
    f.write('\n')

res = ''
with open('ocr_src.txt') as f:
    txt = f.read()
    for c in txt:
        if c in string.ascii_letters:
            res += c
    print(res)
