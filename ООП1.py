class Chair:
    pass


class Bed:
    pass


class People:
    pass


class Room:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Bathroom(Room):
    def __init__(self, a, b):
        super().__init__(a, b)


class Kitchen(Room):
    def __init__(self, a, b, table, chair):
        super().__init__(a, b)
        self.table = table
        self.chair = chair


class LivingRoom(Room):
    def __init__(self, a, b, room_number, table, chair):
        super().__init__(a, b)
        self.people = []
        self.room_number = room_number
        self.chair = chair
        self.table = table
        self.bed = []

    def add_bed(self, bed):
        self.bed.append(bed)

    def add_people(self, man):
        self.people.append(man)

    def people_counter(self):
        return len(self.people)


class DiningRoom:
    def __init__(self):
        self.tables = []
        self.chairs = []

    def add_table(self, table):
        self.tables.append(table)

    def add_chair(self, chair):
        self.chairs.append(chair)


class Floor:
    def __init__(self):
        self.bathrooms = []
        self.living_rooms = []
        self.kitchens = []

    def add_bathroom(self, bathroom):
        self.bathrooms.append(bathroom)

    def add_living_room(self, living_room):
        self.living_rooms.append(living_room)

    def add_kitchen(self, kitchen):
        self.kitchens.append(kitchen)

    def people_counter(self):
        cnt = 0
        for room in self.living_rooms:
            cnt += room.people_counter()
        return cnt

    def bathroom_counter(self):
        return len(self.bathrooms)


class Hostel(Floor):
    def __init__(self, dining_room):
        self.floor_counter = 0
        self.dining_room = dining_room
        self.floors = []

    def add_floor(self, floor):
        self.floors.append(floor)

    def floor_number(self):
        return len(self.floors)

    def people_counter(self):
        cnt = 0
        for floor in self.floors:
            cnt += floor.people_counter()
        return cnt


table = Table()
chair = Chair()
l_room1 = LivingRoom(3, 3, 249, table, chair)
persons = [People() for i in range(5)]

for person in persons:
    l_room1.add_people(person)

table = Table()
chair = Chair()
l_room2 = LivingRoom(3, 4, 250, table, chair)
persons = [People() for i in range(5)]

for person in persons:
    l_room1.add_people(person)

floor1 = Floor()
floor1.add_living_room(l_room1)
floor1.add_living_room(l_room2)

hostel = Hostel(DiningRoom())

hostel.add_floor(floor1)
print(hostel.people_counter())

l_room1.add_people(People())

print(hostel.people_counter())