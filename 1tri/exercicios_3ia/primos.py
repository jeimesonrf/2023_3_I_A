def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    count = 0;
    for i in range(1,int(n/2)+1):
        if n % i == 0:
            count+=1
    if count >= 2:
        return False
    else:
        return True

def primes_to_n(n):
    result = []
    for i in range(n):
        if is_prime(i):
            result.append(i)
    return result

if __name__ == '__main__':
    for i in range(1000):
        if is_prime(i):
            print(i, is_prime(i),end=" ")
    
    numeros_primos = primes_to_n(10000)
    print(numeros_primos)
