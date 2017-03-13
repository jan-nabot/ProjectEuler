from longnumbers import *

llen = len(number2) # how many numbers are there
ilen = len(number2[0]) # how long numbers are

colsum = [0] * ilen # creates list with 50 zeroes
for iT0 in range(0, llen):
    for iT1 in range(0, ilen):
        colsum[iT1] += int(number2[iT0][iT1]) 

multiplier = 1
colmul = [0] * ilen
for iT2 in range(ilen-1, -1, -1):
    colmul[iT2] = colsum[iT2] * multiplier
    multiplier *= 10

grandsum = 0
for iT3 in colmul:
    grandsum += iT3

print(grandsum)
print(str(grandsum)[:10])

# Now that went surprisingly smooth and well, contrary to previous problem    
 

