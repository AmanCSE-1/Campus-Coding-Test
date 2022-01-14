''' Have a function SymmetricTree(strArr) take the array of strings stored in strArr, which will represent a binary tree, 
    and determine if the tree is symmetric (a mirror image of itself). '''
''' The array will be implemented as similar to a binary heap, except tree may not be complete and NULL nodes on any level mat be represented as #.'''


'''Example :- strArr is ["1", "2", "2", "3", "#", "#", "3"], then tree looks like
                                      1
                                    /   \
                                   2     2
                                  / \   / \
                                 3   # #   3
            For the above example, your program should return True.
'''

## Public Test Cases : Input : ["4", "3", "4"]
                     # Output : False
 

def SymmetricTree(strArr):

  # code goes here
  i, factor = 1, 1
  
  while i<len(strArr):
    factor*=2
    
    start, mid, end = i, i+ factor//2, i+factor
    left = strArr[start:mid]
    right = strArr[mid:end]
    
    if left!=right[::-1]:
      return False
    
    i=end
	# end of while loop
    
   return True
  
# keep this function call here
print(SymmetricTree(input())
      
