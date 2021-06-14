from abc import ABC, abstractmethod

class NetworkInterface(ABC):

    @abstractmethod
    def connect(self):
        print("connected : NetworkInterface")
        pass

    @abstractmethod
    def transfer(self):
        print("transferred : NetworkInterface")
        pass

class RealNetwork(NetworkInterface):

    def connect(self):
        # connect to something for real
        print("connected : RealNetwork")
        return

    def transfer(self):
        # transfer a bunch of data
        print("transferred : RealNetwork")
        return

class FakeNetwork(NetworkInterface):

    def connect(self):
        # don't actually connect to anything!
        print("connected : FakeNetwork")
        return

    def transfer(self):
        # don't transfer anything!
        print("transferred : FakeNetwork")
        return


#tmp1 = NetworkInterface()
#tmp1.connect()
#tmp1.transfer()

tmp1: NetworkInterface
tmp1 = RealNetwork()

tmp2 = RealNetwork()
tmp2.connect()
tmp2.transfer()

tmp3 = FakeNetwork()
tmp3.connect()
tmp3.transfer()
