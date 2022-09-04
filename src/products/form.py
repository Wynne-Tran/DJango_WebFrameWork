from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title     =   forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "input here"}))
    email      = forms.EmailField()
    description =   forms.CharField(required=False, widget=forms.Textarea(
                                                            attrs = {
                                                                "class": "new-class-name two",
                                                                "id": "my-id-for-textarea",
                                                                "rows": 10,
                                                                "cols": 100
                                                            }
                                                        ))
    price       =   forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if " " in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email


class RawProductForm(forms.Form):
    title       =   forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "place holder here"}))
    description =   forms.CharField(required=False, widget=forms.Textarea(
                                                            attrs = {
                                                                "class": "new-class-name two",
                                                                "id": "my-id-for-textarea",
                                                                "rows": 10,
                                                                "cols": 120
                                                            }
                                                        ))
    price       =   forms.DecimalField(initial=199.99)
