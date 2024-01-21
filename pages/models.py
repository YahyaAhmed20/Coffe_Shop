from django.db import models


class SignUp(models.Model):
    email = models.EmailField(blank=True)
    # username
    username = models.CharField(max_length=20, blank=True)
    # password
    password = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name='SignUp User'
        
        
        
class SignIn(models.Model):
        usernamee = models.CharField(max_length=20, blank=True)
        passwordd = models.CharField(max_length=30, null=True)
        
        def __str__(self):
            return self.usernamee
        
        class Meta:
            verbose_name='SignIn User'


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price in USD")
    # add image
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)


   
