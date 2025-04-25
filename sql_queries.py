import sqlite3

DB_NAME = 'Flight_management.db'


def getFlightsByDestination(destinationCountry):
    """
    Retrieves all flights going to a specific destination country

    Returns:
        flightNumber, destination country, status, and departure time
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT F.flightNumber, A.country AS destinationCountry, F.status, F.departureTime
            FROM Flight F
            JOIN Airport A ON F.destinationAirportId = A.airportId
            WHERE A.city = ?
        """, (destinationCountry,))
        return cursor.fetchall()


def getFlightsByStatus(status):
    """
    Retrieves all flights based on their status

    Returns:
        flightNumber, departureTime, arrivalTime, and status
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT flightNumber, departureTime, arrivalTime, status
            FROM Flight
            WHERE status = ?
        """, (status,))
        return cursor.fetchall()


def getFlightsByDepartureDate(departureDate):
    """
    Retrieves all flights scheduled to depart on a given date

    Args:
        date in YYYY-MM-DD format

    Returns:
        flightNumber, departureTime, and arrivalTime
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT flightNumber, departureTime, arrivalTime
            FROM Flight
            WHERE DATE(departureTime) = ?
        """, (departureDate,))
        return cursor.fetchall()


def updateFlightSchedule(flightId, newTime, newStatus):
    """
    Updates the departure time and status of a specific flight

    Args:
        ID of the flight to edit
        new time in YYYY-MM-DD HH:MM:SS format
        new status of the flighr

    Returns:
        None
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Flight
            SET departureTime = ?, status = ?
            WHERE flightId = ?
        """, (newTime, newStatus, flightId))
        conn.commit()


def assignPilotToFlight(flightId, pilotId):
    """
    Assigns a pilot to a flight

    Returns:
        None
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Flight
            SET pilotId = ?
            WHERE flightId = ?
        """, (pilotId, flightId))
        conn.commit()


def getFlightsByPilot(pilotId):
    """
    Retrieves all flights assigned to given pilot

    Returns:
        flightNumber, departureTime, arrivalTime, and status.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT flightNumber, departureTime, arrivalTime, status
            FROM Flight
            WHERE pilotId = ?
        """, (pilotId,))
        return cursor.fetchall()


def getAllAirports():
    """
    Retrieves all the airports from the database 

    Returns:
        airportId, airportName, city, and country
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Airport")
        return cursor.fetchall()


def updateAirportCity(airportId, newCity):
    """
    Updates the city name of a specific airport

    Returns:
        None
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Airport
            SET city = ?
            WHERE airportId = ?
        """, (newCity, airportId))
        conn.commit()


def getFlightCountsByDestination():
    """
    Retrieves the number of flights by city

    Returns:
        city name and flight count
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT A.city, COUNT(*) as flightCount
            FROM Flight F
            JOIN Airport A ON F.destinationAirportId = A.airportId
            GROUP BY A.city
        """)
        return cursor.fetchall()


def getFlightCountsByPilot():
    """
    Retrieves the number of flights assigned to each pilot

    Returns:
        pilot full name, pilot ID and flight count
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT P.firstName || ' ' || P.lastName AS pilotName, P.pilotId, COUNT(*) as flightCount
            FROM Flight F
            JOIN Pilot P ON F.pilotId = P.pilotId
            GROUP BY F.pilotId
        """)
        return cursor.fetchall()