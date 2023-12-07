"""
In this file you must implement all your database models.
If you need to use the methods from your database.py call them
statically. For instance:
       # opens a new connection to your database
       connection = Database.connect()
       # closes the previous connection to avoid memory leaks
       connection.close()
"""

from database import Database
from database import Query

class TestModel:
    """
    This is an object model example. Note that
    this model doesn't implement a DB connection.
    """

    def __init__(self, ctx):
        self.ctx = ctx
        self.author = ctx.message.author.name

    def response(self):
        return f'Hi, {self.author}. I am alive'





class UserModel:
    def __init__(self, user_id=None):
        self.user_id = user_id

    def create_user(self, username, email, weather_id):
        return Database.insert(Query.CREATE_USER, (username, email, weather_id))

    def read_user(self):
        return Database.select(Query.READ_USER, (self.user_id,))

    def update_user(self, username, email, weather_id):
        return Database.update(Query.UPDATE_USER, (username, email, weather_id, self.user_id))

    def delete_user(self):
        return Database.delete(Query.DELETE_USER, (self.user_id,))

class VehicleModel:
    def __init__(self, vehicle_id=None):
        self.vehicle_id = vehicle_id

    def create_vehicle(self, vehicle_type, vehicle_company, user_id):
        return Database.insert(Query.CREATE_VEHICLE, (vehicle_type, vehicle_company, user_id))

    def read_vehicle(self):
        return Database.select(Query.READ_VEHICLE, (self.vehicle_id,))

    def update_vehicle(self, vehicle_type, vehicle_company, user_id):
        return Database.update(Query.UPDATE_VEHICLE, (vehicle_type, vehicle_company, user_id, self.vehicle_id))

    def delete_vehicle(self):
        return Database.delete(Query.DELETE_VEHICLE, (self.vehicle_id,))

class WeatherModel:
    def __init__(self, weather_id=None):
        self.weather_id = weather_id

    def create_weather(self, humidity, temperature, pollution_index, wind_speed):
        return Database.insert(Query.CREATE_WEATHER, (humidity, temperature, pollution_index, wind_speed))

    def read_weather(self):
        return Database.select(Query.READ_WEATHER, (self.weather_id,))

    def update_weather(self, humidity, temperature, pollution_index, wind_speed):
        return Database.update(Query.UPDATE_WEATHER, (humidity, temperature, pollution_index, wind_speed, self.weather_id))

    def delete_weather(self):
        return Database.delete(Query.DELETE_WEATHER, (self.weather_id,))





class NotificationModel:
    def __init__(self, notification_id=None):
        self.notification_id = notification_id

    def create_notification(self, timestamp, notification_type):
        return Database.insert(Query.CREATE_NOTIFICATION, (self.notification_id, timestamp, notification_type))

    def read_notification(self):
        return Database.select(Query.READ_NOTIFICATION, (self.notification_id,))

    def update_notification(self, timestamp, notification_type):
        return Database.update(Query.UPDATE_NOTIFICATION, (timestamp, notification_type, self.notification_id))

    def delete_notification(self):
        return Database.delete(Query.DELETE_NOTIFICATION, (self.notification_id,))

    def get_most_recent_notification(self):
      return Database.select(Query.GET_MOST_RECENT_NOTIFICATION)


class MailingListModel:
    def __init__(self, mailing_id=None):
        self.mailing_id = mailing_id

    def create_mailing_list_info(self, address):
        return Database.insert(Query.CREATE_MAILING_LIST_INFO, (address,))

    def read_mailing_list_info(self):
        return Database.select(Query.READ_MAILING_LIST_INFO, (self.mailing_id,))

    def update_mailing_list_info(self, address):
        return Database.update(Query.UPDATE_MAILING_LIST_INFO, (address, self.mailing_id))

    def delete_mailing_list_info(self):
        return Database.delete(Query.DELETE_MAILING_LIST_INFO, (self.mailing_id,))

class RouteModel:
    def __init__(self, route_id=None):
        self.route_id = route_id

    def create_route(self, distance, route_name):
        return Database.insert(Query.CREATE_ROUTE, (self.route_id, distance, route_name))

    def read_route(self):
        return Database.select(Query.READ_ROUTE, (self.route_id,))

    def update_route(self, distance, route_name):
        return Database.update(Query.UPDATE_ROUTE, (distance, route_name, self.route_id))

    def delete_route(self):
        return Database.delete(Query.DELETE_ROUTE, (self.route_id,))

