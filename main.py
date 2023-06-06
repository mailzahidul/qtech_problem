from math import sin, cos, acos, radians
import json

path = 'information.json'
with open(path, 'r') as f:
    data = json.load(f)
dict_len = len(data)
earth_radius = 6371.01              # Approximate value of Radius of earth
row={}
temp_dict = {}
real_dict = {}

i = 'uttara'                        # Start from uttara
row['latitude'] = 23.8728568
row['longitude'] = 90.3984184
lst=[]

for z in range(0, dict_len-1): # A
    count=0
    for j, col in data.items(): # B
        if i == j:
            continue
        lat1 = radians(row['latitude'])
        lon1 = radians(row['longitude'])
        lat2 = radians(col['latitude'])
        lon2 = radians(col['longitude'])
        distance = earth_radius * acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(lon1 - lon2))
        from_to = f'{i}>{j}'
        to_from = f'{j}>{i}'
        if to_from not in real_dict and j not in lst:
            temp_dict[from_to] = distance
        count +=1
        if dict_len-1 == count:
            m_d = min(temp_dict, key=temp_dict.get)
            slc = m_d.split('>')
            destination = slc[1]
            if destination not in lst:
                i=destination
                row['latitude'] = data[i]['latitude']
                row['longitude'] = data[i]['longitude']
    min_dist = min(temp_dict, key=temp_dict.get)
    real_dict[min_dist] = temp_dict[min_dist]
    temp_dict = {}
    for key in real_dict.keys():
        split_key = key.split('>')
        lst.append(split_key[0])


print('   The best optimized traffic route for traveling all those given location\'s latitude and longitude')
counter=0
for location, distnc in real_dict.items():
    counter+=1
    print(f'    {counter} route {location}', distnc)

