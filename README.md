# Financial Calculations Project

## Overview

This project is designed to manage financial calculations, including income tracking and fiscal year calculations. It utilizes Django and Django REST Framework to provide a RESTful API for creating and managing financial records.

## Features

- Create and manage financial records with basic information such as year, month, and amount.
- Calculate income based on fiscal year multipliers.
- Use of class-based views and services for better structure and maintainability.
- Allows for both integer and decimal input for amounts.

## Installation

To get started with this project, follow the steps below:

### Prerequisites

- Python 3.8 or higher
- Django 5.1.2
- Django REST Framework
- SQLite (or any other database of your choice)

### Steps to Run the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the API:**

   Open your browser or Postman and navigate to `http://127.0.0.1:8000/shahkar/income/` to interact with the API.

## Usage

- **GET** request to `/shahkar/income/` will return all income records. 
- You can filter the results by year and month by adding query parameters, e.g., `?year=1402&month=3`.

- **POST** request to `/shahkar/income/` requires the following JSON body:

    ```json
    {
        "year": 1402,
        "month": 3,
        "amount": "100"
    }
    ```

- **PUT** request can be made to update an existing record, using the ID of the record.

## Development Status

This project is currently under development. Contributions and suggestions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
