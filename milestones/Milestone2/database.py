import os
import pymysql.cursors

# Database configuration
db_host = os.environ["DB_HOST"]
db_username = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]
db_name = "Eco-Friendly-TransportationDB"


class Database:

  @staticmethod
  def connect():
    """
        Creates a connection with the database.
        """
    try:
      conn = pymysql.connect(host=db_host,
                             user=db_username,
                             password=db_password,
                             db=db_name,
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)
      print(f"Connected to database {db_name}")
      return conn
    except Exception as err:
      print(f"Connection error: {err}")
      return None

  @staticmethod
  def get_response(query, values=None, fetch=False, many_entities=False):
    """
        Executes the given SQL query with provided values.
        """
    response = None
    connection = Database.connect()
    if connection is None:
      print("Failed to connect to the database.")
      return response

    try:
      with connection.cursor() as cursor:
        cursor.execute(query, values)
        if fetch:
          response = cursor.fetchall() if many_entities else cursor.fetchone()
        else:
          connection.commit()
    except Exception as e:
      print(f"An error occurred: {e}")
    finally:
      if connection:
        connection.close()
    return response

  @staticmethod
  def select(query, values=None):
    """
        Executes a SELECT query.
        """
    return Database.get_response(query, values, fetch=True)

  @staticmethod
  def insert(query, values=None, many_entities=False):
    """
        Executes an INSERT query.
        """
    return Database.get_response(query, values, many_entities=many_entities)

  @staticmethod
  def update(query, values=None):
    """
        Executes an UPDATE query.
        """
    return Database.get_response(query, values)

  @staticmethod
  def delete(query, values=None):
    """
        Executes a DELETE query.
        """
    return Database.get_response(query, values)


