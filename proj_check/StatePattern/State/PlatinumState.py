from .IState import IState


class PlatinumState(IState):

    def get_benefits(self):
        print("--------------------------------------------------------")
        print("Account is in Platinum state.Your Benefits are listed below :\n")
        print("20% of on groceries with the use of debit card\n")
        print("25% of on beauty products with the use of debit card\n")
        print("--------------------------------------------------------\n")
