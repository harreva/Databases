import sqlite3

"""Modifiers"""

def addFlight(cursor):
    """
    Add new flight to database
    """
    flightNumber = input("Enter flight number: ")
    departureTime = input("Enter departure time (YYYY-MM-DD HH:MM:SS): ")
    arrivalTime = input("Enter arrival time (YYYY-MM-DD HH:MM:SS): ")
    status = input("Enter flight status: ")
    pilotId = input("Enter pilot ID : ") 
    depAirportId = input("Enter departure airport ID: ")
    destAirportId = input("Enter destination airport ID: ")

    cursor.execute("""
        INSERT INTO Flight (flightNumber, departureTime, arrivalTime, status, pilotId, departureAirportId, destinationAirportId)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (flightNumber, departureTime, arrivalTime, status, pilotId, depAirportId, destAirportId))
    print(f"Flight {flightNumber} added successfully.")
    

def deleteFlight(cursor):
    """
    Delete flight from database
    """
    flightId = input("Enter flight ID to delete: ")

    cursor.execute("DELETE FROM Flight WHERE flightId = ?", (flightId,))
    print(f"Flight {flightId} deleted successfully.")


def updateFlightTime(cursor):
    """
    Updates departure time, arrival time, and status of a flight
    """
    flightId = input("Enter flight ID to update: ")
    newDeparture = input("Enter new departure time (YYYY-MM-DD HH:MM:SS): ")
    newArrival = input("Enter new arrival time (YYYY-MM-DD HH:MM:SS): ")
    newStatus = input("Enter new flight status: ")

    cursor.execute("""
        UPDATE Flight
        SET departureTime = ?, arrivalTime = ?, status = ?
        WHERE flightId = ?
    """, (newDeparture, newArrival, newStatus, flightId))
    print(f"Flight {flightId} timings updated to departure: {newDeparture} and arrival: {newArrival}.")


def updateDestination(cursor):
    """
    Updates destination airport of a flight
    """
    flightId = input("Enter flight ID to update: ")
    newDestAirportId = input("Enter new destination airport ID: ")

    cursor.execute("""
        UPDATE Flight
        SET destinationAirportId = ?
        WHERE flightId = ?
    """, (newDestAirportId, flightId))
    print(f"Flight {flightId} destination updated to airport ID: {newDestAirportId}")


def updateStatus(cursor):
    """
    Update status of flight
    """
    flightId = input("Enter flight ID to update: ")
    newStatus = input("Enter new flight status: ")

    cursor.execute("""
        UPDATE Flight
        SET status = ?
        WHERE flightId = ?
    """, (newStatus, flightId))
    print(f"Flight {flightId} status updated to: {newStatus}")

def assignPilotToFlight(cursor):
    """
    Assign a pilot to flight
    """
    flightId = input("Enter flight ID to assign pilot to: ")
    pilotId = input("Enter pilot ID to assign: ")

    cursor.execute("""
        UPDATE Flight
        SET pilotId = ?
        WHERE flightId = ?
    """, (pilotId, flightId))
    print(f"Pilot {pilotId} assigned to flight {flightId}")


"""Retrievers"""

def getFlightsByDestination(cursor, destinationCity):
    """
    Retrieves flights with a specific destination city
    """
    cursor.execute("""
        SELECT F.flightNumber, A.city AS destinationCity, F.status, F.departureTime
        FROM Flight F
        JOIN Airport A ON F.destinationAirportId = A.airportId
        WHERE A.city = ?
    """, (destinationCity,))
    return cursor.fetchall()


def getFlightsByStatus(cursor, status):
    """
    Retrieves flights with a specific status
    """
    cursor.execute("""
        SELECT flightNumber, departureTime, arrivalTime, status
        FROM Flight
        WHERE status = ?
    """, (status,))
    return cursor.fetchall()


def getFlightsByDepartureDate(cursor, departureDate):
    """
    Retrieves flights departing on a specific date
    """
    cursor.execute("""
        SELECT flightNumber, departureTime, arrivalTime
        FROM Flight
        WHERE DATE(departureTime) = ?
    """, (departureDate,))
    return cursor.fetchall()


def getPilotSchedule(cursor):
    """
    Get all flights assigned to a pilot
    """
    pilotId = input("Enter pilot ID to view schedule: ")

    cursor.execute("""
        SELECT flightId, departureTime, arrivalTime, status
        FROM Flight
        WHERE pilotId = ?
    """, (pilotId,))
    flights = cursor.fetchall()

    if flights:
        print(f"Pilot {pilotId}'s Schedule:")
        for flight in flights:
            print(f"Flight ID: {flight[0]}, Departure: {flight[1]}, Arrival: {flight[2]}, Status: {flight[3]}")
    else:
        print(f"No flights assigned to pilot {pilotId}")


def viewFlightsByCriteria(cursor):
    """
    View flights based on destination, status, or departure date
    """
    print("\nView Flights by:")
    print("1. Destination City")
    print("2. Flight Status")
    print("3. Departure Date")
    choice = input("Select an option: ")

    if choice == '1':
        city = input("Enter destination city: ")
        results = getFlightsByDestination(cursor, city)
    elif choice == '2':
        status = input("Enter flight status (e.g., Scheduled, Delayed): ")
        results = getFlightsByStatus(cursor, status)
    elif choice == '3':
        date = input("Enter departure date (YYYY-MM-DD): ")
        results = getFlightsByDepartureDate(cursor, date)
    else:
        print("Error. Please choose a valid option")
        return

    if results:
        for result in results:
            print(result)
    else:
        print("No flights found matching your criteria.")

def printMenu():
    """
    Main menu
    """
    print("Flight management system. Please select from the menu below")
    print(" 1 - Add flight")
    print(" 2 - Delete flight")
    print(" 3 - Update flight arrival/departure times and status")
    print(" 4 - Update flight destination")
    print(" 5 - Update flight Status")
    print(" 6 - Assign a new pilot to a flight")
    print(" 7 - View flights by either destination, status or departure")
    print(" 8 - View flights by pilot")
    print(" 9 - Exit")


def main():
    """
    Main loop
    """
    conn = sqlite3.connect('Flight_management.db')
    cursor = conn.cursor()

    switch_dict = {
        '1': addFlight,
        '2': deleteFlight,
        '3': updateFlightTime,
        '4': updateDestination,
        '5': updateStatus,
        '6': assignPilotToFlight,
        '7': viewFlightsByCriteria,
        '8': getPilotSchedule
    }
    
    while True:
        printMenu()
        choice = input("\nSelect an option: ")

        if choice == '9':
            print("Exiting")
            break
        
        # Execute the function based on the user's choice
        func = switch_dict.get(choice)
        
        if func:
            func(cursor)
        else:
            print("Error. Please choose a valid option")

    conn.close()


if __name__ == '__main__':
    main()
