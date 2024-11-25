PI = 3.1415


def stopnie(rad):
    return (180 * rad)/PI

def radiany(stopnie):
    return stopnie*PI/180

print(radiany(90))

# PI rad -> 180deg
# x rad -> y deg

#y = (180deg * x)/PI
#x = y*PI/180deg