class TripSharingModel:
    def __init__(self, trip_sharing_id=None):
        self.trip_sharing_id = trip_sharing_id

    def create_trip_sharing(self):
        return Database.insert(Query.CREATE_TRIP_SHARING, (self.trip_sharing_id,))

    def read_trip_sharing(self):
        return Database.select(Query.READ_TRIP_SHARING, (self.trip_sharing_id,))

    def delete_trip_sharing(self):
        return Database.delete(Query.DELETE_TRIP_SHARING, (self.trip_sharing_id,))






class StationsModel:
    def __init__(self, station_id=None):
        self.station_id = station_id

    def create_station(self, station_name, station_location, station_type):
        return Database.insert(Query.CREATE_STATIONS, (self.station_id, station_name, station_location, station_type))

    def read_station(self):
        return Database.select(Query.READ_STATIONS, (self.station_id,))

    def update_station(self, station_name, station_location, station_type):
        return Database.update(Query.UPDATE_STATIONS, (station_name, station_location, station_type, self.station_id))

    def delete_station(self):
        return Database.delete(Query.DELETE_STATIONS, (self.station_id,))

class ChargingStationModel:
    def __init__(self, stations_station_id=None):
        self.stations_station_id = stations_station_id

    def create_charging_station(self, station_name, station_location, charging_units):
        return Database.insert(Query.CREATE_CHARGING_STATION, (station_name, station_location, charging_units, self.stations_station_id))

    def read_charging_station(self):
        return Database.select(Query.READ_CHARGING_STATION, (self.stations_station_id,))

    def update_charging_station(self, station_name, station_location, charging_units):
        return Database.update(Query.UPDATE_CHARGING_STATION, (station_name, station_location, charging_units, self.stations_station_id))

    def delete_charging_station(self):
        return Database.delete(Query.DELETE_CHARGING_STATION, (self.stations_station_id,))

class FuelingStationModel:
    def __init__(self, stations_station_id=None):
        self.stations_station_id = stations_station_id

    def create_fueling_station(self, station_name, station_location):
        return Database.insert(Query.CREATE_FUELING_STATION, (station_name, station_location, self.stations_station_id))

    def read_fueling_station(self):
        return Database.select(Query.READ_FUELING_STATION, (self.stations_station_id,))

    def update_fueling_station(self, station_name, station_location):
        return Database.update(Query.UPDATE_FUELING_STATION, (station_name, station_location, self.stations_station_id))

    def delete_fueling_station(self):
        return Database.delete(Query.DELETE_FUELING_STATION, (self.stations_station_id,))

    
      

    def find_by_zipcode(self, zipcode):
      query = Query.FIND_FUEL_STATIONS  
      return Database.select(query, (f"%{zipcode}%",))
     


class RegionsModel:
    def __init__(self, region_id=None):
        self.region_id = region_id

    def create_region(self, region_radius, coordinates):
        return Database.insert(Query.CREATE_REGIONS, (self.region_id, region_radius, coordinates))

    def read_region(self):
        return Database.select(Query.READ_REGIONS, (self.region_id,))

    def update_region(self, region_radius, coordinates):
        return Database.update(Query.UPDATE_REGIONS, (region_radius, coordinates, self.region_id))

    def delete_region(self):
        return Database.delete(Query.DELETE_REGIONS, (self.region_id,))




class EnvironmentalImpactModel:
    def __init__(self, impact_id=None):
        self.impact_id = impact_id

    def create_environmental_impact(self, date):
        return Database.insert(Query.CREATE_ENVIRONMENTAL_IMPACT, (self.impact_id, date))

    def read_environmental_impact(self):
        return Database.select(Query.READ_ENVIRONMENTAL_IMPACT, (self.impact_id,))

    def update_environmental_impact(self, date):
        return Database.update(Query.UPDATE_ENVIRONMENTAL_IMPACT, (date, self.impact_id))

    def delete_environmental_impact(self):
        return Database.delete(Query.DELETE_ENVIRONMENTAL_IMPACT, (self.impact_id,))

class CityModel:
    def __init__(self, regions_region_id=None):
        self.regions_region_id = regions_region_id

    def create_city(self, city_name, city_area, environmental_impact_id, weather_id):
        return Database.insert(Query.CREATE_CITY, (city_name, city_area, self.regions_region_id, environmental_impact_id, weather_id))

    def read_city(self):
        return Database.select(Query.READ_CITY, (self.regions_region_id,))

    def update_city(self, city_name, city_area, environmental_impact_id, weather_id):
        return Database.update(Query.UPDATE_CITY, (city_name, city_area, environmental_impact_id, weather_id, self.regions_region_id))

    def delete_city(self):
        return Database.delete(Query.DELETE_CITY, (self.regions_region_id,))


      
        
    def get_avg_weather_by_city():
        query = Query.GET_AVG_WEATHER_BY_CITY
        return Database.select(query)


