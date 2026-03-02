# 🔐 Console-Based Password Manager (Python)

A simple and secure command-line Password Manager built using Python.  
This application allows users to store and retrieve credentials using persistent file storage while demonstrating structured programming and core backend logic.

---

## 🚀 Features

- 🔑 Add new website credentials
- 📂 View all stored passwords
- 🔍 Search password by website name
- 💾 Persistent data storage using text file
- 🔁 Menu-driven CLI interface
- ▶ Continuous execution until user exits

---

## 🛠 Technologies Used

- Python 3
- File Handling (read, write, append)
- Loops & Conditional Statements
- Command Line Interface (CLI)

---

## 📂 Project Structure

```
PasswordManager/
│
├── password_manager.py
├── data.txt
└── README.md
```

---

## ▶ How to Run

### 1️⃣ Clone the repository

```
git clone https://github.com/Dinesh23123/password-manager-python.git
```

### 2️⃣ Navigate into the folder

```
cd password-manager-python
```

### 3️⃣ Run the program

```
python password_manager.py
```

(Use `python3 password_manager.py` if required)

---

## 💡 Example Usage

```
===== Password Manager =====
1. Add Password
2. View All Passwords
3. Search Password
4. Exit

Enter choice: 1
Enter website name: github
Enter password: mypassword123

Data stored successfully!
```

---

## 🧠 Concepts Demonstrated

- File handling for persistent data storage
- Searching and retrieving records from files
- Menu-driven program structure
- Loop control using `while True`
- Basic error handling and validation
- Structured function-based design

---

## 🔒 How It Works

- Credentials are stored in a text file (`data.txt`).
- Each record is saved in a structured format.
- The program reads the file to retrieve or search stored credentials.
- Data remains saved even after program termination.

---

## 📌 Future Improvements

- Add password encryption for enhanced security
- Use `getpass` module for password masking
- Add duplicate website detection
- Implement user authentication system
- Upgrade to GUI version using Tkinter
- Integrate SQLite database for structured storage

---

## 👨‍💻 Author

**Dinesh Sonawane**  
Python Developer | Backend Enthusiast  

---

⭐ If you found this project helpful, feel free to star the repository!
