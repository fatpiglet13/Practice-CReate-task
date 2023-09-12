restaurants = ["In N Out", "Mcdonalds", "Chick fil A", "Jack in the box", "Taco Bell"] 
new_res = input("What restaurant would you like to rank into your list?")
def rank_restaurant(new_res, restaurants):
    for i in range(len(restaurants)):
        rank = input("Do you like A) ", + new_res + "more or B)" + restaurants[i]+ "more? A/B")
        if rank == "A": 
            restaurants.insert(i,new_res)
            break
        elif rank == "B": 
            continue
    if new_res not in restaurants:
        restaurants.append(new_res)
    return restaurants

print("Your new ranking of restaurantts is ", rank_restaurant(new_res, restaurants))