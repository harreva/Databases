from sql_queries import *

""" Modifiers """

def cliAddFlight():
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

    addFlight(flightNumber, departureTime, arrivalTime, status, pilotId, depAirportId, destAirportId)
    print(f"Flight {flightNumber} added successfully.")


def cliDeleteFlight():
    """
    Delete flight
    """
    flightId = input("Enter flight ID to delete: ")
    deleteFlight(flightId)
    print(f"Flight {flightId} deleted successfully.")


def cliUpdateFlightTime():
    """
    Update flight time by ID
    """
    flightId = input("Enter flight ID to update: ")
    newDeparture = input("Enter new departure time (YYYY-MM-DD HH:MM:SS): ")
    newArrival = input("Enter new arrival time (YYYY-MM-DD HH:MM:SS): ")
    newStatus = input("Enter new flight status: ")

    updateFlightTime(flightId, newDeparture, newArrival, newStatus)
    print(f"Flight {flightId} updated successfully.")


def cliUpdateDestination():
    """
    Update flight destination by ID
    """
    flightId = input("Enter flight ID: ")
    newDest = input("Enter new destination airport ID: ")
    updateDestination(flightId, newDest)
    print(f"Flight {flightId} destination updated.")


def cliUpdateStatus():
    """
    Update flight status by ID
    """
    flightId = input("Enter flight ID: ")
    newStatus = input("Enter new status: ")
    updateStatus(flightId, newStatus)
    print(f"Flight {flightId} status updated to {newStatus}.")


def cliUpdatePilot():
    """
    Update which pilot is assigned to the flight by flight ID
    """
    flightId = input("Enter flight ID: ")
    pilotId = input("Enter pilot ID to assign: ")
    assignPilotToFlight(flightId, pilotId)
    print(f"Pilot {pilotId} assigned to flight {flightId}")

def cliUpdateAirportCity():
    """
    Update airport city by airport ID
    """
    airportId = input("Enter airport ID: ")
    newCity = input("Enter new city name: ")
    updateAirportCity(airportId, newCity)
    print(f"Airport {airportId} updated to city: {newCity}")


""" Getters """

def cliViewFlightsByCriteria():
    """
    Get flights by either destination, flight status or departure date
    """
    print("\nView Flights by:")
    print("1. Destination City")
    print("2. Flight Status")
    print("3. Departure Date")
    choice = input("Select an option: ")

    if choice == '1':
        city = input("Enter destination city: ")
        results = getFlightsByDestination(city)
    elif choice == '2':
        status = input("Enter flight status: ")
        results = getFlightsByStatus(status)
    elif choice == '3':
        date = input("Enter departure date (YYYY-MM-DD): ")
        results = getFlightsByDepartureDate(date)
    else:
        print("Invalid choice.")
        return

    if results:
        for row in results:
            print(row)
    else:
        print("No flights found using that criteria")


def cliGetPilotSchedule():
    """
    Get pilot schedule by pilot ID
    """
    pilotId = input("Enter pilot ID: ")
    results = getPilotSchedule(pilotId)
    if results:
        print(f"\nPilot {pilotId}'s schedule:")
        for row in results:
            print(f"Flight ID: {row[0]}, Departure: {row[1]}, Arrival: {row[2]}, Status: {row[3]}")
    else:
        print("No flights currently found for this pilot")


def cliViewAirports():
    """
    Get all airports
    """
    results = getAllAirports()
    for row in results:
        print(row)


"""Menu"""

def printMenu():
    """
    Prints main menu
    """
    print("\nFlight Management System")
    print("1 - Add flight")
    print("2 - Delete flight")
    print("3 - Update flight times and status")
    print("4 - Update flight destination")
    print("5 - Update flight status")
    print("6 - Add a new pilot to flight")
    print("7 - Update airport city")
    print("8 - View flights by destination, status or date")
    print("9 - View pilot schedule")
    print("10 - View all airports")
    print("0 - Exit")


def main():
    """
    Main application loop
    """
    while True:
        printMenu()
        choice = input("Enter choice: ")

        actions = {
            '1': cliAddFlight,
            '2': cliDeleteFlight,
            '3': cliUpdateFlightTime,
            '4': cliUpdateDestination,
            '5': cliUpdateStatus,
            '6': cliUpdatePilot,
            '7': cliUpdateAirportCity,
            '8': cliViewFlightsByCriteria,
            '9': cliGetPilotSchedule,
            '10': cliViewAirports,
        }

        if choice == '0':
            print("Exiting program.")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()