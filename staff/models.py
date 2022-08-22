from django.db import models
from django.contrib.auth import get_user_model
USER = get_user_model()

class StaffLocation(models.Model):
    
    lattitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.lattitude} {self.longitude}"

class StaffAddress(models.Model):
    building_name = models.CharField(max_length=64)
    place = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    post_office = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=8)
    location = models.ForeignKey(
        StaffLocation, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.building_name}"

class StaffProfile(models.Model):
    MALE = "m"
    FEMALE = "f"
    LGBTQ = "lgbtq"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (LGBTQ, "LGBTQ"),
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    dob = models.DateField()
    id_proof = models.FileField(upload_to="staff/id_proof/", null=True, blank=True)
    image = models.ImageField(upload_to="staff/profile_image/")
    address = models.ForeignKey(
        StaffAddress, on_delete=models.SET_NULL, null=True, blank=True
    )
    email = models.EmailField(max_length = 254)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



