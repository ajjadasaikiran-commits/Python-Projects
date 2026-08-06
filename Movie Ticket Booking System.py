# ================================
#      MOVIE TICKET BOOKING
# ================================

movies = {
    "Sakhi": 200,
    "Bombay": 250,
    "Nayakan": 250,
    "Dark": 2000,
    "Summer": 2500
}

booking = []

while True:
    print("\n==============================")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. Cancel Ticket")
    print("4. View Bookings")
    print("5. Search Booking")
    print("6. Show Collection")
    print("7. Exit")
    print("==============================")

    option = int(input("Enter Option: "))

    # --------------------------------------------------
    # VIEW MOVIES
    # --------------------------------------------------
    if option == 1:
        print("\n========== MOVIES ==========")
        for movie, price in movies.items():
            print(f"{movie:<10} ₹{price}")
        print("============================")

    # --------------------------------------------------
    # BOOK TICKET
    # --------------------------------------------------
    elif option == 2:

        name = input("Enter Customer Name: ")
        moviename = input("Enter Movie Name: ")

        if moviename not in movies:
            print("Movie Not Found")
            continue

        seats = int(input("Enter Number of Seats: "))

        found = False

        for b in booking:
            if b["Name"] == name and b["MovieName"] == moviename:
                b["Seat"] += seats
                b["Amount"] = b["Seat"] * movies[moviename]
                print("Booking Updated Successfully")
                print("Amount:", b["Amount"])
                found = True
                break

        if not found:
            newdict = {}
            newdict["Name"] = name
            newdict["MovieName"] = moviename
            newdict["Seat"] = seats
            newdict["Amount"] = seats * movies[moviename]

            booking.append(newdict)

            print("Ticket Booked Successfully")
            print("Amount:", newdict["Amount"])

    # --------------------------------------------------
    # CANCEL TICKET
    # --------------------------------------------------
    elif option == 3:

        name = input("Enter Customer Name: ")

        found = False

        for b in booking:

            if b["Name"] == name:

                seats = int(input("Enter Seats To Cancel: "))

                if seats <= b["Seat"]:

                    b["Seat"] -= seats
                    b["Amount"] = b["Seat"] * movies[b["MovieName"]]

                    if b["Seat"] == 0:
                        booking.remove(b)

                    print("Ticket Cancelled Successfully")

                else:
                    print("Invalid Seat Count")

                found = True
                break

        if not found:
            print("Booking Not Found")

    # --------------------------------------------------
    # VIEW BOOKINGS
    # --------------------------------------------------
    elif option == 4:

        if len(booking) == 0:
            print("No Bookings")
        else:

            print("\n========== BOOKINGS ==========")

            for b in booking:

                print("Customer :", b["Name"])
                print("Movie    :", b["MovieName"])
                print("Seats    :", b["Seat"])
                print("Amount   :", b["Amount"])
                print("------------------------------")

    # --------------------------------------------------
    # SEARCH BOOKING
    # --------------------------------------------------
    elif option == 5:

        name = input("Enter Customer Name: ")

        found = False

        for b in booking:

            if b["Name"] == name:

                print("\nBooking Found")
                print("Customer :", b["Name"])
                print("Movie    :", b["MovieName"])
                print("Seats    :", b["Seat"])
                print("Amount   :", b["Amount"])

                found = True
                break

        if not found:
            print("Booking Not Found")

    # --------------------------------------------------
    # SHOW COLLECTION
    # --------------------------------------------------
    elif option == 6:

        total_amount = 0
        total_seats = 0

        for b in booking:
            total_amount += b["Amount"]
            total_seats += b["Seat"]

        print("\n========== COLLECTION ==========")
        print("Total Tickets Sold :", total_seats)
        print("Total Collection   : ₹", total_amount)
        print("================================")

    # --------------------------------------------------
    # EXIT
    # --------------------------------------------------
    elif option == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Option")