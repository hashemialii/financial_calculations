
# Financial Calculations Project

## Overview

This project is designed to manage financial calculations, including income tracking and fiscal year calculations. It utilizes Django and Django REST Framework to provide a RESTful API for creating and managing financial records.

## Features

- **Models**:
  - **ShahkarIncomeModel**: Tracks income with fields for income amount, year, and month.
  - **ShahkarBasicModel**: Stores basic financial data linked to the income model, ensuring unique entries for each year and month.

- **Serializers**:
  - **IncomeSerializer**: Serializes and deserializes the ShahkarIncomeModel data.
  - **BasicSerializer**: Serializes ShahkarBasicModel data and includes nested IncomeSerializer for related income information.

- **Services**:
  - **IncomeCalculator**: Contains methods for calculating income based on fiscal year multipliers.
  - **IncomeService**: Manages the creation and updating of income and basic entries, ensuring data integrity and consistency.

- **API Endpoints**:
  - `POST /shahkar/income-calculations/`: Creates a new basic entry and its associated income entry.
  - `GET /shahkar/income-calculations/`: Retrieves all basic entries along with their income details.
  - `PUT /shahkar/income-calculations/{id}/`: Updates an existing basic entry and its associated income entry.
  - `DELETE /shahkar/income-calculations/{id}/`: Deletes a basic entry and its associated income entry.

- **Use of class-based views** for better structure and maintainability, along with support for both integer and decimal input for amounts.

## Installation

To get started with this project, follow the steps below:

### Prerequisites

- Python 3.8 or higher
- Django 5.1.2
- Django REST Framework
- PostgreSQL (or any other database of your choice)

### Steps to Run the Project

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hashemialii/financial_calculations.git
   cd financial_calculations
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

5. **Configure the database in `settings.py`:** Ensure that your database settings are correct, particularly for PostgreSQL or your chosen database.

6. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the API:**

   Open your browser or Postman and navigate to `http://127.0.0.1:8000/shahkar/income-calculations/` to interact with the API.

## Usage

- **GET** request to `/shahkar/income-calculations/` will return all basic entries with their associated income records.
- You can filter the results by year and month by adding query parameters, e.g., `?year=1402&month=3`.

- **POST** request to `/shahkar/income-calculations/` requires the following JSON body:

    ```json
    {
        "year": 1402,
        "month": 3,
        "amount": "100"
    }
    ```

- **PUT** request can be made to update an existing record, using the ID of the record.

- **DELETE** request can be made to remove an existing record by its ID.

## Development Status

This project is currently under development. Contributions and suggestions are welcome!