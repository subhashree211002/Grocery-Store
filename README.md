<h1>Description :</h1>
A multi-user application that leverages the power of technology to provide an efficient and user-friendly platform that assists store managers, staff, and customers in various aspects of grocery shopping and management. It allows for improved customer experience, better inventory management, accurate sales analysis, and reduced manual work.

<h1>Technologies :</h1>
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

<h1>DB schema design : </h1>
    The database has several models/tables created: Users, Managers, Category, Products, Orders_Desc, Order_Details
    

<h1>API design : </h1>
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

<h1>Architecture and Features : </h1>
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

<h1>Additional features : </h1>
    <ol>
        <li>Styling and Aesthetics</li>
        <li>Export section/product engagement (for manager):</li>
            <ul><li>Provides category-wise and product-wise graphs of sales within a given timeline</li></ul>
        <li>Update existing stock-based user checkout</li>
        <li>Ability to update stock of products in a cart when it is checked out</li>
    </ol>
