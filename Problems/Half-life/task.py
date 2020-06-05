ra_n = int(input())
ra_r = int(input())
period = 0
while ra_n > ra_r:
    ra_n *= 0.5
    period += 1
print(period * 12)
