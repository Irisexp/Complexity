from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


"""class quiz_Page(Page):

    form_model = "player"
    form_fields = ["Q1_choice", "Q2_choice", "Q3_choice", "Q4_choice","Q5_choice"]"""

class Summary(Page):
    pass

class Q1_Page(Page):

    form_model = "player"
    form_fields = ["Q1_choice"]


class Q2_Page(Page):

    form_model = "player"
    form_fields = ["Q2_choice"]


class Q3_Page(Page):

    form_model = "player"
    form_fields = ["Q3_choice"]


class Q4_Page(Page):

    form_model = "player"
    form_fields = ["Q4_choice"]


class Results(Page):
    def vars_for_template(self):
        self.player.correct = self.player.num_correct()
        self.player.round_payoff = self.player.correct*0.5
        self.participant.payoff += self.player.round_payoff
        print(self.participant.payoff)
        correct = self.player.correct
        return{'correct': correct}

page_sequence = [Summary, Q1_Page, Q2_Page, Q3_Page, Q4_Page, Results]
