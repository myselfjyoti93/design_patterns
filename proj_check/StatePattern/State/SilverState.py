from .IState import IState


class SilverState(IState):

    def get_benefits(self):
        print("--------------------------------------------------------")
        print("Account is in Silver state.Your Benefits are listed below : \n")
        print("10% of on groceries with the use of debit card\n")
        print("15% of on beauty products with the use of debit card\n")
        print("--------------------------------------------------------\n")
