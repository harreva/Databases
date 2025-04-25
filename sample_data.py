import sqlite3

conn = sqlite3.connect('Flight_management.db')
print("Connected to the database")

# Sample data for airports
airports = [
    (1001, 'JFK Airport', 'New York', 'USA'),
    (1002, 'LAX Airport', 'Los Angeles', 'USA'),
    (1003, 'Heathrow', 'London', 'UK'),
    (1004, 'Charles de Gaulle', 'Paris', 'France'),
    (1005, 'Changi Airport', 'Singapore', 'Singapore'),
    (1006, 'Dubai International', 'Dubai', 'UAE'),
    (1007, 'Sydney Airport', 'Sydney', 'Australia'),
    (1008, 'Tokyo Narita', 'Tokyo', 'Japan'),
    (1009, 'Berlin Brandenburg', 'Berlin', 'Germany'),
    (1010, 'Hong Kong International', 'Hong Kong', 'China')
]

# Sample data for pilots
pilots = [
    (1234, 'Alice', 'Johnson', 'A123456'),
    (5678, 'Emma', 'Williams', 'E234567'),
    (9101, 'Olivia', 'Brown', 'O345678'),
    (1122, 'Sophia', 'Jones', 'S456789'),
    (3344, 'Isabella', 'Miller', 'I567890'),
    (5566, 'Mia', 'Davis', 'M678901'),
    (7788, 'Amelia', 'Martinez', 'A789012'),
    (9900, 'Harper', 'Garcia', 'H890123'),
    (2233, 'Evelyn', 'Rodriguez', 'E901234'),
    (4455, 'Abigail', 'Hernandez', 'A012345')
]

# Sample data for Flights
flights = [
    (2001, 'AA123', '2025-04-25 10:00', '2025-04-25 14:00', 'On Time', 1234, 1001, 1002),
    (2002, 'BA456', '2025-04-26 11:00', '2025-04-26 15:00', 'Delayed', 5678, 1002, 1003),
    (2003, 'AF789', '2025-04-27 09:00', '2025-04-27 13:00', 'On Time', 9101, 1003, 1004),
    (2004, 'SQ101', '2025-04-28 12:00', '2025-04-28 16:00', 'Cancelled', 1122, 1004, 1005),
    (2005, 'DL202', '2025-04-29 13:00', '2025-04-29 17:00', 'On Time', 3344, 1001, 1005),
    (2006, 'UA303', '2025-05-01 07:00', '2025-05-01 11:00', 'On Time', 5566, 1006, 1007),
    (2007, 'LH404', '2025-05-02 08:00', '2025-05-02 12:00', 'Delayed', 7788, 1007, 1008),
    (2008, 'AF505', '2025-05-03 10:00', '2025-05-03 14:00', 'On Time', 9900, 1008, 1009),
    (2009, 'AC606', '2025-05-04 14:00', '2025-05-04 18:00', 'Cancelled', 2233, 1009, 1010),
    (2010, 'VS707', '2025-05-05 15:00', '2025-05-05 19:00', 'On Time', 4455, 1001, 1006)
]

# Insert data
conn.executemany("INSERT INTO Airport (airportId, airportName, city, country) VALUES (?, ?, ?, ?)", airports)
conn.executemany("INSERT INTO Pilot (pilotId, firstName, lastName, licenseNumber) VALUES (?, ?, ?, ?)", pilots)
conn.executemany("INSERT INTO Flight (flightId, flightNumber, departureTime, arrivalTime, status, pilotId, departureAirportId, destinationAirportId) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", flights)

# Commit changes and close connection
conn.commit()
conn.close()

print("Sample data added successfully")
