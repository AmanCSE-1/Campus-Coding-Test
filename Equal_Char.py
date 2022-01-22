''' You are given a binary string of 1's and 0's. Your task is to find if is it possible to make all the characters of the string equal, using the below given operation :
    You can choose any two equal adjacent characters and toggle its value. This operation can be performed as many times as you want.

    For example if the string is "0110111" , following are some of the valid operations :
    you can toggle the characters at position 5 and 6 , to make "0110001".
    you cannot toggle the characters at position 4 and 5 , because they are unequal.
    
    Note: Toggling means changing 0 to 1 and vice versa. See sample input explanation for more clarity. '''

test_cases = int(input())

for _ in range(test_cases):
    binaryString = input()
    stack = []
    
    for i in binaryString:
        if not stack:
            stack.append(i)
        
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
     
   
    if stack: print("NO")
    else: print("YES")
    
