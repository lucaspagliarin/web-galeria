from django import forms


class FormAdiciona(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['tags'] = forms.CharField(max_length=500, label='tags', required=False)

