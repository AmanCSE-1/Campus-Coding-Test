''' Have a function ArrayAddition1(arr) take the array of numbers stored in arr and return the string True if any combination of numbers in the array 
    (excluding the largest number) can be added up to the equal the largest number in the array, otherwise return False.'''

''' For example, if arr contains [4, 6, 23, 10, 1, 3], output should be True  because 4 + 6 + 10 + 3 = 23.'''
''' Constraints : The array will not be empty, wil not contain all the same numbers, and may contain negative numbers'''


## Public Test Case -> Input : [5, 7, 16, 1, 2]
#                      Output : False

## Public Test Case -> Input : [3, 5, -1, 8, 12]
#                      Output : True


def ArrayAdditionI(arr): 
    arr.sort()
    
    memory = dict()
    
    def checkAddition(num, total):
        if num == 0:
            return False
        if num == 1:
            return arr[0] == total
          
        if (num, total) in memory.keys():
            return memory[(num, total)]
          
        else:
            result = checkAddition(num - 1, total) or checkAddition(num - 1, total - arr[num-1])
            memory[(num, total)] = result
            return result
    return checkAddition(len(arr) - 1, arr[-1])
