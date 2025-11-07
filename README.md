# 🔐 Streamlit Authentication App

Aplikasi web berbasis Streamlit dengan sistem autentikasi MySQL/SQLite dan dashboard interaktif.

## ✨ Features

- 🔑 **Login System** - Autentikasi aman dengan database
- 🏠 **Dashboard** - Interface yang responsive dengan metrics dan charts
- 💾 **Database Flexibility** - Support MySQL dan SQLite
- ☁️ **Cloud Ready** - Siap deploy ke Streamlit Cloud
- 🛡️ **Security** - CSRF protection dan session management

## 🚀 Quick Start

### Local Development

1. **Clone repository**
   ```bash
   git clone <your-repo-url>
   cd streamlit-auth-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run application**
   ```bash
   streamlit run app.py
   ```

4. **Access application**
   ```
   http://localhost:8501
   ```

### Default Login Credentials
- **Username**: `admin`
- **Password**: `password123`

## ☁️ Deploy to Streamlit Cloud

1. **Push ke GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy di Streamlit Cloud**
   - Buka [share.streamlit.io](https://share.streamlit.io)
   - Connect dengan GitHub repository
   - Pilih `app.py` sebagai main file
   - Deploy!

3. **Database Configuration (Optional)**
   
   Untuk MySQL di cloud, tambahkan di Streamlit secrets:
   ```toml
   # .streamlit/secrets.toml
   [database]
   host = "your-mysql-host"
   user = "your-username"
   password = "your-password"
   database = "your-database"
   port = 3306
   ```

## 🗄️ Database

### SQLite (Default)
- Otomatis menggunakan SQLite jika MySQL tidak tersedia
- File database: `app_database.db`
- Cocok untuk development dan small deployment

### MySQL (Production)
- Konfigurasi melalui environment variables atau Streamlit secrets
- Support untuk production deployment
- Lebih scalable untuk user yang banyak

## 📁 Project Structure

```
streamlit-auth-app/
├── app.py                 # Main Streamlit application
├── db_cloud.py           # Database handler (MySQL/SQLite)
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── README.md            # Documentation
└── .streamlit/
    └── config.toml      # Streamlit configuration
```

## 🔧 Configuration

### Local Development
- Database: SQLite (otomatis terbuat)
- Host: `127.0.0.1:8501`
- Security: CSRF protection enabled

### Production/Cloud
- Database: MySQL atau SQLite
- Configuration via secrets atau environment variables
- SSL/HTTPS ready

## 🛠️ Development

### Add New User
```python
from db_cloud import add_user

# Tambah user baru
add_user("username", "password")
```

### Database Schema
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);
```

## 📝 TODO / Roadmap

- [ ] Password hashing (bcrypt)
- [ ] User registration form
- [ ] Role-based access control
- [ ] Password reset functionality
- [ ] Email notifications
- [ ] User profile management

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

Jika ada pertanyaan atau masalah:
- Open an issue di GitHub
- Contact: [your-email@example.com]

---

**Made with ❤️ using Streamlit**