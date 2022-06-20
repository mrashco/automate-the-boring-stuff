from commacode import makestring

def test_basic():
    assert makestring(['apples', 'bananas', 'tofu', 'cats']) == 'apples, bananas, tofu, and cats'
    assert makestring(['hello', 'there', 'again', 'world']) == 'hello, there, again, and world'
    assert makestring(['Python', 'C++', 'JavaScript']) == 'Python, C++, and JavaScript'