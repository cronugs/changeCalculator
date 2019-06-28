def test_are_equal(actual, expected):
    assert expected == actual, 'Expected %s, got %s'%(expected, actual)

def test_not_equal(a, b):
    assert a != b, 'Did not expect %s, but got %s'%(a, b)

def test_is_in(collection, item):
    assert item in collection, '%s does not contain %s'%(collection, item)

def test_not_in(collection, item):
    assert item not in collection, '%s is in %s'%(item, collection)

def test_between(upper_limit, lower_limit, actual):
    assert lower_limit <= actual <= upper_limit, '%s is not between %s and %s'%(actual, lower_limit, upper_limit)

#test_is_in([1,2], 2)
#test_not_in([1], 2)
#test_between(15, 1, 20)
