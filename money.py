#its a random program :)

import random
s = []
for x in range(7):
	s.append(random.randint(1,1001))

avg = sum(s) / len(s)
print(s)
print(sum(s))
print(avg)
