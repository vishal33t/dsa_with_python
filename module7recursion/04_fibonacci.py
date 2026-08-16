def recur_fibo(n):
    
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

n_terms = 10

if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence up to {n_terms} terms:")
    for i in range(n_terms):
        print(recur_fibo(i), end=" ")