class EmissionModel:
    def __init__(self, emission_id=None):
        self.emission_id = emission_id

    def create_emission(self, fuel_type, carbon_emission, pollution_index, vehicle_id):
        return Database.insert(Query.CREATE_EMISSION, (fuel_type, carbon_emission, pollution_index, vehicle_id))

    def read_emission(self):
        return Database.select(Query.READ_EMISSION, (self.emission_id,))

    def update_emission(self, fuel_type, carbon_emission, pollution_index):
        return Database.update(Query.UPDATE_EMISSION, (fuel_type, carbon_emission, pollution_index, self.emission_id))

    def delete_emission(self):
        return Database.delete(Query.DELETE_EMISSION, (self.emission_id,))

class CampaignModel:
    def __init__(self, campaign_id=None):
        self.campaign_id = campaign_id

    def create_campaign(self, date, campaign_type, campaign_name):
        return Database.insert(Query.CREATE_CAMPAIGN, (self.campaign_id, date, campaign_type, campaign_name))

    def read_campaign(self):
        return Database.select(Query.READ_CAMPAIGN, (self.campaign_id,))

    def update_campaign(self, date, campaign_type, campaign_name):
        return Database.update(Query.UPDATE_CAMPAIGN, (date, campaign_type, campaign_name, self.campaign_id))

    def delete_campaign(self):
        return Database.delete(Query.DELETE_CAMPAIGN, (self.campaign_id,))


class CompanyModel:
    def __init__(self, company_id=None):
        self.company_id = company_id

    def create_company(self, company_name, vehicle_count, market_cap):
        return Database.insert(Query.CREATE_COMPANY, (company_name, vehicle_count, market_cap))

    def read_company(self):
        return Database.select(Query.READ_COMPANY, (self.company_id,))

    def update_company(self, company_name, vehicle_count, market_cap):
        return Database.update(Query.UPDATE_COMPANY, (company_name, vehicle_count, market_cap, self.company_id))

    def delete_company(self):
        return Database.delete(Query.DELETE_COMPANY, (self.company_id,))


class ContractsModel:
    def __init__(self, contract_id=None):
        self.contract_id = contract_id

    def create_contract(self, date, contract_name, contract_type):
        return Database.insert(Query.CREATE_CONTRACTS, (date, contract_name, contract_type))

    def read_contract(self):
        return Database.select(Query.READ_CONTRACTS, (self.contract_id,))

    def update_contract(self, date, contract_name, contract_type):
        return Database.update(Query.UPDATE_CONTRACTS, (date, contract_name, contract_type, self.contract_id))

    def delete_contract(self):
        return Database.delete(Query.DELETE_CONTRACTS, (self.contract_id,))


class MaintenanceModel:
    def __init__(self, maintenance_id=None):
        self.maintenance_id = maintenance_id

    def create_maintenance(self, maintenance_name, vehicle_user_user_id):
        return Database.insert(Query.CREATE_MAINTENANCE, (maintenance_name, vehicle_user_user_id))

    def read_maintenance(self):
        return Database.select(Query.READ_MAINTENANCE, (self.maintenance_id,))

    def update_maintenance(self, maintenance_name, vehicle_user_user_id):
        return Database.update(Query.UPDATE_MAINTENANCE, (maintenance_name, vehicle_user_user_id, self.maintenance_id))

    def delete_maintenance(self):
        return Database.delete(Query.DELETE_MAINTENANCE, (self.maintenance_id,))








class AccountModel:
    def __init__(self, user_user_id=None):
        self.user_user_id = user_user_id

    def create_account(self, phone_number, email, account_name, company_company_id):
        return Database.insert(Query.CREATE_ACCOUNT, (phone_number, email, account_name, self.user_user_id, company_company_id))

    def read_account(self):
        return Database.select(Query.READ_ACCOUNT, (self.user_user_id,))

    def update_account(self, phone_number, email, account_name, company_company_id):
        return Database.update(Query.UPDATE_ACCOUNT, (phone_number, email, account_name, company_company_id, self.user_user_id))

    def delete_account(self):
        return Database.delete(Query.DELETE_ACCOUNT, (self.user_user_id,))





