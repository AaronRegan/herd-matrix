import random

start = 2
stop =  3
limit = 32

result = [[random.randint(start, stop) for i in range(limit)] for j in range(limit)]

print(result)

random.shuffle(result)
for sublist in result:
    random.shuffle(sublist)

print(result)
