from django.db import models
from products.models import Taco, Nevado
from user.models import User


class Venta(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    taco = models.ForeignKey(Taco, on_delete=models.CASCADE, null=True, blank=True)
    Nevado = models.ForeignKey(Nevado, on_delete=models.CASCADE, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    ESTADO_CHOICES = (
        ('Pagado', 'Pagado'),
        ('No_pagado', 'No_pagado')
    )
    estado = models.CharField(max_length=255, choices=ESTADO_CHOICES, default='No_pagado')
