from hello3 import hello

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"


def test_default():    
    assert hello() == "hello, world"
