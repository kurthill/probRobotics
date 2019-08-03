# Simulator to randomly generate weather from the following markov transition
# probabilities
#                           Tomorrow is
#                       sunny   cloudy  rainy
#              sunny     0.8      0.2     0
# today is     cloudy    0.4      0.4    0.2
#              rainy     0.2      0.6    0.2

import random
import numpy as np

def transWeather( yst ):
    table = ( (0.8,0.2,0), (0.4,0.4,0.2), (0.2,0.6,0.2) )
    x = random.uniform(0, 1)

    if x > 0 and x <= table[yst][0]:
        return 0
    elif x > table[yst][0] and x <= (table[yst][0]+table[yst][1]):
        return 1
    else:
        return 2

N = 1000000
hist = [0,0,0]
x = 1
for i in range(N):
    x = transWeather(x)
    hist[x] += 1

hist = [ i / N for i in hist]
print(hist)
