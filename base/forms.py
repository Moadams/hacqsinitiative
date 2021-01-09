from django.forms import ModelForm
from .models import Post,Member

class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'heading',
            'sub_heading',
            'image',
            'body',
        ]    
        
        
class AddMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'