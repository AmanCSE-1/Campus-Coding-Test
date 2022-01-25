def marvel(array, n):
    result= [1]*n
    
    for i in range(1, n):
        if array[i] > array[i-1]:
            result[i] += result[i-1]
    
    return result

if __name__ == "__main__":
    n = int(input())
    
    array = []
    for _ in range(n):
        array.append(int(input()))
    
    forwardPass = marvel(array, n)
    backwardPass = marvel(array[::-1], n)
    
    print(sum(map(max, zip(forwardPass, reversed(backwardPass)))))
