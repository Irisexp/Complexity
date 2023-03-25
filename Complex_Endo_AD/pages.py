from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import itertools
import ast

class init_calc(WaitPage):
    def after_all_players_arrive(self):
        self.group.get_state()
        self.group.get_random_attributes()

class Instructions_first(Page):
    def is_displayed(self):
        return self.round_number == 1


class Question(Page):
    timeout_seconds = Constants.time
    def is_displayed(self):
        return self.player.id_in_group == 2

#
# class Receiver_choice(Page):
#     form_model = 'group'
#     form_fields = ['random_first', 'random_second', 'random_third']
#
#
#     def random_first_choices(self):
#         return[[0, 'What is the background color of the first card?'], [1, 'What is the center shape of the first card?'], [2, 'What is the center letter of the first card?'],
#                [3,'What is the number of the first card?'], [4, 'What is the mathematical symbol of the first card?'],
#                [5, 'What is the background color of the second card?'], [6, 'What is the center shape of the second card?'], [7, 'What is the center letter of the second card?'],
#                [8, 'What is the number of the second card?'], [9, 'What is the mathematical symbol of the second card?'],
#                [10, 'What is the background color of the third card?'], [11, 'What is the center shape of the third card?'], [12, 'What is the center letter of the third card?'],
#                [13, 'What is the number of the third card?'], [14, 'What is the mathematical symbol of the third card?'],
#                [15, 'What is the background color of the fourth card?'], [16, 'What is the center shape of the fourth card?'], [17, 'What is the center letter of the fourth card?'],
#                [18, 'What is the number of the fourth card?'], [19, 'What is the mathematical symbol of the fourth card?'],]
#
#
#     def random_second_choices(self):
#         return[[0, 'What is the background color of the first card?'], [1, 'What is the center shape of the first card?'], [2, 'What is the center letter of the first card?'],
#                [3,'What is the number of the first card?'], [4, 'What is the mathematical symbol of the first card?'],
#                [5, 'What is the background color of the second card?'], [6, 'What is the center shape of the second card?'], [7, 'What is the center letter of the second card?'],
#                [8, 'What is the number of the second card?'], [9, 'What is the mathematical symbol of the second card?'],
#                [10, 'What is the background color of the third card?'], [11, 'What is the center shape of the third card?'], [12, 'What is the center letter of the third card?'],
#                [13, 'What is the number of the third card?'], [14, 'What is the mathematical symbol of the third card?'],
#                [15, 'What is the background color of the fourth card?'], [16, 'What is the center shape of the fourth card?'], [17, 'What is the center letter of the fourth card?'],
#                [18, 'What is the number of the fourth card?'], [19, 'What is the mathematical symbol of the fourth card?'],]
#
#
#     def random_third_choices(self):
#         return[[0, 'What is the background color of the first card?'], [1, 'What is the center shape of the first card?'], [2, 'What is the center letter of the first card?'],
#                [3,'What is the number of the first card?'], [4, 'What is the mathematical symbol of the first card?'],
#                [5, 'What is the background color of the second card?'], [6, 'What is the center shape of the second card?'], [7, 'What is the center letter of the second card?'],
#                [8, 'What is the number of the second card?'], [9, 'What is the mathematical symbol of the second card?'],
#                [10, 'What is the background color of the third card?'], [11, 'What is the center shape of the third card?'], [12, 'What is the center letter of the third card?'],
#                [13, 'What is the number of the third card?'], [14, 'What is the mathematical symbol of the third card?'],
#                [15, 'What is the background color of the fourth card?'], [16, 'What is the center shape of the fourth card?'], [17, 'What is the center letter of the fourth card?'],
#                [18, 'What is the number of the fourth card?'], [19, 'What is the mathematical symbol of the fourth card?'],]
#
#
#     def error_message(self, values):
#         print('values is', values)
#         if values['random_first'] == values['random_second'] or values['random_first'] == values['random_third'] or values['random_second'] == values['random_third']:
#             return 'You must choose three different questions to ask. '
#
#     def is_displayed(self):
#         return self.player.id_in_group == 2




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
        if self.group.random_first == 0:
            return[[1,'White'], [2,'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'],[6, 'Blue'], [7, 'Pink'], [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif  self.group.random_first == 1:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5,'Parallelogram'], [6, 'Cross'], [7,'Pentagon'], [8, 'Diamond'], [9,'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_first == 2:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5,'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'], [11,'H'], [12,'P']]
        elif self.group.random_first == 3:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9,'19'], [10,'7'], [11, '12'], [12, '16']]
        elif self.group.random_first == 4:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],[7, '\u221A'], [8, '\u0025'], [9, '\u00F7'],[10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_first == 5:
            return[[1,'White'], [2,'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'],[6, 'Blue'], [7, 'Pink'], [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif  self.group.random_first == 6:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5,'Parallelogram'], [6, 'Cross'], [7,'Pentagon'], [8, 'Diamond'], [9,'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_first == 7:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5,'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'], [11,'H'], [12,'P']]
        elif self.group.random_first == 8:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9,'19'], [10,'7'], [11, '12'], [12, '16']]
        elif self.group.random_first == 9:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],[7, '\u221A'], [8, '\u0025'], [9, '\u00F7'],[10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_first == 10:
            return[[1,'White'], [2,'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'],[6, 'Blue'], [7, 'Pink'], [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif  self.group.random_first == 11:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5,'Parallelogram'], [6, 'Cross'], [7,'Pentagon'], [8, 'Diamond'], [9,'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_first == 12:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5,'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'], [11,'H'], [12,'P']]
        elif self.group.random_first == 13:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9,'19'], [10,'7'], [11, '12'], [12, '16']]
        elif self.group.random_first == 14:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],[7, '\u221A'], [8, '\u0025'], [9, '\u00F7'],[10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_first == 15:
            return[[1,'White'], [2,'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'],[6, 'Blue'], [7, 'Pink'], [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif  self.group.random_first == 16:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5,'Parallelogram'], [6, 'Cross'], [7,'Pentagon'], [8, 'Diamond'], [9,'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_first == 17:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5,'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'], [11,'H'], [12,'P']]
        elif self.group.random_first == 18:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9,'19'], [10,'7'], [11, '12'], [12, '16']]
        elif self.group.random_first == 19:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],[7, '\u221A'], [8, '\u0025'], [9, '\u00F7'],[10, '\u2229'], [11, '\u2205'], [12, '\u221E']]



    def report_second_choices(self):
        if self.group.random_second == 0:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.group.random_second == 1:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_second == 2:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.group.random_second == 3:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.group.random_second == 4:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_second == 5:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.group.random_second == 6:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_second == 7:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.group.random_second == 8:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.group.random_second == 9:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_second == 10:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.group.random_second == 11:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_second == 12:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.group.random_second == 13:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.group.random_second == 14:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_second == 15:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.group.random_second == 16:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_second == 17:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.group.random_second == 18:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.group.random_second == 19:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]



    def report_third_choices(self):
        if self.group.random_third == 0:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.group.random_third == 1:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_third == 2:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.group.random_third == 3:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.group.random_third == 4:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_third == 5:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.group.random_third == 6:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_third == 7:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.group.random_third == 8:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.group.random_third == 9:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_third == 10:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.group.random_third == 11:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_third == 12:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.group.random_third == 13:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.group.random_third == 14:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]
        elif self.group.random_third == 15:
            return [[1, 'White'], [2, 'Orange'], [3, 'Grey'], [4, 'Purple'], [5, 'Red'], [6, 'Blue'], [7, 'Pink'],
                    [8, 'Yellow'], [9, 'Green'], [10, 'Maroon'], [11, 'Black'], [12, 'Navy']]
        elif self.group.random_third == 16:
            return [[1, 'Square'], [2, 'Round'], [3, 'Triangle'], [4, 'Heart'], [5, 'Parallelogram'], [6, 'Cross'],
                    [7, 'Pentagon'], [8, 'Diamond'], [9, 'Star'], [10, 'Drop'], [11, 'Moon'], [12, 'Cubic']]
        elif self.group.random_third == 17:
            return [[1, 'B'], [2, 'F'], [3, 'J'], [4, 'D'], [5, 'G'], [6, 'M'], [7, 'E'], [8, 'L'], [9, 'K'], [10, 'A'],
                    [11, 'H'], [12, 'P']]
        elif self.group.random_third == 18:
            return [[1, '2'], [2, '11'], [3, '18'], [4, '6'], [5, '9'], [6, '15'], [7, '8'], [8, '13'], [9, '19'],
                    [10, '7'], [11, '12'], [12, '16']]
        elif self.group.random_third == 19:
            return [[1, '\u002B'], [2, '\u2212'], [3, '\u00D7'], [4, '\u003C'], [5, '\u003E'], [6, '\u003D'],
                    [7, '\u221A'], [8, '\u0025'], [9, '\u00F7'], [10, '\u2229'], [11, '\u2205'], [12, '\u221E']]

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



page_sequence = [init_calc, Instructions_first, Instructions_second, Question, Observation, WaitforP2, Sender_report, WaitforP1, Receiver_guess, Waitforall, Results]




