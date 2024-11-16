import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    j = 0
    for i in range(n):
        if arr[i] < 0:
            continue
        
        while i - j > k:
            j += 1
        
        while arr[i] != 0 and (i + k) >= min(n - 1, j):
            if arr[j] > 0:
                j += 1
                continue
            
            x = min(arr[i], abs(arr[j]))
            arr[i] -= x
            arr[j] += x
            
            if arr[j] >= 0:
                j += 1
    
    ans = sum(abs(x) for x in arr)
    print(ans)
main()
