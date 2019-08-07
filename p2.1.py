# Calculate the probability that the sensor is faulty


def filter(bel):
    den = bel + 0.3333*(1-bel)
    return bel / den


p = 0.01
print('0: {}'.format(p))
for i in range(1, 11):
    p = filter(p)
    print('{}: {}'.format(i, p))

print('hello world')
