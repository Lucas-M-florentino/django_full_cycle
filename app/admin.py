from django.contrib import admin
from .models import Player, Team, MyTeams, Match
# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_per_page = 15
    search_fields = ('name')
    
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_date', 'show_match')
    list_filter = ('match_date', 'team_a', 'team_b')
    search_fields = ('team_a__name', 'team_b__name')
    
    def show_match(self, obj):
        if(obj.team_a_goal > obj.team_b_goal):
            return f'{obj.team_a} {obj.team_a_goal} X {obj.team_b_goal} {obj.team_b}'
        elif(obj.team_a_goal < obj.team_b_goal):
            return f'{obj.team_b} {obj.team_b_goal} X {obj.team_a_goal} {obj.team_a}'
        else:
            return f'{obj.team_a} X {obj.team_b} {obj.team_a_goal} X {obj.team_b_goal}'
        
    show_match.short_description = 'Partida'

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(MyTeams)
admin.site.register(Match, MatchAdmin)