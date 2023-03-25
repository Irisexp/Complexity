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

import random
import copy
import itertools

author = 'Junya Zhou'

doc = """
Simple
"""


class Constants(BaseConstants):
    name_in_url = 'Complex_Simple_AD'
    players_per_group = 2
    num_rounds = 20
    time = 15


# if this number changes, the following dim_ report should also change

    initial_prior = 1/3
    sender_payoffs = [c(15), c(12), c(3)]
    receiver_payoffs = [c(15), c(12), c(8), c(3)]

class Subsession(BaseSubsession):

#The code is working, for each round, the profiles are randomly drawn.
    def creating_session(self):
        self.group_randomly(fixed_id_in_group = True)

        Up_first = [1, 2, 2]

        Middle_first = [3, 3, 1]

        Down_first = [2, 1, 3]

        Up_second = [5, 6, 6]

        Middle_second = [4, 5, 4]

        Down_second = [6, 4, 5]

        Up_third = [9, 7, 8]

        Middle_third = [7, 8, 7]

        Down_third = [8, 9, 9]

        Up_fourth = [3, 3, 1]

        Middle_fourth = [2, 1, 3]

        Down_fourth = [1, 2, 2]

        Up_fifth = [4, 5, 4]

        Middle_fifth = [6, 4, 5]

        Down_fifth = [5, 6, 6]

        Up_sixth = [7, 8, 7]

        Middle_sixth = [8, 9, 9]

        Down_sixth = [9, 7, 8]

        Up_seventh = [2, 1, 3]

        Middle_seventh = [1, 2, 2]

        Down_seventh = [3, 3, 1]

        Up_eighth = [6, 4, 5]

        Middle_eighth = [5, 6, 6]

        Down_eighth = [4, 5, 4]

        Up_ninth = [8, 9, 9]

        Middle_ninth = [9, 7, 8]

        Down_ninth = [7, 8, 7]
#second sets

        Up_tenth = [12, 12, 10]

        Middle_tenth = [10, 11, 12]

        Down_tenth = [11, 10, 11]

        Up_eleventh = [3, 3, 2]

        Middle_eleventh = [2, 1, 1]

        Down_eleventh = [1, 2, 3]

        Up_twelfth = [6, 5, 5]

        Middle_twelfth = [4, 4, 6]

        Down_twelfth = [5, 6, 4]

        Up_thirteenth = [10, 11, 12]

        Middle_thirteenth = [11, 10, 11]

        Down_thirteenth = [12, 12, 10]

        Up_fourteenth = [2, 1, 1]

        Middle_fourteenth = [1, 2, 3]

        Down_fourteenth = [3, 3, 2]

        Up_fifteenth = [4, 4, 6]

        Middle_fifteenth = [5, 6, 4]

        Down_fifteenth = [6, 5, 5]

        Up_sixteenth = [11, 10, 11]

        Middle_sixteenth = [12, 12, 10]

        Down_sixteenth = [10, 11, 12]

        Up_seventeenth = [1, 2, 3]

        Middle_seventeenth = [3, 3, 2]

        Down_seventeenth = [2, 1, 1]

        Up_eighteenth = [5, 6, 4]

        Middle_eighteenth = [6, 5, 5]

        Down_eighteenth = [4, 4, 6]

        Up_nineteenth = [7, 7, 7]

        Middle_nineteenth = [8, 8, 9]

        Down_nineteenth = [9, 9, 8]

        Up_twentieth = [11, 10, 12]

        Middle_twentieth = [12, 12, 11]

        Down_twentieth = [10, 11, 10]


        self.session.vars['Up'] = [Up_first, Up_second, Up_third, Up_fourth, Up_fifth, Up_sixth, Up_seventh, Up_eighth, Up_ninth, Up_tenth, Up_eleventh, Up_twelfth, Up_thirteenth, Up_fourteenth, Up_fifteenth, Up_sixteenth, Up_seventeenth, Up_eighteenth, Up_nineteenth, Up_twentieth]
        self.session.vars['Middle'] = [Middle_first, Middle_second, Middle_third, Middle_fourth, Middle_fifth, Middle_sixth, Middle_seventh, Middle_eighth, Middle_ninth, Middle_tenth, Middle_eleventh, Middle_twelfth, Middle_thirteenth, Middle_fourteenth, Middle_fifteenth, Middle_sixteenth, Middle_seventeenth, Middle_eighteenth, Middle_nineteenth, Middle_twentieth]
        self.session.vars['Down'] = [Down_first, Down_second, Down_third, Down_fourth, Down_fifth, Down_sixth, Down_seventh, Down_eighth, Down_ninth, Down_tenth, Down_eleventh, Down_twelfth, Down_thirteenth, Down_fourteenth, Down_fifteenth, Down_sixteenth, Down_seventeenth, Down_eighteenth, Down_nineteenth, Down_twentieth]




