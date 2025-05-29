from django.db import models

class usuarios(models.models):
    id_usuarios =models.AutoField(primary_key=true)
    nome=models.TextField(max_length=255)
    idade =models.IntegerField()