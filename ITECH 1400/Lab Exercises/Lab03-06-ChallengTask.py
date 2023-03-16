user_orders = list()
pizza_cost = {"S":10, "M":12, "L":14}
total_cost = 0

print("\nWelcome to Pizza Calculator\n")

want_more = True
while(want_more):
    print("SMALL pizza cost $10, MEDIUM pizza cost $12, and LARGE pizzas cost $14")
    total_cost = total_cost + pizza_cost[input("Please select your desired Pizza Size (S/M/L)")]

    print("First Three (3) Toppings are FREE, any toppings beyond that will cost a dollar per topping.")
    topping_count = int(input("How many toppings would you like to get 1-6)?"))
    total_cost = total_cost + 0 if topping_count <= 3 else topping_count - 3

    want_more = input("Do you want to add another pizza (Y/N)").upper == 'Y'
    
    if(not want_more):
       break

print("Thank you for using our service.")

