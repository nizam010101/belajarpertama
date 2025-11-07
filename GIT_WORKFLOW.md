# Git Workflow untuk Update Proyek

## 📝 Langkah Update Kode:

### 1. Pastikan di branch yang benar
git status
git branch

### 2. Pull perubahan terbaru (jika ada)
git pull origin main

### 3. Buat perubahan pada kode Anda
# Edit file yang diperlukan...

### 4. Cek perubahan yang dibuat
git status
git diff

### 5. Add file yang diubah
git add .
# atau specific file: git add nama_file.py

### 6. Commit dengan pesan yang jelas
git commit -m "feat: menambah fitur X"
# atau
git commit -m "fix: perbaiki bug Y"
# atau
git commit -m "update: improve dashboard UI"

### 7. Push ke GitHub
git push origin main

## 🔐 Keamanan saat Update:
- Jangan pernah commit file .env
- Selalu cek git status sebelum add
- Gunakan pesan commit yang descriptive

## 🚀 Auto-deployment:
- Streamlit Cloud akan auto-deploy setelah push ke GitHub
- Perubahan akan live dalam 1-3 menit