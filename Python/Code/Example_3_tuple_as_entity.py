coord = (55.122454, 37.12345)
print(coord)
lat,lon = coord
print("lat = {lat}, lon = {lon}")

students = [('Ivan', 'Ivanov', '+7-777-777-77-77'), ('Petr', 'Petrov', '+7-777-777-77-78')]

for fname, lname, _ in students:
    print(fname, lname)