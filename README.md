# Django Search Application

This is a template-based Django search application that allows users to search for dishes and get recommendations for
the best match.

## Features

- Users can enter a query to search for dishes.
- The application searches through the names of dishes and recommends the best match.
- The search results include the dish name and its corresponding price.
- If no dishes are found, a message is displayed indicating that no dishes were found.

## Installation

1. Clone the repository:

   ```shell
   git clone <repository-url>
   ## Navigate to the project directory:
   cd primenumbers
   ## Install the required dependencies:
   pip install -r requirements.txt
   ##Apply the database migrations:
   python manage.py migrate
   ## Start the development server:
   python manage.py runserver
   ## Open a web browser and
   access the application at http://localhost:8000/search.

# Usage

<ol>Enter a search query in the provided input field.
<li>Click the "Search" button to perform the search.</li>
<li>The search results will be displayed in a table, showing the dish name and its corresponding price.</li>
<li>If no dishes are found, a message will be displayed indicating that no dishes were found.</li></ol>

# Technologies Used

<ol><li>Django</li>
<li>SQLite (file-based database)</li>
<li>HTML</li>
<li>CSS</li></ol>

# Screenshots
<img src="./Screenshot%202023-06-29%20180559.png" alt="image not found" loading="lazy">

# Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

# License
This project is licensed under the MIT License.

Feel free to modify the content as needed and include additional sections or information specific to your project.

# Note: 
Don't forget to download the csv from the link . How it is provided in the repository still if you want you can download it from <a href="https://python-exercise.s3.ap-south-1.amazonaws.com/restaurants_small.csv">here</a>