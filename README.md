# My To-Do List App

## Table of Contents
* [About the Project](#about-the-project)
* [Features](#features)
* [Development Stack](#development-stack)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Customization](#customization)
* [License](#license)
* [Contact](#contact)

---

## About the Project
This project is a simple, web-based to-do list application built using the **Django** framework. It allows users to add, mark as complete, and delete tasks. The goal of this project was to learn the fundamentals of full-stack web development with Django, including setting up a project, defining models, creating views, and styling with CSS.

---

## Features
* **Create Tasks:** Easily add new tasks to your to-do list.
* **Mark as Complete:** Toggle tasks as completed or incomplete.
* **Delete Tasks:** Remove unwanted tasks from the list.
* **Custom Styling:** The app features a custom pink, orange, and purple color scheme with a unique star bullet design.

---

## Development Stack
This section outlines the key technologies and tools used to develop and run this project.

* **IDE:** PyCharm (WebStorm to use CSS files)
* **Operating System:** Windows (GitBash)
* **Python Version:** 3.13.7
* **Virtual Environment:** venv
* **Django Version:** 5.2.6
* **Dependencies:**
    Requirements.txt

---

## Getting Started

### Prerequisites
To run this project, you need the following installed on your machine:
* **Python 3.x**
* **pip** (Python package installer)
* **Git Bash** (or another command-line tool)

### Installation
1.  **Clone the repository:**
    ```bash
    git clone [your-repo-url]
    cd todoproject
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```
3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file, you can create one by running `pip freeze > requirements.txt`)*

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```
5.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

---

## Usage
* **Adding a task:** Type your task in the input box and click the "Add" button.
* **Marking a task as complete:** Click on the task's text. A checkmark will appear, and the text will be struck through.
* **Deleting a task:** Click the "❌" icon next to the task.

---

## Customization
You can easily change the styling of the app by editing the **`styles.css`** file located at `todoapp/static/todoapp/styles.css`. Feel free to adjust the colors, fonts, and layout to match your own design preferences.

---

## License
Distributed under the MIT License. See `LICENSE` for more information.
