<h1>Grocery Store Application</h1>
<h3>Description :</h3>
A multi-user application that leverages the power of technology to provide an efficient and user-friendly platform that assists store managers, staff, and customers in various aspects of grocery shopping and management. It allows for improved customer experience, better inventory management, accurate sales analysis, and reduced manual work.

<h3>Tech Stack:</h3>
<ul>
    <li>🛢  Flask: backend of the application.</li>
    <li>🌐 SQLAlchemy: Object-Relational Mapping (ORM), database management and queries.</li>
    <li>🌐 HTML, CSS, JavaScript: Frontend, creating user interfaces, enhancing user experience.</li>
    <li>💻 AJAX: Single page applications, background querying.</li>
    <li>💻 Plotly: graphing library used to create charts and graphs.</li>
    <li>🛢  SQLite: database engine(serverless) for storing application data.</li>
    <li>🌐 Bootstrap: frontend framework for responsive design and styling.</li>
    <li>🌐 Jinja2 templates: HTML generation</li>
</ul>

<h1>Getting Started</h1>
<h3>Prerequisites</h3>
<ul>
    <li>Python 3.x</li>
    <li>pip</li>
    <li>git</li>
    <li>sqlite3(DBBrowser)</li>
</ul>

 
<h3>Installation and Usage</h3>

1. Clone the repository.
    ```
    git clone https://github.com/subhashree211002/Grocery-Store.git
    ```
    
2. cd into your project directory
    ```
    cd path/to/your/folder
    ```
    
3.  For a windows system    
    - Run the run_app.bat file in the terminal
        ```
        ./run_app.bat
        ```
    - Alternatively you can execute the following step by step in the terminal
        - Create a virtual environment (if not already created):
          ```
          python3 -m venv .venv
          ```
        - Activate the virtual environment:
          ```
          .venv/bin/activate
          ```
        - Install project dependencies:
          ```
          pip install -r requirements.txt
          ```
        - Run the application:
          ```
          python main.py
          ```
        - Open a web browser and go to http://localhost:8080 to access the application.
          
        
4. For a linux system
    - Modify permissions for the run_app.sh bash file
        ```
        ./run_app.sh
        ```
    - Alternatively you can execute the following step by step in the terminal
        - Create a virtual environment (if not already created):
          ```
          python3 -m venv .venv
          ```
        - Activate the virtual environment:
          ```
          source .venv/bin/activate
          ```
        - Install project dependencies:
          ```
          pip install -r requirements.txt
          ```
        - Run the application:
          ```
          python main.py
          ```
        - Open a web browser and go to http://localhost:8080 to access the application.


<h1>Implementation Details</h1>
<h3>DB schema design : </h3>
    The database has several models/tables created: Users, Managers, Category, Products, Orders_Desc, Order_Details<br>
    <img src='https://github.com/subhashree211002/Grocery-Store/assets/67853431/d21301fc-24e4-474f-8951-691375c8ab38'><br>
    <img src='https://github.com/subhashree211002/Grocery-Store/assets/67853431/a7203b1d-b893-4694-afa5-e75a5cba8ea1'>



<h3>API design : </h3>
    <ul>
        <li>APIs for interaction with sections and products</li>
            <ul>
                <li>CRUD on sections</li>
                <li>CRUD on products</li>
                <li>APIs for getting the sections/products to display – products are listed under corresponding categories</li>
            </ul>
        <li>Validation</li>
            <ul>
                <li>All form inputs fields - text, numbers, dates, etc. with suitable messages</li>
                <li>Backend validation before storing/selecting from the database</li>
            </ul>
    </ul>

<h3>Architecture and Features : </h3>
    <ol type='a'>
        <li> The project is organized using the Model-View-Controller (MVC) architecture, with the controllers handling logic and routing, templates for displaying views, and models for interacting with the database. </li>
        <li>Features implemented include : </li>
            <ol>
                <li>Admin/Store Manager login and User login</li>
                <li>User Registration</li>
                <li>Category Management (for the manager only)</li>
                    <ul>
                        <li>Create a new category (handles multiple languages - utf8 encoding)</li>
                        <li>View the created category and products under it</li>
                        <li>Edit a category</li>
                        <li>Delete a category</li>
                    </ul>
                <li>Product Management (for the manager only)</li>
                    <ul>
                        <li>Create a new product under a category (multiple language input - utf8 encoding)</li>
                        <li>View a created product and details</li>
                        <li>Edit a product’s details</li>
                        <li>Delete a product</li>
                    </ul>
                <li>Display all available categories with products listed under them (manager and user)</li>
                <li>Buy products from one or multiple Categories (for user)</li>
                    <ul>
                        <li>Add to cart</li>
                        <li>View cart</li>
                        <li>Delete products from the cart</li>
                        <li>Edit quantities of products in the cart</li>
                        <li>Show the total amount to be paid for the transaction.</li>
                        <li>Shows out-of-stock products before adding them to the cart</li>
                    </ul>
                <li>Search for Category/Product (manager and user)</li>
                    <ul>
                        <li>Search by Category name</li>
                        <li>Search by Product name</li>
                        <li>Search products with an upper limit on pricing</li>
                    </ul>
            </ol>
    </ol>

<h3>Additional features : </h3>
    <ol>
        <li>Styling and Aesthetics</li>
        <li>Export section/product engagement (for manager):</li>
            <ul><li>Provides category-wise and product-wise graphs of sales within a given timeline</li></ul>
        <li>Update existing stock-based user checkout</li>
        <li>Ability to update stock of products in a cart when it is checked out</li>
    </ol>
