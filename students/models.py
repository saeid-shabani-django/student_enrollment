from django.db import models

class Stud(models.Model):
    s_name = models.CharField(max_length=255)
    s_class = models.CharField(max_length=255)
    s_addr = models.CharField(max_length=255)
    s_school = models.CharField(max_length=255)
    s_email = models.EmailField(max_length=255)
