-- Insert data into Weather table
INSERT INTO `Weather` (`weather_id`, `humidity`, `temperature`, `pollution_index`, `wind_speed`) VALUES
(1, 70, 25.5, 40, 15.2),
(2, 65, 23.8, 42, 14.5),
(3, 68, 24.3, 38, 16.0);


-- Insert data into User table
INSERT INTO `User` (`User_id`, `Username`, `email`, `Weather_weather_id`) VALUES
(1, 'User1', 'user1@email.com', 1),
(2, 'User2', 'user2@email.com', 2),
(3, 'User3', 'user3@email.com', 3);



-- Insert data into Vehicle table
INSERT INTO `Vehicle` (`vehicle_id`, `vehicle_type`, `vehicle_company`, `User_User_id`) VALUES
(1, 'Car', 'Company1', 1),
(2, 'Bike', 'Company2', 2),
(3, 'Scooter', 'Company3', 3);


-- Insert data into Notifications table
INSERT INTO `Notifications` (`notification_id`, `timestamp`, `type`) VALUES
(1, '2023-10-25 12:00:00', 'Alert'),
(2, '2023-10-25 13:30:00', 'Notification'),
(3, '2023-10-26 10:15:00', 'Reminder');

-- Insert data into Mailing List Info table
INSERT INTO `Mailing List Info` (`mailing_id`, `address`) VALUES
(1, 'address1'),
(2, 'address2'),
(3, 'address3');

-- Insert data into Route table
INSERT INTO `Route` (`route_id`, `distance`, `route_name`) VALUES
(1, 50.5, 'Route1'),
(2, 35.7, 'Route2'),
(3, 42.2, 'Route3');


-- Insert data into Trip Sharing table
INSERT INTO `Trip Sharing` (`trip_sharing_id`) VALUES
(1),
(2),
(3);

-- Insert data into Stations table
INSERT INTO `Stations` (`station_id`, `station_name`, `station_location`, `station type`) VALUES
(1, 'Station1', 'Location1', 'Type1'),
(2, 'Station2', 'Location2', 'Type2'),
(3, 'Station3', 'Location3', 'Type3');

-- Insert data into Charging Station table
INSERT INTO `Charging Station` (`station_name`, `station_location`, `charging_units`, `Stations_station_id`) VALUES
(1, 'ChargingLocation1', 10, 1),
(2, 'ChargingLocation2', 8, 2),
(3, 'ChargingLocation3', 12, 3);


-- Insert data into Fueling Station table
INSERT INTO `Fueling Station` (`station_name`, `station_location`, `Stations_station_id`) VALUES
('FuelingLocation1', 'Location1', 1),
('FuelingLocation2', 'Location2', 2),
('FuelingLocation3', 'Location3', 3);

-- Insert data into Regions table
INSERT INTO `Regions` (`region_id`, `region_radius`, `cooridnates`) VALUES
(1, 10.5, 'Coordinates1'),
(2, 8.7, 'Coordinates2'),
(3, 12.3, 'Coordinates3');

-- Insert data into Environmental Impact table
INSERT INTO `Environmental Impact` (`impact_id`, `date`) VALUES
(1, '2023-10-25 14:00:00'),
(2, '2023-10-26 15:30:00'),
(3, '2023-10-27 12:45:00');



-- Insert data into City table
INSERT INTO `City` (`city_name`, `city_area`, `Regions_region_id`, `Environmental Impact_impact_id`) VALUES
('City1', 100.5, 1, 1),
('City2', 85.7, 2, 2),
('City3', 120.3, 3, 3);


-- Insert data into emission table
INSERT INTO `emission` (`emission_id`, `fuel_tye`, `carbon_emission`, `pollution_index`, `Vehicle_vehicle_id`) VALUES
(1, 'Gasoline', 50.2, 30.5, 1),
(2, 'Electric', 10.3, 5.2, 2),
(3, 'Diesel', 60.8, 35.7, 3);


-- Insert data into Campaign table
INSERT INTO `Campaign` (`campaign`, `date`, `campaign_type`, `campaign_name`) VALUES
(1, '2023-10-25 16:00:00', 'Promotion', 'Campaign1'),
(2, '2023-10-26 14:30:00', 'Awareness', 'Campaign2'),
(3, '2023-10-27 11:15:00', 'Charity', 'Campaign3');

-- Insert data into company table
INSERT INTO `company` (`company_id`, `company_name`, `vehicle_count`, `market_cap`) VALUES
(1, 'Company1', 100, 500000.00),
(2, 'Company2', 75, 400000.00),
(3, 'Company3', 120, 600000.00);


