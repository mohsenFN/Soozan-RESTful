# Soozan Restful App

## To-Do
- [ ] Custom error message for simplejwt user_not_found response (I can't find this kinda error message)
- [ ] More specified and accurate way for users location (check Documentation/docs.md for current method)
- [ ] Write tests
- [ ] Use rate limit for views
- [ ] Create a documentation for end-points
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

---

## How to generate database diagram

1. **Change directory to access manage.py:**
   ```bash
   cd SoozanProject
   ```

2. **Use graph models to generate diagram:**
   ```bash
   python manage.py graph_models -a -o ../Documentation/models_diagram.pdf
   ```

---

## Directories explained 

This repository contains the source code for the Soozan RESTful API project. The project is organized into the following directories and apps:

### Project Directory (soozan_project)

The main directory for the project, containing settings and the root URLs.

### User App (user)

An app for managing users and their authentication.

### Artist & Applicant Apps (artist & applicant)

Apps for managing artist and applicant profiles.

### Post App (post)

An app for managing posts shared by artists.

**Note:**
- If you save your first image, there should be a `media` directory, which includes the images for posts.

Feel free to explore each directory and app for more details on the structure and functionality of the Soozan RESTful API.

---

## Directories explained 

### Soozan RESTful is using all default file names + some local script/modules

user/manager.py : We need to use our own user manager class for using Django's AbstractBaseUser as our user.
user/permissions.py : Custom authorization classes
