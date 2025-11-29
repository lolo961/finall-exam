products = [
    ["noodles", 3],
    ["cheese", 5],
    ["crisp", 2],
    ["juice", 7],
    ["chocolate", 4]
]

print("Hello customer, choose the number of your product!\n")

print("Available products:\n")
for i, item in enumerate(products, start=1):
    name = item[0]
    price = item[1]
    print(f"{i}. {name} - ${price}")

choice = input("\nEnter the product number you want: ")

if not choice.isdigit():
    print("\noops, invalid number here :)")

else:
    choice = int(choice)
    if choice < 1 or choice > len(products):
        print("\noops, invalid number here :)")
    else:
        product_name = products[choice - 1][0]
        product_price = products[choice - 1][1]
        taxed_price = product_price * 1.15

        print(f"\nYou selected: {product_name}")
        print(f"Original price: ${product_price}")
        print(f"Price with 15% tax: ${taxed_price:.2f}")
