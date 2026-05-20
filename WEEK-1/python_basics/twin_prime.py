def twin_prime(n, m):
    prime_list = []
    
    
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
    
    for a in range(n, m -1):
        b = a + 2
        if is_prime(a) and is_prime(b):
            prime_list.append((a, b))
            
    return prime_list
    
    
n = int(input())
m = int(input())
print(twin_prime(n, m))