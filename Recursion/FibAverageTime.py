"""
Name: ThankGod Ofurum
Function: calculates the average time required to compute
fib values
"""
import time
from RecursiveFib import *
from IterativeFib import *

#Instances
sum1, sum2, sum3, sum4, sum5, sum6 = 0, 0, 0, 0, 0, 0
list1, list2, list3, list4, list5, list6 = [], [], [], [], [], []

#STORE IN LISTS
for i in range(100):
    startTime = time.time()
    rfib(10)
    elaspedTime = time.time() - startTime
    list1.append(elaspedTime)

for j in range(100):
    startTime = time.time()
    rfib(20)
    elaspedTime = time.time() - startTime
    list2.append(elaspedTime)

for k in range(100):
    startTime = time.time()
    rfib(30)
    elaspedTime = time.time() - startTime
    list3.append(elaspedTime)

for l in range(100):
    startTime = time.time()
    fib(10)
    elaspedTime = time.time() - startTime
    list4.append(elaspedTime)

for m in range(100):
    startTime = time.time()
    fib(20)
    elaspedTime = time.time() - startTime
    list5.append(elaspedTime)

for n in range(100):
    startTime = time.time()
    fib(30)
    elaspedTime = time.time() - startTime
    list6.append(elaspedTime)

#FIND AVERAGE TIMES
for o in list1:
    sum1 += o
print(sum1 / len(list1))

for p in list2:
    sum2 += p
print(sum2 / len(list2))

for q in list3:
    sum3 += q
print(sum3 / len(list3))

for r in list4:
    sum4 += r
print(sum4 / len(list4))

for s in list5:
    sum5 += s
print(sum5 / len(list5))

for t in list6:
    sum6 += t
print(sum6 / len(list6))
    
