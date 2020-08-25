from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    # task_photo = forms.ImageField(required=False)


    class Meta:
        model = Task
        fields = ['text', 'task_photo']
        widgets = {
            'user': forms.HiddenInput(),
            'date_published': forms.HiddenInput()
        }


class EditCommentForm(TaskForm):

    class Meta:
        model = Task
        fields = ['text', 'task_photo']
        widgets = {
            'user': forms.HiddenInput(),
        }