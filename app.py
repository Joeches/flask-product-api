from flask import Flask, jsonify, request, abort
from threading import Lock
import logging
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory data structure to store products
products = {}
product_id_counter = 1
lock = Lock()  # To handle concurrent requests


@app.route('/products', methods=['POST'])
def create_product():
    """Create a new product."""
    global product_id_counter
    data = request.get_json()

    if not data or 'name' not in data or 'price' not in data:
        logger.warning("Invalid input: 'name' and 'price' are required.")
        abort(400, description="Invalid input: 'name' and 'price' are required.")

    with lock:
        product_id = product_id_counter
        products[product_id] = {
            'id': product_id,
            'name': data['name'],
            'price': float(data['price'])  # Ensure price is stored as a float
        }
        product_id_counter += 1

    logger.info(f"Product created: {products[product_id]}")
    return jsonify(products[product_id]), 201


@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all products."""
    logger.info("Retrieved all products.")
    return jsonify(list(products.values())), 200


@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    """Retrieve a specific product by ID."""
    product = products.get(id)
    if not product:
        logger.error(f"Product not found: {id}")
        abort(404, description="Product not found.")

    logger.info(f"Retrieved product: {product}")
    return jsonify(product), 200


@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    """Update an existing product."""
    if id not in products:
        logger.error(f"Attempted to update non-existent product: {id}")
        abort(404, description="Product not found.")

    data = request.get_json()

    if not data or ('name' not in data and 'price' not in data):
        logger.warning("Invalid input: at least one of 'name' or 'price' is required.")
        abort(400, description="Invalid input: at least one of 'name' or 'price' is required.")

    with lock:
        if 'name' in data:
            products[id]['name'] = data['name']
        if 'price' in data:
            products[id]['price'] = float(data['price'])  # Ensure price is updated as a float

    logger.info(f"Updated product: {products[id]}")
    return jsonify(products[id]), 200


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    """Delete a specific product by ID."""
    if id not in products:
        logger.error(f"Attempted to delete non-existent product: {id}")
        abort(404, description="Product not found.")

    with lock:
        del products[id]

    logger.info(f"Product deleted: ID {id}")
    return jsonify({'message': 'Product deleted successfully.'}), 200


@app.errorhandler(400)
def bad_request(error):
    """Handle bad request errors."""
    logger.error(f"Bad request: {error}")
    return jsonify({'error': str(error)}), 400


@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    logger.error(f"Not found: {error}")
    return jsonify({'error': str(error)}), 404


if __name__ == '__main__':
    # Use environment variable for debug mode; default to False
    debug_mode = os.getenv('FLASK_DEBUG', '0') == '1'

    app.run(debug=debug_mode)

