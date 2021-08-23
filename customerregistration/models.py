from django.db import models



class customer(models.Model):

    tc_no = models.CharField(unique = True, max_length = 11)
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    phone_no = models.CharField(unique = True, max_length = 11)
    city = models.CharField(max_length = 100,)
    district = models.CharField(max_length = 100)
    registration_date = models.DateField(auto_now_add = True)


