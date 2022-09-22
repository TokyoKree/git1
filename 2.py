n = int(input())
mas = list(map(int, input().split()))
mas = mas[(n-1):] + mas[:(1)]
print(mas)
