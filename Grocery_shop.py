
print("      Hello Friends! ")
print("   What Item do you want to buy ?")
print("   You may Check our Product_List")
product = ["Rice", "Cereal", "Soap", "Biscuit", "Chips"]
catagory = ({"Basmati Rice": 90,
            "Gouri": 85,
             "Gobindovog": 79,
             "Golden Silky Rice": 26,
             "Normal Rice": 50},
            {"Arhar Dal": 271,
             "Toor Dal": 212,
             "Chana Dal": 150,
             "Green Moong Dal": 200,},
            {"Fiama Gel Bar": 192,
             "Dettol": 206,
             "Pears": 192,
             "Dove": 312,
             "Santoor": 132,
             "Savlon": 150,},
            {"Little heart": 13,
             "Parle g gold": 100,
             "Horlicks": 90,
             "Britannia": 30,},
            {"Lays": 40,
             "Kurkure": 45,
             "jolochip": 199,
             "maxx": 10,
             })

cart = []
price = []
while (1):
    x = input("Any Item do you want to buy? Press- y /  Press- n to exit")
    if x == "n":
        break
    if x == "y":
        print("Available products:")
        for i in product:
            print(i)
        p = input("What product do you want?")
        indx = product.index(p)
        for i, j in catagory[indx].items():
            print(i, ":", j)
        item = input("Which type do you want?")
        qnty = int(input("How many product you need??"))
        cart.append(item)
        price.append(catagory[indx][item] * qnty)
# if x=="yes":
print(cart, price)

total = sum(price)
print("____________ INVOICE_____________")
print("The Total Price is :", total)
print("""Go to Cart and Checkout....
      Thank You For Shopping With Us!""")
