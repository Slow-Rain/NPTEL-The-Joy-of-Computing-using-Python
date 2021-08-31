lst = [int(x) for x in input().split()]

k = int(input())

lst.sort()

a=int(len(lst))

print(lst[a-k], end="")

