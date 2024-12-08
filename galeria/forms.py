from django import forms
from galeria.funcoes import busca_colecoes

class FormAdiciona(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        self.fields['tags'] = forms.CharField(max_length=500, label='Tags', required=False)
        self.fields['new_collection'] = forms.CharField(max_length=500, label='Collection', required=False)
        # self.opcoes = colecoes(request)
        self.fields['pick_collection'] = forms.ChoiceField(choices=busca_colecoes(self.user), initial='0', required=False)
        self.fields['favorite'] = forms.BooleanField(required=False, initial=False)


class FormLogin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

        self.fields['username'] = forms.CharField(max_length=150, label='Username', required=True)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Email or Username',
            'autocomplete': 'off',
        })
        self.fields['password'] = forms.CharField(max_length=500, label='Password', required=True, widget=forms.PasswordInput)
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'autocomplete': 'off',
        })


class FormCadastro(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'] = forms.CharField(max_length=150, label='Username', required=True)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'autocomplete': 'off',
        })
        self.fields['password'] = forms.CharField(max_length=500, label='Password', required=True, widget=forms.PasswordInput)
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'autocomplete': 'off',
        })
        self.fields['first_name'] = forms.CharField(label='First Name', required=True)
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First Name',
            'autocomplete': 'off',
        })
        self.fields['last_name'] = forms.CharField(label='Last Name', required=True)
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name',
            'autocomplete': 'off',
        })
        self.fields['email'] = forms.EmailField(required=True)
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'autocomplete': 'off',
        })