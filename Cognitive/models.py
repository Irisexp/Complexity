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
Cognitive recognition test
"""


class Constants(BaseConstants):
    name_in_url = 'Cognitive'
    players_per_group = None
    num_rounds = 1
    # cost = c(4)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    round_payoff = models.CurrencyField()


    Q1_choice = models.IntegerField(
    label='A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?'
)

    Q2_choice = models.IntegerField(
    label='A farmer had 15 sheep and all but 8 died. How many are left?'
)


    Q3_choice = models.IntegerField(
label= ''
)

    Q4_choice = models.IntegerField(
        label=''
    )

    correct = models.IntegerField()
    correct_1 = models.IntegerField()
    correct_2 = models.IntegerField()
    correct_3 = models.IntegerField()
    # correct_4 = models.IntegerField()
    # correct_5 = models.IntegerField()


    def num_correct(self):
        if self.Q1_choice == 5:
            self.correct_1 = 1
        else:
            self.correct_1 = 0
        if self.Q2_choice == 8:
            self.correct_2 = 1
        else:
            self.correct_2 = 0
        if self.Q3_choice == 0:
            self.correct_3 = 1
        else:
            self.correct_3 = 0
        # if self.Q5_choice == 2:
        #     self.correct_5 = 1
        # else:
        #     self.correct_5 = 0
        self.correct = self.correct_1 + self.correct_2 + self.correct_3
        return self.correct


