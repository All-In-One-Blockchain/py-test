from hello.hello import say_hello


def test_say_hello_default():
    """Test say_hello with default parameter"""
    assert say_hello() == "Hello, World!"


def test_say_hello_with_name():
    """Test say_hello with a specific name"""
    assert say_hello("Devin") == "Hello, Devin!"


def test_say_hello_with_empty_string():
    """Test say_hello with empty string"""
    assert say_hello("") == "Hello, !"
