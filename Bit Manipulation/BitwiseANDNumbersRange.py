from abc import abstractmethod


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        pass


class Human:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def walk(self):
        pass


class Man(Human):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def walk(self):
        if self.age >= 18:
            print(f'{self.name} est tres rapide pour un age {self.age}')


man = Man('A', 30)

man.walk()




number = 3
number_2 = 2
binary_32_bit = f'{number:032b}'
binary_32_bit_1 = f'{number_2:032b}'
print(f"32-Bit Binary Format (f-string): {binary_32_bit}")
print(f"32-Bit Binary Format (f-string): {binary_32_bit_1}")


