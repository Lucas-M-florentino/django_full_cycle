from django.db import models


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    initial_price = models.FloatField(verbose_name="Preço Inicial")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Jogador"
        verbose_name_plural = "Jogadores"

class Team(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"


class MyTeams(models.Model):
    player = models.ManyToManyField(Player, verbose_name="Jogadores")

    def __str__(self):
        return [str(p.name) for p in self.player.all()].__str__()
    class Meta:
        verbose_name = "Meu Time"
        verbose_name_plural = "Meus Times"


class Match(models.Model):
    match_date = models.DateTimeField()
    team_a = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name="team_a_matches",
        verbose_name="Time A",
    )
    team_a_goal = models.IntegerField(default=0)
    team_b = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name="team_b_matches",
        verbose_name="Time B",
    )
    team_b_goal = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team_a} X {self.team_b} - {self.match_date} ----- {self.team_a_goal} X {self.team_b_goal}"
    
    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"
