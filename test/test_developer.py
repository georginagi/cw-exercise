from expects import *
from developer import Developer

with description('Sorting'):
    with it('sorts a list in ascending ordered by a given attribute'):
        test_list = devs = [
            Developer("John", 29, 3),
            Developer("Linda", 29, 5),
            Developer("Robert", 24, 1)
        ]

        expect(parent_category.contains(child_category)).to(be_true)

    with it('does not contain another category if the path is not contained'):
        parent_category = Category(id=1, path=['Moda'])
        child_category = Category(id=2, path=['Deportes', 'Fitness'], parent_id=1)

        expect(parent_category.contains(child_category)).to(be_false) 