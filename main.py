class Second:
    color = input("Ievadiet krāsu:")
    form = input("Ievadiet formu:")
  
    #color = "red"
    #form = "circle"
    def changecolor(self,newcolor):
        self.color = newcolor
    def changeform(self,newform):
        self.form = newform
obj1 = Second()
obj2 = Second()
print (obj1.color, obj1.form) # izvade "red circle"
print (obj2.color, obj2.form) # izvade "red circle"
color2=input("Ievadiet jaunu krāsu:")
obj1.changecolor(color2) # pirmā objekta krāsas maiņa
obj2.changecolor("blue") # otrā objekta krāsas maiņa
obj2.changeform("oval") # otrā objekta formas maiņa
print (obj1.color, obj1.form) # izvade "green circle"
print (obj2.color, obj2.form) # izvade "blue oval"