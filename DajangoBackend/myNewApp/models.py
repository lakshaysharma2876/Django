from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KW', 'KIWI'),
        ('PL', 'PLAIN'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    

# one to many relationship
class ChaiReviews(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=100)
    review_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.name} left a rating and review of {self.chai.name}'
    

# Many to Many Relationship
class ChaiStore(models.Model) :
    chai_varities = models.ManyToManyField(ChaiVariety, related_name='stores')


    def __str__(self):
        return self.name
    

# One to One Relationship
class ChaiCertificates(models.Model) :
    certificate = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificates')

    def __str__(self):
        return self.name
