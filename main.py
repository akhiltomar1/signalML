import random
from statistics import mean


#PILOT TESTING

inputs = []
outputs = []

for i in range(10):
    x = random.random() * 100
    inputs.append(x)
print(inputs)

for i in range(10):
    x = random.random() * 100
    outputs.append(x)
print(outputs)

#y = h*x  + n

h = []
for i in range(10):
    temp = (outputs[i]-(random.random()*100))/inputs[i]
    h.append(temp)
print(h)
h_avg = sum(h)/len(h)
print(h_avg)

#ACTUAL OUTPUTS


Rx = []

for i in range(100):
    x = random.random() * 100
    Rx.append(x)
print(Rx)


#Prediction of Input

Tx = []

for i in range(100):
    x =(Rx[i] - (random.random()*100))/h_avg
    Tx.append(x)
print(Tx)



