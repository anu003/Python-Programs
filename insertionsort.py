#!/bin/python
def insertionSort(ar):   
    l = len(ar)
    sorted_list = []
    for i in range(1,l):
        temp = ar[i]
        for j in ar[:i][::-1]:
            if j > temp:
                ar.pop(ar.index(temp))
                ar = ar[:ar.index(j)] + [temp] + ar[ar.index(j):]
        sorted_list += ar
    return sorted_list

m = input()
ar = [int(i) for i in raw_input().strip().split()]
sorted_list = insertionSort(ar)
temp_list = []
i = 0
while i < len(sorted_list):
    temp_list.append(sorted_list[i:i+int(m)])
    i += int(m)

for item in temp_list: 
    print " ".join(map(str, item))
