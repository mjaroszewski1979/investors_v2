## Famous Investors
### This particular software is a Python application that utilizes the Django framework and its Object-Relational Mapper (ORM) to facilitate the retrieval of stored data. It is connected to a MySQL database hosted on the Pythonanywhere server. The software's primary objective is to enable users to execute complex filtering operations while prioritizing the speed and efficiency of querying.

#### By utilizing this software, users can save valuable time by executing advanced filtering operations quickly and efficiently. Additionally, the software's Python and Django backend offer flexibility and customizability, making it an ideal choice for users who want to customize their querying process to fit their specific needs.

### Features
* CSRF Protection: Uses Django's built-in CSRF protection to prevent data theft or corruption by ensuring that requests are genuine.
* Modular Applications: Improves code organization by breaking down logic into smaller, manageable Django applications.
* Model and Utility Functions: Enhances maintainability and performance by concentrating functionality in models and utility files.
* Query Optimization with Annotate: Adds pseudo-fields to querysets for dynamic filtering and ordering, enhancing query capabilities.
* Aggregations: Performs complex calculations on querysets using Django's aggregate functions, improving query efficiency.
* Optimized Database Queries with 'Select Related': Reduces the number of database queries by joining related tables in a single query.
* Environment Variables for Security: Stores sensitive information in environment variables to separate them from the codebase and enhance security.

### Problem Solved
This project addresses the challenge of executing complex filtering operations on large datasets efficiently. By using Django's ORM and optimizing queries, it ensures fast and reliable data retrieval.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/mjaroszewski1979/investors_v2.git
    ```
2. Navigate to the project directory:
    ```bash
    cd investors_v2
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
### Usage
1. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
2. Start the development server:
    ```bash
    python manage.py runserver
    ```
3. Access the application at `http://127.0.0.1:8000/`.

### Testing
Run the following command to execute unit tests and generate a coverage report:
```bash
coverage run -p manage.py test investors && coverage run -p manage.py test selenium_tests && coverage combine && coverage html
```

### Code Coverage:
* Selenium and unit tests combined

<img src="https://github.com/mjaroszewski1979/investors_v2/blob/main/cov_report.png">

### Technologies Used
* Python
* Django
* MySQL
* Docker
* Selenium

### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

### Contact
For any inquiries or issues, please contact https://github.com/mjaroszewski1979/


![caption](https://github.com/mjaroszewski1979/investors_v1/blob/main/investors_mockup.png)
  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pyan1.png">](http://mjapp.pythonanywhere.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/investors_v2) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_compose.png">](https://github.com/mjaroszewski1979/investors_v1/blob/main/docker-compose.yml) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/mysql.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/selenium.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/coverage.png">
