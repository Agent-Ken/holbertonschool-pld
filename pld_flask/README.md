# PLD Flask Project
This implementation does not use a database!

## Step 1: Setup and Project Structure
1) First, create a directory for the project and set up a virtual environment then activate it:
```
python -m venv venv
venv\Scripts\activate
```

2) Install Flask using pip:
`pip install Flask`

3) Afterwards make sure to have these folders and app.py in your project folder:
```
/[PROJECT_FOLDER]
    /static
    /templates
    app.py
```

## Step 2: Get all the files ready
Have all the *static* and *templates* files ready for the application. In this project we have 2 CSS files in *static* (`styles.css` and `edit-post.css`) and HTML files in *templates* (`home.html`, `post.html`, `add_post.html`, `edit_post.html`).

## Step 3: Run the Flask Application: 
Run the following command:
`flask run`

## Step 4: Access the Application:
Open a web browser and go to `http://127.0.0.1:5000/` to view your blog web application.

## Step 5: Use the blog:
You can add a blog, edit an existing blog or delete it and view them in detail (by clicking *Read more*).
