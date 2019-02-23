import geocoder

def get_current_location():
    g = geocoder.ip('me')
    return g.latlng

def get_current_location_from_address(address):
    try:
        g = geocoder.osm(address)
        coords = []
        coords.append(g.osm['x'])
        coords.append(g.osm['y'])
        return coords
    except:
        return []
