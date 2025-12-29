#!/usr/bin/env python3
"""
GAIA Project Setup Script
Team: Akshra Reddy, Gagan Chowdary, Rakesh
Creates the complete frozen project structure
"""

import os
import subprocess
import sys
from pathlib import Path

# =============================================================================
# BLOCK 1: TEAM INFORMATION & CONFIGURATION
# =============================================================================

TEAM_MEMBERS = [
    "Akshra Reddy",
    "Gagan Chowdary", 
    "Rakesh"
]

def display_team_info():
    """Display team information"""
    print("🎓 GAIA - Generative AI for Automated Assessment in Education")
    print("=" * 60)
    print("👥 Development Team:")
    for member in TEAM_MEMBERS:
        print(f"   • {member}")
    print("=" * 60)

# =============================================================================
# BLOCK 2: PROJECT STRUCTURE CREATION
# =============================================================================

def create_structure():
    """Create the complete project structure"""
    
    print("🚀 Creating GAIA project structure...")
    
    # Define the directory structure
    structure = {
        'streamlit_app': ['pages', 'components', 'utils'],
        'backend': {
            'app': [],
            'models': [],
            'services': [],
            'tests': []
        },
        'infrastructure': [],
        'database': [],
        'docs': [],
    }
    
    # Create directories
    for main_dir, sub_dirs in structure.items():
        if isinstance(sub_dirs, list):
            # Create main directory
            Path(main_dir).mkdir(exist_ok=True)
            print(f"📁 Created: {main_dir}/")
            
            # Create subdirectories
            for sub_dir in sub_dirs:
                sub_path = Path(main_dir) / sub_dir
                sub_path.mkdir(parents=True, exist_ok=True)
                print(f"  └── {sub_dir}/")
        else:
            # Nested structure
            Path(main_dir).mkdir(exist_ok=True)
            print(f"📁 Created: {main_dir}/")
            
            for sub_dir, sub_sub_dirs in sub_dirs.items():
                sub_path = Path(main_dir) / sub_dir
                sub_path.mkdir(parents=True, exist_ok=True)
                print(f"  ├── {sub_dir}/")
                
                for sub_sub_dir in sub_sub_dirs:
                    sub_sub_path = sub_path / sub_sub_dir
                    sub_sub_path.mkdir(parents=True, exist_ok=True)
                    print(f"  │   └── {sub_sub_dir}/")
    
    print("✅ Directory structure created successfully!")

# =============================================================================
# BLOCK 3: REQUIREMENTS.TXT CREATION
# =============================================================================

def create_requirements():
    """Create requirements.txt file"""
    
    requirements_content = """# GAIA Project Dependencies
# Team: Akshra Reddy, Gagan Chowdary, Rakesh

# Web Framework
streamlit==1.28.0
fastapi==0.104.1
uvicorn==0.24.0

# AI & Machine Learning
openai==1.3.0

# Database
psycopg2-binary==2.9.9

# Authentication & Security
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
PyJWT==2.8.0

# AWS Services
boto3==1.28.0

# Utilities
python-dotenv==1.0.0
pydantic==2.5.0
requests==2.31.0
python-multipart==0.0.6
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements_content)
    
    print("✅ Created: requirements.txt")

# =============================================================================
# BLOCK 4: ENVIRONMENT FILES CREATION
# =============================================================================

def create_environment_files():
    """Create environment configuration files"""
    
    # Create .env file
    env_content = """# GAIA Project Configuration
# Team: Akshra Reddy, Gagan Chowdary, Rakesh

# Application Settings
DEBUG=True
ENVIRONMENT=development

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# AWS Configuration (for future use)
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key

# Database Configuration (for future use)
DATABASE_URL=postgresql://username:password@localhost:5432/gaia_dev

# JWT Secret Key
SECRET_KEY=your-super-secret-jwt-key-change-in-production
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    # Create .gitignore
    gitignore_content = """# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# AWS
*.aws
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    
    print("✅ Created: .env")
    print("✅ Created: .gitignore")

# =============================================================================
# BLOCK 5: BACKEND FILES CREATION
# =============================================================================

def create_backend_files():
    """Create backend FastAPI application"""
    
    # Create backend/app/__init__.py
    Path("backend/app/__init__.py").write_text("# Backend application package\n")
    
    # Create backend/app/main.py
    main_py_content = '''"""
