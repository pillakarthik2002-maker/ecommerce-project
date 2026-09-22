# E-Commerce Website

A beginner-friendly E-Commerce Website developed using **Python and Django**.

This project provides a simple online shopping system where users can manage their accounts, browse products, add products to a cart, and place orders.

---

## About the Project

The E-Commerce Website is a Django-based web application created to understand the development of a real-world shopping website.

The project is divided into different Django applications such as:

- Accounts
- Products
- Cart
- Orders

The project uses Django templates, HTML, CSS, and SQLite3 for the database.

---

## Features

### User Account

- User registration
- User login
- User logout
- User authentication

### Products

- Display products
- View product information
- Product management through Django Admin

### Shopping Cart

- Add products to cart
- View cart items
- Manage cart items
- Calculate cart details

### Orders

- Place orders
- Manage orders
- View order information

### Admin Panel

Django Admin is used to manage the application data.

Administrators can manage:

- Users
- Products
- Orders
- Cart-related data

---

## Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite3
- Django Templates
- Git
- GitHub

---

## Project Structure

```text
EcommerceProject/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── cart/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── ecommerce_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── orders/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── products/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── static/
│
├── templates/
│
├── media/
│
├── manage.py
│
└── .gitignore
````

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pillakarthik2002-maker/ecommerce-project.git
```

### 2. Open the Project Folder

```bash
cd ecommerce-project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

If the project contains a `requirements.txt` file, you can install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## Database Setup

Run Django migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## Create Superuser

To access the Django Admin Panel:

```bash
python manage.py createsuperuser
```

Enter:

* Username
* Email
* Password

---

## Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

## Django Admin

The Django Admin Panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials created earlier.

---

## Application Modules

### Accounts

Responsible for user-related functionality such as registration, login, and authentication.

### Products

Responsible for displaying and managing products.

### Cart

Responsible for shopping cart functionality.

### Orders

Responsible for order-related functionality.

---

## Static and Media Files

The project contains separate folders for static and uploaded media files.

```text
static/
media/
```

Static files are used for website styling and other static resources.

Media files are used for uploaded content such as product images.

---

## Database

The project uses **SQLite3** as the database.

The database file is excluded from GitHub using `.gitignore`.

```text
db.sqlite3
```

This means the local database will not be uploaded to the repository.

---

## Git and GitHub

Git is used for version control, and GitHub is used to store and share the project source code.

The project includes a `.gitignore` file to prevent unnecessary files from being uploaded.

Files and folders ignored include:

* Virtual environments
* Python cache files
* SQLite database
* Environment variables
* IDE configuration files

---

## What I Learned

Through this project, I learned:

* Django project structure
* Django applications
* Django models
* Django views
* Django templates
* URL routing
* User authentication
* CRUD operations
* Shopping cart functionality
* Order management
* Static and media files
* SQLite database
* Django Admin
* Git and GitHub

---

## Future Enhancements

The project can be further improved by adding:

* Product search
* Product categories
* Product filtering
* Product reviews and ratings
* Wishlist
* Online payment integration
* Order tracking
* User profile management
* Email notifications
* Responsive UI improvements

---

## Author

**Karthik**

Master of Computer Applications (MCA)

---

## GitHub Repository

```text
https://github.com/pillakarthik2002-maker/ecommerce-project
```

---

