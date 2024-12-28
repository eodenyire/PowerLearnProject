# Week 3 Assignment

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.

    Returns:
    float: The final price after applying the discount, or the original price if discount < 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Prompt user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate and print the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    if final_price < original_price:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print("No discount applied. The original price is:", original_price)
except ValueError:
    print("Please enter valid numerical inputs for the price and discount percentage.")
