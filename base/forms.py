from django.forms import ModelForm
from .models import Post,Executive

class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'heading',
            'sub_heading',
            'image',
            'body',
        ]    
        
        
class AddExecutiveForm(ModelForm):
    class Meta:
        model = Executive
        fields = '__all__'