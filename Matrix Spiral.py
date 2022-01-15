def MatrixSpiral(strArr):
    # write your code here
    matrix = []
    for i in strArr:
        i = i.replace('[', '').replace(']', '')
        matrix.append(list(map(int, i.split(','))))

    spiral= []
    if matrix==[]: return spiral

    left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1

    while left<=right and top<=bottom:
        for j in range(left, right+1):
            spiral.append(str(matrix[top][j]))

        for i in range(top+1, bottom):
            spiral.append(str(matrix[i][right]))

        for j in reversed(range(left, right+1)):
            if top<bottom:
                spiral.append(str(matrix[bottom][j]))

        for i in reversed(range(top+1, bottom)):
            if left<bottom:
                spiral.append(str(matrix[i][left]))

        left, right, top, bottom = left+1, right-1, top+1, bottom-1

    return ','.join(spiral)
