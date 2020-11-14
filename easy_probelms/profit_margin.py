''' Create a function that calculates the profit margin given cost_price and
    sales_price. Return the result as a percentage formated string, and rounded
    to one decimals. To calculate profit margin you subtract the cost from the
    sales price, then divide by salesprice.'''


def profit_margin(cost_price, sales_price):
    return str(round((sales_price - cost_price) / sales_price * 100, 1)) + "%"

print(profit_margin(50, 50))
print(profit_margin(28, 39))
print(profit_margin(33, 84))

