#!/usr/bin/env python3

def partition_by(fn, it):
    """Divides an iterable (ie. list or string)
       into chunks based on the return value of
       a function (fn here)."""
    prev = None
    acc = []
    for i in it:
        if prev == None:
            prev = fn(i)
            acc += [i]
        else:
            t = fn(i)
            if prev != t:
                prev = t
                yield acc
                acc = []
            acc += [i]
    if len(acc) > 0:
        yield acc

def group(it, ct):
    """Groups the values in an iterable into lists
       of count. group([1, 2, 3, 4], 2) = [[1, 2], [3, 4]]"""
    li = list(it)
    l = len(li)
    return map(lambda x: map(lambda y: y[1], x),
               partition_by(lambda i: int(i[0]/ct),
                            enumerate(li)))

def un_enc(enc):
    """Decompresses a string."""
    if not enc[0].isdigit():
        enc = '1' + enc
    p2s = lambda i: i[1][0] * int(''.join(i[0])) + ''.join(i[1][1:])
    grps = group(partition_by(str.isdigit, enc), 2)
    s = ''.join(p2s(list(i)) for i in grps)
    return s

def un_enc_file(fil):
    """Decompresses a file."""
    with open(fil) as f:
        return un_enc(f.read().strip())

def un_enc_files(*files):
    """Decompresses an abitrary number
       of files. Puts the decompression
       in the order that the files appear."""
    return ''.join(un_enc_file(i) for i in files)

def is_dec(dec, encs):
    """Validates everything. Prints everything out."""
    t = un_enc_files(*encs)
    print("The decompression: "+ t)
    with open(dec) as d:
        t2 = ''.join(filter(str.isalpha, d.read()))
        print("The unencoded file with alphabetics only: " + t2)
        return t2 == t

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Too few arguments!")
        print("USAGE: python[3] test_enc.py [original file] [compressed files in order ...]")
    else:
        print(is_dec(sys.argv[1], sys.argv[2:]))
