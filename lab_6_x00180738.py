# Lab 6

class hotel:
    hotelName = ""
    hotelAddress = ""
    hotelYear = 0
    hotelRooms = 0
    hotelSpa = False

    def __init__(self, hotelName_in=None, hotelAddress_in=None, hotelYear_in=None, hotelRooms_in=None, hotelSpa_in=None):
        if hotelYear_in < 0:
            self.hotelYear = 0
        else:
            self.hotelYear = hotelYear_in
        if hotelRooms_in < 0:
            self.hotelRooms = 0
        else:
            self.hotelRooms = hotelRooms_in
        if hotelName_in is not None:
            self.hotelName = hotelName_in
        else:
            self.hotelName = ""
        if hotelAddress_in is not None:
            self.hotelAddress = hotelAddress_in
        else:
            self.hotelAddress = ""
        if hotelSpa_in is not None:
            self.hotelSpa = hotelSpa_in
        else:
            self.hotelSpa = False

    def cost_insurance(self):
        total = 1000
        if self.hotelYear <= 1950:
            total += 1000
        elif self.hotelYear > 1950 and self.hotelYear <= 1999:
            total += 750
        else:
            total += 500
        if self.hotelRooms < 25:
            total += 300
        elif self.hotelRooms >= 25 and self.hotelRooms <= 50:
            total += 400
        elif self.hotelRooms >= 51 and self.hotelRooms <= 100:
            total += 650
        else:
            total += 900
        if self.hotelSpa:
            total += 300
        return total

    def print_details(self):
        print("*****************************************")
        print("************ Hotel Details **************")
        print("Hotel Name: \t\t", self.hotelName)
        print("Hotel Year: \t\t", self.hotelYear)
        print("Hotel Address: \t\t", self.hotelAddress)
        print("Hotel # Rooms: \t\t", self.hotelRooms)
        print("Hotel has SPA: \t\t", self.hotelSpa)
        print("Hotel Insurance: \t\t", self.cost_insurance())
        print("*****************************************")

# Creating Hotel instances
h1 = hotel(hotelName_in="Hotel Marion", hotelAddress_in="Ballsbridge", hotelYear_in=2001, hotelRooms_in=200, hotelSpa_in=True)
h2 = hotel("Hotel Lavery", "OConnell St", 1960, 90, False)

# printing hotel details
h1.print_details()
h2.print_details()

# checking which hotel has higher insurance
if h1.cost_insurance() > h2.cost_insurance():
    print("{} has higher insurance than {}".format(h1.hotelName, h2.hotelName))
elif h1.cost_insurance() == h2.cost_insurance():
    print("{} has the same insurance as {}".format(h1.hotelName, h2.hotelName))
else:
    print("{} has higher insurance than {}".format(h2.hotelName, h1.hotelName))

# printing average hotel insurance for these 2 instances
average_insurance = (h1.cost_insurance()+h2.cost_insurance())/2
print("The average insurance cost for both Hotels is {} ".format(average_insurance))
