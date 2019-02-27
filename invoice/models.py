from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_heading = models.CharField(max_length=250)
    invoice_body = models.TextField()
