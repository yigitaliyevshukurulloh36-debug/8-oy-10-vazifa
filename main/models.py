from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nomi")
    location = models.CharField(max_length=250, verbose_name="Joylashuvi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaxti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Kompaniya"
        verbose_name_plural="Kompaniyalar"



class Worker(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nomi")
    age = models.IntegerField(validators=[
        MinValueValidator(18, message="18 yoshga to'lganlarni uchun mumkin !!!"),
    ], verbose_name="Yosh")
    job = models.CharField(max_length=250, verbose_name="Kasb")
    salary = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Oylik")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar"




class Building(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nomi")
    image = models.ImageField(upload_to="image/", null=True, blank=True, verbose_name="Rasmi")
    floors = models.IntegerField(validators=[
        MinValueValidator(1, message="0 dan katta son kiriting !!!"),
        MaxValueValidator(100, message=" 100 dan kichik son kiriting !!!")
    ], verbose_name="Qavat")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="buildings", verbose_name="Kompaniya")
    workers = models.ManyToManyField(Worker, related_name="buildings", verbose_name="Ishchilar")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Narx")
    is_finished = models.BooleanField(default=False, verbose_name="Tugallangan")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaxti")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Bino"
        verbose_name_plural = "Binolar"
    


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="Foydalanuvchi")
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="comments" ,verbose_name="Bino")
    text = models.TextField(max_length=5000, verbose_name="Matn")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaxt")

    def __str__(self):
        return f"{self.user.username}-> {self.text[:11]}"
