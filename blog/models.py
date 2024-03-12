# Django imports
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.templatetags.static import static
from django.urls import reverse
from django.utils.text import slugify

# Third-party imports
from cloudinary.models import CloudinaryField
from cloudinary.uploader import destroy


class Post(models.Model):
    """Represents a blog post."""

    CATEGORY_CHOICES = (
        ('frontend', 'Front-End'),
        ('backend', 'Back-End'),
        ('design', 'UI/UX Design'),
        ('devops', 'DevOps'),
        ('perspectives', 'Thoughts & Perspectives'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    post_image = CloudinaryField('image', folder='commit/post_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the absolute URL for the current instance."""

        return reverse('post-detail', kwargs={'slug': self.slug})

    def get_post_image(self):
        """Returns the URL of the hero image or a default static image URL."""

        if self.post_image and hasattr(self.post_image, 'url'):
            return self.post_image.url
        else:
            # Return the URL to the default image in the static directory
            return static('images/default-post-image.webp')
