# Soozan Restful App

## To-Do
- [x] Cleaner error handling in User.views (Like Post.views)
- [ ] Save post images with a specific name set
- [ ] More specified and accurate way for users location (check Documentation/docs.md for current method)
- [ ] Implement more secure authentication method
- [ ] Write tests
- [ ] Update documentation
- [ ] Update readme
- [ ] Celebrate the success! 🎉


## Overview

Soozan Restful is a Django-based RESTful web application that provides a platform for tattoo enthusiasts; With Soozan-RESTful you can manage a secure and robust system for connecting tattoo artists and clients. This application is designed to offer a straightforward and efficient way to handle data through a RESTful API.

## Features

- **Task Management:** Create, update, delete, and retrieve tasks using the RESTful API.
- **User Authentication:** Secure your data with user authentication to ensure only authorized users can access and manage tasks.
- **API Documentation:** Explore and understand the available API endpoints and functionalities through comprehensive documentation.

## Installation

Follow these steps to set up and run the Soozan Restful app:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mohsenFN/Soozan-restful.git
   ```

2. **Run a Virtual environment:**
   ```bash
   cd Soozan-restful
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install requirements:**
   ```bash
   pip install -r requirements
   ```

4. **Take a Smoke Test:**
   ```bash
   python manage.py runserver
   ```



## How to generate database diagram

1. **Change directory to access manage.py:**
   ```bash
   cd SoozanProject
   ```

2. **Use graph models to generate diagram:**
   ```bash
   python manage.py graph_models -a -o ../Documentation/models_diagram.pdf
   ```
