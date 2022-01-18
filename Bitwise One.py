''' Have a function BitwiseOne(strArr) take the array of strings stored in strArr, which will only contain two strings of equal length that represent binary numbers,
    and return a final binary string that performed bitwise OR operation on both the strings.
    
    A Bitwise OR operation places a 0 in new string where there are zeros in both the binary strings. otherwise it places 1 in that spot.'''
    
''' For example :- strArr is ["1001", "0100"] then your program should return the string "1101"'''

## Public Test Case -> Input : ["100", "000"]
#                      Output : 100

def BitwiseOne(strArr):
      result = ""

      for i in range(len(strArr[0])):
          if strArr[0][i]=='0' and strArr[1][i]=='0':
              result += '0'
          else:
              result += '1'

      return result
