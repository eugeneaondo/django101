from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField('Customer', max_length=20)
    age=models.IntegerField()
    note=models.TextField(blank=True,null=True)
    email=models.EmailField(max_length=255,blank=True,null=True)
    credit=models.FloatField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    TYPE_CHOICES=(
        ('Custoner', 'Customer'),
        ('Supplier', 'Supplier'),
        ('Student', 'Student')
    )

    type=models.CharField(choices=TYPE_CHOICES)

    def __str__(self) -> str:
        return self.name