from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
        'class' : 'form-control',
        'placeholder' : 'example@email.com'
        }))
    subject = forms.CharField(initial='Inquiry', widget=forms.TextInput(
        attrs={
        'class' : 'form-control',
        }))
    from_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
        'class' : 'form-control',
        'placeholder' : 'name'
        }))
    from_company = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
        'class' : 'form-control',
        'placeholder' : 'company'
        }))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
        'rows' : '5',
        'class' : 'form-control',
        'placeholder' : 'Ask us!'
        }))
