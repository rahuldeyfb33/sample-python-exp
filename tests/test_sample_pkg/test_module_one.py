from sample_pkg.module_one import greet

def test_greet():
    assert greet("World") == "Hello, World!"