import sqlite3

conn = sqlite3.connect('Flight_management.db')
print("Database has been created")

# Enable foreign key support
conn.execute("PRAGMA foreign_keys = ON;")

# Pilot table
conn.execute("""
CREATE TABLE IF NOT EXISTS Pilot (
    pilotId INTEGER PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    licenseNumber TEXT UNIQUE NOT NULL
)""")

# Airport table
conn.execute("""
CREATE TABLE IF NOT EXISTS Airport (
    airportId INTEGER PRIMARY KEY,
    airportName TEXT NOT NULL,
    city TEXT NOT NULL,
    country TEXT NOT NULL
)""")

# Flight table
conn.execute("""
CREATE TABLE IF NOT EXISTS Flight (
    flightId INTEGER PRIMARY KEY,
    flightNumber TEXT NOT NULL,
    departureTime TEXT NOT NULL,
    arrivalTime TEXT NOT NULL,
    status TEXT,
    pilotId INTEGER,
    departureAirportId INTEGER,
    destinationAirportId INTEGER,
    FOREIGN KEY (pilotId) REFERENCES Pilot(pilotId),
    FOREIGN KEY (departureAirportId) REFERENCES Airport(airportId),
    FOREIGN KEY (destinationAirportId) REFERENCES Airport(airportId)
)""")

conn.commit()
conn.close()

print("Tables created successfully")