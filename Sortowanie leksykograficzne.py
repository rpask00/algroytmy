def sortuj_alfabetycznie(list):
    return sorted(list, key=lambda x: x[0][0])


def sortuj_po_sredniej(list):
    return sorted(list, key=lambda x: x[1])


sample = [
    ("Kowalski", 3.12),
    ("Kasprowicz", 4.40),
    ("Nowak", 6.00),
    ("Kosak", 5.44),
    ("Nasiadka", 5.32),
    ("Nowicki", 3.44),
    ("Kanigowski", 4.00),
    ("Danusiak", 4.00),
    ("Dworznik", 4.20),
    ("Kaspro", 3.00),
    ("Kasprowicz", 4.00),
    ("Kasprowicz", 3.10),
    ("Danusiak", 2.00),
    ("Danusiak", 2.1),
    ("Andreasik", 2.1),
]


for i in sortuj_alfabetycznie(sample):
    print(i)

print('-------')

for i in sortuj_po_sredniej(sample):
    print(i)

