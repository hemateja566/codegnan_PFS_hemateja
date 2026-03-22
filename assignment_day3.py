print("--- Inventory Management System ---")

# 1. Assignment Operators
    
apples_stock = 50    
oranges_stock = 100
apple_price = 1.50
orange_price = 0.75
    
# 2. Arithmetic Operators
total_apples_value = apples_stock * apple_price
total_oranges_value = oranges_stock * orange_price
total_inventory_value = total_apples_value + total_oranges_value
average_price = total_inventory_value / (apples_stock + oranges_stock)
    
print(f"\nInitial total inventory value: ${total_inventory_value:.2f}")
print(f"Average item price: ${average_price:.2f}")
    
# Floor division (//) and Modulo (%)
boxes_of_apples = apples_stock // 10
remaining_apples = apples_stock % 10
print(f"Apples can fill {boxes_of_apples} boxes (10 per box) with {remaining_apples} left over.")

# 3. Comparison Operators
# Check if stock levels are low
low_stock_threshold = 20
is_apples_low = apples_stock <= low_stock_threshold
is_oranges_low = oranges_stock < low_stock_threshold
    
print(f"\nIs apple stock below threshold? {is_apples_low}")
print(f"Is orange stock below threshold? {is_oranges_low}")

# 4. Logical Operators
# Decide if an order is needed based on both stocks
need_restock = is_apples_low or is_oranges_low
print(f"Need to restock inventory? {need_restock}")
    
# 5. Assignment Operators (compound)
# A shipment arrives
apples_received = 30
oranges_sold = 15
    
apples_stock += apples_received # Equivalent to apples_stock = apples_stock + apples_received
oranges_stock -= oranges_sold   # Equivalent to oranges_stock = oranges_stock - oranges_sold
    
print(f"\nUpdated apple stock after shipment: {apples_stock}")
print(f"Updated orange stock after sales: {oranges_stock}")

# 6. Membership Operators
# Check if certain fruits are in a specific list
available_fruits = ["apple", "banana", "orange", "grape"]
check_fruit_1 = "apple" in available_fruits
check_fruit_2 = "kiwi" in available_fruits
    
print(f"\nIs 'apple' in the available fruits list? {check_fruit_1}")
print(f"Is 'kiwi' in the available fruits list? {check_fruit_2}")
    
# 7. Identity Operators
# Check if two variables point to the same memory location
# Different lists, same content (== True, is False)
list1 = ["apple", "orange"]
list2 = ["apple", "orange"]
list3 = list1
    
print(f"\nDo list1 and list2 have the same identity? {list1 is list2}") # Compares memory location
print(f"Do list1 and list3 have the same identity? {list1 is list3}") # Points to the same object
print(f"Are list1 and list2 equal in value? {list1 == list2}") # Compares value

# 8. Bitwise Operators (applied to stock IDs for demonstration)
# Simple example of bitwise operations for status flags or IDs
status_apples = 5  # Binary: 0101 (e.g., in stock, popular)
status_oranges = 3 # Binary: 0011 (e.g., in stock, on sale)
    
# Bitwise AND (&) - find common flags
common_status = status_apples & status_oranges
# Bitwise OR (|) - combine all flags
combined_status = status_apples | status_oranges
    
print(f"\nApple status binary: {bin(status_apples)}, Orange status binary: {bin(status_oranges)}")
print(f"Common status (Bitwise AND): {common_status} ({bin(common_status)})")
print(f"Combined status (Bitwise OR): {combined_status} ({bin(combined_status)})")

