import phonenumbers

from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import folium

# from test import number

def getLocation(number):
    from phonenumbers import geocoder

    key = "3e8e4f5f242245c987233fa0424f921a"

    check_number = phonenumbers.parse(number)
    number_location = geocoder.description_for_number(check_number, "en")
    
    print(number_location)

    
    service_provider = phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider, "en"))

    
    geocoder = OpenCageGeocode(key)

    query = str(number_location)
    results = geocoder.geocode(query)

    lat = results[0]["geometry"]["lat"]
    lng = results[0]["geometry"]["lng"]

    map_location = folium.Map(location = [lat,lng], zoom_start=5)
    folium.Marker([lat,lng], popup=number_location).add_to(map_location)
    print(map_location)
    map_location.save("python\\cincyhacks24\\templates\\mylocation.html")
