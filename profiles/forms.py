from django import forms

from .models import User, UserProfile


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'type': "email",
    }))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    pic_choices = [
        ('missingbook.png', 'Choose Your Avatar'),
        ('1.png', 'Experimented Man'),
        ('2.png', 'Female Explorer'),
        ('3.png', 'Hipster Man'),
        ('4.png', 'Wise Lady'),
        ('5.png', 'Rebel Kid'),
        ('6.png', 'Chic Girl'),
    ]
    pic_url = forms.CharField(widget=forms.Select(choices=pic_choices,
                                                  attrs={'id': "select-img", }
                                                  ), required=False)
    is_writer = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'type': "checkbox",
        'disabled': True,
    }), required=False)

    class Meta:
        model = UserProfile
        fields = ['pic_url', 'is_writer']