class Group(BaseGroup):

    true_state = models.IntegerField(label="")

    profile_num = models.IntegerField(label="")
    #
    # random_first = models.IntegerField(label="The first question is:")
    #
    # random_second = models.IntegerField(label="The second question is:")
    #
    # random_third = models.IntegerField(label="The third question is:")

    attribute_first = models.IntegerField(label="")

    attribute_second = models.IntegerField(label="")

    attribute_third = models.IntegerField(label="")

    report_first = models.IntegerField(label="")

    report_second = models.IntegerField(label="")

    report_third = models.IntegerField(label="")

    message = models.IntegerField(label="")

    guess = models.IntegerField(label="")

    check_first = models.IntegerField(label="")

    check_second = models.IntegerField(label="")

    check_third = models.IntegerField(label="")


    def get_state(self):
        self.true_state = random.choices([1, 2, 3], weights = [Constants.initial_prior, Constants.initial_prior, Constants.initial_prior])[0]
        print(self.true_state)
        return self.true_state


    def get_correct_attributes(self):
        # print(self.session.vars['Up'])
        # print(self.session.vars['Middle'])
        # print(self.session.vars['Down'])
        if self.message == 1:
            self.attribute_first =  self.session.vars['Up'][self.round_number - 1][0]
            self.attribute_second =  self.session.vars['Up'][self.round_number - 1][1]
            self.attribute_third =  self.session.vars['Up'][self.round_number - 1][2]
        elif self.message == 2:
            self.attribute_first = self.session.vars['Middle'][self.round_number - 1][0]
            self.attribute_second = self.session.vars['Middle'][self.round_number - 1][1]
            self.attribute_third = self.session.vars['Middle'][self.round_number - 1][2]
        else:
            self.attribute_first =  self.session.vars['Down'][self.round_number - 1][0]
            self.attribute_second =  self.session.vars['Down'][self.round_number - 1][1]
            self.attribute_third =  self.session.vars['Down'][self.round_number - 1][2]
        print(self.attribute_first)
        print(self.attribute_second)
        print(self.attribute_third)
        return self.attribute_first, self.attribute_second, self.attribute_third



    def get_check_first(self):
        if self.attribute_first == self.report_first:
            self.check_first = 1
        else:
            self.check_first = 0

        # print(self.attribute_first)
        # print(self.report_first)
        # print(self.check_first)
        # return self.check_first


    def get_check_second(self):
        if self.attribute_second == self.report_second:
            self.check_second = 1
        else:
            self.check_second = 0

        # print(self.attribute_second)
        # print(self.report_second)
        # print(self.check_second)
        # print(self.check_second)
        # return self.check_second


    def get_check_third(self):
        if self.attribute_third == self.report_third:
            self.check_third = 1
        else:
            self.check_third = 0

        # print(self.attribute_third)
        # print(self.report_third)
        # print(self.check_third)
        # print(self.check_third)
        # return self.check_third
        #



#when the final set is decided, add a function to examine whether the sender is truthfully reporting.

class Player(BasePlayer):

    round_payoff = models.CurrencyField()

    other_payoff = models.CurrencyField()


    def role(self):
        if self.id_in_group == 1:
            return 'Sender'
        else:
            return 'Receiver'




