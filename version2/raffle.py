"""Randomly pick customer and print customer info"""

# Add code starting here
from random import choice
from customers import get_customers_from_file

# Hint: remember to import any functions you need from
# other files or libraries
def pick_random_customer():
    cust_list = get_customers_from_file('customers.txt')
    random_customer = choice(cust_list)
    print(f'Contact {random_customer.name} at {random_customer.email} living at {random_customer.street}, {random_customer.city} {random_customer.zipcode} that they won.')

if __name__ == '__main__':
    pick_random_customer()
