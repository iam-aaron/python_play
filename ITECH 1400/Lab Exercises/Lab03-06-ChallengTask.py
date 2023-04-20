pizza_cost_list = {"S":10, "M":12, "L":14}
pizza_size_list = {"S":"Small", "M":"Medium", "L":"Large"}
want_more = True
total_cost = 0
order_counter = 1
customer_orders = {}

print("\n\nWELCOME TO PIZZA CALCULATOR!\n")

while(want_more):
    print(f"\n\nORDER #{order_counter}\nSMALL pizza cost $10, MEDIUM pizza cost $12, and LARGE pizzas cost $14")
    order_size = input("Please select your desired Pizza Size (S/M/L): ").upper()
    pizza_cost = pizza_cost_list[order_size]
    total_cost += pizza_cost_list[order_size]

    print("\nFirst Two (2) Toppings are FREE, any toppings beyond that will cost a dollar per topping.")
    topping_count = input("How many toppings would you like to get 1-5)? ")

    
    topping_count_invalid = True
    while True:
        if(not topping_count.isdigit() or int(topping_count) > 5 or int(topping_count) < 1):
            print("Invalid input, please try again.")
            topping_count = input("How many toppings would you like to get 1-5)? ")
        else:
            topping_count = int(topping_count)
            break

    

    topping_cost = 0 if topping_count <= 2 else topping_count - 2
    total_cost += topping_cost

    customer_orders["ORDER "+str(order_counter)] = {str(pizza_size_list[order_size])+" pizza":pizza_cost, str(topping_count)+" toppings": topping_cost}

    want_more = input("\nDo you want to add another pizza (Y/N)? ").upper() == 'Y'
    order_counter += 1

    if(not want_more):
       break

print("\n\n\nHERE'S YOUR RECEIPT")
for key, value in customer_orders.items():
    print(f"\n {key} Details")
    for sub_key, sub_value in value.items():
        print(f"{sub_key:>15}:  ${float(sub_value)} ")

print(f"\n\nYOUR TOTAL BILL IS: ${float(total_cost)}")
print("\n\n\nThank you for using our service. Enjoy your pizza! \n\n")


