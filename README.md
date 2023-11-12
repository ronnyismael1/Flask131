# Social Media Website Using Flask

Flask131 is a comprehensive web application developed using the Flask framework in Python. It leverages SQLAlchemy for database operations and Flask-WTF for form handling and validation. The application is designed with a focus on user interaction, allowing users to create accounts, post messages, follow other users, and search for users or messages.

## Features

- **User Authentication**: Implemented secure user authentication using Werkzeug for password hashing. Users can log in, log out, and create new accounts with unique usernames.

- **User Interaction**: Users can follow and unfollow other users. They can also view profiles of other users, which display the last seen time and posted messages.

- **Posting Messages**: Users can create posts with a title and body. These posts are stored in a SQLite database and can be viewed on the user's profile.

- **Search Functionality**: Implemented a search feature that allows users to search for other users or messages by their title.

- **Database Management**: Utilized SQLAlchemy ORM for database operations. The database schema includes tables for users, posts, and followers.

- **Form Handling**: Leveraged Flask-WTF for form creation and validation. Forms are used for user registration, login, post creation, and search functionality.

- **Error Handling**: Implemented a custom 404 error page for handling invalid routes.

- **Unit Testing**: The application includes unit tests to ensure the functionality of core features.

## Installation

To run Flask131, you need to have Python and Flask installed. Clone the repository, navigate to the project directory, and run the `app.py` file.

## Contributions

This project is a collaborative effort of a team of four developers, each contributing to different functionalities as outlined in the `requirements.md` and `meetings.md` files.
