import numpy
import csv
import random

# x = "yangini1.csv";
q = []
with open('DATASET4.csv', 'r') as f:
	for line in f:
		q.append(line)

q = random.sample(q, len(q))

train_data = q[:int((len(q))*.80)] #Remaining 80% to training set
test_data = q[int(len(q)*.80):] #Splits 20% data to test set

print len(train_data)
print train_data
print ""
with open('train4.csv', 'a') as f:
	f.write("".join(train_data))
    # f.write(str(train_data)+'/t')
    # f.close()
print len(test_data)
print test_data
with open('test4.csv', 'a') as f:
	f.write("".join(test_data))
    # f.write(str(test_data)+'/t')
    # f.close()


