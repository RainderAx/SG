import random

a = 4
b = 10

int1 = random.randint(0, a - 1)
int2 = random.randint(a + 3, b - 1)

c = random.choice([int1, int2])

print(c)

c = random.choice([random.randint(0, a - 1), random.randint(a + 3, b - 1)])