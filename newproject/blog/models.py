from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse # Change here
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse # Change here

class Post(models.Model): 
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    surnname = models.CharField(max_length=30)
    Email = models.CharField(max_length=100)
    ADDRESS_1 = models.CharField(max_length=30)
    ADDRESS_2 = models.CharField(max_length=30)
    ADDRESS_3 = models.CharField(max_length=30)
    ADDRESS_4 = models.CharField(max_length=30)
    ADDRESS_5 = models.CharField(max_length=30)
    CODE = models.CharField(max_length=100)
    WHY= models.TextField()
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    MAILING_LIST = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '  |' + self.author
    
    def get_absolute_url(self): # Change here
        return reverse('post-detail', kwargs={'pk': self.pk}) # Change here to bring the user to the post detail view