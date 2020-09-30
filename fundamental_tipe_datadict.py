from typing import Dict, List

print('\ntipe data list')
kamus = {}
kamus['satu'] = 'one'
kamus['dua'] = 'two'
kamus['tiga'] = 'three'
print(kamus)

print('data ini dikirimkan oleh server gojek, untuk memberikan info driver')
data_gojek = {
    'tanggal': '2020 09 30',
    'driver_list': [{'nama': 'dena', 'jarak': 10}, {'nama': 'tami', 'jarak': 20}, 'rafli'],
}
print(data_gojek)
print(f"driver sekitar sini {data_gojek['driver_list']}")
print(f"driver #1 {data_gojek['driver_list'][0]}")
print(f"driver #3 {data_gojek['driver_list'][2]}")
print (f"driver terdekat erjarak {data_gojek['driver_list'][0]['jarak']} meter")