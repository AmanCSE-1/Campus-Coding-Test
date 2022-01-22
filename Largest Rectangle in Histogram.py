''' Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
    return the area of the largest rectangle in the histogram. '''

## Public Test Case : Input: heights = [2,1,5,6,2,3]
#                     Output: 10

## Public Test Case : Input: heights = [2,4]
#                     Output: 4

def largestRectangleArea(heights):
    
    
if __name__ == "__main__":
    test_cases = int(input())
    
    for _ in range(test_cases):
        heights = list(map(int, input().split()))
        print(largestRectangleArea(heights))

  

