''' Mrs. Mary has given homework to her students. Rohan is very busy and does not have time to complete the homework, so he has asked you to help him.
    Mrs. Mary has given some integers a. What the students have to do is check if a has a odd divisor greater than 1.
    
    For example, if a=3, then b=3. if a=4, them no such divisor exists.'''


test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    
    if (n&(n-1))==0:
        print("NO")
    else:
        print("YES")
