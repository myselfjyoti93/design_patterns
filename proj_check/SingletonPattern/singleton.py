"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""


class Singleton :
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(self):
        self.__call__()


    def __call__(self):
        if self._instance is None:
            self._instance = Singleton.__init__()
        print("__call__ Called")
        return self._instance



class MyClass(Singleton):
    """
    Example class.
    """
    pass


def main():
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2


if __name__ == "__main__":
    main()