from django.db import models

class Flowershop(models.Model):
  aneka_bunga = models.CharField(max_length=255)
  warna = models.CharField(max_length=255)
  def __str__(self):
    return f"{self.aneka_bunga}"