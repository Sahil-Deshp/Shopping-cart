# 🛒 Shopping Cart App

A modular, object-oriented shopping cart web application built with **Flask**. This project demonstrates clean architecture using MVC principles, custom exception handling, and a user-friendly interface for managing products and cart operations.

##💡 Object-Oriented Concepts Used

Encapsulation: Each component (e.g., Product, Cart) is defined as a class with its own attributes and methods, keeping logic self-contained.

Inheritance: Common behaviors are abstracted into base classes and extended where needed.

Polymorphism: Methods like add_item() or remove_item() behave differently depending on the object context.

Abstraction: Complex operations are hidden behind clean interfaces, making the app easier to maintain and extend.

## 📁 Project Structure

shopping-cart-app/ 
├── src/ 
│ ├── controllers/ # Business logic and cart operations │ ├── exceptions/ # Custom exception classes 
│ ├── models/ # Product data models 
│ ├── static/ # CSS styles 
│ ├── templates/ # HTML templates (Jinja2) 
│ ├── views/ # GUI and main app logic 
│ ├── tests/ # Unit tests 
├── README.md # Project documentation 
├── requirements.txt # Python dependencies


## 🚀 Features

- Add, remove, and update items in the cart
- View cart summary and total price
- Modular MVC architecture for scalability
- Custom exception handling for robust error management
- Responsive UI using HTML/CSS templates
- Easily extendable product model

## 🧠 Technologies Used

- **Python 3.10+**
- **Flask**
- **Jinja2**
- **HTML/CSS**
- **OOP principles**

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/shopping-cart-app.git
   cd shopping-cart-app```

2.**Create a virtual environment**
  ```python -m venv venv
    source venv/bin/activate  
    # On Windows: venv\Scripts\activate
  ```

3.**Install dependencies**
  pip install -r requirements.txt


4.**Run the application**
  python src/views/main.py

5.**Access the app**
  Open your browser and go to http://localhost:5000


📌 Future Improvements
Add user authentication

Integrate a database (e.g., SQLite or PostgreSQL)

Implement product categories and search

Add RESTful API endpoints

👨‍💻 Author
Developed by Sahil, a passionate data and software enthusiast focused on building impactful, user-friendly applications


