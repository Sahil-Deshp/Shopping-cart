from flask import Flask, render_template, request, redirect, url_for, flash, session
from src.models.products import Electronics, Clothing, Grocery
from src.exceptions.custom_exceptions import OutOfStock

from decimal import Decimal

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.secret_key = 'your-secret-key'

# # Using session to store cart items
# @app._got_first_request
# def initialize_session():
#     if 'cart' not in session:
#         session['cart'] = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_product():
    try:
        product_type = request.form['product_type']
        name = request.form['name']
        price = float(request.form['price'])

        # Using polymorphism to create different product types
        if product_type == 'electronics':
            product = Electronics(name, price)
        elif product_type == 'clothing':
            product = Clothing(name, price)
        elif product_type == 'grocery':
            product = Grocery(name, price)
        else:
            raise OutOfStock("Invalid product type or product out of stock")
        
        # Check if price is valid
        if price <= 0:
            raise OutOfStock("Invalid price - must be greater than 0")

        # Store product details in session
        cart = session.get('cart', [])

        # Example: Limit items in cart to simulate stock
        if len(cart) >= 10:
            raise OutOfStock("Sorry, we're out of stock!")
        
        cart.append({
            'type': product_type,
            'name': product.name,
            'price': str(product.price),
            'details': product.get_details()
        })
        session['cart'] = cart

        flash('Product added successfully!', 'success')
        return redirect(url_for('view_cart'))

    except ValueError as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('index'))
    
    except OutOfStock as e:
        flash(f'Stock Error: {str(e)}', 'warning')
        return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total = sum(Decimal(item['price']) for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/clear')
def clear_cart():
    session['cart'] = []
    flash('Cart cleared!', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)