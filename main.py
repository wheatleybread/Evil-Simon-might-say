import random
from time import sleep


y = 3


list = []


for x in range(y):
    list.append(random.randint(1,4))
    sleep(0.5)

print(list)
print(list[0])