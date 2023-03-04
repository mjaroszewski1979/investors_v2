## Famous Investors
### This particular software is a Python application that utilizes the Django framework and its Object-Relational Mapper (ORM) to facilitate the retrieval of stored data. It is connected to a MySQL database hosted on the Pythonanywhere server. The software's primary objective is to enable users to execute complex filtering operations while prioritizing the speed and efficiency of querying.

#### By utilizing this software, users can save valuable time by executing advanced filtering operations quickly and efficiently. Additionally, the software's Python and Django backend offer flexibility and customizability, making it an ideal choice for users who want to customize their querying process to fit their specific needs.

--------------------------------------------------

### Features:
* One way to ensure that data is transferred safely is by using Django's built-in features, including **Cross-Site Request Forgery Protection**. Cross-site request forgery (CSRF) attacks occur when a malicious website tricks a user's browser into making a request to another website without their knowledge or consent. This type of attack can result in data theft or corruption, making it essential to protect against. Django's CSRF protection works by including a unique token in each form submission. This token is validated on the server-side to ensure that the request came from the correct user and not from a malicious source. By using this feature, developers can ensure that web forms are safe and secure, and that data is transferred safely to the database. In addition to CSRF protection, Django also includes other built-in security features, such as user authentication and authorization, password hashing, and SSL encryption. These features are designed to protect against common security threats and make it easier for developers to build secure web applications.
* **Breaking down logic into smaller, manageable parts** is crucial to ensuring the success of any project. One way to achieve this is by adding various new Django applications to an existing project. By creating smaller, more focused applications within a larger project, developers can improve code organization, maintainability, and scalability. Each application can handle a specific task or feature of the project, such as user authentication, data management, or payment processing. This approach can also make it easier to debug and test individual parts of the codebase. When adding new applications to an existing Django project, it's important to consider the functionality and purpose of each application. Each application should be responsible for a specific feature or function within the project, making it easier to modify and maintain the codebase in the long run. However, it's important to keep in mind that adding too many applications can also have drawbacks. It can increase the complexity of the codebase and slow down the overall performance of the project. Therefore, it's crucial to strike a balance between breaking down the logic of the project and keeping it manageable.
* To achieve clean and maintainable code one should **write as much functionality as possible in Django models or utility files instead of views**. Django allows developers to separate their application's logic into three main components: models, views, and templates. While views are responsible for handling user requests and returning responses, models define the structure of the application's data and provide an interface for interacting with it. By writing as much functionality as possible in models or utility files, developers can improve the maintainability and organization of their codebase. This approach helps to keep views lean and focused on their primary responsibilities, improving code readability and making it easier to debug and maintain. Furthermore, writing functionality in models or utility files can also improve the performance of the application. Since models and utility files are loaded only once when the application starts up, the cost of loading and processing is spread out over the lifetime of the application.
* **Django's annotate() function** is a powerful tool that can greatly enhance the functionality of a queryset. It allows developers to add a pseudo-field to their queryset, which can be utilized for filtering and ordering operations. By utilizing Django's annotate() function, developers can dynamically add new fields to their queryset that do not exist in the database. These fields can be computed based on the values of other fields in the queryset. For instance, developers can utilize the annotate() function to compute the average rating of a product, the total number of comments on a blog post, or the total number of orders placed by a customer. Once the pseudo-field has been added to the queryset, it can be used for filtering and ordering operations, just like any other field in the database. This allows developers to execute complex queries with ease, without having to write complex SQL queries. One of the significant benefits of utilizing Django's annotate() function is that it allows developers to write more efficient code. By using a single query to compute the values of multiple pseudo-fields, developers can reduce the number of database queries executed, thereby improving the performance of their application.
* **Django's aggregate() function** is a powerful tool that can help developers to evaluate a queryset as a whole and obtain a final result. It allows developers to perform complex calculations and generate summary statistics on a queryset. By utilizing Django's aggregate() function, developers can perform a variety of calculations on a queryset, such as computing the average rating of a product, the total number of comments on a blog post, or the total revenue generated by an e-commerce store. One of the significant benefits of utilizing Django's aggregate() function is that it allows developers to perform these calculations efficiently and with minimal code. By using a single query to compute the values of multiple aggregate functions, developers can reduce the number of database queries executed, thereby improving the performance of their application. Django's aggregate() function supports a wide range of aggregate functions, including Count, Sum, Avg, Max, and Min. These functions can be used in conjunction with other Django queryset methods, such as filter() and exclude(), to perform complex queries with ease.
* **Django's select_related function** is a powerful tool that can help developers optimize their application's database queries by minimizing the number of queries needed to retrieve data. By using select_related, developers can specify related objects to include in the same database query. When accessing related objects in Django, developers might find themselves generating a deluge of database queries. Each query executed by the database adds overhead to the system, making it slow and inefficient. However, select_related addresses this issue by joining related tables in a single query, returning the required data in a single database call. One of the significant benefits of using select_related is that it can significantly improve the performance of an application by reducing the number of queries needed to retrieve data. This optimization is particularly valuable when working with large datasets or when accessing related objects that are far down the object graph. Moreover, select_related can also be used to reduce database load by prefetching related objects, allowing developers to avoid executing additional queries. By specifying related objects in the select_related function, developers can optimize their application's database queries and improve its overall performance.
* Understanding the importance of keeping sensitive information secure, we **always store API keys, database passwords, and other credentials in environment variables**. Environment variables are values that can be set in the operating system and accessed by applications. By storing sensitive information in environment variables, developers can keep this information separate from the codebase, reducing the risk of accidental exposure. Storing sensitive information in environment variables also makes it easier to manage and maintain credentials across multiple environments. Rather than hard-coding credentials into the application, environment variables can be set differently for each environment, such as development, staging, and production. This helps to ensure that sensitive information is not accidentally exposed in a non-production environment. However, it's important to keep in mind that environment variables are not a foolproof security measure. They are still vulnerable to potential security breaches if not properly secured or if accessed by unauthorized users. Therefore, it's important to follow best practices for securing sensitive information, such as using strong passwords, limiting access to credentials, and regularly monitoring and auditing access to environment variables.

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
