from django import forms
from django.forms import ModelForm, Form

from apps.estate.models import EstateAgentComment


class EstateAgentCommentForm(ModelForm):
    class Meta:
        model = EstateAgentComment
        fields = ["name", "email", "comment", "stars_count"]


# class EstateAgentCommentForm(Form):
#     name = forms.CharField(max_length=255, required=False)
#     email = forms.EmailField(required=False)
#     comment = forms.CharField(widget=forms.Textarea, required=False)
#     stars_count = forms.IntegerField(required=False)