def txt_py(path):
    def convert_line(ln):
        if len(ln.split(' ')) == 2:
            return ln.replace(' ', '=')
        else:
            toks = ln.split(' ')
            vals = map(lambda x: x.split(','), toks[2:])
            return '{0}=list(0 for i in range({1}))\n'.format(toks[0], toks[1]) +\
                '\n'.join('{0}[{1}] = {2}'.format(toks[0], i[0][1:], i[1][:-1]) for i in vals) + '\n'
    
    with open(path) as f:
        return '\n'.join(map(lambda x: convert_line(x.strip()), f))

def eval_1_input(inp):
    exec(inp + "print({})".format(input("Enter your expression > ")))

def main():
    print("This is very bare-bones. Press Control-C to quit.")
    pref = txt_py(input("Enter the path to the input file > "))
    while True:
        eval_1_input(pref)

if __name__ == "__main__":
    main()
