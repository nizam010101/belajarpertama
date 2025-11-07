#!/usr/bin/env python3

# Script untuk menambahkan user test ke database
import sys
import os

# Tambahkan path ke parent directory agar bisa import db.py
sys.path.append('/root/project/strml/streamlit')

from db import get_db_connection

def add_test_user():
    """Menambahkan user test ke database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Cek apakah user sudah ada
        cursor.execute("SELECT * FROM users WHERE username = %s", ("admin",))
        existing_user = cursor.fetchone()
        
        if existing_user:
            print("✅ User 'admin' sudah ada di database")
        else:
            # Insert user baru
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                ("admin", "password123")
            )
            conn.commit()
            print("✅ User 'admin' berhasil ditambahkan ke database")
        
        # Tampilkan semua users
        cursor.execute("SELECT id, username FROM users")
        users = cursor.fetchall()
        
        print("\n📋 Daftar users di database:")
        for user in users:
            print(f"  - ID: {user[0]}, Username: {user[1]}")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🔧 Menambahkan user test untuk login...")
    add_test_user()
    print("\n💡 Gunakan kredensial berikut untuk login:")
    print("   Username: admin")
    print("   Password: password123")