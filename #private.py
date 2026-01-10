#private
#private attribute and methods are meant to be used inky within the class 
# and are accesible outside the class 

class account:
    def __init__(self,acc_no,acc_psd):
        self.acc=acc_no
        self.__psd=acc_psd


acc1=account("1","123")
print(acc1.acc,acc1.psd)  