# Lab 7

class Room:
    # room variables
    room_number = ''
    max_guests = ''
    booked_guests = ''
    nights_booked = ''
    room_in_use = False

    # static variables
    count_rooms_in_use = 0
    total_number_of_guests = 0
    peak_season = True

    def __init__(self, room_number_in, max_guests_in):
        self.room_number = room_number_in
        self.max_guests = max_guests_in
        self.booked_guests = 0
        self.nights_booked = 0
        self.room_in_use = False


    def cost_room(self):
        if Room.peak_season:
            room_price = self.nights_booked * 250
        else:
            room_price = self.nights_booked * 150
        return room_price

    @staticmethod
    def set_peak_off_peak(season_in):
        Room.peak_season = season_in

    def check_in(self, number_guests_in, nights_booked_in):
        self.booked_guests = number_guests_in
        self.nights_booked = nights_booked_in
        self.room_in_use = True
        Room.count_rooms_in_use += 1
        Room.total_number_of_guests += number_guests_in
        print('Room {} checked in'.format(self.room_number))

    def check_out(self):
        Room.total_number_of_guests -= self.booked_guests
        Room.count_rooms_in_use -= 1
        self.booked_guests = 0
        self.nights_booked = 0
        self.room_in_use = False
        print('Room {} checked out'.format(self.room_number))


roomA = Room(101, 2)
roomB = Room(102, 4)

print('/**************************************** Before check in ****************************************/')
print('Total guests in the hotel: {}'.format(Room.total_number_of_guests))
print('Total rooms in use: {}'.format(Room.count_rooms_in_use))

print('/**************************************** After check in ****************************************/')
roomA.check_in(2, 4)
roomB.check_in(4, 10)
print('Room {} wil cost: {}'.format(roomA.room_number, roomA.cost_room()))
print('Room {} wil cost: {}'.format(roomB.room_number, roomB.cost_room()))
print('Total guests in the hotel: {}'.format(Room.total_number_of_guests))
print('Total rooms in use: {}'.format(Room.count_rooms_in_use))

print('/**************************************** After check out ****************************************/')
roomA.check_out()
roomB.check_out()
print('Total guests in the hotel: {}'.format(Room.total_number_of_guests))
print('Total rooms in use: {}'.format(Room.count_rooms_in_use))
