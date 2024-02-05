from django import forms
from blog.models import Blog


class StyleMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            try:
                input_type = field.widget.input_type
                if input_type == 'checkbox':
                    field.widget.attrs['class'] = 'form-check'
                else:
                    field.widget.attrs['class'] = 'form-control'
            except AttributeError:
                field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleMixin):

    class Meta:
        model = Blog
        exclude = ('slug', 'create_date', 'view_count',)
