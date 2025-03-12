def countdown(n):
    for i in range(n, -1, -1):
        yield i


N = 10
print(list(countdown(N)))