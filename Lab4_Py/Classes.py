class Date:
    def __init__(self, year, month, day):
        self.year=year 
        self.month=month 
        self.day=day 
    def show(self):
        print("Date:%02d/%02d/%4d"%(self.day, self.month, self.year))
class Thing:
    def __init__(self, name, made_y, made_m, made_d, price, amount):
        self.name=name 
        self.made=Date(made_y, made_m, made_d)
        self.price=price 
        self.amount=amount 
    def all_price(self):
        return self.price*self.amount
    def check_date(self, how_long):
        d=self.made.day+how_long.day
        m=self.made.month+how_long.month+d//31
        y=self.made.year+how_long.year+m//13
        d1=d%30
        m1=m%12
        if d%30==0:
            d1=30
        if m%12==0:
            m1=12
        good=Date(y, m1, d1)
        return good 
    def show1(self):
        print(self.name)
        self.made.show()
        print("Price:"+str(self.price)+"; Amount:"+str(self.amount))
class Prom(Thing):
    def __init__(self, name, made_y, made_m, made_d, price, amount, transport, place):
        super().__init__(name, made_y, made_m, made_d, price, amount)
        self.transport=transport 
        self.place=place 
    def show(self):
        super().show1()
        print("Transporting way:"+self.transport)
        print("Place to store:", end="")
        if self.place==0:
            print("Stock")
        else:
            print("Shop")
class Eat(Thing):
    def __init__(self, name, made_y, made_m, made_d, price, amount, long_y, long_m, long_d):
        super().__init__(name, made_y, made_m, made_d, price, amount)
        self.how_long=Date(long_y, long_m, long_d)
    def is_bad(self, today):
        bad=True
        good_day=super().check_date(self.how_long) 
        if today.year<good_day.year:
            bad=False 
        elif today.year==good_day.year and today.month<good_day.month:
            bad=False
        elif today.year==good_day.year and today.month==good_day.month and today.day<=good_day.day:
            bad=False
        return bad
    def show(self):
        super().show1()
        print("You can store this product", self.how_long.year, "years,", self.how_long.month, "months and",
              self.how_long.day, "days")