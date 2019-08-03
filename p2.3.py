# Calculate the probability distribution of the weather of any given 
# day given the transition probabilities:
#
#                           Tomorrow is
#                       sunny   cloudy  rainy
#              sunny     0.8      0.2     0
# today is     cloudy    0.4      0.4    0.2
#              rainy     0.2      0.6    0.2i
#
# and sensor data with accuracy given by:
#
#                            Measured weather
#                          sunny  cloudy  rainy
#                 sunny     0.6     0.4     0
# Actual weather  cloudy    0.3     0.7     0
#                 rainy      0       0      1

def filter( bel ):
    den = bel + 0.3333*(1-bel)
    return bel / den


p = 0.01
print('0: {}'.format(p))
for i in range(1,11):
    p = filter(p)
    print('{}: {}'.format(i,p))
