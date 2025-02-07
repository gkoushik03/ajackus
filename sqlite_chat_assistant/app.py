from flask import Flask, render_template, request, jsonify
import os
import sqlite3

app = Flask(__name__)

# Function to get valid departments from the database
def get_valid_departments():
    conn = sqlite3.connect("sqlite_chat_assistant/chatbot.db")  # Fixed path
    cursor = conn.cursor()
    cursor.execute("SELECT Name FROM Departments")
    departments = [row[0] for row in cursor.fetchall()]
    conn.close()
    return departments

# Function to fetch employees in a specific department
def get_employees_by_department(department):
    conn = sqlite3.connect("sqlite_chat_assistant/chatbot.db")  # Fixed path
    cursor = conn.cursor()
    cursor.execute("SELECT Name, Salary, Hire_Date FROM Employees WHERE Department = ?", (department,))
    employees = cursor.fetchall()
    conn.close()
    return employees

# Function to fetch the manager of a department
def get_manager_by_department(department):
    conn = sqlite3.connect("sqlite_chat_assistant/chatbot.db")  # Fixed path
    cursor = conn.cursor()
    cursor.execute("SELECT Manager FROM Departments WHERE Name = ?", (department,))
    manager = cursor.fetchone()
    conn.close()
    return manager[0] if manager else None

# Function to fetch the manager of an employee
def get_manager_by_employee(employee_name):
    conn = sqlite3.connect("sqlite_chat_assistant/chatbot.db")  # Fixed path
    cursor = conn.cursor()
    cursor.execute("""
        SELECT d.Manager FROM Employees e
        JOIN Departments d ON e.Department = d.Name
        WHERE e.Name = ?
    """, (employee_name,))
    manager = cursor.fetchone()
    conn.close()
    return manager[0] if manager else None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("query", "").strip().lower()

    valid_departments = get_valid_departments()
    response = "Sorry, I couldn't understand your query. Please try again."

    # List employees in a specific department
    if "employees" in user_query and "working in" in user_query:
        department = user_query.split("working in")[-1].strip().title()
        if department in valid_departments:
            employees = get_employees_by_department(department)
            response = "\n".join([f"Name: {e[0]}, Salary: {e[1]}, Hired: {e[2]}" for e in employees]) if employees else f"No employees found in {department}."
        else:
            response = "Invalid department name. Please check and try again."

    # Get manager of a department
    elif "manager of" in user_query:
        department = user_query.split("manager of")[-1].strip().title()
        if department in valid_departments:
            manager = get_manager_by_department(department)
            response = f"The manager of {department} is {manager}." if manager else f"No manager found for {department}."
        else:
            response = "Invalid department name. Please check and try again."

    # Get manager of an employee
    elif "manager of" in user_query:
        employee_name = user_query.split("manager of")[-1].strip().title()
        manager = get_manager_by_employee(employee_name)
        response = f"{employee_name} works in {department}, and the manager of {department} is {manager}." if manager else f"No manager found for {employee_name}."

    print(response)  # Print response in the console
    return jsonify({"response": response})  # Return response to UI

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the PORT from environment
    app.run(host="0.0.0.0", port=port, debug=False)  # B
