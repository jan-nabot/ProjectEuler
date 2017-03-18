'''Collatz sequence starts with arbitrary value n, finish with 1 (unproven).
n > n/2 (n is even)                 n -> 3n + 1 (n is odd)
ie. 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1                 
Once chain starts terms are allowed to go above one million. 
Which number under one million produces longest chain. 
'''


biggest = 0
iter = 0
for it0 in range(1, 1000000):
        curnum = it0
        count = 2
        while curnum != 1:
            if curnum % 2 == 0:
                curnum = curnum // 2 
                count += 1
            else:
                curnum = 3 * curnum + 1
                count += 1
        if count > biggest:
            biggest = count
            iter = it0
            
print(iter, ':', biggest)
