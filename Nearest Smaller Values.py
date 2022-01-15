'''Have a function NearestSmallerValues(arr) take the array of integers stored in arr, and for each element in the list, 
  search all the previous values for the nearest element that is smaller than (or equal to) the current element and create a new list of this numbers.
  If there is no element before a certain position that is samller, input a -1.'''

'''For example, arr is [5, 2, 8, 3, 9, 12],
  Than nearest samller values list is [-1, -1, 2, 2, 3, 9]
'''


def NearestSmallerValues(arr):
    result, stack = [], []

    for i in arr:
        while stack and stack[-1]>i:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        stack.append(i)
       
    return result
 
print(NearestSmallerValues(list(map(int, input().split()))))
