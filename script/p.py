import streamlit as st
import requests

st.markdown("""
<meta property="og:title" content="Bilal Ahmed-Portfolio" />
<meta property="og:description" content="My Streamlit portfolio showcasing my projects, resume, and skills in Data Science & ML." />
<meta property="og:image" content="script/metaprofile.png" />
<meta property="og:url" content="https://bilall2003-my-portfolio-scriptp-zjtvup.streamlit.app/" />
""", unsafe_allow_html=True)

class _portfolio:
    def font(self):
         # Inject custom CSS for background and gradients
        st.markdown("""
        <style>
        /* 🌈 Gradient Background */
        body {
            background: linear-gradient(135deg, #0F2027, #203A43, #2C536F);
            background-attachment: fixed;
            color: black;
        }

        /* 🌈 Animated Gradient Background (optional) */
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        body {
            background: linear-gradient(270deg, #1a2a6c, #b21f1f, #fdbb2d);
            background-size: 600% 600%;
            animation: gradientShift 15s ease infinite;
        }

        /* ✨ Gradient Text Styles */
        .gradient-title {
            font-size: 50px;
            font-weight: 900;
            background: linear-gradient(90deg, #00C9FF, #92FE9D);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .gradient-subheader {
            font-size: 26px;
            font-weight: 600;
            background: linear-gradient(90deg, #FF6B6B, #FFD93D);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .gradient-body {
            font-size: 18px;
            background: linear-gradient(90deg, #A1FFCE, #FAFFD1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .gradient-line {
                height: 5px;
                width: 100%;
                background: linear-gradient(90deg, #ff7e5f, #feb47b, #00c6ff, #0072ff, #8e2de2, #4a00e0);
                border: none;
                margin-top: -8px; /* pulls line closer to text */
                border-radius: 5px;
            }

        """, unsafe_allow_html=True)

        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    
    def __info(self):
        
        st.set_page_config(layout="wide")
        col_1,col_2=st.columns([0.5,1],gap="small")
        with col_1:
            st.markdown("<h1 class='gradient-title'>Hi, I'm Bilal Ahmed</h1>", unsafe_allow_html=True)
            st.markdown("<h4 class='gradient-subheader'>Data Scientist | AI & Machine Learning | Python</h4>", unsafe_allow_html=True)
            st.markdown("<p class='gradient-body'>Karachi, Sindh, Pakistan</p>", unsafe_allow_html=True)
        with col_2:
            st.image("script/profile.png")
            
        
        st.divider()
        st.markdown("<h1 class='gradient-title'>Professional Summary</h1>", unsafe_allow_html=True)
        st.markdown("""
        <p class='gradient-body'>
        I work with Machine Learning to turn data into intelligent insights — from prediction models to smart automation.
        Lately, I’ve been diving into NLP, teaching machines to understand text, analyze sentiment,
        and communicate naturally through chatbot systems.
        </p>
        """, unsafe_allow_html=True)
        st.divider()

        st.markdown("<h1 class='gradient-title'>Core Competencies</h1>", unsafe_allow_html=True)
        st.markdown("<p class='gradient-body'>Leveraging Python and specialized libraries for end-to-end data science projects.</p>", unsafe_allow_html=True)

        col1, col2= st.columns(2 ,gap="large")
        with col1:
            st.image("https://media.istockphoto.com/id/2148264573/vector/stock-market-investment-data-and-analysis-finance-graph-business-financial-chart-with-moving.jpg?s=612x612&w=0&k=20&c=K3HuUFBvH4iFrnb54v0F9iyT7DMmkDIN6tiSwL_9yGA=",width=100)
            st.markdown("<h3 class='gradient-subheader'>Data Analysis</h3>", unsafe_allow_html=True)
            st.markdown("<p class='gradient-body'>Cleaning, processing, and exploratory data analysis (EDA).</p>", unsafe_allow_html=True)

        with col2:
            st.image("https://miro.medium.com/0*EijvT-hrU4R6-nbU.jpg",width=90)
            st.markdown("<h3 class='gradient-subheader'>Machine Learning</h3>", unsafe_allow_html=True)
            st.markdown("<p class='gradient-body'>Building and deploying predictive models for various applications.</p>", unsafe_allow_html=True)
            
        col3, col4= st.columns(2 ,gap="large")
        
        with col3:
            st.image("https://4kwallpapers.com/images/wallpapers/python-logo-dark-3840x2160-16094.png",width=100)
            st.markdown("<h3 class='gradient-subheader'>Python Expertise</h3>", unsafe_allow_html=True)
            st.markdown("<p class='gradient-body'>Proficiency in core Python and scientific computing libraries.</p>", unsafe_allow_html=True)

        with col4:
            st.image("https://img.freepik.com/premium-photo/api-symbol-with-various-technology-icons-connected-by-neon-lines-dark-background-3d-rendering_670147-116377.jpg",width=100)
            st.markdown("<h3 class='gradient-subheader'>API Development</h3>", unsafe_allow_html=True)
            st.markdown("<p class='gradient-body'>Experience in creating and integrating APIs for data services.</p>", unsafe_allow_html=True)
        
        col5,col6=st.columns(2,gap="large")
        
        with col5:
            
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsNj_cw0oHhnQkgAk6Ppm8IhmOaWyhC_L-2Q&s",width=100)
            st.markdown("<h3 class='gradient-subheader'>Streamlit</h3>", unsafe_allow_html=True)
            st.markdown("<p class='gradient-body'>use Streamlit to build dynamic dashboards, AI demos, and data-driven portfolios.</p>", unsafe_allow_html=True)
        
        with col6:
            
            st.image("https://datascientest.com/en/files/2023/09/nlp.jpg",width=150)
            st.markdown("<h3 class='gradient-subheader'>NLP</h3>", unsafe_allow_html=True)
            st.markdown("<p class='gradient-body'>use NLP techniques for tasks like text classification, sentiment analysis, and chatbot development — teaching machines to process and respond to text intelligently.</p>", unsafe_allow_html=True)
            
        st.divider()
        st.markdown("<h1 class='gradient-title'>Education</h1>", unsafe_allow_html=True)
        
        col7,col8=st.columns([1,2],gap="large")
        
        with col7:
            st.markdown("<h3 class='gradient-subheader'>Uit University</h3>", unsafe_allow_html=True)
        
        with col8:
            
            st.markdown("<p2 class='gradient-body'>|****2023-2027****|</p2>", unsafe_allow_html=True)
            
        col9,col10=st.columns([1,2],gap="large")
        
        with col9:
            st.markdown("<h4 class='gradient-title'>Bachelors in Computer Science(BSCS)</h4>", unsafe_allow_html=True)
        
        with col10:
            
            st.markdown("<p2 class='gradient-body'>Khi,Pakistan</p2>", unsafe_allow_html=True)
        st.link_button("University Website","https://uitu.edu.pk/")
        st.divider()
        st.markdown("<h1 class='gradient-title'>Experience</h1>", unsafe_allow_html=True)
            
        col7,col8=st.columns([1,2],gap="large")
        
        with col7:
            st.markdown("<h3 class='gradient-subheader'>Developer Hub And Corporation</h3>", unsafe_allow_html=True)
        
        with col8:
            
            st.markdown("<p2 class='gradient-body'>june-july|****2025****|</p2>", unsafe_allow_html=True)
            
        col9,col10=st.columns([1,2],gap="large")
        
        with col9:
            st.markdown("<h4 class='gradient-title'>Data Science intern</h4>", unsafe_allow_html=True)
        
        with col10:
            
            st.markdown("<p2 class='gradient-body'>Khi,Pakistan</p2>", unsafe_allow_html=True)
        
        st.markdown("<p2 class='gradient-body'>➡ Completed a data science internship where I worked with real-world datasets tobuild several supervised and unsupervised machine learning projects. Developedinteractive dashboards using Streamlit and applied libraries like Pandas, NumPy,Scikit-learn, Seaborn, and Matplotlib to deliver end-to-end solutions.</p2>", unsafe_allow_html=True)
        
        st.link_button("Company LinkedIn","https://www.linkedin.com/company/developershub-corporation/posts/?feedView=all")  
        
        st.divider()
        
        st.markdown("<h1 class='gradient-title'>Certificate</h1>", unsafe_allow_html=True)
        
        col11,col12=st.columns([1,2],gap="large")
        
        with col11:
            st.markdown("<p2 class='gradient-subheader'>Python BootCamp</p2>", unsafe_allow_html=True)
            
        with col12:
            st.markdown("<p2 class='gradient-body'>Udemy| **july10, 2024** |</p2>", unsafe_allow_html=True)
        
        st.link_button("Certificate Link","https://udemy-certificate.s3.amazonaws.com/image/UC-173b6a3a-bc4e-4206-8cd5-b15d3498beaa.jpg?v=1720624599000")
            
    def projects(self):

        st.set_page_config(layout="wide")
        # Add custom CSS
        st.markdown("""
        <style>
            .project-section {
                text-align: center;
                color: #a78bfa;
                font-size: 3rem;
                font-weight: bold;
                margin-bottom: 50px;
            }

            .project-card {
                background: #2b004f;
                border-radius: 15px;
                padding: 25px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
                color: white;
                transition: all 0.2s ease;
            }

            .project-card:hover {
                transform: translateY(-20px);
                box-shadow: 0px 8px 20px rgba(0,50,0,0.5);
            }

            .project-image {
                width: 100%;
                border-radius: 50px;
                margin-bottom: 15px;
            }

            .tag {
                display: inline-block;
                background-color: #5b21b6;
                padding: 5px 10px;
                border-radius: 10px;
                font-size: 0.8rem;
                margin: 2px 3px;
            }

            .github-btn {
                display: inline-block;
                background: linear-gradient(90deg, #6a11cb, #2575fc);
                padding: 10px 25px;
                border-radius: 10px;
                color: white;
                font-weight: bold;
                text-decoration: none;
                margin-top: 10px;
            }

            .github-btn:hover {
                background: linear-gradient(90deg, #2575fc, #6a11cb);
               
            }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("""
                <style>
                .center-container {
                    display: flex;
                    justify-content: center;  /* horizontal center */
                    align-items: center;      /* vertical center */
                    height: 5vh;             /* adjust for how centered you want it */
                    text-align: center;
                }

                .animated-text {
                    font-size: 50px;
                    font-weight: 500;
                    margin-bottom: 60px; 
                    background: linear-gradient(270deg, #ff6ec4, yellow, #4ADEDE, #ff6ec4);
                    background-size: 800% 800%;
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    animation: gradientMove 5s ease infinite;
                }

                @keyframes gradientMove {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }
                </style>

                <div class="center-container">
                    <div class="animated-text">Featured Projects</div>
                </div>
            """, unsafe_allow_html=True)

        # Columns for 3 projects
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("""
            <div class='project-card'>
                <img src='https://www.advanced-television.com/wp-content/uploads/2023/01/IMDB-big.jpg' class='project-image'>
                <h3>IMDb Movie Recommendation Dashboard</h3>
                <p>An interactive Movie Recommendation System + EDA Tool built with Python, Streamlit, and Machine Learning.Upload your movie dataset, explore data insights, and get AI-driven movie recommendations</p>
                <div>
                    <span class='tag'>Machine Learning</span><span class='tag'>Python</span><span class='tag'>Streamlit</span><span class='tag'>EDA</span><span class='tag'>HTML</span><span class='tag'>CSS</span>
                </div>
                <a href='https://github.com/Bilall2003/-IMDb-Movie-Recommendation-Dashboard-.git' class='github-btn'>GitHub</a>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class='project-card'>
                <img src='https://storage.googleapis.com/kaggle-datasets-images/5402820/8973821/04b597ad019ff012e631cca9975bf620/dataset-cover.jpg?t=2024-07-17-08-16-49' class='project-image'>
                <h3>Term-Deposit-Subscription-Prediction-Bank-Marketing-using-Streamlit-Beta</h3>
                <p>An interactive Streamlit application for data analysis, machine learning, and deployment built using the Bank Marketing Dataset . This project automates the end-to-end data science workflow — from data cleaning, exploratory analysis, feature engineering, model training, evaluation, deployment, and user feedback..</p>
                <div>
                    <span class='tag'>Python</span><span class='tag'>AI</span><span class='tag'>Data Analysis</span><span class='tag'>Machine Learning</span>
                </div>
                <a href='https://github.com/Bilall2003/Term-Deposit-Subscription-Prediction-Bank-Marketing-using-Streamlit-Beta-.git' class='github-btn'>GitHub</a>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown("""
            <div class='project-card'>
                <img src='https://images.unsplash.com/photo-1600585154340-be6161a56a0c' class='project-image'>
                <h3>Predicting-Sale-Price-of-Houses</h3>
                <p>This Streamlit application predicts house sale prices using the Ames Housing Dataset.It integrates Exploratory Data Analysis (EDA), preprocessing, insights visualization, model training, evaluation, and deployment of ML models.</p>
                <div>
                    <span class='tag'>Python</span><span class='tag'>Streamlit</span><span class='tag'>Machine Learning</span>
                </div>
                <a href='https://github.com/Bilall2003/Predicting-Sale-Price-of-Houses.git' class='github-btn'>GitHub</a>
            </div>
            """, unsafe_allow_html=True)

        # Button under projects
        st.markdown("""
        <div style='text-align:center; margin-top:40px;'>
            <a href='https://github.com/Bilall2003?tab=repositories' class='github-btn'>More Projects</a>
        </div>
        """, unsafe_allow_html=True)

    
    def contacts(self):
             
        st.set_page_config(layout="centered")
        st.markdown("<h2 class='gradient-title'>Get In Touch</h2>", unsafe_allow_html=True)
        st.markdown("<p1 class='gradient-body'>Have a project in mind or want to collaborate? Feel free to reach out.</p1>", unsafe_allow_html=True)
        st.divider()
        col1, col2 = st.columns([0.2, 3.6]) 
        
        with col1:
            st.image("https://png.pngtree.com/png-vector/20201028/ourmid/pngtree-phone-icon-in-solid-circle-png-image_2380227.jpg",width=30)
            st.image("https://www.vhv.rs/dpng/d/4-42555_transparent-background-white-email-icon-png-png-download.png",width=30)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/960px-LinkedIn_logo_initials.png",width=40)
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnywOeoDKex4ARhs6VszmY1tLzV-PnY5CJ7Q&s",width=70)
        
        with col2:
            
            st.markdown("+923340745241")
            st.markdown("ahmedbilal988766@gmail.com")
            st.page_link("https://www.linkedin.com/in/bilal-ahmed-56b105248/", label="https://www.linkedin.com/in/bilal-ahmed-56b105248/")
            st.page_link("https://github.com/Bilall2003", label="https://github.com/Bilall2003")
      
        st.divider()
        
        st.markdown("<h2 class='gradient-title'>Send a Message</h2>", unsafe_allow_html=True)
        
        name = st.text_area(
        label="Your Name",
        placeholder="Write your name here...",
        height=30,
        label_visibility="collapsed"
    )

        email = st.text_area(
        label="Your Email",
        placeholder="Write your correct email here...",
        height=30,
        label_visibility="collapsed"
    )

        message = st.text_area(
        label="Your Message",
        placeholder="Write your message here...",
        height=200,
        label_visibility="collapsed"
    )

    # --- Formspree endpoint (replace this) ---
        formspree_url = "https://formspree.io/f/mqaynzqv"  # ⬅️ your endpoint here

    # --- Button logic ---
        if st.button("Send Message"):
        # Validation
            if len(name.strip()) == 0 or len(email.strip()) == 0 or len(message.strip()) == 0:
                 st.warning("⚠️ Please fill out all fields before sending.")
            else:
            # Define payload *inside* the else block
                data = {
                    "name": name,
                    "email": email,
                    "message": message,
                }

            try:
                with st.spinner("⏳ Sending your message..."):
                    response = requests.post(formspree_url, data=data)

                if response.status_code == 200:
                    st.success("✅ Your message has been sent successfully! Thank you.")
                else:
                    st.error(f"❌ Something went wrong (Error {response.status_code}). Please try again later.")

            except Exception as e:
                st.error(f"⚠️ Failed to send message")
                    

class stream(_portfolio):
    
    def run_info(self):
        
        self.font()
        self._portfolio__info()
    
    def run_projects(self):
        
        self.font()
        self.projects()
    
    def run_contacts(self):
        
        self.font()
        self.contacts()
        
    def app(self):
        
 
        if "text" not in st.session_state:
            st.session_state["text"] = "Welcome To My Portfolio"

        st.markdown("""
        <style>
        /* This targets the sidebar container */
        [data-testid="stSidebar"] .animated-text {
            font-size: 26px;
            font-weight: 800;
            background: linear-gradient(270deg, #ff6ec4, #7873f5, #4ADEDE);
            background-size: 600% 600%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientMove 3s ease infinite;
            text-align: center;
            margin-bottom: 20px;
            padding-top: 10px;
        }

        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        </style>
    """, unsafe_allow_html=True)
     
        
        st.sidebar.markdown(
            f"<h1 class='animated-text'>{st.session_state['text']}</h1>",
            unsafe_allow_html=True
        )
        
        option={
            "👋 About me":self.run_info,
            "📚 My Projects":self.run_projects,
            "🌐 Connect with me":self.run_contacts
        }
        key_sel=st.sidebar.selectbox("Select",list(option.keys()))
        value_sel=option[key_sel]
        value_sel()
        
obj=stream()
obj.app()