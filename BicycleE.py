class EBicyle:
    def __init__(self):
        self.power = int(50)
        
        
    def charge(self):
        self.power = 50

    def run(self,km):
        if km/10 > self.power:
            self.km = self.power*10
            print('Power is not enough for your way.')
            return self.km
            
        self.power -= km/10
        print('Power:%.2f%%' % (self.power/50*100))
        

class Bicycle(EBicyle):
    def __init__(self, km):
        super().__init__()
        self.km = km



    def Run(self):
        self.run(self.km)
        print('The bicycle runs %.2fkm' %self.km)
        

Bicycle(1000).Run()

    
