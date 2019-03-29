from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic

#CHOICES
YES_NO = (
    ("YES", "Yes"),
    ("NO", "No"),
    )

HOLE_CHOICES = (
    ('-', 'Select Hole'),
    ('Hole 1', 'Hole 1'),
    ('Hole 2', 'Hole 2'),
    ('Hole 3', 'Hole 3'),
    )



