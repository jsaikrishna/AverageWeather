# Shipwell-Average-Weather

The Source Code for the Django Application is in the folder weather/weatherApp

In order to run the project clone the Entire Git Repository into the local-machine, then iterate into weather/weatherApp folder.

Then run the command to start the Django Application Server
```
python manage.py runserver

```

After Starting the Django Application, make sure to start the Provided Flast Application Server to access the different weather filters in the Local Machine by following the instructions in the provided Link below;

```
https://github.com/shipwell/mock-weather-api

```
After Starting the Server, make sure to visit the below server address to enter the latitude, longitude, zipcode, select filter

```
http://127.0.0.1:8000/

```

The Below Shows the Start Page when the Django Application is Initially Starts, where user can either enter zipcode or (latitude, longitude) only, if the user enter both then zip code is entered to calculate the average weather, also user has a choose the one or more filter by select the check box's below.

![Start Page of Django Application](https://github.com/jsaikrishna/Shipwell-AverageWeather/blob/master/images/startPage.png)


So, Now once the user enter's the latitude and longitude as input and select the filter then the output result with the average temperature is displayed in the below image, also the validation of input latitude and longitude are done using Google Map's API and the result is also shown in the image below.

![Longitude and Latitude Input](https://github.com/jsaikrishna/Shipwell-AverageWeather/blob/master/images/coordinates.png)


So, Now the user enter's the zipcode as input and select the filter then the output result with the average temperature is displayed in the below image, also the validation of zipcode's latitude and longitude are done using Google Map's API and the result is also shown in the image below.

![ZipCode Input](https://github.com/jsaikrishna/Shipwell-AverageWeather/blob/master/images/zipCode.png)


So, Now once the user enter's both the zipcode and the latitude and longitude as input and select the filter then the output result with the average temperature is displayed in the below image and also while calculating the average temperature zipcode's latitude and longitude is considered., also the validation of zipcode's latitude and longitude are done using Google Map's API and the result is also shown in the image below.

![ZipCode and Longitude and Latitude Input](https://github.com/jsaikrishna/Shipwell-AverageWeather/blob/master/images/zipCode%20and%20Coordinates.png)





