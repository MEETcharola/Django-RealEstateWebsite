from django import forms
from .models import Property_Residential, Property_Commercial, Property_Plot, Property_PG, Property_Images

property_type_choices = [('Residential', 'Residential'),
                         ('Commercial', 'Commercial'),
                         ('Plot', 'Plot')]
property_for_choices = [('Sale', 'Sale'),
                        ('Rent', 'Rent'),
                        ('PG', 'PG')]
bedroom_choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
                   ('9', '9'), ('10', '10')]
balcony_choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]
bathroom_choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]
furnishing_choices = [('Furnished', 'Furnished'),
                      ('Not-Furnished', 'Not-Furnished'),
                      ('Semi-Furnished', 'Semi-Furnished')]
car_parking_choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
status_choices = [('Ready To Move', 'Ready To Move'), ('In Construction', 'In Construction')]
landzone_choices = [('Industrial', 'Industrial'), ('Commercial', 'Commercial'),
                    ('Transport and Communication', 'Transport and Communication'),
                    ('Public Utilities', 'Public Utilities'),
                    ('Public and Semi Public Use', 'Public and Semi Public Use'), ('Open Spaces', 'Open Spaces'),
                    ('Agriculture Zone', 'Agriculture Zone'), ('Special Economic Zone', 'Special Economic Zone'),
                    ('Natural Conservation Zone', 'Natural Conservation Zone'), ('Government Use', 'Government Use')]
open_side_choices = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
boundry_wall_choices = [('Constructed', 'Constructed'),
                        ('Not-Constructed', 'Not-Constructed')]


class RESPropertyCreationForm(forms.ModelForm):
    property_for = forms.ChoiceField(choices=property_for_choices)
    bedrooms = forms.ChoiceField(choices=bedroom_choices)
    balconies = forms.ChoiceField(choices=balcony_choices)
    bathrooms = forms.ChoiceField(choices=bathroom_choices)
    furnishing = forms.ChoiceField(choices=furnishing_choices)
    car_parking = forms.ChoiceField(choices=car_parking_choices)
    status = forms.ChoiceField(choices=status_choices)

    class Meta:
        model = Property_Residential
        fields = ['property_for', 'title', 'address', 'city', 'locality', 'state', 'zipcode', 'description', 'price',
                  'bedrooms',
                  'balconies', 'bathrooms', 'floor_number', 'total_floor', 'furnishing', 'car_parking', 'carpet_area',
                  'super_area',
                  'status', 'photo_main']


class COMPropertyCreationForm(forms.ModelForm):
    property_for = forms.ChoiceField(choices=property_for_choices)
    landzone = forms.ChoiceField(choices=landzone_choices)
    washrooms = forms.ChoiceField(choices=bathroom_choices)
    personal_washrooms = forms.ChoiceField(choices=bathroom_choices)
    furnishing = forms.ChoiceField(choices=furnishing_choices)
    status = forms.ChoiceField(choices=status_choices)

    class Meta:
        model = Property_Commercial
        fields = ['property_for', 'title', 'address', 'city', 'locality', 'state', 'zipcode', 'landzone',
                  'ideal_for_business', 'description', 'price',
                  'washrooms', 'personal_washrooms', 'floor_number', 'total_floor', 'furnishing', 'carpet_area',
                  'super_area',
                  'status', 'photo_main']


class PLOTPropertyCreationForm(forms.ModelForm):
    property_for = forms.ChoiceField(choices=property_for_choices)
    landzone = forms.ChoiceField(choices=landzone_choices)
    status = forms.ChoiceField(choices=status_choices)
    number_of_openside = forms.ChoiceField(choices=open_side_choices)
    boundry_wall_status = forms.ChoiceField(choices=boundry_wall_choices)

    class Meta:
        model = Property_Plot
        fields = ['property_for', 'title', 'address', 'city', 'locality', 'state', 'zipcode',
                  'floors_allowed_for_construction', 'number_of_openside', 'width_of_road_facing_the_plot',
                  'boundry_wall_status', 'description', 'price',
                  'plot_area', 'plot_length', 'status', 'photo_main']


class PGPropertyCreationForm(forms.ModelForm):
    bedrooms = forms.ChoiceField(choices=bedroom_choices)
    balconies = forms.ChoiceField(choices=balcony_choices)
    bathrooms = forms.ChoiceField(choices=bathroom_choices)
    furnishing = forms.ChoiceField(choices=furnishing_choices)
    status = forms.ChoiceField(choices=status_choices)

    class Meta:
        model = Property_PG
        fields = ['title', 'address', 'city', 'locality', 'state', 'zipcode', 'description', 'monthly_rent',
                  'security_deposit',
                  'bedrooms',
                  'balconies', 'bathrooms', 'furnishing',
                  'status', 'photo_main']


class Images(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Property_Images
        fields = ['image']
