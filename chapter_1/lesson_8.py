"""
Calculating with dictionaries
It is often the case that zip will be useful for that
"""
prices = {
    'acme': 45,
    'aap': 10,
    'foo': 0,
    'fb': 50
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

print('Min price: {0} \n Max price: {1} \n prices_sorted: {2}'.format(min_price, max_price, prices_sorted))