class PaymentMethodModel:
    def __init__(self, payment_id=None):
        self.payment_id = payment_id

    def create_payment_method(self, payment_type, payment_timestamp, stations_station_id, maintenance_maintenance_id):
        return Database.insert(Query.CREATE_PAYMENT_METHOD, (payment_type, payment_timestamp, stations_station_id, maintenance_maintenance_id))

    def read_payment_method(self):
        return Database.select(Query.READ_PAYMENT_METHOD, (self.payment_id,))

    def update_payment_method(self, payment_type, payment_timestamp, stations_station_id, maintenance_maintenance_id):
        return Database.update(Query.UPDATE_PAYMENT_METHOD, (payment_type, payment_timestamp, stations_station_id, maintenance_maintenance_id, self.payment_id))

    def delete_payment_method(self):
        return Database.delete(Query.DELETE_PAYMENT_METHOD, (self.payment_id,))




class BankAccountModel:
    def __init__(self, payment_method_payment_id=None):
        self.payment_method_payment_id = payment_method_payment_id

    def create_bank_account(self, account_number, bank_name, area_code):
        return Database.insert(Query.CREATE_BANK_ACCOUNT, (account_number, bank_name, area_code, self.payment_method_payment_id))

    def read_bank_account(self):
        return Database.select(Query.READ_BANK_ACCOUNT, (self.payment_method_payment_id,))

    def update_bank_account(self, account_number, bank_name, area_code):
        return Database.update(Query.UPDATE_BANK_ACCOUNT, (account_number, bank_name, area_code, self.payment_method_payment_id))

    def delete_bank_account(self):
        return Database.delete(Query.DELETE_BANK_ACCOUNT, (self.payment_method_payment_id,))




class PayPalModel:
    def __init__(self, payment_method_payment_id=None):
        self.payment_method_payment_id = payment_method_payment_id

    def create_paypal(self, paypal_account, paypal_username, timestamp):
        return Database.insert(Query.CREATE_PAYPAL, (paypal_account, paypal_username, timestamp, self.payment_method_payment_id))

    def read_paypal(self):
        return Database.select(Query.READ_PAYPAL, (self.payment_method_payment_id,))

    def update_paypal(self, paypal_account, paypal_username, timestamp):
        return Database.update(Query.UPDATE_PAYPAL, (paypal_account, paypal_username, timestamp, self.payment_method_payment_id))

    def delete_paypal(self):
        return Database.delete(Query.DELETE_PAYPAL, (self.payment_method_payment_id,))




class CryptoWalletModel:
    def __init__(self, payment_method_payment_id=None):
        self.payment_method_payment_id = payment_method_payment_id

    def create_crypto_wallet(self, wallet_address, amount, crypto_type):
        return Database.insert(Query.CREATE_CRYPTO_WALLET, (wallet_address, amount, crypto_type, self.payment_method_payment_id))

    def read_crypto_wallet(self):
        return Database.select(Query.READ_CRYPTO_WALLET, (self.payment_method_payment_id,))

    def update_crypto_wallet(self, wallet_address, amount, crypto_type):
        return Database.update(Query.UPDATE_CRYPTO_WALLET, (wallet_address, amount, crypto_type, self.payment_method_payment_id))

    def delete_crypto_wallet(self):
        return Database.delete(Query.DELETE_CRYPTO_WALLET, (self.payment_method_payment_id,))



class CreditCardModel:
    def __init__(self, bank_account_payment_method_payment_id=None):
        self.bank_account_payment_method_payment_id = bank_account_payment_method_payment_id

    def create_credit_card(self, card_number, card_name, bank_name):
        return Database.insert(Query.CREATE_CREDIT_CARD, (card_number, card_name, bank_name, self.bank_account_payment_method_payment_id))

    def read_credit_card(self):
        return Database.select(Query.READ_CREDIT_CARD, (self.bank_account_payment_method_payment_id,))

    def update_credit_card(self, card_number, card_name, bank_name):
        return Database.update(Query.UPDATE_CREDIT_CARD, (card_number, card_name, bank_name, self.bank_account_payment_method_payment_id))

    def delete_credit_card(self):
        return Database.delete(Query.DELETE_CREDIT_CARD, (self.bank_account_payment_method_payment_id,))



class DebitCardModel:
    def __init__(self, bank_account_payment_method_payment_id=None):
        self.bank_account_payment_method_payment_id = bank_account_payment_method_payment_id

    def create_debit_card(self, card_number, card_name, bank_name, payment_id):
        return Database.insert(Query.CREATE_DEBIT_CARD, (card_number, card_name, bank_name, payment_id, self.bank_account_payment_method_payment_id))

    def read_debit_card(self):
        return Database.select(Query.READ_DEBIT_CARD, (self.bank_account_payment_method_payment_id,))

    def update_debit_card(self, card_number, card_name, bank_name, payment_id):
        return Database.update(Query.UPDATE_DEBIT_CARD, (card_number, card_name, bank_name, payment_id, self.bank_account_payment_method_payment_id))

    def delete_debit_card(self):
        return Database.delete(Query.DELETE_DEBIT_CARD, (self.bank_account_payment_method_payment_id,))



