from geopy.geocoders import Nominatim
from geopy.distance import geodesic

PHARMACIES = [
        {"name": "Drogaria São Paulo - Liberdade", "location": (-23.55990790743397, -46.63816031301579)},
        {"name": "Drogaria São Paulo - Maestro Cardim", "location": (-23.563496211049053, -46.64097933066253)},
        {"name": "Drogasil - Conselheiro Furtado", "location": (-23.563407735629458, -46.632731117534924)},
        {"name": "Tabajara - Brigadeiro", "location": (-23.56286972139421, -46.645501049140556)},
        {"name": "Poupa Mais Farma - Conselheiro Ramalho", "location": (-23.557429627808155, -46.64450781753102)},
        {"name": "Drogaria Galvão - Galvão Bueno", "location": (-23.563407735629458, -46.632731117534924)}]

def get_nearby_pharmacies(location, radius_km, pharmacies):
    geolocator = Nominatim(user_agent="pharmacy_locator")
    location = geolocator.geocode(location)

    if not location:
        return []

    pharmacies_with_distances = []

    for pharmacy in pharmacies:
        distance = geodesic(location.point, pharmacy['location']).kilometers
        if distance <= radius_km:
            pharmacies_with_distances.append({"name": pharmacy['name'], "distance": distance})

    pharmacies_with_distances.sort(key=lambda x: x['distance'])

    return pharmacies_with_distances