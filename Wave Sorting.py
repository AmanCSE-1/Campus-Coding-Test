''' Have a function WaveSorting(arr) take the array of positive intergers stored in arr and return the string True if the numbers can be arranged in a wave pattern.
    a1 > a2 < a3 > a4 < a5 > ..., othewise return the string False.
    
    For Eaxmple : arr is [0, 1, 2, 4, 1, 4], then a possible wave ordering is [2, 0, 4, 1, 4, 1].'''


def WaveSorting(arr):
    arr.sort()

    if len(arr) == len(set(arr)):
        return True

    mid = len(arr//2)
    left, right = arr[:mid], arr[mid:]

    for i in range(mid):
        if left[i] != right[i]:
            continue
        else:
            return False

    return True
