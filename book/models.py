from django.db import models


class addbookmodel(models.Model):
    Book_name=models.CharField(max_length=120)
    Author=models.CharField(max_length=120)
    Price=models.IntegerField(null=False)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.Book_name

class order_model(models.Model):
    Product=models.ForeignKey(addbookmodel,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    quantity = models.IntegerField(null=False)
    choices = [
        ("ordered", "ordered"),
        ("despatched", "despatched"),
        ("cancelled", "cancelled")
    ]
    status = models.CharField(max_length=10, choices=choices, default="ordered")
