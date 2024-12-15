from django import forms
from .models import Image


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image", "title", "description"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter image title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a brief description",
                    "rows": 3,
                }
            ),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image", "title", "description"]
