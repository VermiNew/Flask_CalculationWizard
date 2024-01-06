# FlaskWebsite_UserData

FlaskWebsite_UserData is a web application developed using the Flask microframework for Python. This project provides a user-friendly platform for user registration, login, and data management.
User authentication information and user-specific data are stored in JSON files.

## Features

- **User Registration and Authentication:**
  - Users can register with a unique username and password.
  - Secure authentication ensures authorized access.

- **Data Management:**
  - Manage personal data, including first name, last name, PESEL, birth date, and order information.
  - CRUD functionality: Add, edit, and delete user data.

- **Session Handling and Logout:**
  - Secure management of user sessions.
  - Users can log out to ensure data privacy.

- **Flash Messages:**
  - Real-time feedback during registration, login, and data management operations.

- **JSON Data Storage:**
  - User authentication details and data records are stored in JSON files.

- **Dynamic Table Display:**
  - User data presented in a dynamically generated table.

## Usage

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/VermiNew/FlaskWebsite_UserData
    cd FlaskWebsite_UserData
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Run the Flask web server:**
    ```sh
    python app.py
    ```

2. **Access the application in your web browser:**
    [http://localhost:5000/](http://localhost:5000/)

## Dependencies

- Flask

## Contributing

1. **Fork the repository.**
2. **Create a new branch for your feature:**
    ```sh
    git checkout -b feature-name
    ```

3. **Commit your changes:**
    ```sh
    git commit -m 'Add new feature'
    ```

4. **Push to the branch:**
    ```sh
    git push origin feature-name
    ```

5. **Open a pull request.**

## Issues

Report any issues or suggest improvements by creating a new issue.

## License

This project is licensed under the [MIT License](LICENSE).