class Query:
  CREATE_WEATHER = "INSERT INTO Weather (humidity, temperature, pollution_index, wind_speed) VALUES (%s, %s, %s, %s)"
  READ_WEATHER = "SELECT * FROM Weather WHERE weather_id = %s"
  UPDATE_WEATHER = "UPDATE Weather SET humidity = %s, temperature = %s, pollution_index = %s, wind_speed = %s WHERE weather_id = %s"
  DELETE_WEATHER = "DELETE FROM Weather WHERE weather_id = %s"

  # User Queries
  CREATE_USER = "INSERT INTO User (Username, email, Weather_weather_id) VALUES (%s, %s, %s)"
  READ_USER = "SELECT * FROM User WHERE User_id = %s"
  UPDATE_USER = "UPDATE User SET Username = %s, email = %s, Weather_weather_id = %s WHERE User_id = %s"
  DELETE_USER = "DELETE FROM User WHERE User_id = %s"

  # Vehicle Queries
  CREATE_VEHICLE = "INSERT INTO Vehicle (vehicle_type, vehicle_company, User_User_id) VALUES (%s, %s, %s)"
  READ_VEHICLE = "SELECT * FROM Vehicle WHERE vehicle_id = %s"
  UPDATE_VEHICLE = "UPDATE Vehicle SET vehicle_type = %s, vehicle_company = %s, User_User_id = %s WHERE vehicle_id = %s"
  DELETE_VEHICLE = "DELETE FROM Vehicle WHERE vehicle_id = %s"

  # Notifications Queries
  CREATE_NOTIFICATION = "INSERT INTO Notifications (notification_id, timestamp, type) VALUES (%s, %s, %s)"
  READ_NOTIFICATION = "SELECT * FROM Notifications WHERE notification_id = %s"
  UPDATE_NOTIFICATION = "UPDATE Notifications SET timestamp = %s, type = %s WHERE notification_id = %s"
  DELETE_NOTIFICATION = "DELETE FROM Notifications WHERE notification_id = %s"

  # Mailing List Info Queries
  CREATE_MAILING_LIST_INFO = "INSERT INTO `Mailing List Info` (address) VALUES (%s)"
  READ_MAILING_LIST_INFO = "SELECT * FROM `Mailing List Info` WHERE mailing_id = %s"
  UPDATE_MAILING_LIST_INFO = "UPDATE `Mailing List Info` SET address = %s WHERE mailing_id = %s"
  DELETE_MAILING_LIST_INFO = "DELETE FROM `Mailing List Info` WHERE mailing_id = %s"

  # Route Queries
  CREATE_ROUTE = "INSERT INTO Route (route_id, distance, route_name) VALUES (%s, %s, %s)"
  READ_ROUTE = "SELECT * FROM Route WHERE route_id = %s"
  UPDATE_ROUTE = "UPDATE Route SET distance = %s, route_name = %s WHERE route_id = %s"
  DELETE_ROUTE = "DELETE FROM Route WHERE route_id = %s"

  # Trip Sharing Queries
  CREATE_TRIP_SHARING = "INSERT INTO `Trip Sharing` (trip_sharing_id) VALUES (%s)"
  READ_TRIP_SHARING = "SELECT * FROM `Trip Sharing` WHERE trip_sharing_id = %s"
  DELETE_TRIP_SHARING = "DELETE FROM `Trip Sharing` WHERE trip_sharing_id = %s"

  # Stations Queries
  CREATE_STATIONS = "INSERT INTO Stations (station_id, station_name, station_location, `station type`) VALUES (%s, %s, %s, %s)"
  READ_STATIONS = "SELECT * FROM Stations WHERE station_id = %s"
  UPDATE_STATIONS = "UPDATE Stations SET station_name = %s, station_location = %s, `station type` = %s WHERE station_id = %s"
  DELETE_STATIONS = "DELETE FROM Stations WHERE station_id = %s"

  # Charging Station Queries
  CREATE_CHARGING_STATION = "INSERT INTO `Charging Station` (station_name, station_location, charging_units, Stations_station_id) VALUES (%s, %s, %s, %s)"
  READ_CHARGING_STATION = "SELECT * FROM `Charging Station` WHERE Stations_station_id = %s"
  UPDATE_CHARGING_STATION = "UPDATE `Charging Station` SET station_name = %s, station_location = %s, charging_units = %s WHERE Stations_station_id = %s"
  DELETE_CHARGING_STATION = "DELETE FROM `Charging Station` WHERE Stations_station_id = %s"

  # Fueling Station Queries
  CREATE_FUELING_STATION = "INSERT INTO `Fueling Station` (station_name, station_location, Stations_station_id) VALUES (%s, %s, %s)"
  READ_FUELING_STATION = "SELECT * FROM `Fueling Station` WHERE Stations_station_id = %s"
  UPDATE_FUELING_STATION = "UPDATE `Fueling Station` SET station_name = %s, station_location = %s WHERE Stations_station_id = %s"
  DELETE_FUELING_STATION = "DELETE FROM `Fueling Station` WHERE Stations_station_id = %s"

  # Regions Queries
  CREATE_REGIONS = "INSERT INTO Regions (region_id, region_radius, cooridnates) VALUES (%s, %s, %s)"
  READ_REGIONS = "SELECT * FROM Regions WHERE region_id = %s"
  UPDATE_REGIONS = "UPDATE Regions SET region_radius = %s, cooridnates = %s WHERE region_id = %s"
  DELETE_REGIONS = "DELETE FROM Regions WHERE region_id = %s"

  # Environmental Impact Queries
  CREATE_ENVIRONMENTAL_IMPACT = "INSERT INTO `Environmental Impact` (impact_id, date) VALUES (%s, %s)"
  READ_ENVIRONMENTAL_IMPACT = "SELECT * FROM `Environmental Impact` WHERE impact_id = %s"
  UPDATE_ENVIRONMENTAL_IMPACT = "UPDATE `Environmental Impact` SET date = %s WHERE impact_id = %s"
  DELETE_ENVIRONMENTAL_IMPACT = "DELETE FROM `Environmental Impact` WHERE impact_id = %s"

  # City Queries
  CREATE_CITY = "INSERT INTO City (city_name, city_area, Regions_region_id, `Environmental Impact_impact_id`, weather_id) VALUES (%s, %s, %s, %s, %s)"
  READ_CITY = "SELECT * FROM City WHERE Regions_region_id = %s"
  UPDATE_CITY = "UPDATE City SET city_name = %s, city_area = %s, `Environmental Impact_impact_id` = %s, weather_id = %s WHERE Regions_region_id = %s"
  DELETE_CITY = "DELETE FROM City WHERE Regions_region_id = %s"

  # Emission Queries
  CREATE_EMISSION = "INSERT INTO emission (fuel_tye, carbon_emission, pollution_index, Vehicle_vehicle_id) VALUES (%s, %s, %s, %s)"
  READ_EMISSION = "SELECT * FROM emission WHERE emission_id = %s"
  UPDATE_EMISSION = "UPDATE emission SET fuel_tye = %s, carbon_emission = %s, pollution_index = %s WHERE emission_id = %s"
  DELETE_EMISSION = "DELETE FROM emission WHERE emission_id = %s"

  # Campaign Queries
  CREATE_CAMPAIGN = "INSERT INTO Campaign (campaign, date, campaign_type, campaign_name) VALUES (%s, %s, %s, %s)"
  READ_CAMPAIGN = "SELECT * FROM Campaign WHERE campaign = %s"
  UPDATE_CAMPAIGN = "UPDATE Campaign SET date = %s, campaign_type = %s, campaign_name = %s WHERE campaign = %s"
  DELETE_CAMPAIGN = "DELETE FROM Campaign WHERE campaign = %s"

  # Company Queries
  CREATE_COMPANY = "INSERT INTO company (company_id, company_name, vehicle_count, market_cap) VALUES (%s, %s, %s, %s)"
  READ_COMPANY = "SELECT * FROM company WHERE company_id = %s"
  UPDATE_COMPANY = "UPDATE company SET company_name = %s, vehicle_count = %s, market_cap = %s WHERE company_id = %s"
  DELETE_COMPANY = "DELETE FROM company WHERE company_id = %s"

  # Contracts Queries
  CREATE_CONTRACTS = "INSERT INTO Contracts (contract_id, date, contract_name, contract_type) VALUES (%s, %s, %s, %s)"
  READ_CONTRACTS = "SELECT * FROM Contracts WHERE contract_id = %s"
  UPDATE_CONTRACTS = "UPDATE Contracts SET date = %s, contract_name = %s, contract_type = %s WHERE contract_id = %s"
  DELETE_CONTRACTS = "DELETE FROM Contracts WHERE contract_id = %s"

  # Maintenance Queries
  CREATE_MAINTENANCE = "INSERT INTO Maintenance (maintenance_id, maintenance_name, Vehicle_User_User_id) VALUES (%s, %s, %s)"
  READ_MAINTENANCE = "SELECT * FROM Maintenance WHERE maintenance_id = %s"
  UPDATE_MAINTENANCE = "UPDATE Maintenance SET maintenance_name = %s WHERE maintenance_id = %s"
  DELETE_MAINTENANCE = "DELETE FROM Maintenance WHERE maintenance_id = %s"

  # Account Queries
  CREATE_ACCOUNT = "INSERT INTO Account (phone_number, email, account_name, User_User_id, company_company_id) VALUES (%s, %s, %s, %s, %s)"
  READ_ACCOUNT = "SELECT * FROM Account WHERE User_User_id = %s"
  UPDATE_ACCOUNT = "UPDATE Account SET phone_number = %s, email = %s, account_name = %s, company_company_id = %s WHERE User_User_id = %s"
  DELETE_ACCOUNT = "DELETE FROM Account WHERE User_User_id = %s"

  # Payment Method Queries
  CREATE_PAYMENT_METHOD = "INSERT INTO `Payment Method` (payment_id, payment_type, payment_timestamp, Stations_station_id, Maintenence_maintenance_id) VALUES (%s, %s, %s, %s, %s)"
  READ_PAYMENT_METHOD = "SELECT * FROM `Payment Method` WHERE payment_id = %s"
  UPDATE_PAYMENT_METHOD = "UPDATE `Payment Method` SET payment_type = %s, payment_timestamp = %s, Stations_station_id = %s, Maintenence_maintenance_id = %s WHERE payment_id = %s"
  DELETE_PAYMENT_METHOD = "DELETE FROM `Payment Method` WHERE payment_id = %s"

  # Bank Account Queries
  CREATE_BANK_ACCOUNT = "INSERT INTO `Bank Account` (account_number, bank_name, area_code, `Payment Method_payment_id`) VALUES (%s, %s, %s, %s)"
  READ_BANK_ACCOUNT = "SELECT * FROM `Bank Account` WHERE `Payment Method_payment_id` = %s"
  UPDATE_BANK_ACCOUNT = "UPDATE `Bank Account` SET account_number = %s, bank_name = %s, area_code = %s WHERE `Payment Method_payment_id` = %s"
  DELETE_BANK_ACCOUNT = "DELETE FROM `Bank Account` WHERE `Payment Method_payment_id` = %s"

  # PayPal Queries
  CREATE_PAYPAL = "INSERT INTO Paypal (paypal_account, paypal_username, timestamp, `Payment Method_payment_id`) VALUES (%s, %s, %s, %s)"
  READ_PAYPAL = "SELECT * FROM Paypal WHERE `Payment Method_payment_id` = %s"
  UPDATE_PAYPAL = "UPDATE Paypal SET paypal_account = %s, paypal_username = %s, timestamp = %s WHERE `Payment Method_payment_id` = %s"
  DELETE_PAYPAL = "DELETE FROM Paypal WHERE `Payment Method_payment_id` = %s"

  # Crypto Wallet Queries
  CREATE_CRYPTO_WALLET = "INSERT INTO `Crypto wallet` (wallet_address, amount, crypto_type, `Payment Method_payment_id`) VALUES (%s, %s, %s, %s)"
  READ_CRYPTO_WALLET = "SELECT * FROM `Crypto wallet` WHERE `Payment Method_payment_id` = %s"
  UPDATE_CRYPTO_WALLET = "UPDATE `Crypto wallet` SET wallet_address = %s, amount = %s, crypto_type = %s WHERE `Payment Method_payment_id` = %s"
  DELETE_CRYPTO_WALLET = "DELETE FROM `Crypto wallet` WHERE `Payment Method_payment_id` = %s"

  CREATE_CREDIT_CARD = "INSERT INTO `Credit card` (card_number, card_name, bank_name, `Bank Account_Payment Method_payment_id`) VALUES (%s, %s, %s, %s)"
  READ_CREDIT_CARD = "SELECT * FROM `Credit card` WHERE `Bank Account_Payment Method_payment_id` = %s"
  UPDATE_CREDIT_CARD = "UPDATE `Credit card` SET card_number = %s, card_name = %s, bank_name = %s WHERE `Bank Account_Payment Method_payment_id` = %s"
  DELETE_CREDIT_CARD = "DELETE FROM `Credit card` WHERE `Bank Account_Payment Method_payment_id` = %s"

  # Debit Card Queries
  CREATE_DEBIT_CARD = "INSERT INTO `Debit card` (card_number, card_name, bank_name, payement_id, `Bank Account_Payment Method_payment_id`) VALUES (%s, %s, %s, %s, %s)"
  READ_DEBIT_CARD = "SELECT * FROM `Debit card` WHERE `Bank Account_Payment Method_payment_id` = %s"
  UPDATE_DEBIT_CARD = "UPDATE `Debit card` SET card_number = %s, card_name = %s, bank_name = %s, payement_id = %s WHERE `Bank Account_Payment Method_payment_id` = %s"
  DELETE_DEBIT_CARD = "DELETE FROM `Debit card` WHERE `Bank Account_Payment Method_payment_id` = %s"

  # Mailing List Info_has_User Queries
  CREATE_MAILING_LIST_INFO_HAS_USER = "INSERT INTO `Mailing List Info_has_User` (`Mailing List Info_mailing_id`, `User_User_id`) VALUES (%s, %s)"
  READ_MAILING_LIST_INFO_HAS_USER = "SELECT * FROM `Mailing List Info_has_User` WHERE `Mailing List Info_mailing_id` = %s"
  DELETE_MAILING_LIST_INFO_HAS_USER = "DELETE FROM `Mailing List Info_has_User` WHERE `Mailing List Info_mailing_id` = %s"

  # User_has_User_as_friends Queries
  CREATE_USER_HAS_USER_AS_FRIENDS = "INSERT INTO `User_has_User_as_friends` (`User_User_id`, `User_User_id1`) VALUES (%s, %s)"
  READ_USER_HAS_USER_AS_FRIENDS = "SELECT * FROM `User_has_User_as_friends` WHERE `User_User_id` = %s"
  DELETE_USER_HAS_USER_AS_FRIENDS = "DELETE FROM `User_has_User_as_friends` WHERE `User_User_id` = %s"

  # Company_has_Campaign Queries
  CREATE_COMPANY_HAS_CAMPAIGN = "INSERT INTO `company_has_Campaign` (`company_company_id`, `Campaign_campaign`) VALUES (%s, %s)"
  READ_COMPANY_HAS_CAMPAIGN = "SELECT * FROM `company_has_Campaign` WHERE `company_company_id` = %s"
  DELETE_COMPANY_HAS_CAMPAIGN = "DELETE FROM `company_has_Campaign` WHERE `company_company_id` = %s"

  # Route_has_Vehicle Queries
  CREATE_ROUTE_HAS_VEHICLE = "INSERT INTO `Route_has_Vehicle` (`Route_route_id`, `Vehicle_User_User_id`) VALUES (%s, %s)"
  READ_ROUTE_HAS_VEHICLE = "SELECT * FROM `Route_has_Vehicle` WHERE `Route_route_id` = %s"
  DELETE_ROUTE_HAS_VEHICLE = "DELETE FROM `Route_has_Vehicle` WHERE `Route_route_id` = %s"

  # Notifications_has_User Queries
  CREATE_NOTIFICATIONS_HAS_USER = "INSERT INTO `Notifications_has_User` (`Notifications_notification_id`, `User_User_id`) VALUES (%s, %s)"
  READ_NOTIFICATIONS_HAS_USER = "SELECT * FROM `Notifications_has_User` WHERE `Notifications_notification_id` = %s"
  DELETE_NOTIFICATIONS_HAS_USER = "DELETE FROM `Notifications_has_User` WHERE `Notifications_notification_id` = %s"

  # Emission_has_Environmental Impact Queries
  CREATE_EMISSION_HAS_ENVIRONMENTAL_IMPACT = "INSERT INTO `emission_has_Environmental Impact` (`emission_emission_id`, `Environmental Impact_impact_id`) VALUES (%s, %s)"
  READ_EMISSION_HAS_ENVIRONMENTAL_IMPACT = "SELECT * FROM `emission_has_Environmental Impact` WHERE `emission_emission_id` = %s"
  DELETE_EMISSION_HAS_ENVIRONMENTAL_IMPACT = "DELETE FROM `emission_has_Environmental Impact` WHERE `emission_emission_id` = %s"

  # User_has_Trip Sharing Queries
  CREATE_USER_HAS_TRIP_SHARING = "INSERT INTO `User_has_Trip Sharing` (`User_User_id`, `Trip Sharing_trip_sharing_id`) VALUES (%s, %s)"
  READ_USER_HAS_TRIP_SHARING = "SELECT * FROM `User_has_Trip Sharing` WHERE `User_User_id` = %s"
  DELETE_USER_HAS_TRIP_SHARING = "DELETE FROM `User_has_Trip Sharing` WHERE `User_User_id` = %s"

  # Company_has_Contracts Queries
  CREATE_COMPANY_HAS_CONTRACTS = "INSERT INTO `company_has_Contracts` (`company_company_id`, `Contracts_contract_id`) VALUES (%s, %s)"
  READ_COMPANY_HAS_CONTRACTS = "SELECT * FROM `company_has_Contracts` WHERE `company_company_id` = %s"
  DELETE_COMPANY_HAS_CONTRACTS = "DELETE FROM `company_has_Contracts` WHERE `company_company_id` = %s"


  GET_AVG_WEATHER_BY_CITY = """
SELECT City.city_name, AVG(Weather.temperature) AS avg_temp, AVG(Weather.humidity) AS avg_humidity
FROM City
INNER JOIN Weather ON City.weather_id = Weather.weather_id
GROUP BY City.city_name;
"""

