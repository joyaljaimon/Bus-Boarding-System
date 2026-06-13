# 🚌 Student Bus Boarding System

A Python-based school bus management system that tracks student boarding and deboarding activities using a MySQL database.

## Overview

The Student Bus Boarding System helps schools manage transportation efficiently by maintaining real-time records of which students are on which buses, along with the ability to export reports as CSV files.

## Features

- **Add Students** – Register new students with name, phone number, and gender
- **Remove Students** – Delete a student's record from the system
- **Board Student** – Mark a student as boarded and assign them to a bus number
- **Deboard Student** – Mark a student as deboarded from their bus
- **List All Students** – Display all student records with current status and bus assignment
- **Search Student** – Look up a specific student by name
- **Export to CSV** – Export all student data to `student.csv` for reporting

## Requirements

### Hardware
- OS: Windows 7 or above
- Processor: Pentium or AMD Athlon (Dual Core)
- RAM: 512 MB or more
- Hard Disk: 40 GB or more

### Software
- Python 3.x
- MySQL Server
- Visual Studio Code (recommended)

### Python Libraries
- `mysql-connector-python`
- `csv` (built-in)

## Database Setup

1. Start your MySQL server and log in.
2. Create the database and table:

```sql
CREATE DATABASE jj_bbs;

USE jj_bbs;

CREATE TABLE student (
    name    VARCHAR(10),
    phone   INT,
    gender  CHAR(1),
    bus     INT,
    status  VARCHAR(20) DEFAULT 'Deboard'
);
```

3. Update the connection credentials in the script if needed:

```python
conn = mycon.connect(
    host='localhost',
    user='root',
    password='1234',
    database='jj_bbs'
)
```

## Installation

1. Clone or download the project files.
2. Install the required Python library:

```bash
pip install mysql-connector-python
```

3. Set up the database as described above.
4. Run the program:

```bash
python main.py
```

## Usage

On launch, you'll be presented with a menu:

```
Choose a function
    1) Add Student     [Add]
    2) Remove Student  [Remove]
    3) Board Student   [Board]
    4) Deboard Student [Deboard]
    5) List Data       [List]
    6) Search          [Search]
    7) Export Data     [Export]
Enter action:
```

Type the action keyword (e.g., `add`, `board`, `export`) and follow the prompts. After each action, you'll be asked whether to continue.

## CSV Export

The `Export` action generates a `student.csv` file in the working directory with the following columns:

| Name | Phone | Gender | Bus No. | Status |
|------|-------|--------|---------|--------|

## Project Structure

```
├── main.py          # Main application script
├── student.csv      # Generated on export
└── README.md
```

## Known Limitations

- Student names are limited to 10 characters (database constraint)
- Bus numbers must be whole integers (decimals are rejected)
- No login/authentication system

## Authors

Developed as a school project. Special thanks to group members, teachers of the computer department, and the principal, Rev Fr Sabu Koodappattu CMI.

## References

- [python.org](https://www.python.org)
- NCERT Computer Science XI & XII
- [MySQL Documentation](https://dev.mysql.com/doc/)
