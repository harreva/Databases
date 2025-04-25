**Description**

A flight management system using SQLite and Python as part of the DA MSc Computer Science Databases module. The database tracks important information such as pilots' details, airport locations, and flight schedules. The system is designed for easy data insertion and querying.

**Tables**

The system consists of three main tables:

**PILOT**

pilotId (PRIMARY KEY)
firstName
lastName
licenseNumber


**AIRPORT**

airportId (PRIMARY KEY)
airportName
city
country


**FLIGHT**

flightId (PRIMARY KEY)
flightNumber
departureTime
arrivalTime
status
pilotId (FOREIGN KEY to Pilot)
departureAirportId (FOREIGN KEY to Airport)
destinationAirportId (FOREIGN KEY to Airport)


**Setup
**
Clone this repository

run
python main.py

This will create the Flight_management.db SQLite database

run 
python sample_data.py 

This will fill the database with sample data (Sample data was created by chatGPT)

run 
commandLine_app.py 

This will start the command line application which allows you to interact with the database with a basic command line GUI.

sql_queries.py has SQL queries that have been used to help test the system. 