#   GET_RECENT_NOTIFICATIONS = """
# SELECT type, COUNT(*) AS count 
# FROM Notifications 
# WHERE timestamp >= NOW() - INTERVAL 7 DAY 
# GROUP BY type;
# """

  GET_MOST_RECENT_NOTIFICATION = """
 SELECT type, COUNT(*) AS count 
 FROM Notifications 
 WHERE timestamp >= NOW() - INTERVAL 7 DAY 
 GROUP BY type
 ORDER BY timestamp DESC
 LIMIT 1;
 """
  FIND_FUEL_STATIONS = """
SELECT station_name, station_location
FROM `Fueling Station`
WHERE station_location LIKE %s;
      
"""



#I was not able to figure out python code to retrieve these commands in main.py, i am getting errors for type while using dictionaries so i just tried to work on all the sql queries. my bot is fully functional!

GET_MOST_RECENT_NOTIFICATION = """
SELECT type, COUNT(*) AS count
FROM Notifications
WHERE timestamp >= NOW() - INTERVAL 7 DAY
GROUP BY type
ORDER BY timestamp DESC
LIMIT 1;
"""

FIND_FUEL_STATIONS = """
SELECT station_name, station_location
FROM `Fueling Station`
JOIN Stations ON `Fueling Station`.Stations_station_id = Stations.station_id
WHERE Stations.station_location LIKE %s;
"""

