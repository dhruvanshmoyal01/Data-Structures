
def euclid_gcd(a, b):
    if b == 0:
        return a
    x = a%b
    return euclid_gcd(b, x)
    
if __name__ == "__main__":
    a, b = map(int, input().split())
    res = euclid_gcd(a, b)
    print(int(a*b/res))
