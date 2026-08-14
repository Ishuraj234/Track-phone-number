import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber, "en")

print(location)


from phonenumbers import carrier
service_provider = carrier.name_for_number(pepnumber, "en")
print("Service Provider:", service_provider)


from opencage.geocoder import OpenCageGeocode
key = '1cb668add52044739e59755ee0bbf046'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=10)

folium.Marker(
    [lat, lng],
    popup=location
).add_to(myMap)


myMap.save("mylocation.html")