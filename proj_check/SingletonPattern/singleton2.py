class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state

class Singleton(Borg):
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self.__dict__.update(kwargs)

    def __str__(self):
        return str(self.__dict__)

x = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(x)
y = Singleton(SMTP = "Simple Network Management Protocol")
print(y)