from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balance) or account2 > len(self.balance):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.withdraw(account1, money)
        self.deposit(account2, money)
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


# Your Bank object will be instantiated and called as such:
balance = [[[10,100,20,50,30]],[3,10],[5,1,20],[5,20],[3,4,15],[10,50]]
obj = Bank(balance)
obj.withdraw(3, 10)
obj.transfer(5,1,20)
obj.deposit(5,20)
obj.transfer(3,4,15)
obj.withdraw(10, 50)

print(f"balance: {obj.balance}")
