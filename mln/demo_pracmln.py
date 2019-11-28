from pracmln import MLN

# from docs: http://www.pracmln.org/apidoc.html

def test_mln():
    mln = MLN()
    mln << 'foo(x)' # predicate declaration
    mln << 'bar(y)' # another pred declaration
    mln << 'bar(?x) => bar(?y).' # hard logical constraint
    mln << 'logx(.75)/log(.25) foo(?x)' # weighted formula
    print('mln write')
    mln.write()
    print('mln predicates:')
    for pred in mln.predicates:
        print(repr(pred))
    print('mln formulas:')
    for f in mln.formulas:
        print(f)
        f.print_structure()   

def test_db():
    pass

if __name__ == "__main__":
    test_mln()