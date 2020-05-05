from django.db import models

# Create your models here.
class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=200)
    school_domain = models.CharField(max_length=200)
    def __str__(self):
        return self.school_name