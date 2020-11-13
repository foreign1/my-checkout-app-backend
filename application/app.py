from flask import Flask, request, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
catalogue = {"Apple": {"cost": 0.60, "discount": 1/2, "discount_min": 1},
             "Orange": {"cost": 0.25, "discount": 2/3, "discount_min": 3}}

local_cart = {}


@app.route("/")
def home():
    return "<h2> Kindly direct all post requests to /api/v1/checkout/ "

@app.route("/api/v1/checkout/", methods = ['POST'])
def checkout():
    """Provides checkout logic."""
    """Will handle calculation of input"""
    try:
        data = request.get_json()
        generate_local_cart(data["shoppingCart"])
        cost_local_cart()
        apply_discount_to_cart(data)
        return json.dumps("{}c".format(cart_total()))
    except ValueError as identifier:
        return json.dumps({"error": "invalid input"})

def generate_local_cart(shopping_cart):
    local_cart.clear()
    for item in shopping_cart:
        if item in local_cart:
            continue
        local_cart[item] = {"count": shopping_cart.count(item)}

def cost_local_cart():
    for item in local_cart:
        local_cart[item]["cost"] = catalogue[item]["cost"] * \
            local_cart[item]["count"]


def cart_total():
    total = 0
    for item in local_cart:
        total += local_cart[item]["cost"]
    return total

def apply_discount_to_cart(data):
    for item in local_cart:
        if data["discount"][item]:
            # updates cost
            x = local_cart[item]["count"]
            rem = x % catalogue[item]["discount_min"]
            if rem:
                x = x-rem
            x = x * catalogue[item]["discount"] * catalogue[item]["cost"]
            local_cart[item]["cost"] = x + (rem * catalogue[item]["cost"])



