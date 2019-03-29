from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic


#import models here
from catalog.models import LaTourHoleModel, PlayerModel, LaTourAllocationModel, LaTourScoreModel, LaTourStablefordModel

#import forms here


#DEFINITIONS
#Playernames
player1name = LaTourAllocationModel.objects.get(player_slot = '1').player_name
player2name = LaTourAllocationModel.objects.get(player_slot = '2').player_name
player3name = LaTourAllocationModel.objects.get(player_slot = '3').player_name

#PlayerImages
#player1_image = LaTourAllocationModel.objects.get(player_slot = '1').player_name.picture

#Handicaps
slot1_HC = LaTourAllocationModel.objects.get(player_slot = '1').player_name.HC
slot2_HC = LaTourAllocationModel.objects.get(player_slot = '2').player_name.HC
slot3_HC = LaTourAllocationModel.objects.get(player_slot = '3').player_name.HC

