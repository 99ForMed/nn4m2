from .models import EntrySubmission
from django.forms import ModelForm

class EntrySubmissionForm(ModelForm):
    class Meta:
        model = EntrySubmission
        fields = ['first_name', 'last_name', 'email', 'atar', 'gpa', 'phone']

    def __init__(self, *args, **kwargs):
        super(EntrySubmissionForm, self).__init__(*args, **kwargs)
        self.fields['atar'].widget.attrs['min'] = 0
        self.fields['atar'].widget.attrs['max'] = 100
        self.fields['gpa'].widget.attrs['min'] = 0
        self.fields['gpa'].widget.attrs['max'] = 7