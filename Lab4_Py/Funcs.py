import Classes
def create_proms(x, prom):
    for i in range(x):
        name=input("Enter the name:")
        made_y=int(input("Enter the date when the product was made. Year:"))
        made_m=int(input("Month:"))
        made_d=int(input("Day:"))
        price=int(input("Enter the price:"))
        amount=int(input("Enter the amount:"))
        transport=input("What is the way of thansporting? ")
        place=int(input("Where to store it? Press 0 for stock and 1 for shop: "))
        thing=Classes.Prom(name, made_y, made_m, made_d, price, amount, transport, place)
        prom.append(thing)
    for j in range(x):
        prom[j].show()
def create_eats(x, eats):
    for i in range(x):
        name=input("Enter the name:")
        made_y=int(input("Enter the date when the product was made. Year:"))
        made_m=int(input("Month:"))
        made_d=int(input("Day:"))
        price=int(input("Enter the price:"))
        amount=int(input("Enter the amount:"))
        long_y=int(input("Enter how long can you store it. Years:"))
        long_m=int(input("Months:"))
        long_d=int(input("Days:"))
        thing=Classes.Eat(name, made_y, made_m, made_d, price, amount, long_y, long_m, long_d)
        eats.append(thing)
    for j in range(x):
        eats[j].show()
def bad_products(x, eats):
    sum=0
    y=int(input("What date is it today? Year:"))
    m=int(input("Month:"))
    d=int(input("Day:"))
    today=Classes.Date(y, m, d)
    for i in range(x):
        if eats[i].is_bad(today)==True:
            sum+=eats[i].all_price()
    return sum
def stock_products(x, proms):
    sum=0
    for i in range(x):
        if proms[i].place==0:
            sum+=proms[i].all_price()
    return sum
def show(bads, stock):
    print("The total price of bad products is:", bads)
    print("The total price of stock products is:", stock)