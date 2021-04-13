from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # A user associated with a profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Profile image for users
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}`s Profile'

    """def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the image for the profile instance
        img = Image.open(self.image.path)  # resize image

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # Resize and save it
            img.thumbnail(output_size)
            # Saving it
            img.save(self.image.path)"""

