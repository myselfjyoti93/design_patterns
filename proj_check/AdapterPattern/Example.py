class ClassA:

    def __init__(self, obj1):
        self.obj1 = obj1

    def A1(self):
        print("In class A")
        self.obj1.print_obj1()

class ClassB:

    def __init__(self, data_taken: list[int]):
        self.data = data_taken

    def print_x(self):
        print("x")

    def print_obj1(self):
        print("This is class B")
        print(self.data)

class ClassC:

    def __init__(self, data_taken):
        self.list_obj = list(data_taken)

    def print_obj1(self):
        print("This is class B")
        print(self.list_obj)

list_val = [1,2,3]
b_obj = ClassB(list_val)

a_obj = ClassA(b_obj)
a_obj.A1()

tuple_val = (1, 2, 3)

adapter_obj = ClassC(tuple_val)

a_adap_obj = ClassA(adapter_obj)
a_adap_obj.A1()