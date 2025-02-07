# SQLite Chat Assistant

This project is a Flask-based chatbot that interacts with an SQLite database to answer queries about employees and departments.

## Features
- Retrieve employees based on department.
- Get the manager of a specific department.
- Find the manager of a given employee.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- SQLite3
- Flask

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gkoushik03/ajackus.git
   cd ajackus/sqlite_chat_assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Ensure the SQLite database is set up:**
   - The database file `chatbot.db` should be placed inside `sqlite_chat_assistant/`
   - The database should contain the following tables:
     
     **Employees Table**
     | ID | Name    | Department  | Salary | Hire_Date  |
     |----|---------|------------|--------|------------|
     | 1  | Alice   | Sales      | 50000  | 2021-01-15 |
     | 2  | Bob     | Engineering| 70000  | 2020-06-10 |
     | 3  | Charlie | Marketing  | 60000  | 2022-03-20 |

     **Departments Table**
     | ID | Name         | Manager  |
     |----|-------------|----------|
     | 1  | Sales       | Alice    |
     | 2  | Engineering| Bob      |
     | 3  | Marketing  | Charlie  |

4. **Run the application:**
   ```bash
   python app.py
   ```

## Usage
Once the Flask app is running, you can send queries via a frontend or API request.

### Example Queries & Responses
#### Employees in a Department
```
You: employees working in Sales
Bot: Name: Alice, Salary: 50000, Hired: 2021-01-15

You: employees working in Engineering
Bot: Name: Bob, Salary: 70000, Hired: 2020-06-10

You: employees working in Marketing
Bot: Name: Charlie, Salary: 60000, Hired: 2022-03-20
```

#### Manager of a Department
```
You: manager of Sales
Bot: The manager of Sales is Alice.

You: manager of Engineering
Bot: The manager of Engineering is Bob.

You: manager of Marketing
Bot: The manager of Marketing is Charlie.
```

#### Manager of an Employee
```
You: manager of Alice
Bot: Alice works in Sales, and the manager of Sales is Alice.

You: manager of Bob
Bot: Bob works in Engineering, and the manager of Engineering is Bob.

You: manager of Charlie
Bot: Charlie works in Marketing, and the manager of Marketing is Charlie.
```

## API Endpoint
### POST `/chat`
**Request Format:**
```json
{
    "query": "employees working in Sales"
}
```

**Response Format:**
```json
{
    "response": "Name: Alice, Salary: 50000, Hired: 2021-01-15"
}
```

## License
This project is licensed under the MIT License.

