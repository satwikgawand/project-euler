LIMIT = 1000

multiples = []

for i in range(0,LIMIT):
    if i%3 == 0 or i%5 == 0:
        multiples.append(i)

print(sum(multiples))