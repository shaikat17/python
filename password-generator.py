import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}()#_-*;."

all = lower + upper + number + symbol

password = "".join(random.sample(all,9))

print("Your Password is: ", password)
