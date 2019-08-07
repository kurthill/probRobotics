# Calculate the probability distribution of the weather of any given
# day given the transition probabilities:
#
#                           Tomorrow is
#                       sunny   cloudy  rainy
#              sunny     0.8      0.2     0
# today is     cloudy    0.4      0.4    0.2
#              rainy     0.2      0.6    0.2
#
# and sensor data with accuracy given by:
#
#                            Measured weather
#                          sunny  cloudy  rainy
#                 sunny     0.6     0.4     0
# Actual weather  cloudy    0.3     0.7     0
#                 rainy      0       0      1

trans = ((0.8, 0.2, 0), (0.4, 0.4, 0.2), (0.2, 0.6, 0.2))
sense = ((0.6, 0.4, 0), (0.3, 0.7, 0), (0, 0, 1))


def filter(bel, z):

    bbel = [0, 0, 0]
    for x in range(len(bel)):

        # print('x = {}'.format(x))
        for xi in range(len(bel)):
            # (print('xi = {}: {} * {} = {}'.format(xi, trans[xi][x],
            #                                       bel[xi],
            #                                       trans[xi][x] * bel[xi])))
            bbel[x] += trans[xi][x] * bel[xi]
            # print(bbel)

        # (print('x = {}: {} * {} = {}'.format(x, sense[x][z],
        #                                      bbel[x],
        #                                      sense[z][x] * bbel[x])))
        bbel[x] = sense[x][z] * bbel[x]
        # print(bbel)

    s = sum(bbel)
    bbel = [x / s for x in bbel]
    return bbel


b = [1, 0, 0]
z = (1, 1, 2, 0)
# z = (1, 1)

for z in z:
    b = filter(b, z)
    print(b)
