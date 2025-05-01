from django.db import models

class Yunalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Yunalish"
        verbose_name_plural = "Yunalishlar"


class Fan(models.Model):
    nom = models.CharField(max_length=255)
    asosiy = models.BooleanField(default = False)
    yunalish = models.ForeignKey(Yunalish, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"


class Ustoz(models.Model):
    BAKALAVR = 'Bakalavr'
    MAGISTR = 'Magistr'
    DOCTOR = 'Doctor'

    DARAJA_CHOICES = (
        (BAKALAVR , 'Bakalavr'),
        (MAGISTR , 'Magistr'),
        (DOCTOR , 'Doctor')
    )
    GENDER_CHOICES = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    ]
    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10, choices=GENDER_CHOICES)
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=20, choices = DARAJA_CHOICES, default = MAGISTR)
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name = "Ustoz"
        verbose_name_plural = "Ustozlar"
