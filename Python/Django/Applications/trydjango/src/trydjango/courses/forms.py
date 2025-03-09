from django import forms
from .models import Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError('This is not a valid title!')
        return title