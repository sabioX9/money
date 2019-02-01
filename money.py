#its a random program :)


'''
import random
s = []
for x in range(7):
	s.append(random.randint(1,1001))

avg = sum(s) / len(s)
print(s)
print(sum(s))
print(avg)'''

import random

li = [random.randint(1,1001) for x in range(7)]
print('Here is a list of random numbers between 1 and 1000:', li)
print('Let\'s print a sum of all numbers: {} and average of all numbers: {}'.format(sum(li), round(sum(li)/len(li),2)))