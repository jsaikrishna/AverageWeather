from django import forms


class inputForm(forms.Form):

    zipcode = forms.CharField( required= False,
        max_length= 30,
        widget= forms.TextInput(
            attrs= {
                'placeholder': 'Numerical Values Only'
            }
        )

    )
    latitude = forms.CharField( required= False,
        max_length= 30,
        widget= forms.TextInput(
            attrs= {
                'placeholder': 'Numerical Values Only'
            }
        )

    )
    longitude = forms.CharField( required=False,
        max_length= 30,
        widget= forms.TextInput(
            attrs= {
                'placeholder': 'Numerical Values Only'
            }
        )

    )

    filters = forms.MultipleChoiceField(
        choices = (
            ('accuweather', "AccuWeather"),('noaa', "NOAA"), ('weatherdotcom', "Weather.com")
        ),
        initial= 'accuweather',
        widget = forms.CheckboxSelectMultiple,

    )

