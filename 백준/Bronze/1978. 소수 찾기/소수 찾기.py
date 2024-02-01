def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count

def main():
    n = int(input())
    numbers = list(map(int, input().split()))

    prime_count = count_primes(numbers)
    print(prime_count)

if __name__ == "__main__":
    main()
