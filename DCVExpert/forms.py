from django import forms
from .models import CurriculumItem, CurriculumThems, Curriculum

class CurriculumItemForm(forms.ModelForm):
    class Meta:
        model = CurriculumItem
        fields = ['curriculum_thems', 'objective']
        widgets = {
            'objective': forms.TextInput(attrs={'class': 'vTextField', 'placeholder': 'Introdu obiectivul'}),
        }

class CurriculumThemsForm(forms.ModelForm):
    class Meta:
        model = CurriculumThems
        fields = ['curriculum', 'title']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Titlul trebuie să aibă cel puțin 3 caractere!")
        return title
        
class CurriculumForm(forms.ModelForm):
    class Meta:
        model = Curriculum
        fields = ['course', 'curriculum_name']

    def clean_curriculum_name(self):
        curriculum_name = self.cleaned_data['curriculum_name']
        if len(curriculum_name) < 5:
            raise forms.ValidationError("Numele curriculumului trebuie să aibă cel puțin 5 caractere!")
        return curriculum_name
