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
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 0,
        'is_cancelled': False,
    },
    {
        'flight_number': 'SK082',
        'destination': 'Oslo',
        'departure_time': '14:40',
        'gate': '87',
        'passengers': 99,
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
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 0,
        'is_cancelled': False,
    },
    {
        'flight_number': 'SK574',
        'destination': 'New York',
        'departure_time': '19:00',
        'gate': '2',
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 1,
        'is_cancelled': False,
    },
    {
        'flight_number': 'sk107',
        'destination': 'London',
        'departure_time': '23:50',
        'gate': '1B',
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 59,
        'is_cancelled': False,
    },
    {
        'flight_number': 'FI306',
        'destination': 'Helsinki',
        'departure_time': '16:10',
        'gate': '66',
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 20,
        'is_cancelled': False,
    },
    {
        'flight_number': 'KLM387',
        'destination': 'Amsterdam',
        'departure_time': '14:45',
        'gate': '4D',
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 19,
        'is_cancelled': False,
    },
    {
        'flight_number': 'LH345',
        'destination': 'Berlin',
        'departure_time': '21:00',
        'gate': '5A',
        'passengers': 99,
        'maximum_capacity': 167,
        'delay_in_minutes': 60,
        'is_cancelled': True,
    },
]

for flight in flights:
    status = 'ON TIME'
    if flight['is_cancelled']:
        status = 'CANCELLED'
    elif flight['delay_in_minutes'] > 59:
        status = 'SEVERELY DELAYED'
    elif flight['delay_in_minutes'] > 19:
        status = 'DELAYED'
    elif flight['delay_in_minutes'] > 0:
        status = 'SLIGHT DELAY'

    print(f"{flight['flight_number']} to {flight['destination']} leaving from Gate {flight['gate']} at {flight['departure_time']} is {status}")