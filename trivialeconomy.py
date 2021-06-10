#!/usr/bin/env python3

class Asset:
    def __init__(self, name, amount=0, buy_price=None, sell_price=None):
        self.name = name
        self.amount = amount
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.buy_action = None
        self.sell_action = None


gold = Asset("Gold", amount=100)
farmland = Asset("Farmland", buy_price=10, sell_price=9)
wheat = Asset("Wheat", buy_price=0.02, sell_price=0.01)
rats = Asset("Rats")
cats = Asset("Cats", buy_price=1)

assets = [
    gold,
    farmland,
    wheat,
    rats,
    cats,
]

asset_index = dict((g.name, g) for g in assets)

actions = [None]
for g in assets:
    if g.buy_price:
        g.buy_action = len(actions)
        actions.append((g, True))
    if g.sell_price:
        g.sell_action = len(actions)
        actions.append((g, False))

while True:
    print(
        """\nYour property:
    Asset          Amount    |   Buy   Price        Max   |   Sell  Price
"""
    )

    for g in assets:
        max_buy_amount = None
        if g.buy_price:
            max_buy_amount = int(gold.amount / g.buy_price)
        print(
            "    {:10} {:10}    |   ({:2})  {:5} {:10}   |   ({:2})  {:5}".format(
                g.name,
                g.amount,
                g.buy_action or "",
                g.buy_price or "",
                max_buy_amount or "",
                g.sell_action or "",
                g.sell_price or "",
            )
        )

    print(
        """
    (0) Advance to next year
    (quit) Done playing
"""
    )

    action = None
    while action not in range(0, len(actions)):
        action = input("Action: ")
        if action == "quit":
            quit()
        try:
            action = int(action)
        except Exception:
            action = None

    if action == 0:
        sowing = min(wheat.amount, farmland.amount * 100)
        used_land = sowing / 100

        harvest = sowing * 10
        wheat.amount -= sowing

        rotted = wheat.amount // 5
        wheat.amount -= rotted
        wheat.amount += harvest

        rat_birth = wheat.amount // 200
        rats.amount += rat_birth

        max_rats = wheat.amount // 70
        rat_starved = max(0, rats.amount - max_rats)
        rats.amount -= rat_starved

        rat_eaten = int(min(rats.amount * 0.9, cats.amount * rats.amount / farmland.amount))
        rats.amount -= rat_eaten

        rat_feed = int(min(wheat.amount * 0.9, 10 * rats.amount))
        wheat.amount -= rat_feed

        cat_cost = cats.amount
        gold.amount -= cat_cost

        print(
            f"""
{used_land} of {farmland.amount} land was used to grow crops.
{sowing} wheat was sown, resulting in a harvest of {harvest}.
{rotted} wheat rotted in the stocks.
{rat_feed} wheat was eaten by rats.
Your cats caught {rat_eaten} rats, and did cost {cat_cost} gold.
"""
        )

    else:
        asset, buy = actions[action]

        amount = None
        while amount is None:
            amount = input("Amount: ")
            try:
                amount = int(amount)
            except Exception:
                amount = None

        if buy:
            cost = amount * asset.buy_price
            if cost > gold.amount:
                print(f"Your funds are only sufficient for buying {gold.amount // asset.buy_price} {asset.name}\n")
            else:
                gold.amount -= cost
                asset.amount += amount
        else:
            cost = amount * asset.sell_price
            if amount > asset.amount:
                print(f"Your stock only consists of {asset.amount} {asset.name}\n")
            else:
                gold.amount += cost
                asset.amount -= amount
