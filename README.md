**Flask Bliss Bites Application**

This is a simple Flask application that showcases a basic E-Commerce website for displaying products. The application follows the provided requirements to create three routes: a home page, a products listing page, and a product details page. No database is required for this assignment; product information is stored in a Python list, and product photos are stored in the 'static' directory of the application.

**Requirements**

1. **Routes:**
    a. **Home Page ("/")**: Displays the team name, developer's name, and a photo.
    b. **Products Listing ("/products")**: Displays a list of at least four products with their images, titles, and prices. Users can click on the product title or image to view more details.
    c. **Product Details ("/products/<product_id>")**: Displays a single product's title, image, short description, and price. An "Add to Cart" button is provided.

2. **Templates:**
    - The application uses templates stored in the 'templates' directory.
    - A base template is created and extended by each route's template.

3. **Styling:**
    - Bootstrap CSS framework is used for styling.
    - The application's styling can be customized to suit the developer's preferences.

4. **Data Storage:**
    - Product information is stored as hard-coded values in a Python list.
    - Product photos are stored in the 'static' directory.

**Usage**

1. Clone the repository:
   ```
   git clone git@github.com:shae1994/BlissBites.git
   ```

2. Install Flask and required dependencies:
   ```
   pip install Flask
   ```

3. Navigate to the project directory:
   ```
   cd BlissBites
   ```

4. Run the Flask application:
   ```
   flask run
   ```

5. Open a web browser and go to `http://localhost:5000` to access the home page.

**Directory Structure**

```
BlissBites/
│
├── static/
│   ├── css/
│   ├── images/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── product_list.html
│   ├── product_details.html
│
├── app.py
├── README.md
```

**Notes**

- This application serves as a basic example and doesn't include actual shopping cart functionality or interactivity.

Feel free to customize and enhance the application as needed for your individual assignment. Happy coding!