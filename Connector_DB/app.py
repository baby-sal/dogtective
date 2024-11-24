
import requests
from flask import Flask, jsonify, request
from db_utils import get_all_desserts, delete_dessert_by_id, add_new_dessert_item

app = Flask(__name__) #dunder "name"
@app.route('/menu_items', methods=['GET']) # defines a route to handle GET requests to /menu_items
def get_all_items_requested():
    return jsonify(get_all_requestable_items())
# returns all dessert menu items

@app.route("/menu_items/remove/<int:id>", methods=["DELETE"]) # removes an item from the dessert menu
def delete_item():
    return jsonify(delete_dessert_by_id(id))
# removes a dessert from the menu item

@app.route('/menu_items', methods=['PUT'])
def add_new_requestable_item():
    new_item = request.get_json()
    add_new_dessert_item(
        dessert_id=new_item['dessert_id'],
        name=new_item['name'],
        description=new_item['description'],
        price=new_item['price'],
    )

    return new_item

if __name__ == "__main__": # ensures the application only runs if the script is executed directly
    app.run(debug=True) # starts the Flask development server with the debug model enabled