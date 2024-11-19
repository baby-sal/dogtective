# imports relevant files
import requests
import json

def get_all_items_front_end():
    endpoint = "http://127.0.0.1:5000/menu_items"
    result = requests.get(endpoint).json()
    return result

# API interaction functions
"""Implement 2 API endpoints with appropriate functionality 
- GET /menus: This endpoint retrieves the entire menu for a specific store or restaurant &
 POST /menus/items: This endpoint adds a new item to the menu."""
# GET /desserts - API endpoint1: Fetches a list of all desserts from the server.
def delete_a_dessert_by_id(id):
    endpoint = f"http://127.0.0.1:5000/menu_items/remove/{id}"
    result = requests.delete(endpoint).json()
    return result
# DELETE /desserts/{dessert_id} - API end point additional: Deletes a dessert by its ID from the server.

def add_a_new_menu_item(sprite_id, name, damage, health):

    new_item = {
         "sprite_id": sprite_id,
         "name": name,
         "damage": damage,
         "health": health,
    }

    result = requests.put(
        'http://127.0.0.1:5000/men_items',
        headers={'content-type': 'application/json'},
        data=json.dumps(new_item)
    )

    return result.json()

## have a run() function and Implement client-side for each of the 3 API endpoints you have created.
# def function()
def main():
    print("Welcome to the Dogdetective!, Choose an option:")
    print("A: View all menu items")
    print("B: Remove an item by ID")
    print("C: Add a sprite to the game board")

    answer = input("What would you like to do? (A, B or C): ").strip().upper()

    if answer == "A":
        if get_all_items_front_end() is None:
            print("Failed to retrieve records.")

        print(get_all_items_front_end())
    elif answer == "B":
        characters = get_all_items_front_end()
        print("Here is the registry: \n")
        print(characters)
        if characters is not None:
            id_to_remove = input("\nEnter the ID of the character you would like to remove: ").strip()
            print("Student removed from registry")
            print("Here is the registry:")
            print(delete_a_dessert_by_id(id_to_remove))
        else:
            print("Could not load characters for deletion.")
    elif answer == "C":
        sprite_id = int(input('a number over 3: '))
        name = input('add a dessert you would like to see on the menu')
        damage = input('add a description for what you want in the dessert')
        health = float(input('enter a decimal price'))
        add_a_new_menu_item(sprite_id, name, damage, health)
        print("thank you for your feedback, we will look at getting this item added to the menu ASAP")
    else:
        print("Invalid option. Please select either A, B or C.")

def server_request():
    response = requests.get('http://127.0.0.1:5000')
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":# special in built function """__name__: This is a special built-in variable in Python.
    # When a Python script is run, the interpreter sets the __name__ variable. If the script is being run directly,
    # __name__ is set to "__main__". If the script is being imported as a module in another script,
    # __name__ is set to the script’s name."""
    server_request()
    main()# calls the run function, executing it.


