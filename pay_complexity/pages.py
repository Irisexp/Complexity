from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class FinalPaymentWaitPage(WaitPage):
    def after_all_players_arrive(self):
        # random.seed(random.randint(1, 999))
        apps_to_pay = [0]
        rounds_to_pay =  [random.randint(3,19)]
        for p in self.group.get_players():
            payoff_list = p.participant.vars.get('payoffs', [])
            p.participant.vars['app_display_list'] = apps_to_pay
            round_list = p.participant.vars.get('rounds_display_list', [])
            round_list.append(rounds_to_pay)
            # print(rounds_to_pay)
            p.participant.vars['rounds_display_list'] = round_list
            # now saving to otree's payoff variable for currency calculations
            for r in rounds_to_pay:
                p.payoff += payoff_list[apps_to_pay[0]][rounds_to_pay[0]]



class FinalPayment(Page):
    def vars_for_template(self):
        apps_list = self.player.participant.vars.get('app_display_list', [])
        rounds_list = self.player.participant.vars.get('rounds_display_list', [])
        payoff_list = self.player.participant.vars.get('payoffs', [])
        django_display_list = []
        for i in range(len(apps_list)):
            a_list = [apps_list[i]+1]  # we need to add 1 so that apps and rounds line up with a 1 instead of 0 index
            a_list.append([r+1 for r in rounds_list[i]])
            temp_list = []
            for r in rounds_list[i]:
                temp_list.append(int(payoff_list[apps_list[i]][r]))
            # a_list.append(payoff_list[apps_list[i]][rounds_list[i]])
            a_list.append(temp_list)
            django_display_list.append(a_list)


        dollars = self.participant.payoff_plus_participation_fee()
        self.player.dollars = dollars

        return dict(display_list=django_display_list, dollars=dollars)



page_sequence = [
    FinalPaymentWaitPage,
    FinalPayment,
]


