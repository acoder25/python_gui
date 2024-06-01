import random
import string


val=random.choice([1,2,3])
# it will choose any element from the list and return in val
# random password creator

str1 = string.digits
str2 = string.ascii_letters
str3 = string.punctuation

str4 = str1 + str2 + str3
lst1 = list(str4)

password=""
pass_length=12

for i in range(pass_length):
    x=random.choice(lst1)
    password+=x

print("your random password is:",password)