from sympy import factorint, primerange
from sympy.ntheory import isprime

if __name__ == "__main__":
    primes = set(primerange(200))
    print(primes)
    for i in range(1, 100):
        num = i * 2
        factors = set(factorint(num).keys())
        pots = (sorted(list(primes - factors)))
        for p in pots:
            if (num - p) in primes:
                print(f"{num}\t{sorted(list(factors))}\t\tsum of {p} and {num - p}")
                break
        else:
            print(f"No solution for {num}")
