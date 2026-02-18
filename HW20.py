#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class items:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double(self):
        tomatosauce.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
pie = items(5, 10, 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989)
tomatosauce = items(50, 100, 1000)
tomato = items(0, 5000, 25000)
#3. Print the stock of all three objects and the cost of the second store item.
print(pie.stock, tomatosauce.stock, tomato.stock)
print(tomatosauce.cost)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
tomatosauce.double()
print(tomatosauce.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
tomato.stock /= 4
print(tomato.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del pie
try:
    print(pie.weight)
except:
    raise ValueError("THIS DOESNT EXIST ANYMORE WERE SOLD OUT PICK A NEW ITEM")