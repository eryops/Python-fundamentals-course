flights = [
    {
        'flight_number': 'SK087',
        'destination': 'Arlanda',
        'departure_time': '13:00',
        'gate': '3B',
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 0,
        'is_cancelled': False,
    },
    {
        'flight_number': 'SK099',
        'destination': 'Landvetter',
        'departure_time': '12:30',
        'gate': '4C',
        'passengers': 134,
        'maximum_capacity': 167,
        'delay_in_minutes': 0,
        'is_cancelled': False,
    },
    {
        'flight_number': 'SK082',
        'destination': 'Oslo',
        'departure_time': '14:40',
        'gate': '87',
        'passengers': 65,
        'maximum_capacity': 167,
        'delay_in_minutes': 0,
        'is_cancelled': False,
    },
    {
        'flight_number': 'BLX386',
        'destination': 'Kos',
        'departure_time': '06:50',
        'gate': '44',
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 0,
        'is_cancelled': False,
    },
    {
        'flight_number': 'DK346',
        'destination': 'Gran Canaria',
        'departure_time': '14:00',
        'gate': '89',
        'passengers': 134,
        'maximum_capacity': 167,
        'delay_in_minutes': 0,
        'is_cancelled': False,
    },
    {
        'flight_number': 'SK574',
        'destination': 'New York',
        'departure_time': '19:00',
        'gate': '2',
        'passengers': 167,
        'maximum_capacity': 167,
        'delay_in_minutes': 1,
        'is_cancelled': False,
    },
    {
        'flight_number': 'sk107',
        'destination': 'London',
        'departure_time': '23:50',
        'gate': '1B',
        'passengers': 44,
        'maximum_capacity': 167,
        'delay_in_minutes': 59,
        'is_cancelled': False,
    },
    {
        'flight_number': 'FI306',
        'destination': 'Helsinki',
        'departure_time': '16:10',
        'gate': '66',
        'passengers': 166,
        'maximum_capacity': 167,
        'delay_in_minutes': 20,
        'is_cancelled': False,
    },
    {
        'flight_number': 'KLM387',
        'destination': 'Amsterdam',
        'departure_time': '14:45',
        'gate': '',
        'passengers': 22,
        'maximum_capacity': 167,
        'delay_in_minutes': 19,
        'is_cancelled': False,
    },
    {
        'flight_number': 'LH345',
        'destination': 'Berlin',
        'departure_time': '21:00',
        'gate': '5A',
        'passengers': 150,
        'maximum_capacity': 167,
        'delay_in_minutes': 60,
        'is_cancelled': True,
    },
]

number_of_scheduled_flights = 0
number_of_canceled_flights = 0
number_of_delayed_flights = 0
number_of_flights_on_time = 0
total_number_of_passengers = 0
largest_number_of_passengers = 0
number_of_flight_with_80_percent_filled = 0

for flight in flights:
    number_of_scheduled_flights += 1
    total_number_of_passengers += flight['passengers']

    if flight['passengers'] > largest_number_of_passengers:
        largest_number_of_passengers = flight['passengers']

    if flight['passengers'] / flight['maximum_capacity'] > 0.8:
        number_of_flight_with_80_percent_filled += 1

    status = 'ON TIME'
    if flight['is_cancelled']:
        status = 'CANCELLED'
        number_of_canceled_flights += 1
    elif flight['delay_in_minutes'] > 59:
        status = 'SEVERELY DELAYED'
    elif flight['delay_in_minutes'] > 19:
        status = 'DELAYED'
    elif flight['delay_in_minutes'] > 0:
        status = 'SLIGHT DELAY'

    if status == 'ON TIME':
        number_of_flights_on_time += 1
    elif status != 'CANCELLED':
        number_of_delayed_flights += 1    

    print(f"{flight['flight_number']} to {flight['destination']} leaving from Gate {flight['gate'] or 'Gate not assigned'} at {flight['departure_time']} is {status}")

print(f"""
number_of_scheduled_flights {number_of_scheduled_flights}
number_of_canceled_flights {number_of_canceled_flights}
number_of_delayed_flights {number_of_delayed_flights}
number_of_flights_on_time  {number_of_flights_on_time}
total_number_of_passengers {total_number_of_passengers}
average_number_of_passengers {total_number_of_passengers/number_of_scheduled_flights}
largest_number_of_passengers {largest_number_of_passengers}
number_of_flight_with_80_percent_filled {number_of_flight_with_80_percent_filled}
""")

search_flight = input("Search for a flight: ")
search_flight_not_found = True

for flight in flights:
    if flight['flight_number'] == search_flight:
        print(f"{flight['flight_number']} to {flight['destination']} leaving from Gate {flight['gate']} at {flight['departure_time']} is {status}")
        search_flight_not_found = False
        break
if search_flight_not_found:
    print('Flight not found')