from django.db import models

class Jurnal(models.Model):
  group = models.CharField(max_length=8)
  image = models.ImageField(upload_to="", null=True)
  amount = models.IntegerField()

  def __str__(self):
    return self.group
