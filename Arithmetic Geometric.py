def ArithGeo(str):
    # Checking for Arithmetic Series
    difference =arr[0]-arr[1]
    isAP = True
    for i in range(1, len(arr)-1):
        if arr[i]-arr[i+1]!=difference:
            isAP = False
            break
    
    if isAP: return 'Arithmetic'
    
    # Checking for Geometric Series
    ratio = arr[0]/arr[1]
    isGP = True
    for i in range(1, len(arr)-1):
        if arr[i]/arr[i+1]!=ratio:
            isGP = False
            break
    
    if isGP: return 'Geometric'
    
    # If Neither Airthmetic nor Geometric
    return -1

print(ArithGeo(input()))
