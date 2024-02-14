import random

class person:
    def __init__(self, name, money, interest_tech,interest_car):
        self.name = name
        self.money = money
        self.interest_tech = interest_tech
        self.interest_car = interest_car
        self.inventory = []
    
    
    def calc_appeal(self,item,cost):    
        '''This function is used to calculate the relative appeal the person has to an object that is being offered for sale this should be a decimal from 0 to 1
            item: the thing being sold this should only be of the thing class
            cost: the cost of the item in question. type int
        '''
        item_type = item.type
        if item_type == "tech":
            interes_value = self.interest_tech
        elif item_type == "car":
            interes_value = self.interest_car
        appeal = interes_value/cost
        appeal = appeal*100+.1
        return appeal
    
    def should_buy(self,appeal):
        if appeal < .25:
            return False
        elif appeal > .75:
            return True
        else:
            if 0.5 > appeal:
                upperbound = 1 - appeal
                print(f"the upperbound is {upperbound}")
                chance = random.uniform(0,upperbound)

            elif 0.5 < appeal:
                lowerbound = 1 - appeal
                print(f"The lower bound is {lowerbound}")
                chance = random.uniform(lowerbound,1)
            else:
                print("exactly 50 now rolling")
                chance = random.uniform(0,1)
        
        if chance > 0.5:
            return True
        elif chance < 0.5:
            return False
        else:
            return self.should_buy(appeal)
   
    def add_item(self,item):
       self.inventory.append(item)
    
    def remove_item(self,item):
        self.inventory.remove(item)

    def add_funds(self,amount):
        self.money + amount
    
    def remove_funds(self,amount):
        self.money - amount




class thing:
    def __init__(self,name,itemtype) -> None:
        self.name = name
        self.type = itemtype
        self.relvalue = 0

    def set_relvalue(self,i):
        self.relvalue = i

    def get_relvalue(self):
        return self.relvalue

