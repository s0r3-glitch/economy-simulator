from core.person import *
import random

people_list = []
tech_name = ["rtx 4090", "phone", "pc", "laptop", "earbuds", "tv", "headphones", "sound bar", "ryzen cpu", "drone", 'robodog']
car_name = ["ford", 'toyota', 'subaru', 'kia', 'mazda', 'honda','ferarri', 'marcadies-bens','acura','voltswagon','audi']


tony = person("tony", random.randint(0,1000), random.uniform(0,1), random.uniform(0,1))
bob = person("bob", random.randint(0,1000), random.uniform(0,1), random.uniform(0,1))
joe = person("joe", random.randint(0,1000), random.uniform(0,1), random.uniform(0,1))
sam = person("sam", random.randint(0,1000), random.uniform(0,1), random.uniform(0,1))
tim = person("tim", random.randint(0,1000), random.uniform(0,1), random.uniform(0,1))
zack = person("zack", random.randint(0,1000), random.uniform(0,1), random.uniform(0,1))
people_list.append(tony)
people_list.append(bob)
people_list.append(joe)
people_list.append(sam)
people_list.append(tim)
people_list.append(zack)

for i in range(random.randint(0,10)):
    if random.randint(0,1) == 1:
        temp = thing(tech_name[random.randint(0,len(tech_name)-1)],"tech")
    else:
        temp = thing(car_name[random.randint(0,len(car_name)-1)],"car")
    temp.set_relvalue(random.uniform(0,500))
    people_list[random.randint(0,len(people_list)-1)].add_item(temp)

    
    
print('items out')

print('time to trade')
for i in range(10000):
    seller = None
    buyer = None
    while seller == buyer:
        seller = people_list[random.randint(0,len(people_list)-1)]
        if len(seller.inventory) == 0:
            while len(seller.inventory) == 0:
                seller = people_list[random.randint(0,len(people_list)-1)]
        buyer = people_list[random.randint(0,len(people_list)-1)]
    
    seller_item = seller.inventory[random.randint(0,len(seller.inventory)-1)]
    sell_price = seller_item.get_relvalue()
    print(f'{seller.name}: hey {buyer.name} want to buy {seller_item.name} for {sell_price}?')
    buyer_appeal = buyer.calc_appeal(seller_item,sell_price)
    should_buy = buyer.should_buy(buyer_appeal)
    if should_buy and buyer.money >= sell_price:
        print(f'{buyer.name}: I would love to buy that from you {seller.name}')
        seller.add_funds(sell_price)
        buyer.remove_funds(sell_price)
        buyer.add_item(seller_item)
        seller.remove_item(seller_item)
    else:
        print(f'{buyer.name}: No thank you {seller.name}')


print('yeet')
