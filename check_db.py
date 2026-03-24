#!/usr/bin/env python3
import sqlite3
import os

db_path = "/vercel/share/v0-project/flask_app/data/pr_data.db"

print(f"[v0] Checking database at: {db_path}")
print(f"[v0] Database exists: {os.path.exists(db_path)}")

if os.path.exists(db_path):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print(f"[v0] Tables found: {tables}")
        
        # Check each table for data
        for table in tables:
            table_name = table[0]
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]
            print(f"[v0] Table '{table_name}': {count} rows")
        
        conn.close()
        print("[v0] Database is accessible and has data")
    except Exception as e:
        print(f"[v0] ERROR accessing database: {e}")
else:
    print("[v0] Database file does not exist!")
