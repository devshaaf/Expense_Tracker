from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["amount", "category", "description"]

        widgets = {
        "amount":forms.NumberInput(attrs={
            "id":"amount",
            "placeholder":"e.g., 50.00",
            "required":True
        }),

        "category":forms.Select(attrs={
            "id":"category",
            "required":True
        }),

        "description": forms.Textarea(attrs={
            "id":"description",
            "placeholder":"e.g., Lunch with friends",
            "rows":3
        })
    }
        

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

        widgets = {
            "first_name":forms.TextInput(attrs={
                    "id":"first-name",
                    "placeholder":"John",
                    "required":True,
                    "name":"firstname"
                }),

            "last_name":forms.TextInput(attrs={
                    "id":"last-name",
                    "placeholder":"Doe",
                    "required":True
                }),

            "username":forms.TextInput(attrs={
                    "id":"username",
                    # "placeholder":"johndoe123",
                    "required":True
                }),
            
            "email":forms.EmailInput(attrs={
                    "id":"email",
                    "placeholder":"john.doe@example.com",
                    "required":True
                }),

            "password1":forms.PasswordInput(attrs={
                    "id":"password",
                    "placeholder":"Enter your password",
                    "required":True
                }),

            "password2":forms.PasswordInput(attrs={
                    "id":"password",
                    "placeholder":"Confirm your password",
                    "required":True
                })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user