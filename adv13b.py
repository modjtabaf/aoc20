
if False:
    input = [7, 13, 0, 0, 59, 0, 31, 19]
else:    
    input = [29, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 37, 0, 0, 0, 0, 0, 409, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 13, 19, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 353, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 41]

# See "Chinese remainder theorem" section "Search by sieving" on Wikipedia for the algorithm

for rem, n in enumerate(input):
    if n == 0:
        continue

    if rem == 0:
        x = 0
        d = n
        continue

    k = 0
    while (x + rem) % n != 0:
        x += d

    d *= n

print(x)
