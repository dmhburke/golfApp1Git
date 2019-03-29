from django.contrib import admin

# Register your models here.
from catalog.models import LaTourHoleModel, PlayerModel, LaTourAllocationModel, LaTourScoreModel, LaTourStablefordModel

# Define the new admin class for each model
class LaTourHoleModelAdmin(admin.ModelAdmin):
     list_display = ('number', 'par', 'index', 'meters', 'CTP', 'LD', 'tussle',)
     ordering = ('number',)

# Register the admin class with the associated model
admin.site.register(LaTourHoleModel, LaTourHoleModelAdmin)

# Define the new admin class for each model
class PlayerModelAdmin(admin.ModelAdmin):
     list_display = ('name', 'HC',)

# Register the admin class with the associated model
admin.site.register(PlayerModel, PlayerModelAdmin)

# Define the new admin class for each model
class LaTourAllocationModelAdmin(admin.ModelAdmin):
     list_display = ('player_slot', 'player_name', 'player_holesplayed', 'player_score', 'player_stbl')
     ordering = ('player_slot',)

# Register the admin class with the associated model
admin.site.register(LaTourAllocationModel, LaTourAllocationModelAdmin)

# Define the new admin class for each model
class LaTourScoreModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_score','slot2_score', 'slot3_score',)

# Register the admin class with the associated model
admin.site.register(LaTourScoreModel, LaTourScoreModelAdmin)

# Define the new admin class for each model
class LaTourStablefordModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_stbl','slot2_stbl', 'slot3_stbl',)

# Register the admin class with the associated model
admin.site.register(LaTourStablefordModel, LaTourStablefordModelAdmin)
