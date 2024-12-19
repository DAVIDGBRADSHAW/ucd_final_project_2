from django.db import models
from django.contrib.auth.models import User
from PIL import Image 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=30)
    surnname = models.CharField(max_length=30)
    Email = models.CharField(max_length=100)
    ADDRESS_1 = models.CharField(max_length=30)
    ADDRESS_2 = models.CharField(max_length=30)
    ADDRESS_3 = models.CharField(max_length=30)
    ADDRESS_4 = models.CharField(max_length=30)
    ADDRESS_5 = models.CharField(max_length=30)
    CODE = models.CharField(max_length=100)# ask do i put carlow etc in here
    WHY= models.TextField()
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    MAILING_LIST = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