GAIA Backend API
Team: Akshra Reddy, Gagan Chowdary, Rakesh
Generative AI for Automated Assessment in Education
"""

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import jwt
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="GAIA API",
    description="Generative AI for Automated Assessment in Education - Backend by Akshra Reddy, Gagan Chowdary, Rakesh",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://127.0.0.1:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Models
class UserRegister(BaseModel):
    full_name: str
    email: str
    password: str
    role: str
    institution: str

class UserLogin(BaseModel):
    email: str
    password: str

# Mock DB
users_db = {}

def validate_edu_email(email: str):
    """Validate educational email domains"""
    allowed_domains = [".edu", ".ac.", ".edu.in", ".school.nz", ".ac.uk", ".edu.au"]
    domain = email.split('@')[-1].lower()
    return any(allowed_domain in domain for allowed_domain in allowed_domains)

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@app.get("/")
def root():
    return {
        "message": "🎓 GAIA Backend API", 
        "status": "running", 
        "version": "1.0.0",
        "team": ["Akshra Reddy", "Gagan Chowdary", "Rakesh"]
    }

@app.get("/health")
def health():
    return {
        "status": "healthy", 
        "timestamp": datetime.utcnow().isoformat(),
        "service": "GAIA Backend API"
    }

@app.post("/api/auth/register")
def register(user: UserRegister):
    if not validate_edu_email(user.email):
        raise HTTPException(status_code=400, detail="Please use a valid educational email address (.edu, .ac.* domains)")
    
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    
    users_db[user.email] = {
        "full_name": user.full_name,
        "password_hash": hash_password(user.password),
        "role": user.role,
        "institution": user.institution,
        "created_at": datetime.utcnow()
    }
    
    return {
        "message": "Registration successful", 
        "email": user.email,
        "role": user.role
    }

@app.post("/api/auth/login")
def login(login_data: UserLogin):
    user = users_db.get(login_data.email)
    if not user or not verify_password(login_data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    return {
        "message": "Login successful",
        "email": login_data.email,
        "role": user["role"],
        "full_name": user["full_name"]
    }

@app.get("/api/auth/validate-email")
def validate_email(email: str):
    """Validate email format"""
    is_valid = validate_edu_email(email)
    return {
        "email": email,
        "is_valid_educational": is_valid,
        "message": "Valid educational email" if is_valid else "Please use .edu or academic domain"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''
    
    Path("backend/app/main.py").write_text(main_py_content)
    print("✅ Created: backend/app/main.py")

# =============================================================================
# BLOCK 6: FRONTEND FILES CREATION - UPDATED WITH BETTER UI
# =============================================================================

def create_frontend_files():
    """Create Streamlit frontend application with improved UI"""
    
    # Create streamlit_app/app.py
    app_py_content = '''"""
