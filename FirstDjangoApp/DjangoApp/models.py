from django.db import models
from django.utils import timezone


class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ("ML", "MASALA"),
        ("GR", "GINGER"),
        ("KL", "KIWI"),
        ("PL", "PLAIN"),
        ("EL", "ELACHI"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='Delicious Chai')
    price = models.FloatField(default=20.0)

    def __str__(self):
        return self.name

