# School Management System (Python - Tkinter Version)

## Overview

The **School Management System** is a desktop application designed to streamline the management of academic and administrative tasks within a school environment. This is the **first version** of the system, developed using **Python** and the **Tkinter interface framework**, with data stored in CSV or text files. The application is offline and operates on a single desktop, providing essential features for managing students, teachers, assignments, and communication within the school.

## Features

### 1. **Student Record Management**

- Add, edit, and delete student details.
- Store essential information such as name, grade, section, and contact details.
- Search and filter student records.

### 2. **Teacher Record Management**

- Manage teacher details, including names and assigned subjects.
- Facilitate communication between teachers and administrators.

### 3. **Class and Section Management**

- Organize students and teachers into specific classes and sections.

### 4. **Messaging System**

- Enable offline communication between administrators, teachers, and students.
- Messages are stored locally and accessible within the application.

### 5. **Assignment Management**

- Administrators and teachers can assign tasks to students.
- Students can submit assignments within the system.
- All assignment data is stored locally.

### 6. **Data Storage**

- Uses **CSV files** and **plain text files** to store all data, ensuring simplicity and ease of access.

### 7. **User Authentication**

- Role-based access for administrators, teachers, and students.
- Basic validation to ensure secure login and role-specific permissions.

### 8. **User-Friendly Interface**

- Simple and intuitive interface designed with **Tkinter**, ensuring ease of use for non-technical users.

## Limitations

- **Offline and Single Desktop Use**: The system operates entirely offline and is not designed for networked environments.
- **Basic Validation**: The business logic and validation mechanisms are less robust compared to the latest version (C# Windows Forms).
- **No Attendance System**: This version lacks attendance tracking features present in the C# version.

## Future Development

This project served as the foundation for the second version of the system, developed using **C# Windows Forms**. The updated version introduced:
- An enhanced attendance system.
- Improved validation and business logic.
- Migration from CSV/text files to a **SQLite database** for more efficient and secure data storage.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Developed by **Gebremariam Birhanu**.
- Inspired by the need to digitize manual record-keeping processes in schools.
