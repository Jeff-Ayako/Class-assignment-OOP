"""
This programme was developed by the following group members:
Jeff Ayako HSC
Clifford Kathurima
Jospine Njoroge
Tyron Okwara
Stacy Agoe
"""


import random
import math


class Circles:
    def __init__(self,radius):
        self.radius=radius  
    
    def Area(self,radius):
        area= math.pi*pow(radius,2)
        return area

    def Perimeter(self,radius):
        perimeter=math.pi*(2*radius)
        return perimeter

    def Diameter(self,radius):
        diameter=2*radius
        return diameter


generated_radius=[]#we created an empty list that will be filled dynamically in the for loop using the . append method
for i in range(1,11):
    random_radius=random.uniform(1.0,9.9)
    generated_radius.append(random_radius)# the . append adds new elements into an empty list above



    if len(generated_radius)==10:#this line is important as we only want a list to be created once else without wounld create many lists with different lengths
        generated_radius

        
for radius in generated_radius:
    circle_content=Circles(radius)
    print('The circle area is: ',circle_content.Area(radius))
    print('The circle diameter is: ',circle_content.Diameter(radius))
    print("The circle Perimeter is: ",circle_content.Perimeter(radius))
    print('\n')
    



