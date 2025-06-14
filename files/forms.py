from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        help_text='Allowed file types: PDF, JPG, JPEG'
    )

    def clean_file(self):
        file = self.cleaned_data['file']
        content_type = file.content_type.lower()
        if content_type not in ['application/pdf', 'image/jpeg', 'image/jpg']:
            raise forms.ValidationError('Only PDF, JPG, and JPEG files are allowed.')
        return file
