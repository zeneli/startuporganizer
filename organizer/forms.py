from django import forms
from django.core.exceptions import ValidationError

from .models import NewsLink, Startup, Tag


class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug


# TagForm inherits from forms.ModelForm so we can connect it to the
# corresponding Tag model. Helps maintain DRY principle.
# TagForm inherits from SlugCleanMixin in order to mix the
# clean_slug functionality into the TagForm.
class TagForm(SlugCleanMixin, forms.ModelForm):
    # Connect TagForm to Tag model.
    # No longer need field names and save method.
    class Meta:
        model = Tag
        fields = '__all__'

    # clean_name ensures the name field is lowercase.
    def clean_name(self):
        return self.cleaned_data['name'].lower()


class StartupForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'


class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'
