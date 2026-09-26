t = int(input())

for _ in range(t):
    n = int(input())
    
    x = []
    for val in input().split():
        x.append(int(val))
        
    y = {}
    
    for z in x:
        
        for _ in range(50):
            s = 0
            s = z
            
            while s > 0:
                digit = s % 10
                s += digit * digit
                s //= 10
                
            z = s
            
        if z in y:
            y[z] += 1
        else:
            y[z] = 1
            
    ans = 0
    for i in y.values():
        ans += i * (i - 1) // 2
        
    print(ans)