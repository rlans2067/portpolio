def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    a, b = map(int, input().split())
    
    greatest_common_divisor = gcd(a, b)
    least_common_multiple = lcm(a, b)
    
    print(greatest_common_divisor)
    print(least_common_multiple)

if __name__ == "__main__":
    main()
