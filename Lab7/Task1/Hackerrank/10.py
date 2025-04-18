def average(array):
    a_set = set(array)
    total = 0
    size = len(a_set)
    for x in a_set:
        total += x
    return(total/size)
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)