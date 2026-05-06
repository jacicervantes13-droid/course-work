http://localhost:8502/

import streamlit as st
import sqlite3
import pandas as pd

# Database connection
@st.cache_resource
def get_connection():
    return sqlite3.connect("employees.db", check_same_thread=False)

cnx = get_connection()

# Create table if it doesn't exist
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        position TEXT
    )
    """
    cnx.execute(query)
    cnx.commit()

create_table()

# CREATE
def create_record():
    st.subheader("Add a New Record")
    name = st.text_input("Name", key="create_name")
    age = st.number_input("Age", min_value=0, max_value=150, key="create_age")
    position = st.text_input("Position", key="create_position")

    if st.button("Add Record"):
        if name and position:
            query = "INSERT INTO employees (name, age, position) VALUES (?, ?, ?)"
            cnx.execute(query, (name, age, position))
            cnx.commit()
            st.success("Record added successfully")
        else:
            st.warning("Please fill out all fields")

# READ
def read_records_pandas():
    st.subheader("View Records")
    df = pd.read_sql("SELECT * FROM employees", cnx)
    st.dataframe(df)

# UPDATE
def update_record():
    st.subheader("Update a Record")

    rows = cnx.execute("SELECT id, name FROM employees").fetchall()
    if not rows:
        st.info("No records available")
        return

    record_dict = {f"{id} - {name}": id for id, name in rows}
    selected = st.selectbox("Select record", list(record_dict.keys()))

    record_id = record_dict[selected]

    row = cnx.execute(
        "SELECT name, age, position FROM employees WHERE id = ?",
        (record_id,)
    ).fetchone()

    name, age, position = row

    new_name = st.text_input("Name", value=name, key="update_name")
    new_age = st.number_input("Age", value=age, key="update_age")
    new_position = st.text_input("Position", value=position, key="update_position")

    if st.button("Update Record"):
        cnx.execute(
            "UPDATE employees SET name=?, age=?, position=? WHERE id=?",
            (new_name, new_age, new_position, record_id)
        )
        cnx.commit()
        st.success("Record updated successfully")

# DELETE
def delete_record():
    st.subheader("Delete a Record")

    rows = cnx.execute("SELECT id, name FROM employees").fetchall()
    if not rows:
        st.info("No records available")
        return

    record_dict = {f"{id} - {name}": id for id, name in rows}
    selected = st.selectbox("Select record to delete", list(record_dict.keys()))

    record_id = record_dict[selected]

    if st.button("Delete Record"):
        cnx.execute("DELETE FROM employees WHERE id=?", (record_id,))
        cnx.commit()
        st.warning("Record deleted")

# MAIN APP
def main():
    st.title("CRUD App with SQLite")

    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        create_record()
    elif choice == "Read":
        read_records_pandas()
    elif choice == "Update":
        update_record()
    elif choice == "Delete":
        delete_record()

if __name__ == "__main__":
    main()
