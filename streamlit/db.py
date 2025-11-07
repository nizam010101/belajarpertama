import mysql.connector

DB_CONFIG = {
    'host': 'localhost',  # Ubah dari IP eksternal ke localhost karena MySQL di VPS yang sama
    'user': 'belajarmysql',
    'password': 'Nizam.160721',
    'database': 'belajarpertama'
}

def check_db_connection():
    try:
        conn = get_db_connection()
        conn.close()
        print("Koneksi ke database MySQL berhasil.")
        return True
    except Exception as e:
        print(f"Gagal terhubung ke database MySQL: {e}")
        return False

def create_users_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def authenticate(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None



if __name__ == "__main__":
    print("Menguji koneksi ke database...")
    check_db_connection()
    create_users_table()
