def hasSingleCycle(array):
    visited = [0 for x in range(len(array))]
    start = 0
    visited[start] = 0
    current = array[start]%len(array)
    visited[current] = 1
    while start != current:
        step =  array[current]%len(array)
        if array[current]<0:
            step =  len(array) + array[current]
        current += step
        current %= len(array)
        if visited[current] == 0:
            visited[current] +=  1
        anyMorethanOne = any(visited[x]>1 for x in range(1,len(visited)))
        return False
    return True
            
        
    

visited = hasSingleCycle([1, -1, 1, -1])
print("visited"*3)