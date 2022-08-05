from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


class Location(models.Model):
    lattitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.lattitude} {self.longitude}"


class Address(models.Model):
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
        Location, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.building_name}"


class Profile(models.Model):
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
    id_proof = models.FileField(upload_to="student/id_proof/", null=True, blank=True)
    image = models.ImageField(upload_to="student/profile/image/")
    address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SessionYearModel(models.Model):
    start = models.DateField()
    end = models.DateField()
    year= models.CharField(max_length=120)

    def __str__(self):
        return f"{self.start} {self.end}"


class Department(models.Model):
    name = models.CharField(max_length=120)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.SET_NULL, null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    is_hod = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


class Student(models.Model):
    profile = models.OneToOneField(
        Profile, on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


class Enroll(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True
    )
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    session_year = models.ForeignKey(
        SessionYearModel, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student}"
