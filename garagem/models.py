from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()
    
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.upper()
    
class Descricao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao.upper()
    
class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def _str_(self):
        return self.descricao.upper()
    
class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def _str_(self):
        return self.descricao.upper()
    
class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.marca.upper()} {self.ano.upper()} {self.cor.upper()}"