class MailingListInfoHasUserModel:
    def __init__(self, mailing_id=None, user_id=None):
        self.mailing_id = mailing_id
        self.user_id = user_id

    def create_relation(self):
        return Database.insert(Query.CREATE_MAILING_LIST_INFO_HAS_USER, (self.mailing_id, self.user_id))

    def read_relation(self):
        return Database.select(Query.READ_MAILING_LIST_INFO_HAS_USER, (self.mailing_id,))

    def delete_relation(self):
        return Database.delete(Query.DELETE_MAILING_LIST_INFO_HAS_USER, (self.mailing_id,))





class CompanyHasCampaignModel:
    def __init__(self, company_id=None, campaign_id=None):
        self.company_id = company_id
        self.campaign_id = campaign_id

    def create_company_campaign(self):
        return Database.insert(Query.CREATE_COMPANY_HAS_CAMPAIGN, (self.company_id, self.campaign_id))

    def read_company_campaign(self):
        return Database.select(Query.READ_COMPANY_HAS_CAMPAIGN, (self.company_id,))

    def delete_company_campaign(self):
        return Database.delete(Query.DELETE_COMPANY_HAS_CAMPAIGN, (self.company_id,))


class RouteHasVehicleModel:
    def __init__(self, route_id=None, vehicle_user_user_id=None):
        self.route_id = route_id
        self.vehicle_user_user_id = vehicle_user_user_id

    def create_route_vehicle(self):
        return Database.insert(Query.CREATE_ROUTE_HAS_VEHICLE, (self.route_id, self.vehicle_user_user_id))

    def read_route_vehicle(self):
        return Database.select(Query.READ_ROUTE_HAS_VEHICLE, (self.route_id,))

    def delete_route_vehicle(self):
        return Database.delete(Query.DELETE_ROUTE_HAS_VEHICLE, (self.route_id,))

class NotificationsHasUserModel:
    def __init__(self, notification_id=None, user_id=None):
        self.notification_id = notification_id
        self.user_id = user_id

    def create_notification_user(self):
        return Database.insert(Query.CREATE_NOTIFICATIONS_HAS_USER, (self.notification_id, self.user_id))

    def read_notification_user(self):
        return Database.select(Query.READ_NOTIFICATIONS_HAS_USER, (self.notification_id,))

    def delete_notification_user(self):
        return Database.delete(Query.DELETE_NOTIFICATIONS_HAS_USER, (self.notification_id,))






class EmissionHasEnvironmentalImpactModel:
    def __init__(self, emission_id=None, impact_id=None):
        self.emission_id = emission_id
        self.impact_id = impact_id

    def create_emission_impact(self):
        return Database.insert(Query.CREATE_EMISSION_HAS_ENVIRONMENTAL_IMPACT, (self.emission_id, self.impact_id))

    def read_emission_impact(self):
        return Database.select(Query.READ_EMISSION_HAS_ENVIRONMENTAL_IMPACT, (self.emission_id,))

    def delete_emission_impact(self):
        return Database.delete(Query.DELETE_EMISSION_HAS_ENVIRONMENTAL_IMPACT, (self.emission_id,))




class UserHasTripSharingModel:
    def __init__(self, user_id=None, trip_sharing_id=None):
        self.user_id = user_id
        self.trip_sharing_id = trip_sharing_id

    def create_user_trip_sharing(self):
        return Database.insert(Query.CREATE_USER_HAS_TRIP_SHARING, (self.user_id, self.trip_sharing_id))

    def read_user_trip_sharing(self):
        return Database.select(Query.READ_USER_HAS_TRIP_SHARING, (self.user_id,))

    def delete_user_trip_sharing(self):
        return Database.delete(Query.DELETE_USER_HAS_TRIP_SHARING, (self.user_id,))


class CompanyHasContractsModel:
    def __init__(self, company_id=None, contract_id=None):
        self.company_id = company_id
        self.contract_id = contract_id

    def create_company_contract(self):
        return Database.insert(Query.CREATE_COMPANY_HAS_CONTRACTS, (self.company_id, self.contract_id))

    def read_company_contract(self):
        return Database.select(Query.READ_COMPANY_HAS_CONTRACTS, (self.company_id,))

    def delete_company_contract(self):
        return Database.delete(Query.DELETE_COMPANY_HAS_CONTRACTS, (self.company_id,))

