# Library Management System

This Django project is designed to create a Library Management System. It includes various APIs for handling user and admin functionalities, as well as a user view, home page, and login/logout/password reset functionality.

## Getting Started

To get started with the Library Management System, follow these steps:

1. Clone the repository: `git@github.com:rathorel24/library-management-system.git`
2. Navigate to the project directory: `cd library/`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the project: `python manage.py runserver`
--> pyhton manage.py createsuperuser -- Create super user to login on Admin panel
5. Open your web browser and go to http://localhost:8000/register/ To create your account
6. Open your web browser and go to http://localhost:8000/login/ For login


## Role-based Redirect

The Library Management System includes role-based redirect functionality, which will redirect users to different pages based on their role:

- If your role is `manager`, you will be redirected to the user view page.
- If your role is `librarian`, you will be redirected to the Django admin page.

To set a user's role, log in as an admin and navigate to the user detail page. There you can select the user's role from a dropdown menu.

## APIs

The Library Management System includes the following APIs:

- `admin/`: The admin dashboard where you can manage all aspects of the system.
- `users/`: A list view of all registered users.
- `users/register/`: A view for registering new users.
- `users/<pk>/`: A detail view for a specific user.
- `api-root/`: The root API endpoint.
- `user_view/`: A view for displaying personalized information for each logged-in user.

## Views

The Library Management System includes the following views:

- `home/`: The home page that welcomes visitors and provides information about the site.
- `login/`: A view for logging in to the system.
- `logout/`: A view for logging out of the system.
- `password_change/`: A view for changing a user's password.
- `password_change/done/`: A view displayed after a user has successfully changed their password.
- `password_reset/`: A view for resetting a user's password.
- `password_reset/done/`: A view displayed after a user has requested a password reset.
- `reset/<uidb64>/<token>/`: A view for resetting a user's password using a unique URL.
- `reset/done/`: A view displayed after a user has successfully reset their password.
