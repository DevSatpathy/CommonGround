import geocoder

def getCurrentLocation():
    g = geocoder.ip('me')
    return g.latlng

print(getCurrentLocation())