-- Insert data into Contracts table
INSERT INTO `Contracts` (`contract_id`, `date`, `contract_name`, `contract_type`) VALUES
(1, '2023-10-25 16:30:00', 'Contract1', 'Service'),
(2, '2023-10-26 14:45:00', 'Contract2', 'Maintenance'),
(3, '2023-10-27 11:30:00', 'Contract3', 'Lease');

-- Insert data into Maintenence table
INSERT INTO `Maintenence` (`maintenance_id`, `maintenance_name`, `Vehicle_User_User_id`) VALUES
(1, 'Maintenance1', 1),
(2, 'Maintenance2', 2),
(3, 'Maintenance3', 3);


-- Insert data into Account table
INSERT INTO `Account` (`phone_number`, `email`, `account_name`, `User_User_id`, `company_company_id`) VALUES
(123456789, 'account1@email.com', 'Account1', 1, 1),
(234567890, 'account2@email.com', 'Account2', 2, 2),
(345678901, 'account3@email.com', 'Account3', 3, 3);

-- Insert data into Payment Method table
INSERT INTO `Payment Method` (`payment_id`, `payment_type`, `payment_timestamp`, `Stations_station_id`, `Maintenence_maintenance_id`) VALUES
(1, 'Credit Card', '2023-10-25 17:00:00', 1, 1),
(2, 'Paypal', '2023-10-26 15:45:00', 2, 2),
(3, 'Crypto Wallet', '2023-10-27 12:30:00', 3, 3);


-- Insert data into Bank Account table
INSERT INTO `Bank Account` (`account_number`, `bank_name`, `area_code`, `Payment Method_payment_id`) VALUES
('12345678', 'Bank1', 'Area1', 1),
('23456789', 'Bank2', 'Area2', 2),
('34567890', 'Bank3', 'Area3', 3);


-- Insert data into Paypal table
INSERT INTO `Paypal` (`paypal_account`, `paypal_username`, `timestamp`, `Payment Method_payment_id`) VALUES
('PaypalAccount1', 'Username1', '2023-10-25 17:30:00', 1),
('PaypalAccount2', 'Username2', '2023-10-26 16:15:00', 2),
('PaypalAccount3', 'Username3', '2023-10-27 13:00:00', 3);


-- Insert data into Crypto wallet table
INSERT INTO `Crypto wallet` (`wallet_address`, `amount`, `crypto_type`, `Payment Method_payment_id`) VALUES
(12345, 5000.00, 'Bitcoin', 1),
(23456, 8000.00, 'Ethereum', 2),
(34567, 7000.00, 'Litecoin', 3);

-- Insert data into Credit card table
INSERT INTO `Credit card` (`card_number`, `card_name`, `bank_name`, `Bank Account_Payment Method_payment_id`) VALUES
(98765432, 'Card1', 'Bank1', 1),
(87654321, 'Card2', 'Bank2', 2),
(76543210, 'Card3', 'Bank3', 3);


-- Insert data into Debit card table
INSERT INTO `Debit card` (`card_number`, `card_name`, `bank_name`, `Bank Account_Payment Method_payment_id`) VALUES
(55554444, 'Card4', 'Bank1', 1),
(44443333, 'Card5', 'Bank2', 2),
(33332222, 'Card6', 'Bank3', 3);


-- Insert data into Mailing List Info_has_User table
INSERT INTO `Mailing List Info_has_User` (`Mailing List Info_mailing_id`, `User_User_id`) VALUES
(1, 1),
(2, 2),
(3, 3);


-- Insert data into User_has_User_as_friends table
INSERT INTO `User_has_User_as_friends` (`User_User_id`, `User_User_id1`) VALUES
(1, 2),
(2, 3),
(3, 1);


-- Insert data into company_has_Campaign table
INSERT INTO `company_has_Campaign` (`company_company_id`, `Campaign_campaign`) VALUES
(1, 1),
(2, 2),
(3, 3);


-- Insert data into Route_has_Vehicle table
INSERT INTO `Route_has_Vehicle` (`Route_route_id`, `Vehicle_User_User_id`) VALUES
(1, 1),
(2, 2),
(3, 3);


-- Insert data into Notifications_has_User table
INSERT INTO `Notifications_has_User` (`Notifications_notification_id`, `User_User_id`) VALUES
(1, 1),
(2, 2),
(3, 3);

-- Insert data into company_has_Contracts table

INSERT INTO `Eco-Friendly-TransportationDB`.`company_has_Contracts` (`company_company_id`, `Contracts_contract_id`) VALUES (2, 2);
INSERT INTO `Eco-Friendly-TransportationDB`.`company_has_Contracts` (`company_company_id`, `Contracts_contract_id`) VALUES (3, 3);





-- Insert data into emission_has_Environmental Impact table
INSERT INTO `emission_has_Environmental Impact` (`emission_emission_id`, `Environmental Impact_impact_id`) VALUES
(1, 1),
(2, 2),
(3, 3);










