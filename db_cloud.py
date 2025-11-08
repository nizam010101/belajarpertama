# Database configuration for Streamlit Cloud deployment
import os
import sqlite3
import streamlit as st

# Try to import mysql.connector, but fallback to SQLite if not available
try:
    import mysql.connector
    MYSQL_AVAILABLE = True
except ImportError:
    MYSQL_AVAILABLE = False

def get_database_config():
    """Get database configuration based on environment"""
    
    # Check if running in Streamlit context
    try:
        import streamlit as st
        # Check if running on Streamlit Cloud
        if hasattr(st, 'secrets') and "database" in st.secrets:
            # Use Streamlit Cloud secrets
            return {
                'type': 'mysql',
                'config': {
                    'host': st.secrets["database"]["host"],
                    'user': st.secrets["database"]["user"],
                    'password': st.secrets["database"]["password"],
                    'database': st.secrets["database"]["database"],
                    'port': st.secrets["database"].get("port", 3306)
                }
            }
    except (ImportError, Exception):
        # Not in Streamlit context or secrets not available
        pass
    
    # Check environment variables
    if os.getenv('DATABASE_URL') or os.getenv('DB_HOST'):
        # Parse environment variables for production deployment
        return {
            'type': 'mysql',
            'config': {
                'host': os.getenv('DB_HOST', 'localhost'),
                'user': os.getenv('DB_USER', 'root'),
                'password': os.getenv('DB_PASSWORD', ''),
                'database': os.getenv('DB_NAME', 'streamlit_app'),
                'port': int(os.getenv('DB_PORT', 3306))
            }
        }
    
    else:
        # Default to SQLite for local development and cloud deployment
        return {
            'type': 'sqlite',
            'config': {
                'database': 'app_database.db'
            }
        }

def get_db_connection():
    """Get database connection based on configuration"""
    db_config = get_database_config()
    
    if db_config['type'] == 'mysql' and MYSQL_AVAILABLE:
        try:
            return mysql.connector.connect(**db_config['config'])
        except mysql.connector.Error as e:
            print(f"MySQL connection failed: {e}")
            print("Falling back to SQLite...")
            # Fallback to SQLite
            return sqlite3.connect('app_database.db')
    else:
        # Use SQLite
        return sqlite3.connect(db_config['config']['database'])

def check_db_connection():
    """Check if database connection is working"""
    try:
        conn = get_db_connection()
        db_config = get_database_config()
        
        if db_config['type'] == 'mysql':
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.fetchone()
            cursor.close()
        else:
            # SQLite
            cursor = conn.cursor()
            cursor.execute("SELECT 1")
            cursor.fetchone()
            cursor.close()
        
        conn.close()
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def create_users_table():
    """Create users table (compatible with both MySQL and SQLite)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    db_config = get_database_config()
    
    if db_config['type'] == 'mysql':
        # MySQL syntax
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            )
        ''')
    else:
        # SQLite syntax
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
    
    conn.commit()
    cursor.close()
    conn.close()

def authenticate(username, password):
    """Authenticate user (compatible with both MySQL and SQLite)"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        db_config = get_database_config()
        
        if db_config['type'] == 'mysql':
            query = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(query, (username, password))
        else:
            query = "SELECT * FROM users WHERE username=? AND password=?"
            cursor.execute(query, (username, password))
        
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
        
    except Exception as e:
        print(f"Authentication error: {e}")
        # Try to create table and default user
        try:
            create_users_table()
            add_user("admin", "password123")
        except:
            pass
        return False

def add_user(username, password):
    """Add new user (compatible with both MySQL and SQLite)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    db_config = get_database_config()
    
    try:
        if db_config['type'] == 'mysql':
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        else:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        cursor.close()
        conn.close()
        return False

if __name__ == "__main__":
    print("🔧 Testing database connection...")
    
    # Test connection
    check_db_connection()
    
    # Create table
    create_users_table()
    
    # Add test user
    if add_user("admin", "password123"):
        print("✅ Test user 'admin' added successfully!")
    else:
        print("ℹ️ User 'admin' might already exist.")
    
    # Test authentication
    if authenticate("admin", "password123"):
        print("✅ Authentication test passed!")
    else:
        print("❌ Authentication test failed!")