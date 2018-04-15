import requests

api_key = '<your_api_key>'
api_call = 'https://api.openweathermap.org/data/2.5/weather?appid=' + api_key

running = True

print('Welcome to Jaimes Subroto\'s current weather application using OpenWeatherMap\'s API!')

# Program loop
while running:

    # Asks the user for the city or zip code to be queried
    while True:

        # Input validation
        try:
            print('\nThis application supports search by city(0) or search by zip code(1).')
            search = int(input('Please input 0 or 1: '))
        except ValueError:
            print("Sorry, I didn't understand that.")
        else:
            # Passed the validation test

            if search == 0:
                city = input('Please input the city name: ')
                if city.lower() == 'sf':
                    city = 'San Francisco, US'

                # Appends the city to the api call
                api_call += '&q=' + city
                break
                
            elif search == 1:
                zip_code = input('Please input the zip code: ')
                
                # Appends the zip code to the api call
                api_call += '&zip=' + zip_code
                break
                
            else:
                # Prints the invalid number (not 0 or 1)
                print('{} is not a valid option.'.format(search))

    # Stores the Json response
    json_data = requests.get(api_call).json()

    # Temperature is measured Kelvin
    temperature = json_data['main']['temp']

    data = {
        'description': json_data['weather'][0]['description'],
        'city': json_data['name'],
        'country': json_data['sys']['country']
    }

    # Prints the city, country
    print('\n{city}, {country}'.format(**data))

    # Prints the description as well as the temperature in Celcius and Farenheit
    print('Weather condition: %(description)s' % data)
    print('Celcius: {:.2f}'.format(temperature - 273.15))
    print('Farenheit: %.2f' % (temperature * 9/5 - 459.67))

    # Asks user if he/she wants to exit
    while True:
        running = input('\nAnything else we can help you with? ')
        if running.lower() == 'yes' or running.lower() == 'y':
            print('Great!')
            break
        elif running.lower() == 'no' or running.lower() == 'n' or running == 'exit':
            print('Thank you for using Jaimes Subroto\'s current weather application.')
            print('Have a great day!')
            running = False
            break
        else:
            print('Sorry, I didn\'t get that.')