RETRIEVE_ALL_PAYMENTS = """
SELECT `Payment Method`.payment_type, `Payment Method`.payment_timestamp
FROM `Payment Method`
JOIN Stations ON `Payment Method`.Stations_station_id = Stations.station_id
WHERE Stations.station_name = %s;
"""

INSERT_NEW_USER = """
INSERT INTO User (Username, email, Weather_weather_id) VALUES (%s, %s, %s);
INSERT INTO Vehicle (vehicle_type, vehicle_company, User_User_id) VALUES (%s, %s, LAST_INSERT_ID());
"""

INSERT_NEW_MAINTENANCE_RECORD = """
INSERT INTO Maintenance (maintenance_name, Vehicle_User_User_id)
SELECT %s, v.User_User_id
FROM Vehicle v
WHERE v.vehicle_type = %s;
"""

UPDATE_USER_CONTACT_INFO = """
UPDATE User SET email = %s, Username = %s WHERE User_id = %s;
UPDATE `Mailing List Info` m
JOIN User u ON m.mailing_id = u.Mailing_MailingId
SET m.address = %s
WHERE u.User_id = %s;
"""

UPDATE_CONTRACT_DETAILS = """
UPDATE Contracts c
JOIN company_has_Contracts cc ON c.contract_id = cc.Contracts_contract_id
SET c.contract_name = %s, c.contract_type = %s
WHERE cc.company_company_id = %s;
"""

