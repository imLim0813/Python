num = int(input())

tmp = list(map(int, input().split()))
tmp = [i / max(tmp) * 100 for i in tmp]

print(sum(tmp) / num)