GAIA Frontend Application
Team: Akshra Reddy, Gagan Chowdary, Rakesh
AI-Powered Assessment Platform
"""

import streamlit as st
import requests
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="GAIA - AI Assessment Platform",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern UI
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        padding: 2rem 0;
    }
    .login-container {
        background: white;
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        margin: 2rem auto;
        max-width: 500px;
        border: 1px solid #e0e0e0;
    }
    .header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .team-info {
        text-align: center;
        color: #666;
        font-size: 0.9rem;
        margin-top: 1rem;
        padding: 0.5rem;
        background: #f8f9fa;
        border-radius: 10px;
    }
    .role-badge {
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem 0;
    }
    .professor-badge {
        background: #e3f2fd;
        color: #1976d2;
    }
    .student-badge {
        background: #f3e5f5;
        color: #7b1fa2;
    }
    .stButton button {
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .dashboard-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

def login_ui():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="header">
        <h1 style='text-align: center; color: #1976d2; margin-bottom: 0; font-size: 3rem;'>🎓</h1>
        <h2 style='text-align: center; color: #333; margin-top: 0; margin-bottom: 0.5rem;'>GAIA</h2>
        <p style='text-align: center; color: #666; font-size: 1.1rem; margin-bottom: 2rem;'>AI-Powered Educational Assessment Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Team info
    st.markdown("""
    <div class="team-info">
        <strong>Development Team:</strong> Akshra Reddy, Gagan Chowdary, Rakesh
    </div>
    """, unsafe_allow_html=True)
    
    # Login/Register Tabs
    tab1, tab2 = st.tabs(["🔐 **Sign In**", "📝 **Create Account**"])
    
    with tab1:
        with st.form("login_form"):
            st.subheader("Welcome Back")
            email = st.text_input("📧 Email Address", placeholder="your.email@your-university.edu")
            password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
            
            login_btn = st.form_submit_button("🚀 Sign In to GAIA", use_container_width=True, type="primary")
            
            if login_btn:
                if email and password:
                    # Enhanced email validation
                    if any(domain in email.lower() for domain in ['.edu', '.ac.', '.school', '.college']):
                        st.session_state.logged_in = True
                        st.session_state.user_email = email
                        # Extract domain for institution name
                        domain = email.split('@')[-1]
                        st.session_state.user_institution = domain.split('.')[0].title()
                        st.session_state.user_role = "professor" if any(word in email.lower() for word in ['prof', 'staff', 'faculty']) else "student"
                        st.success(f"✅ Welcome back, {email}!")
                        st.rerun()
                    else:
                        st.error("❌ Please use a valid educational email address (.edu, .ac.* domains)")
                else:
                    st.error("❌ Please fill in all fields")
    
    with tab2:
        with st.form("register_form"):
            st.subheader("Join GAIA Platform")
            full_name = st.text_input("👤 Full Name", placeholder="Enter your full name")
            email = st.text_input("📧 Educational Email", placeholder="name@your-university.edu")
            password = st.text_input("🔒 Create Password", type="password", placeholder="Minimum 8 characters")
            confirm_password = st.text_input("🔒 Confirm Password", type="password", placeholder="Re-enter your password")
            role = st.selectbox("🎯 Your Role", ["Student", "Professor", "Researcher", "Administrator"])
            
            # Dynamic institution from email domain
            institution = ""
            if email and '@' in email:
                domain_parts = email.split('@')[-1].split('.')
                if len(domain_parts) >= 2:
                    institution = domain_parts[-2].title() + " University"
            
            institution_input = st.text_input("🏫 Institution", value=institution, placeholder="Will auto-detect from email")
            
            # Role badge with dynamic styling
            if role == "Professor":
                st.markdown(f'<div class="role-badge professor-badge">👨‍🏫 {role} Account</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="role-badge student-badge">👨‍🎓 {role} Account</div>', unsafe_allow_html=True)
            
            agree_terms = st.checkbox("I agree to the Terms of Service and Privacy Policy")
            
            register_btn = st.form_submit_button("🎓 Create GAIA Account", use_container_width=True, type="primary")
            
            if register_btn:
                if not all([full_name, email, password, institution_input]):
                    st.error("❌ Please fill in all required fields")
                elif len(password) < 8:
                    st.error("❌ Password must be at least 8 characters long")
                elif password != confirm_password:
                    st.error("❌ Passwords do not match")
                elif not agree_terms:
                    st.error("❌ Please agree to the terms and conditions")
                elif not any(domain in email.lower() for domain in ['.edu', '.ac.', '.school', '.college']):
                    st.error("❌ Please use a valid educational email address (.edu, .ac.* domains)")
                else:
                    st.success(f"✅ Registration successful! Welcome to GAIA, {full_name}!")
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.session_state.user_role = role.lower()
                    st.session_state.user_institution = institution_input
                    st.session_state.full_name = full_name
                    st.rerun()
    
    # Demo Access
    st.markdown("---")
    with st.expander("🛠️ Quick Demo Access"):
        st.info("For testing and demonstration purposes:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**👨‍🏫 Professor Account:**")
            st.code("prof.smith@harvard.edu\\nAnyPassword123")
            if st.button("Quick Login as Professor", key="prof_demo", use_container_width=True):
                st.session_state.logged_in = True
                st.session_state.user_email = "prof.smith@harvard.edu"
                st.session_state.user_role = "professor"
                st.session_state.user_institution = "Harvard"
                st.session_state.full_name = "Professor Smith"
                st.rerun()
        
        with col2:
            st.write("**👨‍🎓 Student Account:**")
            st.code("student.john@stanford.edu\\nAnyPassword123")
            if st.button("Quick Login as Student", key="student_demo", use_container_width=True):
                st.session_state.logged_in = True
                st.session_state.user_email = "student.john@stanford.edu"
                st.session_state.user_role = "student"
                st.session_state.user_institution = "Stanford"
                st.session_state.full_name = "John Student"
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def professor_dashboard():
    """Professor dashboard with modern UI"""
    st.markdown(f'<div class="dashboard-card">', unsafe_allow_html=True)
    st.title("👨‍🏫 Professor Dashboard")
    st.write(f"Welcome back, **{st.session_state.get('full_name', 'Professor')}** from **{st.session_state.get('user_institution', 'your institution')}**")
    
    # Quick stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Active Courses", "3")
    with col2:
        st.metric("Total Students", "142")
    with col3:
        st.metric("Assignments", "12")
    
    st.markdown("---")
    
    # Create Assignment Form
    st.subheader("📝 Create New Assignment")
    with st.form("create_assignment"):
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("Assignment Title", placeholder="e.g., Midterm Essay - Shakespeare")
        with col2:
            due_date = st.date_input("Due Date")
        
        course = st.selectbox("Select Course", ["Introduction to Computer Science", "Advanced Mathematics", "Literature 101", "Data Structures"])
        question = st.text_area("Assignment Question", height=150, placeholder="Enter the assignment question or prompt...")
        expected_answer = st.text_area("Expected Answer Guide (Optional)", height=100, placeholder="Guidance for AI assessment...")
        points = st.slider("Total Points", 10, 100, 50)
        
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.form_submit_button("📤 Create Assignment", use_container_width=True, type="primary"):
                if title and question:
                    st.success(f"✅ Assignment '{title}' created successfully! Worth {points} points.")
                else:
                    st.error("❌ Please fill in title and question")
        with col2:
            if st.form_submit_button("Save as Draft", use_container_width=True):
                st.info("💾 Assignment saved as draft")
    
    st.markdown('</div>', unsafe_allow_html=True)

def student_dashboard():
    """Student dashboard with modern UI"""
    st.markdown(f'<div class="dashboard-card">', unsafe_allow_html=True)
    st.title("👨‍🎓 Student Dashboard")
    st.write(f"Welcome back, **{st.session_state.get('full_name', 'Student')}** from **{st.session_state.get('user_institution', 'your institution')}**")
    
    # Current assignments
    st.subheader("📚 Current Assignments")
    
    # Sample assignments
    assignments = [
        {"title": "Essay on Machine Learning", "due": "2024-12-15", "status": "Pending"},
        {"title": "Math Problem Set #5", "due": "2024-12-10", "status": "Submitted"},
        {"title": "Literature Review", "due": "2024-12-20", "status": "Pending"}
    ]
    
    for i, assignment in enumerate(assignments):
        with st.expander(f"📄 {assignment['title']} - Due: {assignment['due']}"):
            st.write(f"Status: **{assignment['status']}**")
            if assignment['status'] == "Pending":
                answer = st.text_area(f"Your Answer #{i}", height=150, placeholder="Type your answer here...")
                if st.button(f"Submit Assignment #{i+1}", key=f"submit_{i}"):
                    if answer:
                        st.success("✅ Assignment submitted! AI feedback coming soon.")
                    else:
                        st.error("❌ Please write your answer")
    
    st.markdown('</div>', unsafe_allow_html=True)

def main_dashboard():
    """Main dashboard with sidebar navigation"""
    
    # Sidebar
    with st.sidebar:
        st.title("🎓 GAIA Platform")
        st.write(f"**Welcome,** {st.session_state.get('full_name', st.session_state.user_email)}")
        st.write(f"**Role:** {st.session_state.user_role.title()}")
        st.write(f"**Institution:** {st.session_state.get('user_institution', 'Not specified')}")
        
        st.markdown("---")
        st.markdown("### 👥 Development Team")
        st.write("Akshra Reddy, Gagan Chowdary, Rakesh")
        
        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    # Main content based on role
    if st.session_state.user_role == "professor":
        professor_dashboard()
    else:
        student_dashboard()

# Check authentication
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_ui()
else:
    main_dashboard()
'''
    
    Path("streamlit_app/app.py").write_text(app_py_content)
    print("✅ Created: streamlit_app/app.py")

# =============================================================================
# BLOCK 7: VIRTUAL ENVIRONMENT SETUP
# =============================================================================

def setup_virtual_environment():
    """Create and setup virtual environment"""
    print("🐍 Setting up virtual environment...")
    
    try:
        # Create virtual environment
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Virtual environment created: venv/")
        
        # Determine the correct pip path
        if os.name == 'nt':  # Windows
            pip_path = os.path.join("venv", "Scripts", "pip")
        else:  # Unix/Linux/Mac
            pip_path = os.path.join("venv", "bin", "pip")
        
        # Install requirements
        print("📦 Installing dependencies...")
        subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error setting up virtual environment: {e}")
        print("💡 You can manually run: python -m venv venv && source venv/bin/activate && pip install -r requirements.txt")

# =============================================================================
# BLOCK 8: MAIN EXECUTION FUNCTION
# =============================================================================

def main():
    """Main setup function"""
    display_team_info()
    
    # Get current directory
    current_dir = Path.cwd()
    print(f"📂 Setting up project in: {current_dir}")
    
    # Create project structure
    create_structure()
    create_requirements()
    create_environment_files()
    create_backend_files()
    create_frontend_files()
    
    # Setup virtual environment
    setup_virtual_environment()
    
    print("=" * 60)
    print("🎉 GAIA Project Setup Complete!")
    print("\n🚀 Next steps:")
    print("1. Activate virtual environment:")
    print("   - Windows: venv\\Scripts\\activate")
    print("   - Mac/Linux: source venv/bin/activate")
    print("\n2. Start the backend:")
    print("   cd backend && uvicorn app.main:app --reload --port 8000")
    print("\n3. Start the frontend (new terminal):")
    print("   cd streamlit_app && streamlit run app.py")
    print("\n4. Open http://localhost:8501 in your browser")
    print("\n👥 Developed by: Akshra Reddy, Gagan Chowdary, Rakesh")

# =============================================================================
# BLOCK 9: SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()