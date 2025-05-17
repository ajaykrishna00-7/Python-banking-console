# 💰 Banking System CLI – From Scratch to SQL (My High School Projects)

This repository is a showcase of two full-fledged **command-line banking systems** I built back in **11th and 12th grade**, without any AI or external frameworks.

- ✅ Fully functional CLI apps  
- ✅ Secure PIN-based access  
- ✅ Account creation, deposit, withdrawal, transfer  
- ✅ Complaint system, admin panel, account modifications  
- ✅ Built before I even officially learned DBMS or file handling  

---

## 📂 What’s Inside

### 🔹 `11th_Grade_Version_banking_dicts_only.py`

> My first version – all in-memory using just Python dictionaries.

- Built **without file handling or databases**
- `dict()`-based storage for accounts, pins, and complaints
- Features include:
  - Account creation  
  - Deposits & Withdrawals  
  - Transfers  
  - Customer complaints  
  - Bank PIN-protected admin view  
- Pure logic. No persistence. But works like a mini bank.

---

### 🔹 `12th_Grade_Version_banking_mysql_version.py`

> One year later — I scaled it up with real **MySQL backend integration**.

- Connected to **MySQL using `mysql-connector-python`**
- Used `SELECT`, `INSERT`, `UPDATE`, and `DELETE` queries
- Added:
  - Transaction logging  
  - Date-based records  
  - Bulk transfers  
  - CSV logs for customer biodata & complaints  
  - Better security with PIN checks and admin access  

---

## 🚀 How to Run (for 12th Grade Version)

1. Install the required package:

```bash
pip install mysql.connector
```

2. Enter your MySQL DB password in the script:

Inside `12th_Grade_Version_banking_mysql_version.py`, find this line and replace with your credentials:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    passwd="your_mysql_password"
)
```

3. Run the script:

```bash
python 12th_Grade_Version_banking_mysql_version.py
```

> ✅ It will automatically create the database and tables if they don't exist.

> 📌 Transaction history will be stored in MySQL, and additional customer biodata/queries are saved in CSV files.

---

## 🚀 How to Run (for 11th Grade Version)

1. No installations needed. Just run it:

```bash
python 11th_Grade_Version_banking_dicts_only.py
```

> ⚠️ Data is not saved — it runs entirely in memory.  
> When you close the program, everything resets. That’s the charm 😎

---

## 🧠 Why This Exists


- ✅ In 11th: Built a bank using only Python dictionaries  
- ✅ In 12th: Rebuilt it with MySQL, CSVs, and transaction history  

---

