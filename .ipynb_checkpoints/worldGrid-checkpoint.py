import math

'''
Tools to create a lattice of dots, roughly uniformly spaced, all around the Earth.
Partitions surface area using hypothetical square regions; expect poor placement for low numbers of dots.
'''

# Constants (in km)
earthRadius = 6360
earthArea = 4 * math.pi * earthRadius**2
earthCircum = 2 * math.pi * earthRadius

def sectionArea(num):
    '''Return area of section of Earth'''
    return earthArea / num

def sectionSide(area):
    '''Return length of side of square section'''
    return math.sqrt(area)

def sectionAngle(length):
    '''Return angle (in radians) associated with length'''
    pctCircum = length / earthCircum
    angle = 2 * math.pi * pctCircum
    return angle

def arcLenFromCount(count):
    '''Return arc length (in radians) from point count'''
    area = sectionArea(count)
    side = sectionSide(area)
    angle = sectionAngle(side)
    return (angle, angle * (180 / math.pi))

def scaleByLat(lat):
    '''Percent by which to scale latitude relative to equator'''
    rad = abs(lat) * (math.pi / 180)
    return 1 / math.cos(rad)

def getLattice(count):
    '''Return list of points on earth, roughly evenly spaced'''
    arc = arcLenFromCount(count)
    arcrad = arc[0]
    arcdeg = arc[1]

    locs = []

    # List of latitudes to loop over
    lats = [(lat*arcdeg) - 90 for lat in range(int(180 / arcdeg))]

    for lat in lats:
        scale = scaleByLat(lat)
        scaled_arcdeg = scale * arcdeg
        # List of longitudes to loop over
        lngs = [(lng * scaled_arcdeg) - 180 \
                for lng \
                in range(int(360 / scaled_arcdeg))]
        for lng in lngs:
            locs.append((lat, lng))
    return locs