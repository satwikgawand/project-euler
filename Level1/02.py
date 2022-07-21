LIMIT = 4000000

series = [2]
x = 1
y = 2

while x <= LIMIT:
    z = x+y
    if z%2 == 0:
        series.append(z)
    x = y
    y = z

print(sum(series))