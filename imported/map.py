__author__ = 'william'

txt = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr '\
      'ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'


def map(txt):
    a = ord('a')
    z = ord('z')
    r = ''

    for c in txt:
        i = ord(c)
        r += c if not (i in range(a, z+1)) else (chr(i+2) if (i + 2) <= z else chr(((i + 2) % z) + a - 1))

    print(r)

txt = 'map'

map(txt)