n=list(map(int, input().split()))

counter=0

if n[0] == n[1] or n[0] == n[2] or n[0] == n[3]:
    counter += 1

if n[1] == n[2] or n[1] == n[3]:
    counter += 1

if n[2] == n[3]:
    counter += 1

print(counter)
