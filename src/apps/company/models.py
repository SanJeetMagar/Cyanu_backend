from django.db import models

# Create your models here.

class CompanyInfo(models.Model):
    name = models.CharField(max_length= 255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=155)
    email = models.EmailField(unique= True)
    descriptions = models.TextField()
    logo= models.ImageField(upload_to="company/", null= True, blank= True)
    facebook_link = models.URLField(max_length=255, null= True, blank= True)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Company Info'
        verbose_name_plural = "Company Infos"




class OutreachNumber(models.Model):
    countries_served = models.IntegerField() 
    countries_empowered = models.IntegerField()
    saas_product_built = models.IntegerField()
    clients_served = models.IntegerField()   

    class Meta:
        verbose_name = 'OutrangeNumber'
        verbose_name_plural = "OutrangeNumber"                                                                                                                                                                                                                                                                                                                                                