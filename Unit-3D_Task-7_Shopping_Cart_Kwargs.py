# Unit 3D - Task 7: Shopping Cart Using **kwargs
def shopping_cart(**products):
    total = 0
    for item, price in products.items():
        print(item, ": Rs.", price)
        total = total + price
    print("Total amount: Rs.", total)

shopping_cart(apple=15, orange=12, mango=10)
