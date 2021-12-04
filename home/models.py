from django.db import models

# Create your models here.
class Email(models.Model):

    sender = models.EmailField(verbose_name="email")
    username = models.CharField(max_length=100, blank=True, null=True)
    text =models.CharField(max_length=500, blank=True, null=True)
    pushat = models.DateField(auto_created=True, auto_now_add=True)
    message  =models.TextField(blank=True, null=True)
    class Meta():
        verbose_name = "Email inviate"

