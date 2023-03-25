from django.forms import ModelForm
from django import forms
from .models import Project, Review, Tag

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs): # 
        super(ProjectForm, self).__init__(*args, **kwargs) 
        self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Project Title'})
        self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Project Description'})
        self.fields['demo_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Demo Link'})
        self.fields['source_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Source Link'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote',
        }

    def __init__(self, *args, **kwargs): 
        super(ReviewForm, self).__init__(*args, **kwargs) 
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})