def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }

def add_to_cart(cart, name, price, qty):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })

def update_price(price_info, new_price):
    try:
        price_info[0] = new_price
    except TypeError:
        print("Tuple is immutable!")

def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]

    total -= total * cart["discount"] / 100
    return total


cart1 = create_cart("Harini",10)
cart2 = create_cart("Rahul",5)

add_to_cart(cart1,"Book",200,2)
add_to_cart(cart1,"Pen",20,5)

add_to_cart(cart2,"Laptop",50000,1)

print(cart1)
print("Total:",calculate_total(cart1))

print(cart2)
print("Total:",calculate_total(cart2))

price = ("Book",200)
update_price(price,300)

# Discussion:
# discount=0 is safe because it is immutable.
# cart=[] is dangerous because lists are mutable.
# Mutable: list, dict, set
# Immutable: int, float, str, tuple
# Changes to mutable objects inside functions are reflected outside.