DELETE_USER_ACCOUNT = """
DELETE FROM User WHERE User_id = %s;
"""

DELETE_SHARED_TRIP_RECORD = """
DELETE FROM `Trip Sharing` WHERE trip_sharing_id = %s;
"""

CREATE_TRIGGER_TRIP_SHARING_NOTIFICATION = """
CREATE TRIGGER TriggerOnTripSharing
AFTER INSERT ON `User_has_Trip Sharing`
FOR EACH ROW
BEGIN
 INSERT INTO Notifications (notification_id, timestamp, type)
 VALUES (NEW.User_User_id, NOW(), 'Trip Sharing Participation');
END;
"""

CREATE_TRIGGER_ON_NEW_EMISSION_TYPE = """
CREATE TRIGGER TriggerOnNewEmissionType
AFTER INSERT ON emission
FOR EACH ROW
BEGIN
 -- Update Environmental Impact logic here
END;
"""

GET_VEHICLE_MAINTENANCE_HISTORY = """
CREATE PROCEDURE GetVehicleMaintenanceHistory(IN vehicle_id INT)
BEGIN
 SELECT maintenance_name, date
 FROM Maintenance
 WHERE Vehicle_User_User_id = vehicle_id;
END;
"""

CALCULATE_TRIPS_PER_VEHICLE_TYPE = """
CREATE FUNCTION CalculateTripsPerVehicleType(User_id INT)
RETURNS TABLE
BEGIN
 RETURN SELECT vehicle_type, COUNT(*) as trip_count
 FROM Vehicle v
 JOIN `Route_has_Vehicle` rv ON v.vehicle_id = rv.Vehicle_User_User_id
 WHERE v.User_User_id = User_id
 GROUP BY vehicle_type;
END;
"""

CALCULATE_USER_AVG_POLLUTION_INDEX = """
CREATE FUNCTION CalculateUserAvgPollutionIndex(User_id INT)
RETURNS DECIMAL(10,2)
BEGIN
 DECLARE avg_pollution DECIMAL(10,2);
 SELECT AVG(e.pollution_index) INTO avg_pollution
 FROM emission e
 JOIN Vehicle v ON e.Vehicle_vehicle_id = v.vehicle_id
 WHERE v.User_User_id = User_id;
 RETURN avg_pollution;
END;
"""

