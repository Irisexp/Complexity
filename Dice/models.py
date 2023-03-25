from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Junya Zhou'
doc = """
Dice task
"""


class Constants(BaseConstants):
    name_in_url = 'Dice'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    round_payoff = models.CurrencyField()


    Q1_choice = models.IntegerField(
    label='What is the number you draw in the first throw? ',min=1, max=6
)

