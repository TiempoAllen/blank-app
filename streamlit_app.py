import streamlit as st

# Sidebar for navigation
st.sidebar.title("ALLEN TIEMPO")
pages = ["Home", "About Me", "Skills", "Portfolio"]
choice = st.sidebar.radio("Go to", pages)

# Home Page
if choice == "Home":
    st.title("ALLEN TIEMPO")
    st.write("""
        Full-Stack Web Developer
    """)

# About Me Page
elif choice == "About Me":
    st.title("About Me")
    st.write("""
        ### Hello, I'm Allen Tiempo!
        
        Welcome to my corner of the internet! I'm John Allen Tiempo, a web developer based in Cebu City, Philippines. With a passion for web development, I am dedicated to creating innovative and efficient web solutions.
             
        When I'm not immersed in coding, I'm a student, constantly learning and expanding my knowledge. My journey in the field of web development is just beginning, and while I haven't achieved significant milestones yet, I'm driven by a mission to craft digital experiences that are both functional and visually appealing.
             
        Feel free to explore, connect, and join me on this exciting journey as I continue to grow and make my mark in the world of web development!
    """)

#Skills Page
elif choice == "Skills":
    st.title("My Expertise")
    st.write("""
        ### Software Development
        ###### Specialized in Object-Oriented Programming principles and utilizing robust languages like Java and Javascript.
        ### Frotend Dev - ReactJs
        ###### Skilled in crafting responsive and user-friendly web interfaces using HTML, CSS, JS, ReactJS Framework.
        ### Backend Dev - ExpressJS, PostgreSQL
        ###### Excel in implementing APIs with ExpressJS and Spring Boot. Knowledgable with relational databases like PostgreSQL and MySQL.
             """)

# Portfolio Page
elif choice == "Portfolio":
    st.title("Portfolio")
    st.write("""
         ### Personal Portfolio Website
        - **Description**: Developed a responsive personal portfolio webstie to showcase projects and skills using ReactJS
        - **Key Features**: Responsive Design, interactive elements, integration with social media profiles
        - **Link**: https://tiempoallen.onrender.com/
        
        ### Campus Sync
        - **Description**: Developed a comprehensive system for campus announcements and event management.
        - **Key Features**: User authentication and authorization, CRUD operations for announcements and events, Notifications for new announcements and events
        - **Link**: https://tiempoallen.onrender.com/
        
        ### CITU Streamlined Service Portal
        - **Description**: Designed and developed a system where users can request various types of technicians, including janitors, electricians, and plumbers.
        - **Key Features**: User-friendly interface for service requests, Role-based access control for users and administrators, Comprehensive reporting and analytics.
        - **Link**: https://github.com/TiempoAllen/streamlined-service-portal.git
    """)

# Footer
st.sidebar.write("""
    ---
    © [2024] [Allen Tiempo]
""")