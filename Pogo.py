'''Once a upon a time in mumbai, there were two friends name Rahul and Rohan they both were very smart in coding. 
   They usually comes with a optimise solution of every problem they solve. 
   As Claimed by Rahul and Rohan of mumbai, a number is called perfect if it is of the form (3040*(10^k)) for integer K ≥0.
   Some of the good numbers are: 3040,304000,30400000.
   
   
   POGO gives you a number N and askes you whether, the given number can be represented as a sum of perfect numbers.
   Your task is to calculate or compute the minimum number of perfect-numbers required for that.'''


test_cases = int(input())

for i in range(test_cases):
    n = int(input())
    
    if n%3040:
        print(-1)
        continue
    
    quotient = n/3040
    count = 0
    
    while quotient!=0:
        count += quotient%10
        quotient = quotient/10
    
    print(count)
        
