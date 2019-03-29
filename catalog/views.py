from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic
from catalog.definitions import *

#Import models
from catalog.models import LaTourHoleModel, PlayerModel, LaTourAllocationModel, LaTourScoreModel, LaTourStablefordModel

#Import forms
from catalog.forms import LaTourScoreForm #ListDetailForm

# LOGIN PAGE
def login (request):
    """Creates site landing page and login"""

    # Build views here

    #Add HTML context here
    context = {
    }

    #Create HTML request/return details
    return render(request, 'Playgolf.html', context=context)

# LA TOURETTE HOLE LIST PAGE
class latourette (generic.ListView):
    """View to create hole list"""

    model = LaTourHoleModel
    template_name = 'LaTourette.html'


# LA TOURETTE SCOREBOARD PAGE
def latourette_scoreboard(request):
    """Creates scoreboard view"""

    # Build views here
    allocation_list = LaTourAllocationModel.objects.all

    #Add HTML context here
    context = {
    'player1name': player1name,
    'allocation_list': allocation_list,
    }

    #Create HTML request/return details
    return render(request, 'Scoreboard.html', context=context)
    

def holedetail_view(request, pk):
    """View to enable hole=by-hole scoring"""

    #HTML Context definitions
    hole_number = LaTourHoleModel.objects.get(pk=pk).number
    hole_index = LaTourHoleModel.objects.get(pk=pk).index
    hole_par = LaTourHoleModel.objects.get(pk=pk).par
    hole_meters = LaTourHoleModel.objects.get(pk=pk).meters
    player1_image = LaTourAllocationModel.objects.get(player_slot = '1').player_name.picture
    selected_hole = LaTourHoleModel.objects.get(number=pk)
    stblford_two = 2
    
#-- HANDLE FORM INPUT (CREATE, EDIT, DISPLAY)
    if request.method == 'POST':
        form = LaTourScoreForm(request.POST)
        try:
            instance = LaTourScoreModel.objects.get(hole=selected_hole)
            instance.slot1_score = form.save(commit=False).slot1_score
            instance.slot2_score = form.save(commit=False).slot2_score
            instance.slot3_score = form.save(commit=False).slot3_score
            instance.save()
            return redirect('latourette')
        except:
            if form.is_valid():
                post = form.save(commit=False)
                post.hole = selected_hole
                post.save()
                return redirect('latourette')

    else:
        try:
            form = LaTourScoreForm(instance=get_object_or_404(LaTourScoreModel,hole=selected_hole))
        except:
            form = LaTourScoreForm()

# --HANDLE STABLEFORD CONVERSION

    def stableford_conversion(par, index, HC, score):
        if HC >= hole_index + 18:
            stblford_add = 2
        elif HC >= hole_index:
            stblford_add = 1
        else:
            stblford_add = 0
    
        score_diff = par - score
        stableford_conversion = max(stblford_add + stblford_two + score_diff,0)
        return stableford_conversion

    #-Establish active score by slot
    # - Slot 1
    try:
        slot1_active_score = LaTourScoreModel.objects.get(hole=selected_hole).slot1_score
        slot1_stable = stableford_conversion(hole_par,hole_index,slot1_HC,slot1_active_score)            
    except:
        slot1_stable = None
    # - Slot 2
    try:
        slot2_active_score = LaTourScoreModel.objects.get(hole=selected_hole).slot2_score
        slot2_stable = stableford_conversion(hole_par,hole_index,slot2_HC,slot2_active_score)
    except:
        slot2_stable = None
    # - Slot 3
    try:
        slot3_active_score = LaTourScoreModel.objects.get(hole=selected_hole).slot3_score
        slot3_stable = stableford_conversion(hole_par,hole_index,slot3_HC,slot3_active_score)
    except:
        slot3_stable = None

    #- Record stableford scores by slots
    try:
        stbl_instance = LaTourStablefordModel.objects.get(hole=selected_hole)
        stbl_instance.slot1_stbl = slot1_stable
        stbl_instance.slot2_stbl = slot2_stable
        stbl_instance.slot3_stbl = slot3_stable
        stbl_instance.save()
    except:
        stbl_create = LaTourStablefordModel(hole=selected_hole)
        stbl_create.save()
        
#-- ADD BACK TO ALLOCATION MODEL

    # Player 1
    player1total = list(LaTourScoreModel.objects.aggregate(Sum('slot1_score')).values())[0]
    player1totalSTBL = list(LaTourStablefordModel.objects.aggregate(Sum('slot1_stbl')).values())[0]
    player1holesplayed = LaTourScoreModel.objects.filter(slot1_score__gt=1).count()
#    player1rank = player1totalSTBL / player1holesplayed
    allocation_update1 = LaTourAllocationModel.objects.get(player_slot='1')
    allocation_update1.player_score = player1total
    allocation_update1.player_stbl = player1totalSTBL
    allocation_update1.player_holesplayed = player1holesplayed
#    allocation_update1.player_rank = player1rank
    allocation_update1.save()

    # Player 2
    player2total = list(LaTourScoreModel.objects.aggregate(Sum('slot2_score')).values())[0]
    player2totalSTBL = list(LaTourStablefordModel.objects.aggregate(Sum('slot2_stbl')).values())[0]
    player2holesplayed = LaTourScoreModel.objects.filter(slot2_score__gt=1).count()
    allocation_update2 = LaTourAllocationModel.objects.get(player_slot='2')
    allocation_update2.player_score = player2total
    allocation_update2.player_stbl = player2totalSTBL
    allocation_update2.player_holesplayed = player2holesplayed
    allocation_update2.save()

    # Player 3
    player3total = list(LaTourScoreModel.objects.aggregate(Sum('slot3_score')).values())[0]
    player3totalSTBL = list(LaTourStablefordModel.objects.aggregate(Sum('slot3_stbl')).values())[0]
    player3holesplayed = LaTourScoreModel.objects.filter(slot3_score__gt=1).count()
    allocation_update3 = LaTourAllocationModel.objects.get(player_slot='3')
    allocation_update3.player_score = player3total
    allocation_update3.player_stbl = player3totalSTBL
    allocation_update3.player_holesplayed = player3holesplayed
    allocation_update3.save()

    active_players = LaTourAllocationModel.objects.all()

    context = {
        'player1': player1name,
        'player2': player2name,
        'player3': player3name,
        'hole_number': hole_number,
        'hole_index': hole_index,
        'hole_par': hole_par,
        'hole_meters': hole_meters,
        'active_players': active_players,
        'form': form,

        }
 
    return render(request, 'holeDetailLaTour.html', context)    
