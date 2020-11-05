from django.db import models

class A(models.Model):
    title = models.CharField(max_length=100)
    b = models.ForeignKey(
        'B',
        on_delete=models.CASCADE,
        related_name='name_b',
        null=True,
        blank=True
    )


class B(models.Model):
    title = models.CharField(max_length=100)
    a = models.ForeignKey(A, on_delete=models.CASCADE, related_name='name_a')

class C(models.Model):
    title = models.CharField(max_length=100)

class D(models.Model):
    title = models.CharField(max_length=100)
    m2m = models.ManyToManyField(C)


