'''Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks,
  and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. 
  If so, then your program should return the string true, otherwise it should return the string false. 
  If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.'''

'''For example: If str is "arrb6???4xxbl5???eee5" then your program should return true 
  because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.'''


def QuestionsMarks(strParam):
  	# code goes here
	a, flag, count = None, False, 0

		for i in strParam:
			if i.isdigit():
				if a is None:
					a = int(i)
				else:
					if a+int(i)==10:
						if count==3:
							flag = True
						else:
							return False
				count = 0

			elif i=='?':
				count += 1

	return flag

# keep this function call here 
print(QuestionsMarks(input()))
