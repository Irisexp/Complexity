from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import itertools
import ast

class init_calc(WaitPage):
    def after_all_players_arrive(self):
        self.group.get_state()

class Instructions_first(Page):
    def is_displayed(self):
        return self.round_number == 1


class Instructions_second(Page):
    def is_displayed(self):
        return self.round_number == 1

class Observation(Page):
    timeout_seconds = Constants.time


class WaitforP2(WaitPage):
    wait_for_all_groups = True


class Sender_report(Page):

    form_model = 'group'
    form_fields = ['message', 'report_first', 'report_second', 'report_third']

    def message_choices(self):
        return [[1, 'Up'], [2, 'Middle'], [3, 'Down']]

    def report_first_choices(self):
        return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]

    def report_second_choices(self):
        return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]

    def report_third_choices(self):
        return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5,'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'], [11,'H'], [12,'P']]

    def is_displayed(self):
        return self.player.id_in_group == 1


class WaitforP1(WaitPage):
    def after_all_players_arrive(self):
        self.group.get_correct_attributes()
        self.group.get_check_first()
        self.group.get_check_second()
        self.group.get_check_third()


class Receiver_guess(Page):

    form_model = 'group'
    form_fields = ['guess']

    def guess_choices(self):
        return[[1, 'Up'], [2, 'Middle'], [3, 'Down']]

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        message = self.group.message
        return{'message': message}


class Waitforall(WaitPage):

    def after_all_players_arrive(self):

        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
        if self.group.guess == 1:
            if self.group.true_state == 1:
                p1.round_payoff = Constants.sender_payoffs[0]
                p2.other_payoff = Constants.sender_payoffs[0]
                p2.round_payoff = Constants.receiver_payoffs[0]
                p1.other_payoff = Constants.receiver_payoffs[0]
            elif self.group.true_state == 2:
                p1.round_payoff = Constants.sender_payoffs[0]
                p2.other_payoff = Constants.sender_payoffs[0]
                p2.round_payoff = Constants.receiver_payoffs[2]
                p1.other_payoff = Constants.receiver_payoffs[2]
            else:
                p1.round_payoff = Constants.sender_payoffs[0]
                p2.other_payoff = Constants.sender_payoffs[0]
                p2.round_payoff = Constants.receiver_payoffs[3]
                p1.other_payoff = Constants.receiver_payoffs[3]
        elif self.group.guess == 2:
            if self.group.true_state == 1:
                p1.round_payoff = Constants.sender_payoffs[1]
                p2.other_payoff = Constants.sender_payoffs[1]
                p2.round_payoff = Constants.receiver_payoffs[1]
                p1.other_payoff = Constants.receiver_payoffs[1]
            elif self.group.true_state == 2:
                p1.round_payoff = Constants.sender_payoffs[1]
                p2.other_payoff = Constants.sender_payoffs[1]
                p2.round_payoff = Constants.receiver_payoffs[0]
                p1.other_payoff = Constants.receiver_payoffs[0]
            else:
                p1.round_payoff = Constants.sender_payoffs[1]
                p2.other_payoff = Constants.sender_payoffs[1]
                p2.round_payoff = Constants.receiver_payoffs[2]
                p1.other_payoff = Constants.receiver_payoffs[2]
        else:
            if self.group.true_state == 1:
                p1.round_payoff = Constants.sender_payoffs[2]
                p2.other_payoff = Constants.sender_payoffs[2]
                p2.round_payoff = Constants.receiver_payoffs[3]
                p1.other_payoff = Constants.receiver_payoffs[3]
            elif self.group.true_state == 2:
                p1.round_payoff = Constants.sender_payoffs[2]
                p2.other_payoff = Constants.sender_payoffs[2]
                p2.round_payoff = Constants.receiver_payoffs[1]
                p1.other_payoff = Constants.receiver_payoffs[1]
            else:
                p1.round_payoff = Constants.sender_payoffs[2]
                p2.other_payoff = Constants.sender_payoffs[2]
                p2.round_payoff = Constants.receiver_payoffs[0]
                p1.other_payoff = Constants.receiver_payoffs[0]


        for p in self.group.get_players():
            app1_list = p.participant.vars.get('app1_payoffs',[])
            app1_list.append(p.round_payoff)
            p.participant.vars['app1_payoffs'] = app1_list

        for p in self.group.get_players():
            if self.round_number == Constants.num_rounds:
                payoff_list = p.participant.vars.get('payoffs', [])
                app1_list = p.participant.vars.get('app1_payoffs', [])
                payoff_list.append(app1_list)
                p.participant.vars['payoffs'] = payoff_list



class Results(Page):
    def vars_for_template(self):
        round = self.round_number
        return{'round': round}




page_sequence = [init_calc, Instructions_first, Instructions_second, Observation, WaitforP2, Sender_report, WaitforP1, Receiver_guess, Waitforall, Results]




