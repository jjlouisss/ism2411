# Self-Assesment 
# 1. The most surprising thing about Python lists is how easy it is
# to add, remove, and sort items without rewriting the whole list.
# I also didn't expect negative indexing to make accessing items so simple.
# 2. In a retail store, Python lists could be used to track daily
# sales and calculate total revenue. Instead of manually entering
# and calculating everything in Excel, a Python loop could quickly
# find the average sales and identify the best-selling days.

# Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(f"{inventory}")
print(f"{len(inventory)}")
print()

# Exercise 2

print(f"First item: {inventory[0]}")
print(f"Last item: {inventory[-1]}")
print(f"Middle item: {inventory[len(inventory) // 2]}")
print()

# Exercise 3

print(f"First three: {inventory[:3]}")
print(f"Last two: {inventory[-2:]}")
print(f"Every other: {inventory[::2]}")
print()

# Exercise 4

inventory.append("envelope")
print(f"After append: {inventory}")

inventory.remove("tape")
print(f"After remove: {inventory}")

inventory.sort()
print(f"After sort: {inventory}")
print()

# Exercise 5

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print(f"TypeError caught: Tuples cannot be changed.")
    print(f"Tuples are useful for coordinates because values stay unchanged.")

print(f"Coordinates: {coords}")
print()

# Exercise 6

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Best: {best}")
print(f"Worst: {worst}")
print()

# Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print(f"Original: {prices}")
print(f"Discounted: {discounted}")
print()

# Exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

count = len(high_sales)
average = sum(high_sales) / count

print(f"High Sales: {high_sales}")
print(f"Count: {count}")
print(f"Avg: {average:.2f}")
print()