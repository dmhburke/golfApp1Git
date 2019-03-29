from django.db import models
from django.urls import reverse
from catalog.choices import *

# Create your models here

class LaTourHoleModel(models.Model):
    number = models.IntegerField(primary_key=True)
    par = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    meters = models.IntegerField(blank=True, null=True)
    CTP = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)
    LD = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)
    tussle = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)

    #Enables individual model records to be displayed
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('holedetail', args=[str(self.pk)])

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '%s' % self.number

class PlayerModel(models.Model):
    name = models.CharField(max_length=30)
    HC = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(upload_to='media/images/', blank=True, null=True)
    jacket = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)

    def __str__(self):
        return self.name

class LaTourAllocationModel(models.Model):
    player_slot = models.IntegerField(unique=True)
    player_name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True)
    player_holesplayed = models.IntegerField(blank=True, null=True)
    player_score = models.IntegerField(blank=True, null=True)
    player_stbl = models.IntegerField(blank=True, null=True)
#    player_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-player_stbl']

class LaTourScoreModel(models.Model):
    hole = models.ForeignKey('LaTourHoleModel', on_delete = models.CASCADE)
    slot1_score = models.IntegerField(blank=True, null=True)
    slot2_score = models.IntegerField(blank=True, null=True)
    slot3_score = models.IntegerField(blank=True, null=True)

class LaTourStablefordModel(models.Model):
    hole = models.ForeignKey('LaTourHoleModel', on_delete = models.CASCADE)
    slot1_stbl = models.IntegerField(blank=True, null=True)
    slot2_stbl = models.IntegerField(blank=True, null=True)
    slot3_stbl = models.IntegerField(blank=True, null=True)
