from django.db import models

class perpus(models.Model):
    nama = models.CharField(max_length=30)
    alamat = models.TextField()
    npm = models.CharField(max_length=30)
    profesi = models.CharField(max_length=30)


    def __str__(self):
        return "{}.{}" .format(self.id,self.nama)