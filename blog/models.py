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

    def get_author_profile_picture_url(self):
        """Returns the URL of the profile picture or a default static image."""

        if self.author.profile.profile_picture:
            return self.author.profile.profile_picture.url
        else:
            return static('images/default-profile-image.webp')

    def save(self, *args, **kwargs):
        """
        Overrides the save method to generate a slug if it doesn't exist.
        """

        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """Represents a comment on a blog post."""

    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

    class Meta:
        ordering = ['-created_at']


class Profile(models.Model):
    """Represents a user's profile information."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    profile_picture = CloudinaryField(
        'image', folder='commit/profile_images', blank=True
    )
    bio = models.TextField(blank=True, default='')
    birthday = models.DateField(null=True, blank=True)
    profession = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='')
    website_url = models.URLField(max_length=250, blank=True, default='')
    github_url = models.URLField(max_length=250, blank=True, default='')
    linkedin_url = models.URLField(max_length=250, blank=True, default='')
    medium_url = models.URLField(max_length=250, blank=True, default='')

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def profile_picture_url(self):
        """
        Returns the URL of the profile picture for the user.
        If profile picture is set, the URL of the profile picture is returned.
        """
        if self.profile_picture:
            return self.profile_picture.url
        else:
            # Return the URL to the default image in the static directory
            return static('images/default-profile-image.webp')

    def delete(self, *args, **kwargs):
        """
        Deletes the model instance and its associated image from Cloudinary.
        """

        destroy(self.profile_picture.public_id)
        super().delete(*args, **kwargs)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile."""

    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
