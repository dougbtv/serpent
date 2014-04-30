#!/usr/bin/python
import sys
from serpent import compiler
t = open('tests.txt').readlines()
i = 0
while 1:
    o = []
    while i < len(t) and (not len(t[i]) or t[i][0] != '='):
        o.append(t[i])
        i += 1
    i += 1
    print '================='
    text = '\n'.join(o).replace('\n\n','\n')
    print text
    ast = compiler.parse(text)
    print "AST:",ast
    print ""
    aevm = compiler.compile_to_assembly(text)
    print "AEVM:",' '.join([str(x) for x in aevm])
    print ""
    code = compiler.compile(text)
    # print "!trace compiled here ----------------------------- \n", code
    print "Output:",code.encode('hex'),"\n\n"
    # print compiler.deserialize("600a60005460146020546020536000530160405460286040530b0d630000002a59600a604053026060546032608054");
    sys.exit(0)
    if i >= len(t):
        break

