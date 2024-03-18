# Django imports
from django import forms

# Third-party imports
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget

# Local application imports
from .models import Comment, Post, Profile


class PostForm(forms.ModelForm):
    """
    A form for creating or updating an post.
    """

    title = forms.CharField(
        max_length=100,
        error_messages={
            'required': 'This field is required.',
            'max_length':
            'Ensure value has at most 100 characters (it has %(show_value)d).',
        }
    )
    post_image = CloudinaryFileField(
        required=False,
        label='Post Image',
        error_messages={
            'invalid': 'Invalid file type.',
        }
    )
    excerpt = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'post-excerpt-field',
            'placeholder': 'Please write a short description for your post.'
        }),
        max_length=250,
        error_messages={
            'required': 'This field is required.',
            'max_length':
            'Ensure value has at most 250 characters (it has %(show_value)d).',
        }
    )
    content = forms.CharField(
        required=True,
        widget=SummernoteWidget(
            attrs={'summernote': {'width': '100%', 'height': '400px'}}),
        error_messages={
            'required': 'This field is required.',
        }
    )

    class Meta:
        model = Post
        fields = ['title', 'post_image', 'category', 'excerpt', 'content']


class CommentForm(forms.ModelForm):
    """
    A form for submitting comments.
    """

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'post-comment-field',
            'placeholder': 'Leave a comment.'
        }),
    )

    class Meta:
        model = Comment
        fields = ['content']


class ProfileForm(forms.ModelForm):
    """
    A form for updating the user's profile.
    """

    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio', 'birthday', 'country',
                  'city', 'profession', 'website_url', 'github_url', 'linkedin_url', 'medium_url']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            self.fields['profile_picture'].label = "Profile Picture"
