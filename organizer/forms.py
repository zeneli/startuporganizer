from django import forms
from django.core.exceptions import ValidationError

from .models import NewsLink, Startup, Tag


# TagForm inherits from forms.ModelForm so we can connect it to the
# corresponding Tag model. Helps maintain DRY principle.
class TagForm(forms.ModelForm):
    # Connect TagForm to Tag model.
    # No longer need field names and save method.
    class Meta:
        model = Tag
        fields = '__all__'

    # clean_name ensures the name field is lowercase.
    def clean_name(self):
        return self.cleaned_data['name'].lower()

    # clean_slug must do two things:
    # 1) ensure slug is lowercase (to prevent alphabetization and conflicts)
    # 2) ensure slug is not create (to prevent URL path collision)
    def clean_slug(self):
        new_slug = (slef.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug


class StartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'

    # clean_slug (copy of TagForm's clean_slug)
    def clean_slug(self):
        new_slug = (slef.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug


class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'
