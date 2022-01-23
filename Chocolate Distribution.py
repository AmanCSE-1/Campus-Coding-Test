''' Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates.
    There are m students, the task is to distribute chocolate packets such that: 
    1. Each student gets one packet.
    2. The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.
'''

## Public Test Case: Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
#                    Output: Minimum Difference is 2 
#                    Explanation: We have seven packets of chocolates and we need to pick three packets for 3 students.
#                                 If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.

# Public Test Case:- Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
#                    Output: Minimum Difference is 6 
#                    Explanation: The set goes like 3,4,7,9,9 and the output is 9-3 = 6.



def chocolateDistribution(array, k, n):
    array.sort()
    
    result = array[-1] - array[0]
    for i in range(0, n-k+1, 1):
        result = min(result, array[i+k-1]-array[i])
    return result

if __name__ == "__main__":
    nk = list(map(int, input().split())))
    
    k, n = nk[0], nk[1]
    array = list(map(int, input().split())))
    print(chocolateDistribution(array, k, n))
