from django.db import models
from datetime import datetime



class Category(models.Model):
    name = models.CharField(verbose_name='Тип блюда', max_length=100, db_index= True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category,verbose_name='Категория', related_name='products', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название блюда', max_length=150, db_index= True)
    slug = models.CharField(max_length=150, db_index= True, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d/')
    description = models.TextField(verbose_name='Описание блюда', max_length=1000)
    price = models.DecimalField(verbose_name='Цена блюда',max_digits=10, decimal_places=2)
    available = models.BooleanField(verbose_name='Наличие блюда', default= True)
    new  = models.BooleanField(verbose_name="Новое блюдо", default= False)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        index_together = (('id', 'slug'), )
        
    def __str__(self):
        return self.name    

        
