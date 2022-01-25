def symmetricMatrix(n, matrix):
    mid = n//2
    if n%2: mid +=1
        
    for i in range(n//2):
        if matrix[i] != matrix[-i-1]:
            return False
    
    for j in range(n):
        if matrix[j][:n//2] != matrix[j][mid:][::-1]:
            return False
     
    return True


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        
        matrix = []
        for j in range(n):
            matrix.append(input())
        
        if symmetricMatrix(n, matrix):
            print("YES")
        else:
            print("NO")
