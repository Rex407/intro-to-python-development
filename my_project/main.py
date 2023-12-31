import phonenumbers
import folium
import opencage
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')
print()
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print()
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = 'a0f874689bcb4cb5b5f32f9375b42cb9'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)
