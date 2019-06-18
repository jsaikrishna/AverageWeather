from django.shortcuts import render

from .forms import inputForm
import requests

import googlemaps
gmaps = googlemaps.Client(key='Enter the key here from the Google Cloud to call the Geocoding API')

weather_sources = []


def index(request):
    accuweather_url = 'http://127.0.0.1:5000/{}?latitude={}&longitude={}'
    noaa_url = 'http://127.0.0.1:5000/{}?latlon={},{}'
    weatherdotcom_url = 'http://127.0.0.1:5000/{}'
    temperatures = [] # stores the current temperatures from the user input filters

    if request.method == 'POST':
        form = inputForm(request.POST)

        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            filters = form.cleaned_data['filters']
            zipcode = form.cleaned_data['zipcode']

            # Function to Validate whether the Latitude and Longitude and ZipCode are numerical values or not
            latitude_numerical_check, longitude_numerical_check, zipcode_numerical_check = validate(latitude, longitude, zipcode)

            if latitude_numerical_check and longitude_numerical_check and zipcode_numerical_check:

                # Function to get the latitude, longitude and address object
                latitude, longitude, float_latitude, float_longitude, reverse_geocode_result = getCordinates(latitude, longitude, zipcode)

                if reverse_geocode_result: # Checking if address object is null or not null
                    for filter in filters:
                        if filter == 'accuweather':
                            accuweather(accuweather_url, filter, float_latitude, float_longitude, temperatures)
                        elif filter == 'noaa':
                            noaa(noaa_url, filter, float_latitude, float_longitude, temperatures)
                        elif filter == 'weatherdotcom':
                            weatherdotcom(weatherdotcom_url, filter, latitude, longitude, temperatures)

                    # Temperature List is formed by adding the current temperatures of each filter.
                    # Calculating the Average Temperature from the temperatures List

                    average_Temperature = {'average_temperatures': sum(temperatures) / len(temperatures)}

                    CoOrdinates_are_Not_Valid = 'Yes, Co-Ordinates are Valid'
                    Cordinates_Valid = {'CoOrdinates_Valid': CoOrdinates_are_Not_Valid}

                    context = {'Average_Temperature': average_Temperature, 'Is_Coordinates_Valid': Cordinates_Valid, 'form': form}
                    return render(request, 'avgWeatherApp/index.html', context)
                else:
                    CoOrdinates_are_Not_Valid = 'No, Co-Ordinates are Not Valid, Please re-enter the latitude and longitude or ZipCode'
                    Cordinates_Valid = {'CoOrdinates_Valid': CoOrdinates_are_Not_Valid}
                    context = {'Is_Coordinates_Valid': Cordinates_Valid, 'form': form}

                return render(request, 'avgWeatherApp/index.html', context)

            else:
                CoOrdinates_are_Not_Valid = 'No, Co-Ordinates are Not Numerical Values, Please re-enter the latitude and longitude or ZipCode'
                Cordinates_Valid = {'CoOrdinates_Valid': CoOrdinates_are_Not_Valid}
                context = {'Is_Coordinates_Valid': Cordinates_Valid, 'form': form}

                return render(request, 'avgWeatherApp/index.html', context)


    form = inputForm()
    return render(request, 'avgWeatherApp/index.html', {'form': form})


def validate(latitude, longitude, zipcode):
    # Code to Validate whether the Latitude and Longitude and ZipCode numerical values or not
    latitude_numerical_check = True
    for la in latitude:
        if not la.isdigit():
            latitude_numerical_check = False
            break

    longitude_numerical_check = True
    for ln in longitude:
        if not ln.isdigit():
            longitude_numerical_check = False
            break

    zipcode_numerical_check = True
    for zp in zipcode:
        if not zp.isdigit():
            zipcode_numerical_check = False
            break;

    return latitude_numerical_check, longitude_numerical_check, zipcode_numerical_check


def getCordinates(latitude, longitude, zipcode):
    # Code to get the latitude, longitude and address object
    float_latitude = 0
    float_longitude = 0

    # Converting the values to float from string
    if latitude and longitude:
        float_latitude = float(latitude)
        float_longitude = float(longitude)

    # Function to get the latitudes and longitudes from Google Map's API
    if zipcode and len(zipcode) == 5:
        latitude, longitude,float_latitude, float_longitude = getCoordinates(zipcode)

    # Funnction to Validate the Ccordinatees using Google Map's API
    reverse_geocode_result = validateCoordinates(float_latitude, float_longitude)
    #print(reverse_geocode_result)
    return latitude, longitude,float_latitude, float_longitude, reverse_geocode_result

def getCoordinates(zipcode):
    # Code to get the latitude and longitude from the Google Maps API

    float_latitude = 0
    float_longitude = 0

    latitude = gmaps.geocode(zipcode)[0]['geometry']['bounds']['northeast']['lat']
    longitude = gmaps.geocode(zipcode)[0]['geometry']['bounds']['northeast']['lng']
    float_latitude = float(latitude)
    float_longitude = float(longitude)

    return latitude, longitude, float_latitude, float_longitude


def validateCoordinates(float_latitude, float_longitude):
    # Code to Validate the Ccordinatees using Google Map's API
    reverse_geocode_result = gmaps.reverse_geocode((float_latitude, float_longitude))
    return reverse_geocode_result


def accuweather(accuweather_url, filter, latitude, longitude, temperatures):
    r = requests.get(accuweather_url.format(filter, latitude, longitude))

    if r.status_code == 200:
        r = r.json()
        temperatures.append(int(r['simpleforecast']['forecastday'][0]['current']['fahrenheit']))
    else:
        print(r.status_code)


def noaa(noaa_url, filter, latitude, longitude, temperatures):
    r = requests.get(noaa_url.format(filter, latitude, longitude))

    if r.status_code == 200:
        r = r.json()
        temperatures.append(int(r['today']['current']['fahrenheit']))
    else:
        print(r.status_code)


def weatherdotcom(weatherdotcom_url, filter, latitude, longitude, temperatures):

    json = {"lat": latitude, "lon": longitude}
    r = requests.post(weatherdotcom_url.format(filter), None, json)

    if r.status_code == 200:
        r = r.json()
        temperatures.append(int(r['query']['results']['channel']['condition']['temp']))
    else:
        print(r.status_code)
