print ('/n data tipe skalar')

anak1 = 'dena'
anak2 = 'tami'
anak3 = 'rafli'
anak4 = 'rizka'
anak5 = 'nazriel'

print (anak1)
print (anak2)
print (anak3)
print (anak4)
print (anak5)

print ('\ntipe data list/array')
anak = []
anak.append ('dena')
anak.append ('tami')
anak.append ('rafli')
anak.append ('rizka')
anak.append ('nazriel')
print (anak)
anak = ['dena', 'tami', 'rafli', 'rizka', 'nazriel']
print (anak)
anak.append ('gausahada')
print (anak)
print ('\n sapa anak')
print (f'hai {anak[3]} !')
print ('\nsapa semua anak')
for b in anak :
    print (f'hai {b} !')
print ('\n sapa semua anak cara ribet')
for b in range (0, len (anak)) :
    print (f'{b+1}.hai {anak [b]}')

