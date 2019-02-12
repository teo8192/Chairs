f = open("reservations.csv")

for reservation in f:
    name, number = reservation.split(",")
    try:
        chairs_per_person = 50 / int(number)
    except:
        print("error")
    else:
        print("{} will get {} chairs per person".format(name, chairs_per_person))
