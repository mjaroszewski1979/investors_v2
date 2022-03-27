## Famous Investors
### This is a Python application powered by Django and its Object-Relational Mapper to provide convenient access to stored data. It is connected to a MySQL database hosted on Pythonanywhere server. It allows users to perform advanced filtering operations and prioritizes efficiency of querying. 

--------------------------------------------------

### Features:
* Utilizing Django's built-in features like cross-site request forgery protection to ensure safe data transfer in web forms to a database
* Breaking logic into smaller parts by adding various new Django applications to an existing project 
* Writing as much functionality as possible in models or utility files instead of views 
* Implementing annotate() - it allows us to add a pseudo field to our queryset, which can then further be used for filter lookups or ordering
* Using aggregate() - it evaluates the queryset as a whole and brings out the final result
* Working with select_related to create an SQL join and include the fields of the related object in the SELECT statement - it gets the related objects in the same database query ( designed to stop the deluge of database queries that are caused by accessing related objects )
* Storing app’s secure credentials in environment variables

--------------------------------------------------

### Code Coverage:
* Selenium and unit tests combined

```
coverage run -p manage.py test investors && coverage run -p manage.py test selenium_tests && coverage combine && coverage html

```

<img src="https://github.com/mjaroszewski1979/investors_v2/blob/main/cov_report.png">

------------------------------------------------


![caption](https://github.com/mjaroszewski1979/investors_v1/blob/main/investors_mockup.png)
  
  Live | Code | Docker | Technologies
  ---- | ---- | ------ | ------------
  [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/pyan1.png">](http://mjapp.pythonanywhere.com/) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/github_g.png">](https://github.com/mjaroszewski1979/investors_v2) | [<img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/docker_compose.png">](https://github.com/mjaroszewski1979/investors_v1/blob/main/docker-compose.yml) | <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/python_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/django_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/mysql.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/html_g.png"> <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/css_g.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/htmlup.png"> &nbsp; &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/selenium.png"> &nbsp; <img src="https://github.com/mjaroszewski1979/mjaroszewski1979/blob/main/coverage.png">
