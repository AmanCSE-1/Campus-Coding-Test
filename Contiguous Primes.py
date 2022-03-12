''' Given an array of n integers, for each index i, find the maximum length of the prime segment, the elements of index i is part of.

    A prime segment of an array A is an subarray of A which has all the elements as prime.
    For example, if array=[1, 2, 3, 5, 7, 1, 11, 12], then two prime segments are :
                 [2, 3, 5, 7]
                 [11]
    
    Input : n : number of elements in array
            array : n integers'''


# Public Test Cases : Input :- n = 5
#                              array = [1 2 3 4 5]
#                     Output :- 0 2 2 0 1

#---------------------#

# Pre-computing prime numbers
limit = 10**5
primes = [True]*(limit+1)

p = 2
while p <= limit**.5:
  if primes[p]:
    for i in range(p+p, limit+1, p):
      primes[i] = False
  p += 1

primes[0] = primes[1] = False


# Taking user-input :
n = int(input())
array = list(map(int, input().split()))

length = 0
result = []

for i in array:
    if primes[i]:
        length += 1
    else:
        result.extend([length]*length)
        result.append(0)
        length = 0

if length!=0:
    result.extend([length]*length)

print(*result, sep=' ')
