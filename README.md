<h1>Description :</h1>
A multi-user application that leverages the power of technology to provide an efficient and user-friendly platform that assists store managers, staff, and customers in various aspects of grocery shopping and management. It allows for improved customer experience, better inventory management, accurate sales analysis, and reduced manual work.

<h1>Technologies :</h1>
    <ul>
        <li>💻 Flask: backend of the application.</li>
        <li>💻 SQLAlchemy: Object-Relational Mapping (ORM), database management and queries.</li>
        <li>💻 HTML, CSS, JavaScript: Frontend, creating user interfaces, enhancing user experience.</li>
        <li>💻 AJAX: Single page applications, background querying.</li>
        <li>💻 Plotly: graphing library used to create charts and graphs.</li>
        <li>💻 SQLite: database engine(serverless) for storing application data.</li>
        <li>💻 Bootstrap: frontend framework for responsive design and styling.</li>
        <li>💻 Jinja2 templates: HTML generation</li>
    </ul>

<h1>DB schema design : </h1>
    The database has several models/tables created: 
    Users, Managers, Category, Products, Orders_Desc, Order_Details


<h1>API design : </h1>
    APIs for interaction with sections and products
    CRUD on sections
    CRUD on products
    APIs for getting the sections/products to display – products are listed under corresponding categories
    Validation
    All form inputs fields - text, numbers, dates, etc. with suitable messages
    Backend validation before storing/selecting from the database

<h1>Architecture and Features : </h1>
    a. The project is organized using the Model-View-Controller (MVC) architecture, with the controllers handling logic and routing, templates for displaying views, and models for interacting with the database. 
    b. Features implemented include : 
        Admin/Store Manager login and User login
        User Registration
        Category Management (for the manager only)
            Create a new category (handles multiple languages - utf8 encoding)
            View the created category and products under it
            Edit a category
            Delete a category
        Product Management (for the manager only)
            Create a new product under a category (multiple language input - utf8 encoding)
            View a created product and details
            Edit a product’s details
            Delete a product
        Display all available categories with products listed under them (manager and user)
        Buy products from one or multiple Categories (for user)
            Add to cart
            View cart
            Delete products from the cart
            Edit quantities of products in the cart
            Show the total amount to be paid for the transaction.
            Shows out-of-stock products before adding them to the cart
        Search for Category/Product (manager and user)
            Search by Category name
            Search by Product name
            Search products with an upper limit on pricing 

<h1>Additional features : </h1>
    1. Styling and Aesthetics
    2. Export section/product engagement (for manager):
    Provides category-wise and product-wise graphs of sales within a given timeline 
    3. Update existing stock-based user checkout
    4. Ability to update stock of products in a cart when it is checked out
