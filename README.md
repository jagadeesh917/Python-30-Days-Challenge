from pathlib import Path

# Define the content for the GitHub README.md file
readme_content = """
# 🐍 30 Days of Python Challenge

Welcome to the **30 Days of Python Challenge**! This is a structured, hands-on journey to strengthen your Python programming skills day by day.

Each day includes a topic and a small coding challenge to reinforce what you've learned.

---

## 📅 Challenge Schedule

| Day        | Topic                                      | Challenge of the Day                                                                 |
|------------|--------------------------------------------|---------------------------------------------------------------------------------------|
| Day 0️⃣1️⃣ | Introduction to Python                     | Write a program that prints "Hello, World!" followed by your name                    |
| Day 0️⃣2️⃣ | Variables and Data Types                   | Calculate the area of a rectangle using user-input length and width                  |
| Day 0️⃣3️⃣ | Lists, Tuples, and Dictionaries            | Create an inventory system tracking items and quantities with a dictionary           |
| Day 0️⃣4️⃣ | Control Structures                         | Check if a user-entered number is prime                                              |
| Day 0️⃣5️⃣ | Functions                                  | Write a function that computes the sum and average of a list of numbers              |
| Day 0️⃣6️⃣ | Modules and Packages                       | Generate a random 8-character password                                               |
| Day 0️⃣7️⃣ | File Handling                              | Count word frequencies in a text file                                                |
| Day 0️⃣8️⃣ | Object-Oriented Programming (Part 1)       | Create a Car class with attributes and a display method                              |
| Day 0️⃣9️⃣ | Object-Oriented Programming (Part 2)       | Extend Car into an ElectricCar subclass with battery capacity                        |
| Day 1️⃣0️⃣ | Exception Handling                         | Read numbers from a file and handle errors gracefully                                |
| Day 1️⃣1️⃣ | Working with Dates and Times               | Create a program that displays the number of days left in the year                   |
| Day 1️⃣2️⃣ | Regular Expressions                        | Extract all email addresses from a given string                                      |
| Day 1️⃣3️⃣ | Data Structures                            | Implement a stack and a queue using lists                                            |
| Day 1️⃣4️⃣ | Recursion                                  | Write a recursive function to calculate the factorial of a number                    |
| Day 1️⃣5️⃣ | Comprehensions                             | Use list, dictionary, and set comprehensions to clean and transform data             |
| Day 1️⃣6️⃣ | Lambda, Map, Filter, Reduce                | Use `map`, `filter`, and `reduce` to process a list of numbers                       |
| Day 1️⃣7️⃣ | Working with JSON                          | Read a JSON file and display the contents in a formatted manner                      |
| Day 1️⃣8️⃣ | Python with CSV and Excel                  | Read a CSV file and calculate column-wise averages                                   |
| Day 1️⃣9️⃣ | Web Scraping with BeautifulSoup            | Scrape the title and price of products from a sample e-commerce site                 |
| Day 2️⃣0️⃣ | Introduction to APIs                       | Use an API to fetch weather data for a city and display it                           |
| Day 2️⃣1️⃣ | Virtual Environments & pip                 | Create a virtual environment and install required packages using `pip`               |
| Day 2️⃣2️⃣ | Unit Testing                               | Write unit tests for a function that processes user input                            |
| Day 2️⃣3️⃣ | Debugging Techniques                       | Debug a program that calculates student grades with logical errors                   |
| Day 2️⃣4️⃣ | Logging                                    | Add logging to a file-processing script to track errors                              |
| Day 2️⃣5️⃣ | Working with Databases (SQLite)            | Create a database to store and retrieve book information                             |
| Day 2️⃣6️⃣ | Python and Pandas                          | Load a CSV into Pandas and analyze the top 5 records                                 |
| Day 2️⃣7️⃣ | Data Visualization with Matplotlib         | Create a bar chart showing monthly expenses                                          |
| Day 2️⃣8️⃣ | Python and NumPy                           | Create a 2D array and perform basic operations like mean and transpose               |
| Day 2️⃣9️⃣ | Capstone Project Day 1                     | Plan and start building a mini project using learned concepts                        |
| Day 3️⃣0️⃣ | Capstone Project Day 2                     | Complete and submit the project with documentation                                   |

---

✅ Make sure to submit your daily progress using the form provided in the challenge posts.

Happy Coding! 🚀
"""

# Save the content to a README.md file
readme_path = Path("/mnt/data/30_Days_of_Python_Challenge_README.md")
readme_path.write_text(readme_content.strip())

readme_path

