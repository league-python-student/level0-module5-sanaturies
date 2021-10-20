"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    def prime(num):
        num=num**0.5
        num//=1
        num=str(num)
        num=num[0:-2]
        num=int(num)
        print(num)
        for i in range(2,num-1):
            if num%i==0:
                return True
        return False
    print(prime(8))


