import sqlite3

DB_NAME = 'Flight_management.db'


""" Modifiers """

def addFlight(flightNumber, departureTime, arrivalTime, status, pilotId, depAirportId, destAirportId):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Flight (flightNumber, departureTime, arrivalTime, status, pilotId, departureAirportId, destinationAirportId)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (flightNumber, departureTime, arrivalTime, status, pilotId, depAirportId, destAirportId))


def deleteFlight(flightId):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Flight WHERE flightId = ?", (flightId,))


def updateFlightTime(flightId, newDeparture, newArrival, newStatus):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Flight
            SET departureTime = ?, arrivalTime = ?, status = ?
            WHERE flightId = ?
        """, (newDeparture, newArrival, newStatus, flightId))


def updateDestination(flightId, newDestAirportId):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Flight
            SET destinationAirportId = ?
            WHERE flightId = ?
        """, (newDestAirportId, flightId))


def updateAirportCity(airportId, newCity):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Airport
            SET city = ?
            WHERE airportId = ?
        """, (newCity, airportId))


def updateStatus(flightId, newStatus):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Flight
            SET status = ?
            WHERE flightId = ?
        """, (newStatus, flightId))


def assignPilotToFlight(flightId, pilotId):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Flight
            SET pilotId = ?
            WHERE flightId = ?
        """, (pilotId, flightId))


""" Getters """

def getFlightsByDestination(destinationCity):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT F.flightNumber, A.city AS destinationCity, F.status, F.departureTime
            FROM Flight F
            JOIN Airport A ON F.destinationAirportId = A.airportId
            WHERE A.city = ?
        """, (destinationCity,))
        return cursor.fetchall()


def getFlightsByStatus(status):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT flightNumber, departureTime, arrivalTime, status
            FROM Flight
            WHERE status = ?
        """, (status,))
        return cursor.fetchall()


def getFlightsByDepartureDate(departureDate):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT flightNumber, departureTime, arrivalTime
            FROM Flight
            WHERE DATE(departureTime) = ?
        """, (departureDate,))
        return cursor.fetchall()


def getPilotSchedule(pilotId):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT flightId, departureTime, arrivalTime, status
            FROM Flight
            WHERE pilotId = ?
        """, (pilotId,))
        return cursor.fetchall()


def getAllAirports():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Airport")
        return cursor.fetchall()