from django import forms
from .models import Order



class CheckoutForm(forms.ModelForm):
    PAYMENT_CHOICES = [
        ('direct_bank_transfer', 'Direct Bank Transfer'),
        ('check_payments', 'Check Payments'),
        ('cash_on_delivery', 'Cash Delivery'),
        ('paypal', 'Paypal'),
    ]
    
    

    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect,
        label='Payment Method'
    )
    
    

    create_account = forms.BooleanField(required=False, label="Create an account")
    class Meta:
        model = Order
        fields = ['username',
            'first_name', 'last_name', 'company_name', 'address', 'house_number_street_name',
            'town_city', 'country', 'postcode_zip', 'mobile', 'email_address', 'payment_method',
            'total_price'
            
        ]

      
















