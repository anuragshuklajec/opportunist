from datetime import datetime, timedelta
from statistics import mode
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User



class JobType(models.TextChoices):
    FullTime = 'Permanent'
    Internship = 'Internship'
    Freelancing = 'Freelancing'


class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'


class Industry(models.TextChoices):
    Bussiness = 'Bussiness'
    IT = 'Information Technology'
    Banking = 'Banking'
    Education = 'Education'
    Telecommunication = 'Telecommunication'
    Others = 'Others'


class Experience(models.TextChoices):
    NO_EXPERIENCE = 'No Experience'
    ONE_YEAR = '1 Year'
    TWO_YEARS = '2 Years'
    FIVE_YEARS_PLUS = '5 Years above'


def Getdatetime():
    now = datetime.now()
    return now + timedelta(days=5)


class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    jobType = models.CharField(
        max_length=100, choices=JobType.choices, default=JobType.FullTime)
    education = models.CharField(
        max_length=100, choices=Education.choices, default=Education.Bachelors)
    industry = models.CharField(
        max_length=30, choices=Industry.choices, default=Industry.IT)
    experience = models.CharField(
        max_length=30, choices=Experience.choices, default=Experience.NO_EXPERIENCE)
    salary = models.IntegerField(default=1, validators=[
                                 MinValueValidator(1), MaxValueValidator(10000000)])
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    lastDate = models.DateTimeField(default=Getdatetime)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)



class CandidatesApplied(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resume = models.CharField(max_length=200)
    appliedAt = models.DateTimeField(auto_now_add=True)
