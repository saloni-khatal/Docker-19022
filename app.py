from flask import Flask, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "The White Tiger", "author": "Aravind Adiga"},
    {"id": 2, "title": "God of Small Things", "author": "Arundhati Roy"},
    {"id": 3, "title": "Train to Pakistan", "author": "Khushwant Singh"},
    {"id": 4, "title": "Malgudi Days", "author": "R.K. Narayan"},
    {"id": 5, "title": "The Guide", "author": "R.K. Narayan"},
    {"id": 6, "title": "The Inheritance of Loss", "author": "Kiran Desai"},
    {"id": 7, "title": "A Fine Balance", "author": "Rohinton Mistry"},
    {"id": 8, "title": "The Namesake", "author": "Jhumpa Lahiri"},
    {"id": 9, "title": "The Palace of Illusions", "author": "Chitra Banerjee Divakaruni"},
    {"id": 10, "title": "Midnight’s Children", "author": "Salman Rushdie"}
]

users = [
    {"id": 1, "name": "Aarav Sharma"},
    {"id": 2, "name": "Ananya Patel"},
    {"id": 3, "name": "Rohan Mehta"},
    {"id": 4, "name": "Ishita Singh"},
    {"id": 5, "name": "Karan Gupta"},
    {"id": 6, "name": "Priya Nair"},
    {"id": 7, "name": "Vikram Iyer"},
    {"id": 8, "name": "Sneha Das"},
    {"id": 9, "name": "Rahul Bansal"},
    {"id": 10, "name": "Neha Joshi"}
]

borrowed = [
    {"user": "Aarav Sharma", "book": "The White Tiger"},
    {"user": "Ananya Patel", "book": "Malgudi Days"},
    {"user": "Rohan Mehta", "book": "The Guide"},
    {"user": "Priya Nair", "book": "The Namesake"}
]

@app.route('/')
def home():
    return render_template('index.html', books=books, users=users, borrowed=borrowed)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
