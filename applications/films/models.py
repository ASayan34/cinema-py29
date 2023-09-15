from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Film(models.Model):
    """
        Модель фильма
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='films', verbose_name='Владелец'
    )
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} --> {self.owner}'
    

class Like(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='likes'
    )
    film = models.ForeignKey(
        Film, on_delete=models.CASCADE,
        related_name='likes'
    )
    is_like = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.owner} liked - {self.film.title}'
    

class Rating(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='ratings'
    )
    film = models.ForeignKey(
        Film, on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.SmallIntegerField(validators=[
        MinValueValidator(1), 
        MaxValueValidator(5)
    ], blank=True, null=True)
    
    def __str__(self):
        return f'{self.owner} --> {self.film.title}'
    