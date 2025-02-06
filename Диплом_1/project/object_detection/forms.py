# object_detection/forms.py

from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

    def clean_image(self):
        image = self.cleaned_data.get('image')
        # Пример проверки размера файла
        if image.size > 5 * 1024 * 1024:  # 5MB
            raise forms.ValidationError("Размер изображения не должен превышать 5MB.")
        return image
