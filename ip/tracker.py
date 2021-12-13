import pygeoip

gi = pygeoip.GeoIP('./ip-information/geo.dat')

def print_record(tgt):
    rec = gi.record_by_addr(tgt)
    city = rec['city']
    country = rec['country_name']
    postal_code = rec['postal_code']
    areacode = rec['area_code']
    long = rec['longitude']
    lat = rec['latitude']
    dma_code = rec['dma_code']
    region_code = rec['region_code']
    timezone = rec['time_zone']
    print(f"[*] Target found {tgt}")
    print(f"Information: \nCity: {city}\mArea code: {areacode}\nCountry: {country}\nPostal Code: {postal_code}\nLongtitude: {long}\nLatitude: {lat}\nDma code: {dma_code}\nTimezone: {timezone}\nRegion Code: {region_code} ")

tgt = input("Please provide the ip adress:")
print_record(tgt)
