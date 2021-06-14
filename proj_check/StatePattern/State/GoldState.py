from .IState import IState


class GoldState(IState):

    def get_benefits(self):
        print("--------------------------------------------------------")
        print("Account is in Gold state.Your Benefits are listed below : \n")
        print("15% of on groceries with the use of debit card\n")
        print("20% of on beauty products with the use of debit card\n")
        print("--------------------------------------------------------\n")
