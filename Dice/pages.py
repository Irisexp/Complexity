from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


"""class quiz_Page(Page):

    form_model = "player"
    form_fields = ["Q1_choice", "Q2_choice", "Q3_choice", "Q4_choice","Q5_choice"]"""


class Q1_Page(Page):

    form_model = "player"
    form_fields = ["Q1_choice"]


class Results(Page):
    def vars_for_template(self):
        if self.player.Q1_choice == 6:
            self.player.round_payoff = 0
        else:
            self.player.round_payoff = self.player.Q1_choice
        self.participant.payoff += self.player.round_payoff
        print(self.participant.payoff)

page_sequence = [Q1_Page, Results]
