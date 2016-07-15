import unittest


class Test(unittest.TestCase):
    def test_no_name(self):
        self.assertEqual(no_name('abcdef', 'dcbafe'), True)
        self.assertEqual(no_name('abcdef', 'abcedg'), False)
        self.assertEqual(no_name('abcdef', 'decba'), False)
        self.assertEqual(no_name('abcdef', ''), False)
        self.assertEqual(no_name('', ''), True)


def no_name2(a, b):
    if len(a) != len(b):
        return False

    for x, c in enumerate(b):
        if a[0] == c:
            return no_name2(a[1:], b[0:x] + b[x+1:])

    return len(b) == 0


def no_name(a, b):
    if len(a) != len(b):
        return False

    for x in a:
        for i, y in enumerate(b):
            if x == y:
                b = b[:i] + b[i+1:]
                break
        if i == len(b)-1:
            return False

    return True


def main():
    unittest.main()

if __name__ == '__main__':
    main()

