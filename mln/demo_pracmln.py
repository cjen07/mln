from pracmln import MLN
from pracmln import Database
from pracmln import MLNQuery

# from docs: http://www.pracmln.org/apidoc.html

def test_mln():
    mln = MLN()
    mln << 'foo(x)' # predicate declaration
    mln << 'bar(y)' # another pred declaration
    mln << 'bar(?x) => bar(?y).' # hard logical constraint
    mln << 'logx(.75)/log(.25) foo(?x)' # weighted formula
    print('mln write:')
    mln.write()
    print('mln predicates:')
    for pred in mln.predicates:
        print(repr(pred))
    print('mln formulas:')
    for f in mln.formulas:
        print(f)
        f.print_structure()  
    return mln 

def test_db():
    mln = test_mln()
    db = Database(mln)
    db << 'foo(X)'
    db['bar(Y)'] = .0
    print('db write:')
    db.write()
    del db['bar(Y)']
    print('db write:')
    db.write()
    return (mln, db)

def test_reasoning():
    mln = MLN.load(files='./mln/alarm.mln')
    db = Database.load(mln, './mln/alarm.db')
    result = MLNQuery(mln=mln, db=db).run()
    result.write()

if __name__ == "__main__":
    test_db()
    test_reasoning()