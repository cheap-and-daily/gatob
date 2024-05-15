from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", required=True, min_length=4, max_length=20,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label="Пароль", min_length=8, max_length=20,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Пароль'}))


class RegisterForm(forms.ModelForm):
    repeat_password = forms.CharField(label="Повторите пароль", required=True, min_length=8, max_length=20,
                                      widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password',
                                                                        'placeholder': 'Повторите пароль'}))

    phone = forms.CharField(label="Номер телефона", required=True, max_length=17,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7-XXX-XXX-XX-XX'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'password']
        labels = {
            'email': "Email",
            'username': "Имя пользователя",
            'first_name': "Имя",
            'last_name': "Фамилия",
            'password': "Пароль",
        }
        help_texts = {
            'username': "Не более 20 символов. Только буквы, цифры и символы @/./+/-/_."
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email'}),
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя пользователя'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу фамилию'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш пароль'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.Meta.fields:
            self.fields[field_name].required = True

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Profile.objects.filter(phone=phone).exists():
            raise ValidationError('Этот номер телефона уже занят.')
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот адрес электронной почты уже занят.')
        return email

    def clean_repeat_password(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("repeat_password")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(label="Аватар", required=False)

    class Meta:
        model = Profile
        fields = ['bio']
        labels = {
            'bio': "Биография",
        }
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу биографию'}),
        }
