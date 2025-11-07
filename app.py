import streamlit as st

# Import fungsi autentikasi dari db_cloud.py (cloud-ready database)
from db_cloud import authenticate, create_users_table, add_user

def dashboard_page():
    """Halaman dashboard setelah login"""
    st.title("🏠 Dashboard")
    st.write("---")
    
    # Header welcome
    if 'username' in st.session_state:
        st.write(f"### Selamat datang, {st.session_state['username']}! 👋")
    else:
        st.write("### Selamat datang di Dashboard! 👋")
    
    # Dashboard content
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="📊 Total Users", 
            value="1,234",
            delta="12"
        )
    
    with col2:
        st.metric(
            label="📈 Monthly Growth", 
            value="85%",
            delta="5.2%"
        )
    
    with col3:
        st.metric(
            label="💰 Revenue", 
            value="$12,345",
            delta="$1,200"
        )
    
    st.write("---")
    
    # Sample chart
    import pandas as pd
    import numpy as np
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Data A', 'Data B', 'Data C']
    )
    
    st.subheader("📈 Sample Analytics")
    st.line_chart(chart_data)
    
    # Quick actions
    st.write("---")
    st.subheader("🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📝 Create Report", use_container_width=True):
            st.success("Creating new report...")
    
    with col2:
        if st.button("👥 Manage Users", use_container_width=True):
            st.info("Opening user management...")
    
    with col3:
        if st.button("⚙️ Settings", use_container_width=True):
            st.info("Opening settings...")
    
    with col4:
        if st.button("🚪 Logout", use_container_width=True, type="primary"):
            st.session_state['logged_in'] = False
            st.session_state.pop('username', None)
            st.rerun()

def login_page():
    """Halaman login"""
    st.title("🔐 Login Page")
    
    # Center the login form
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.write("---")
        username = st.text_input("👤 Username", placeholder="Enter your username")
        password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
        
        if st.button("🚀 Login", use_container_width=True, type="primary"):
            if username and password:  # Check if fields are not empty
                if authenticate(username, password):
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.success("✅ Login successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password.")
            else:
                st.warning("⚠️ Please fill in both username and password.")

def main():
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    
    # Show appropriate page based on login status
    if st.session_state['logged_in']:
        dashboard_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
