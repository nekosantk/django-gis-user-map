from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django.contrib.gis import forms as gis_forms


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Username',
                                       'class': 'form-control',
                                   }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder': 'Email',
                                     'class': 'form-control',
                                 }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Password',
                                        'class': 'form-control',
                                        'data-toggle': 'password',
                                        'id': 'password',
                                    }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Confirm Password',
                                        'class': 'form-control',
                                        'data-toggle': 'password',
                                        'id': 'password',
                                    }))
    home_address = forms.CharField(required=True,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control'
                                       }))
    phone_number = forms.CharField(required=True,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control'
                                       }))
    location = gis_forms.PointField(
        required=True,
        widget=gis_forms.OSMWidget(
            attrs={'map_width': 600,
                   'map_height': 600,
                   'default_lat': 42.1710962,
                   'default_lon': 18.8062112,
                   'default_zoom': 6}))

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'home_address',
            'phone_number',
            'location'
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'placeholder': 'Username',
                                       'class': 'form-control',
                                   }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(
                                   attrs={
                                       'placeholder': 'Password',
                                       'class': 'form-control',
                                       'data-toggle': 'password',
                                       'id': 'password',
                                       'name': 'password',
                                   }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'class': 'form-control'
                                   }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control'
                                 }))
    home_address = forms.CharField(required=True,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control'
                                       }))
    phone_number = forms.CharField(required=True,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control'
                                       }))
    location = gis_forms.PointField(
        required=True,
        widget=gis_forms.OSMWidget(
            attrs={
                'map_width': 600,
                'map_height': 600
            }))

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'home_address',
            'phone_number',
            'location'
        ]
