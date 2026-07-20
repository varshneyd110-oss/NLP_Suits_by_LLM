import streamlit as st
from news_classification import news_classification,create_news_table_to_db
from food_sentiment import food_sentiment,create_database,create_food_table_to_db
from language_detection import language_detection,create_detect_table_to_db
from spam_classifier import spam_classifier,create_spam_table_to_db
from machine_translation import machine_translation,create_translate_table_to_db
import pandas as pd
import json
from datetime import datetime
import sqlite3
import base64


create_food_table_to_db()
create_database()
create_spam_table_to_db()
create_detect_table_to_db()
create_translate_table_to_db()
create_news_table_to_db()



st.set_page_config(layout="wide")

def load_file(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):
        return pd.read_excel(uploaded_file)

    elif file_name.endswith(".xls"):
        return pd.read_excel(uploaded_file)

    elif file_name.endswith(".txt"):

        lines = uploaded_file.read().decode("utf-8").splitlines()

        return pd.DataFrame({"Text": lines})

    elif file_name.endswith(".json"):

        data = json.load(uploaded_file)

        return pd.DataFrame(data)

    return None


st.markdown("""
<style>

/* Download Report Button */
div.stDownloadButton > button {

    width: 100%;
    min-height: 62px;

    background: linear-gradient(135deg,#11998e,#38ef7d);

    color: white;
    border: none;
    border-radius: 15px;

    padding: 18px 25px;

    font-size: 20px;
    font-weight: 700;

    box-shadow: 0 6px 20px rgba(56,239,125,0.45);

    transition: all 0.3s ease;
}

/* Hover Effect */
div.stDownloadButton > button:hover {

    transform: translateY(-4px) scale(1.03);

    box-shadow: 0 10px 30px rgba(56,239,125,0.65);

    background: linear-gradient(135deg,#0f8f84,#32d96d);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>

    /* Text Area Styling */
    .stTextArea textarea {
        background: rgba(255,255,255,0.08);
        color: white;
        border: 2px solid #00c6ff;
        border-radius: 15px;
        padding: 15px;
        font-size: 16px;
        font-weight: 500;
    }

    .stTextArea textarea:focus {
        border: 2px solid #38ef7d;
        box-shadow: 0px 0px 15px rgba(56,239,125,0.5);
    }

    /* Text Input Styling */
    .stTextInput input {
        background: rgba(255,255,255,0.08);
        color: white;
        border: 2px solid #00c6ff;
        border-radius: 15px;
        padding: 15px;
        font-size: 16px;
        font-weight: 500;
    }

    .stTextInput input:focus {
        border: 2px solid #38ef7d;
        box-shadow: 0px 0px 15px rgba(56,239,125,0.5);
    }

    </style>
    """, unsafe_allow_html=True)

st.markdown(
        """
        <div style="
            background: linear-gradient(90deg, #ff6a00, #ee0979);
            padding:20px;
            border-radius:12px;
            text-align:center;
        ">
            <h1 style="color:white;">🚀 NLP Suit Using LLM</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

st.sidebar.markdown("""
        <style>
        .sidebar-banner {
            padding: 12px 15px;
            border-radius: 12px;
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            color: white;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            transition: all 0.4s ease;
            cursor: pointer;
            margin-bottom: 20px;
        }

        .sidebar-banner:hover {
            background: linear-gradient(135deg, #ff416c, #ff4b2b);
            color: black;
            transform: scale(1.05);
        }
        </style>

        <div class="sidebar-banner">
            🌿 Control Panel
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
            <style>

            /* File uploader container */
            .stFileUploader {
                border: 2px dashed #00c6ff;
                border-radius: 15px;
                padding: 20px;
                background: linear-gradient(135deg, #1f1f2e, #2c2c54);
                transition: all 0.4s ease;
            }

            /* Hover effect */
            .stFileUploader:hover {
                border: 2px solid #00f2fe;
                box-shadow: 0 0 15px #00c6ff;
            }

            /* Upload button */
            .stFileUploader button {
                background: linear-gradient(135deg, #00c6ff, #0072ff);
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 8px 15px;
                border: none;
                transition: all 0.3s ease;
            }

            /* Button hover */
            .stFileUploader button:hover {
                background: linear-gradient(135deg, #ff512f, #dd2476);
                color: black;
                transform: scale(1.05);
            }

            /* Uploaded file text */
            .stFileUploader div {
                color: #ffffff;
                font-size: 16px;
            }

            </style>
            """, unsafe_allow_html=True)

st.markdown("""
<style>

/* Tab Container */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    background-color: #1e1e2f;
    padding: 10px;
    border-radius: 15px;
}

/* Normal Tab */
.stTabs [data-baseweb="tab"] {
    height: 50px;
    background-color: #2c2c54;
    border-radius: 12px;
    color: white;
    font-weight: 600;
    border: 1px solid #40407a;
    padding: 0px 20px;
}

/* Hover */
.stTabs [data-baseweb="tab"]:hover {
    background-color: #40407a;
}

/* Active Tab */
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg,#ff6a00,#ee0979);
    color: white !important;
    border: none;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 15px;
    padding: 12px 28px;
    font-size: 18px;
    font-weight: 600;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.35);
}

div.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(102, 126, 234, 0.5);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Selected Value */
.stSelectbox div[data-baseweb="select"] span {
    font-size: 18px !important;
    font-weight: 600 !important;
    color: white !important;
}

/* Dropdown Options */
div[role="option"] {
    font-size: 18px !important;
    font-weight: 500 !important;
    padding: 12px 16px !important;
}

/* Dropdown Menu */
div[role="listbox"] {
    font-size: 18px !important;
}

/* Arrow */
.stSelectbox svg {
    width: 22px !important;
    height: 22px !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* Selectbox Main Box */
.stSelectbox div[data-baseweb="select"] > div{
    background: #3f4049 !important;
    border: 2px solid #00d4ff !important;
    border-radius: 15px !important;
    min-height: 45px !important;
    box-shadow: 0 0 12px rgba(0,212,255,0.20);
}

/* Selected Text */
.stSelectbox span{
    color:white !important;
    font-size:18px !important;
    font-weight:600 !important;
}

/* Hover */
.stSelectbox div[data-baseweb="select"] > div:hover{
    border-color:#00e5ff !important;
    box-shadow:0 0 18px rgba(0,212,255,0.35);
}

/* Dropdown List */
div[role="listbox"]{
    background:#2f3038 !important;
    border:2px solid #00d4ff !important;
    border-radius:15px !important;
}

/* Options */
div[role="option"]{
    color:white !important;
    font-size:16px !important;
    padding:12px !important;
}

/* Option Hover */
div[role="option"]:hover{
    background:rgba(0,212,255,0.15) !important;
}

</style>
""", unsafe_allow_html=True)    

tab1,tab2,tab3,tab4,tab5=st.tabs([
    "📩 Spam Classifier",
    "🌐 Language Detection",
    "😊 Food Sentiment",
    "🌍 Machine Translation",
    "📰 News Classification"
]

)

with tab1:

    def download_spam_csv():


        con = sqlite3.connect("multi_project.db")

        df = pd.read_sql_query(
            "SELECT * FROM Spam_Classifier",
            con
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.markdown(
            create_download_link(
                csv,
                "Spam_Classifier_report.csv",
                "📥 Download Spam Classifier Report",
                "report"
            ),
            unsafe_allow_html=True
        )

        con.close()

    st.write("### 📩 Spam Classification Analysis")

    # ==========================
    # Single Prediction
    # ==========================

    st.write("#### 🔍 Single Prediction")

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("#### 📝 Input Text")


    message = st.text_area("",placeholder="Type your message here...")

    if st.button("Predict Input Message"):

        Spam_classification, probability = spam_classifier(message)

        if Spam_classification.lower() == "spam":
            st.markdown("""
            <div style="
            background-color:#ff4b4b;
            color:white;
            padding:12px 18px;
            border-radius:12px;
            font-size:18px;
            font-weight:600;
            text-align:center;
            box-shadow:0px 4px 12px rgba(255,75,75,0.35);
            animation: blinker 1.2s linear infinite;
            ">
            🚨 SPAM DETECTED 🚨
            </div>

            <style>
            @keyframes blinker {
                50% { opacity: 0.7; }
            }
            </style>
            """, unsafe_allow_html=True)


            st.markdown("<br>", unsafe_allow_html=True)
            st.info(f"📊 Probability : {probability}")
            st.toast("🚨 Spam Detected!")

        else:
            st.markdown("""
            <div style="
            background-color:#28a745;
            color:white;
            padding:12px 18px;
            border-radius:12px;
            font-size:18px;
            font-weight:600;
            text-align:center;
            box-shadow:0px 4px 12px rgba(40,167,69,0.35);
            animation: blinker 1.2s linear infinite;
            ">
            🛡️ MESSAGE VERIFIED AS SAFE
            </div>

            <style>
            @keyframes blinker {
                50% { opacity: 0.7; }
            }
            </style>
            """, unsafe_allow_html=True)

            
            st.markdown("<br>", unsafe_allow_html=True)
            st.info(f"📊 Probability : {probability}")
            st.toast("✅ Safe Message")
            st.balloons()
            st.snow()

    st.divider()

    # ==========================
    # Bulk Prediction
    # ==========================

    st.write("#### 📂 Bulk Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV / Excel / TXT / JSON File",
        type=["csv","xlsx","xls","txt","json"],
        key="bulk_spam_file"
    )

    if uploaded_file:

        df = load_file(uploaded_file)

        st.dataframe(df.head())

        if st.button(
            "Run Bulk Prediction",
            key="bulk_spam_predict"
        ):

            results = []

            column_name = df.columns[0]

            for message in df[column_name]:

                Spam_classification, probability = spam_classifier(message)

                Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                results.append([
                    message,
                    Spam_classification,
                    round(probability, 2),
                    Date
                ])

            result_spam_df = pd.DataFrame(
                results,
                columns=[
                    "Message",
                    "Spam Classification",
                    "Probability",
                    "Date"
                ]
            )

            st.markdown("""
                <style>
                .custom-table th {
                    background-color: #ff4b4b;
                    color: white;
                    text-align: center;
                }
                </style>
                """, unsafe_allow_html=True)

            html_table = result_spam_df.to_html(classes="custom-table", index=False)

            st.markdown(html_table, unsafe_allow_html=True)

            csv = result_spam_df.to_csv(
                index=False
            )

            st.download_button(
                "⬇ Download Results",
                csv,
                "Spam_Classification_results.csv",
                "text/csv"
            )


    # ==========================
    # Sample Spam Dataset
    # ==========================

    sample_spam_data = pd.DataFrame({

        "message":[

        "Hey, are we still meeting at 6 PM today?",
        "Congratulations! You have won ₹25,000 cash reward. Claim now.",
        "Please send the presentation before lunch.",
        "URGENT: Your bank account will be blocked. Verify immediately.",
        "Happy Birthday! Wishing you lots of success.",
        "Exclusive offer! Get 90% discount on all products today.",
        "Can you share today's class notes?",
        "The project meeting has been moved to tomorrow.",
        "You have been selected for a free international vacation.",
        "Thank you for your payment. Transaction successful.",
        "Earn ₹50,000 per week working from home. Register now.",
        "Let's have lunch together tomorrow.",
        "Your mobile number won a lottery worth ₹5 lakh.",
        "Please review the attached document.",
        "Claim your free iPhone before the offer expires.",
        "See you at the office tomorrow morning.",
        "The train will arrive at platform 4 shortly.",
        "You are selected for a lucky draw. Click here.",
        "Can you call me once you reach home?",
        "Your KYC has expired. Update now to avoid suspension.",
        "Thanks for helping me with the assignment.",
        "FREE recharge worth ₹399 available today only.",
        "The interview is scheduled for Monday.",
        "Get rich quickly with this secret investment plan.",
        "Dinner is ready. Please come downstairs.",
        "Limited period offer! Buy 1 Get 3 Free.",
        "Please check your email and confirm.",
        "Meeting starts in 15 minutes.",
        "You won a brand-new Samsung smartphone.",
        "Hope you are feeling better today.",
        "Job offer! Earn ₹1 lakh monthly from home.",
        "Can you send me the project files?",
        "Final reminder: Claim your reward now.",
        "The workshop begins at 10 AM tomorrow.",
        "Special cashback waiting for you. Redeem instantly.",
        "Let's discuss the new feature tomorrow.",
        "Your loan has been approved without verification.",
        "The package has been delivered successfully.",
        "Congratulations! You are today's lucky winner.",
        "Please attend today's online session.",
        "Your ATM card has been suspended. Verify now."
        ]

    })

    # ==========================
    # CSV Convert
    # ==========================

    csv = sample_spam_data.to_csv(index=False).encode("utf-8")

    # ==========================
    # Banner
    # ==========================

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#1e3c72,#2a5298);
        padding:12px;
        border-radius:12px;
        text-align:center;
        margin:8px 0;
    ">

    <h3 style="
        color:white;
        margin:0;
    ">
    📥 Don't have a dataset?
    </h3>

    <p style="
        color:#dcdcdc;
        margin:4px 0 0 0;
        font-size:12px;
    ">
    Download sample spam dataset 🚀
    </p>

    </div>
    """, unsafe_allow_html=True)
    
    # ==========================
    # Download Button Function
    # ==========================

    def create_download_link(csv, filename, text, cls):
        b64 = base64.b64encode(csv).decode()

        return f"""
        <a class="custom-btn {cls}"
        href="data:file/csv;base64,{b64}"
        download="{filename}">
        {text}
        </a>
        """

    # ==========================
    # CSS
    # ==========================

    st.markdown("""
    <style>

    /* Button Base */

    .custom-btn{
        display:block;
        width:85%;
        margin:auto;
        padding:18px 0;
        border-radius:15px;
        font-weight:bold;
        font-size:18px;
        text-decoration:none;
        text-align:center;
        color:white;
        letter-spacing:0.5px;
        transition:all 0.3s ease;
        box-shadow:0 6px 20px rgba(0,0,0,0.3);
        backdrop-filter:blur(5px);
        animation:glow 2s infinite alternate;
    }

    @keyframes glow{
        from{
            box-shadow:0 0 10px rgba(255,255,255,0.2);
        }
        to{
            box-shadow:0 0 25px rgba(255,255,255,0.6);
        }
    }

    .custom-btn:hover{
        transform:translateY(-4px) scale(1.05);
    }

    /* Spam Dataset Button */

    .spam{
        background:rgba(220,38,38,0.25);
        border:1px solid rgba(220,38,38,0.45);
        box-shadow:0 6px 20px rgba(239,68,68,0.6);
    }

    .spam:hover{
        background:rgba(220,38,38,0.40);
        box-shadow:0 12px 40px rgba(239,68,68,0.7);
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # Layout
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        download_spam_csv()

    with col2:

        st.markdown(
            create_download_link(
                csv,
                "spam_dataset.csv",
                "⬇️ Download Sample Spam Dataset",
                "spam"
            ),
            unsafe_allow_html=True
        )

    
    

with tab2:

    def download_detect_csv():

        con = sqlite3.connect("multi_project.db")

        df = pd.read_sql_query(
            "SELECT * FROM Language_Detection",
            con
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.markdown(
            create_download_link(
                csv,
                "Language_Detection_report.csv",
                "📥 Download Language Detection Report",
                "report"
            ),
            unsafe_allow_html=True
        )

        con.close()

    st.write("### 🌐 Language Detection Analysis")

    # ==========================
    # Single Prediction
    # ==========================

    st.write("#### 🔍 Single Prediction")

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("#### 🔍 Language Detection")


    Sentence = st.text_area("",placeholder="Type text in any language...")

    if st.button("Predict Language Detection"):

        Language_Detect, probability = language_detection(Sentence)

        st.markdown(f"""
        <div style="
        background: linear-gradient(135deg,#1f4037,#99f2c8);
        padding:12px;
        border-radius:12px;
        text-align:center;
        color:white;
        box-shadow:0px 3px 10px rgba(0,0,0,0.2);
        ">
            <div style="font-size:18px;font-weight:600;">
                🌐 Detected Language
            </div>
            <div style="font-size:28px;font-weight:bold;margin-top:5px;">
                {Language_Detect}
            </div>
        </div>
        """, unsafe_allow_html=True)


        st.markdown("<br>", unsafe_allow_html=True)

        st.info(f"Probability : {probability}")
        st.balloons()
        st.snow()

    st.divider()

    # ==========================
    # Bulk Prediction
    # ==========================

    st.write("#### 📂 Bulk Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV / Excel / TXT / JSON File",
        type=["csv","xlsx","xls","txt","json"],
        key="bulk_detect_file"
    )

    if uploaded_file:

        df = load_file(uploaded_file)

        st.dataframe(df.head())

        if st.button(
            "Run Bulk Prediction",
            key="bulk_detect_predict"
        ):

            results = []

            column_name = df.columns[0]

            for Sentence in df[column_name]:

                Language_Detect, probability = language_detection(Sentence)

                Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                results.append([
                    Sentence,
                    Language_Detect,
                    round(probability, 2),
                    Date
                ])

            result_detect_df = pd.DataFrame(
                results,
                columns=[
                    "Input Text",
                    "Detected Language ",
                    "Probability",
                    "Date"
                ]
            )

            st.markdown("""
                <style>
                .custom-table th {
                    background-color: #ff4b4b;
                    color: white;
                    text-align: center;
                }
                </style>
                """, unsafe_allow_html=True)

            html_table = result_detect_df.to_html(classes="custom-table", index=False)

            st.markdown(html_table, unsafe_allow_html=True)

            csv = result_detect_df.to_csv(
                index=False
            )

            st.download_button(
                "⬇ Download Results",
                csv,
                "Language_Detection_results.csv",
                "text/csv"
            )

    # ==========================
    # Sample Spam Dataset
    # ==========================

    sample_spam_data = pd.DataFrame({

        "text":[

            "Hello, how are you today?",
            "नमस्ते, आप कैसे हैं?",
            "Bonjour, comment allez-vous ?",
            "Hola, ¿cómo estás?",
            "Hallo, wie geht es dir?",
            "Ciao, come stai?",
            "Olá, como você está?",
            "Привет, как дела?",
            "こんにちは、お元気ですか？",
            "你好，你今天怎么样？",

            "Machine learning is transforming the world.",
            "ਮੈਨੂੰ ਨਵੀਂ ਤਕਨਾਲੋਜੀ ਸਿੱਖਣਾ ਪਸੰਦ ਹੈ।",
            "La science des données est intéressante.",
            "مرحبا كيف حالك؟",
            "আজ मौसम बहुत अच्छा है।",
            "我喜欢学习新技术。",
            "Artificial Intelligence is changing industries.",
            "मैं डेटा साइंस सीख रहा हूँ।",
            "Künstliche Intelligenz verändert die Welt.",
            "Bienvenido a nuestra aplicación.",

            "Welcome to our language detection application.",
            "Je travaille sur un projet de données.",
            "Me encanta aprender nuevas tecnologías.",
            "私は新しい技術を学ぶのが好きです。",
            "Benvenuto nella nostra applicazione.",
            "Eu gosto de aprender novas tecnologias.",
            "Добро пожаловать в наше приложение.",
            "ਹੈਲੋ, ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?",
            "হ্যালো, আপনি কেমন আছেন?",
            "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?",

            "I love learning new technologies.",
            "मुझे नई तकनीक सीखना पसंद है।",
            "La inteligencia artificial está creciendo rápidamente.",
            "Ich lerne gerne neue Technologien.",
            "人工智能正在快速发展。",
            "أحب تعلم التقنيات الجديدة.",
            "ਕ੍ਰਿਤ੍ਰਿਮ ਬੁੱਧੀ ਤੇਜ਼ੀ ਨਾਲ ਵਿਕਸਿਤ ਹੋ ਰਹੀ ਹੈ।",
            "আমি নতুন প্রযুক্তি শিখতে পছন্দ করি।",
            "எனக்கு புதிய தொழில்நுட்பங்களை கற்றுக்கொள்ள பிடிக்கும்.",
            "నాకు కొత్త సాంకేతికతలను నేర్చుకోవడం ఇష్టం.",

            "The weather is beautiful today.",
            "आज मौसम बहुत अच्छा है।",
            "Willkommen in unserer Anwendung.",
            "L'intelligenza artificiale sta crescendo rapidamente.",
            "A inteligência artificial está evoluindo rapidamente.",
            "Искусственный интеллект развивается очень быстро.",
            "私たちのアプリへようこそ。",
            "欢迎使用我们的应用程序。",
            "الذكاء الاصطناعي يتطور بسرعة.",
            "కృత్రిమ మేధస్సు వేగంగా అభివృద్ధి చెందుతోంది."
        ]

    })

    # ==========================
    # CSV Convert
    # ==========================

    csv = sample_spam_data.to_csv(index=False).encode("utf-8")

    # ==========================
    # Banner
    # ==========================

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#1e3c72,#2a5298);
        padding:12px;
        border-radius:12px;
        text-align:center;
        margin:8px 0;
    ">

    <h3 style="
        color:white;
        margin:0;
    ">
    📥 Don't have a dataset?
    </h3>

    <p style="
        color:#dcdcdc;
        margin:4px 0 0 0;
        font-size:12px;
    ">
    Download sample language detection dataset 🚀
    </p>

    </div>
    """, unsafe_allow_html=True)
    
    # ==========================
    # Download Button Function
    # ==========================

    def create_download_link(csv, filename, text, cls):
        b64 = base64.b64encode(csv).decode()

        return f"""
        <a class="custom-btn {cls}"
        href="data:file/csv;base64,{b64}"
        download="{filename}">
        {text}
        </a>
        """

    # ==========================
    # CSS
    # ==========================

    st.markdown("""
    <style>

    /* Button Base */

    .custom-btn{
        display:block;
        width:85%;
        margin:auto;
        padding:18px 0;
        border-radius:15px;
        font-weight:bold;
        font-size:18px;
        text-decoration:none;
        text-align:center;
        color:white;
        letter-spacing:0.5px;
        transition:all 0.3s ease;
        box-shadow:0 6px 20px rgba(0,0,0,0.3);
        backdrop-filter:blur(5px);
        animation:glow 2s infinite alternate;
    }

    @keyframes glow{
        from{
            box-shadow:0 0 10px rgba(255,255,255,0.2);
        }
        to{
            box-shadow:0 0 25px rgba(255,255,255,0.6);
        }
    }

    .custom-btn:hover{
        transform:translateY(-4px) scale(1.05);
    }

    /* Language Detection Button */

    .detect{
        background:rgba(220,38,38,0.25);
        border:1px solid rgba(220,38,38,0.45);
        box-shadow:0 6px 20px rgba(239,68,68,0.6);
    }

    .detect:hover{
        background:rgba(220,38,38,0.40);
        box-shadow:0 12px 40px rgba(239,68,68,0.7);
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # Layout
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        download_detect_csv()

    with col2:

        st.markdown(
            create_download_link(
                csv,
                "language_detection.csv",
                "⬇️ Download Language Detection Dataset",
                "detect"
            ),
            unsafe_allow_html=True
        )

    

with tab3:

    def download_food_csv():

        con = sqlite3.connect("multi_project.db")

        df = pd.read_sql_query(
            "SELECT * FROM Food_review",
            con
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.markdown(
            create_download_link(
                csv,
                "Food_Sentiment_report.csv",
                "📥 Download Food Sentiment Report",
                "report"
            ),
            unsafe_allow_html=True
        )
        con.close()

    st.write("### 😊 Food Sentiment Analysis")

    # ==========================
    # Single Prediction
    # ==========================

    st.write("#### 🔍 Single Prediction")

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("#### 🍽️ Food Review")


    review = st.text_area("",placeholder="Share your food experience here...")

    if st.button("Predict Sentiment"):

        sentiment, probability = food_sentiment(review)

        if sentiment.lower()=="positive":
            st.markdown(f"""
            <div style="
            background: linear-gradient(135deg,#11998e,#38ef7d);
            color:white;
            padding:14px;
            border-radius:12px;
            text-align:center;
            box-shadow:0px 4px 12px rgba(56,239,125,0.35);
            font-size:20px;
            font-weight:bold;
            ">
            😊 POSITIVE SENTIMENT
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.info(f"Probability : {probability}")
            st.balloons()
            st.snow()

        elif sentiment.lower()=="negative":

            st.markdown("""
            <div style="
            background: linear-gradient(135deg,#ff416c,#ff4b2b);
            color:white;
            padding:14px;
            border-radius:12px;
            text-align:center;
            box-shadow:0px 4px 12px rgba(255,75,75,0.35);
            font-size:20px;
            font-weight:bold;
            animation: pulse 2s infinite;
            ">
            😠 NEGATIVE SENTIMENT
            </div>

            <style>
            @keyframes pulse {
                0% {
                    box-shadow: 0px 4px 12px rgba(255,75,75,0.25);
                }
                50% {
                    box-shadow: 0px 4px 18px rgba(255,75,75,0.45);
                }
                100% {
                    box-shadow: 0px 4px 12px rgba(255,75,75,0.25);
                }
            }
            </style>
                        
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.info(f"Probability : {probability}")

        elif sentiment.lower() == "neutral":

            st.markdown(f"""
            <div style="
            background: linear-gradient(135deg,#667eea,#764ba2);
            color:white;
            padding:14px;
            border-radius:12px;
            text-align:center;
            box-shadow:0px 4px 12px rgba(118,75,162,0.35);
            font-size:20px;
            font-weight:bold;
            ">
            😐 NEUTRAL SENTIMENT
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            st.info(f"Probability : {probability}")
                    

    st.divider()

    # ==========================
    # Bulk Prediction
    # ==========================

    st.write("#### 📂 Bulk Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV / Excel / TXT / JSON File",
        type=["csv","xlsx","xls","txt","json"],
        key="bulk_file"
    )

    if uploaded_file:

        df = load_file(uploaded_file)

        st.dataframe(df.head())

        if st.button(
            "Run Bulk Prediction",
            key="bulk_predict"
        ):

            results = []

            column_name = df.columns[0]

            for review in df[column_name]:

                sentiment, probability = food_sentiment(review)

                Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                results.append([
                    review,
                    sentiment,
                    round(probability, 2),
                    Date
                ])

            result_df = pd.DataFrame(
                results,
                columns=[
                    "Review",
                    "Sentiment",
                    "Probability",
                    "Date"
                ]
            )

            st.markdown("""
                <style>
                .custom-table th {
                    background-color: #ff4b4b;
                    color: white;
                    text-align: center;
                }
                </style>
                """, unsafe_allow_html=True)

            html_table = result_df.to_html(classes="custom-table", index=False)

            st.markdown(html_table, unsafe_allow_html=True)

            csv = result_df.to_csv(
                index=False
            )

            st.download_button(
                "⬇ Download Results",
                csv,
                "food_sentiment_results.csv",
                "text/csv"
            )

    # ==========================
    # Sample Spam Dataset
    # ==========================

    sample_spam_data = pd.DataFrame({

       "text":[

        "The pizza was amazing and full of flavor.",
        "The food was cold when it arrived.",
        "The meal was okay, nothing special.",

        "Absolutely loved the butter chicken.",
        "The burger tasted terrible and stale.",
        "Service was average and food was decent.",

        "One of the best restaurants I have visited.",
        "The pasta was overcooked and bland.",
        "The portion size was reasonable.",

        "The dessert was delicious and fresh.",
        "I am disappointed with the quality of food.",
        "The atmosphere was nice and relaxing.",

        "The biryani was outstanding and aromatic.",
        "The fries were soggy and oily.",
        "Food arrived on time and was warm.",

        "Excellent taste and great presentation.",
        "The soup was too salty for my liking.",
        "The meal was satisfactory overall.",

        "Fresh ingredients and authentic flavors.",
        "Worst dining experience ever.",
        "Nothing extraordinary, just average food.",

        "The chocolate cake was heavenly.",
        "The sandwich was dry and tasteless.",
        "The restaurant was clean and organized.",

        "Amazing food and friendly staff.",
        "The noodles lacked flavor.",
        "It was an acceptable dining experience.",

        "I would definitely order this again.",
        "The pizza crust was burnt.",
        "The food met my expectations.",

        "The seafood was fresh and delicious.",
        "The rice was undercooked.",
        "The delivery was neither fast nor slow.",

        "Perfect balance of spices and taste.",
        "The chicken was tough and chewy.",
        "The meal was fine for the price.",

        "Highly recommended for food lovers.",
        "I regret spending money on this meal.",
        "The food was average but edible.",

        "Everything tasted fantastic.",
        "The drink was watered down.",
        "The service was neither good nor bad.",

        "The restaurant exceeded my expectations.",
        "The food quality has dropped significantly.",
        "Overall, it was a normal experience.",

        "Best burger I have ever eaten.",
        "The curry was extremely spicy and unpleasant.",
        "The meal was served promptly."
    ]

    })

    # ==========================
    # CSV Convert
    # ==========================

    csv = sample_spam_data.to_csv(index=False).encode("utf-8")

    # ==========================
    # Banner
    # ==========================

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#1e3c72,#2a5298);
        padding:12px;
        border-radius:12px;
        text-align:center;
        margin:8px 0;
    ">

    <h3 style="
        color:white;
        margin:0;
    ">
    📥 Don't have a dataset?
    </h3>

    <p style="
        color:#dcdcdc;
        margin:4px 0 0 0;
        font-size:12px;
    ">
    Download sample Food Sentiment dataset 🚀
    </p>

    </div>
    """, unsafe_allow_html=True)
    
    # ==========================
    # Download Button Function
    # ==========================

    def create_download_link(csv, filename, text, cls):
        b64 = base64.b64encode(csv).decode()

        return f"""
        <a class="custom-btn {cls}"
        href="data:file/csv;base64,{b64}"
        download="{filename}">
        {text}
        </a>
        """

    # ==========================
    # CSS
    # ==========================

    st.markdown("""
    <style>

    /* Button Base */

    .custom-btn{
        display:block;
        width:85%;
        margin:auto;
        padding:18px 0;
        border-radius:15px;
        font-weight:bold;
        font-size:18px;
        text-decoration:none;
        text-align:center;
        color:white;
        letter-spacing:0.5px;
        transition:all 0.3s ease;
        box-shadow:0 6px 20px rgba(0,0,0,0.3);
        backdrop-filter:blur(5px);
        animation:glow 2s infinite alternate;
    }

    @keyframes glow{
        from{
            box-shadow:0 0 10px rgba(255,255,255,0.2);
        }
        to{
            box-shadow:0 0 25px rgba(255,255,255,0.6);
        }
    }

    .custom-btn:hover{
        transform:translateY(-4px) scale(1.05);
    }

    /* Food Sentiment Button */

    .food{
        background:rgba(220,38,38,0.25);
        border:1px solid rgba(220,38,38,0.45);
        box-shadow:0 6px 20px rgba(239,68,68,0.6);
    }

    .food:hover{
        background:rgba(220,38,38,0.40);
        box-shadow:0 12px 40px rgba(239,68,68,0.7);
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # Layout
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        download_food_csv()

    with col2:

        st.markdown(
            create_download_link(
                csv,
                "food_sentiment.csv",
                "⬇️ Download Food Sentiment Dataset",
                "food"
            ),
            unsafe_allow_html=True
        )

        

with tab4:

    def download_translate_csv():

        con=sqlite3.connect("multi_project.db")

        df=pd.read_sql_query(
            "SELECT * FROM Machine_Translation",
            con
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.markdown(
            create_download_link(
                csv,
                "Machine_Translation_report.csv",
                "📥 Download Machine Translation Report",
                "report"
            ),
            unsafe_allow_html=True
        )

        con.close()

    st.write("### 🌍 Machine Translation Analysis")

    # ==========================
    # Single Prediction
    # ==========================

    st.write("#### 🔍 Single Prediction")

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("#### 📝 Original Text")

    st.write()


    Input_Text = st.text_area("",placeholder="Enter text to translate...")

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("#### 🎯 Target Language")


    targeted_language = st.selectbox(
    "🌍 Select Target Language",
    [
        "Hindi",
        "English",
        "Urdu",
        "Punjabi",
        "Bengali",
        "Gujarati",
        "Marathi",
        "Tamil",
        "Telugu",
        "Kannada",
        "Malayalam",
        "Odia",
        "Assamese",
        "Konkani",
        "Kashmiri",
        "Sindhi",
        "Sanskrit",
        "Maithili",
        "Dogri",
        "Manipuri (Meitei)",
        "Bodo",
        "Santali",
        "Nepali",

        "Arabic",
        "Chinese (Simplified)",
        "Chinese (Traditional)",
        "Japanese",
        "Korean",
        "Thai",
        "Vietnamese",
        "Indonesian",
        "Malay",
        "Filipino (Tagalog)",

        "French",
        "German",
        "Spanish",
        "Portuguese",
        "Italian",
        "Dutch",
        "Russian",
        "Ukrainian",
        "Polish",
        "Turkish",
        "Greek",
        "Swedish",
        "Norwegian",
        "Danish",
        "Finnish",
        "Hungarian",
        "Czech",
        "Romanian",

        "Persian (Farsi)",
        "Hebrew",
        "Swahili",
        "Afrikaans",
        "Zulu",
        "Amharic"
    ]
)



    if st.button("Predict Machine Translation"):

        machine_tranlate, probability = machine_translation(Input_Text,targeted_language)

        st.markdown(f"""
        <div style="
        background: linear-gradient(135deg,#141e30,#243b55);
        padding:14px;
        border-radius:14px;
        text-align:center;
        color:white;
        border:1px solid rgba(255,255,255,0.15);
        box-shadow:0px 4px 15px rgba(0,198,255,0.25);
        ">
            <div style="font-size:18px;font-weight:600;">
                🌍 Translated Text
            </div>
            <div style="font-size:28px;font-weight:bold;margin-top:5px;">
                {machine_tranlate}
            </div>
        </div>
        """, unsafe_allow_html=True)
        

        st.markdown("<br>", unsafe_allow_html=True)

        st.success(f"Probability : {probability}")
        st.balloons()
        st.snow()

    st.divider()

    # ==========================
    # Bulk Prediction
    # ==========================

    st.write("#### 📂 Bulk Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV / Excel / TXT / JSON File",
        type=["csv","xlsx","xls","txt","json"],
        key="bulk_translate_file"
    )

    if uploaded_file:

        df = load_file(uploaded_file)

        st.dataframe(df.head())

        if st.button(
            "Run Bulk Prediction",
            key="bulk_translate_predict"
        ):

            results = []

            column_name_1 = df.columns[0]
            column_name_2 = df.columns[1]



            for Input_Text,targeted_language in zip(
                df[column_name_1],
                df[column_name_2]
            ):

                machine_translate, probability = machine_translation(Input_Text,targeted_language)

                Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                results.append([
                    Input_Text,
                    targeted_language,
                    machine_translate,
                    round(probability, 2),
                    Date
                ])

            result_translate_df = pd.DataFrame(
                results,
                columns=[
                    "Input Text",
                    "Targeted Language",
                    "Machine Translation ",
                    "Probability",
                    "Date"
                ]
            )

            st.markdown("""
                <style>
                .custom-table th {
                    background-color: #ff4b4b;
                    color: white;
                    text-align: center;
                }
                </style>
                """, unsafe_allow_html=True)

            html_table = result_translate_df.to_html(classes="custom-table", index=False)

            st.markdown(html_table, unsafe_allow_html=True)

            csv = result_translate_df.to_csv(
                index=False
            )

            st.download_button(
                "⬇ Download Results",
                csv,
                "Machine_Translation_results.csv",
                "text/csv"
            )

    # ==========================
    # Sample Spam Dataset
    # ==========================

    sample_spam_data = pd.DataFrame({

       "Input_Text":[

        "Hello, how are you today?",
        "Good morning everyone.",
        "I am learning Machine Learning.",
        "Artificial Intelligence is the future.",
        "Welcome to our application.",
        "Thank you for your support.",
        "Please send me the report.",
        "The weather is very pleasant today.",
        "I love learning new technologies.",
        "Can you help me with this task?",

        "My name is Dev.",
        "I live in Noida.",
        "The meeting starts at 10 AM.",
        "This project is very interesting.",
        "Data Science is a growing field.",
        "I enjoy reading books.",
        "Let's discuss the project tomorrow.",
        "Technology is changing the world.",
        "Have a wonderful day.",
        "The train arrived on time.",

        "नमस्ते, आप कैसे हैं?",
        "मेरा नाम देव है।",
        "मैं नोएडा में रहता हूँ।",
        "मुझे नई तकनीक सीखना पसंद है।",
        "आज मौसम बहुत अच्छा है।",
        "मैं डेटा साइंस सीख रहा हूँ।",
        "यह परियोजना बहुत रोचक है।",
        "कृपया मुझे रिपोर्ट भेजें।",
        "बैठक सुबह 10 बजे शुरू होगी।",
        "आपका दिन शुभ हो।",

        "Bonjour, comment allez-vous ?",
        "Je m'appelle Dev.",
        "Bienvenue dans notre application.",
        "La science des données est intéressante.",
        "J'aime apprendre de nouvelles technologies.",

        "Hola, ¿cómo estás?",
        "Me llamo Dev.",
        "Bienvenido a nuestra aplicación.",
        "La inteligencia artificial está creciendo rápidamente.",
        "Me gusta aprender nuevas tecnologías.",

        "Hallo, wie geht es dir?",
        "Ich heiße Dev.",
        "Willkommen in unserer Anwendung.",
        "Künstliche Intelligenz verändert die Welt.",
        "Ich lerne gerne neue Technologien.",

        "Ciao, come stai?",
        "Mi chiamo Dev.",
        "Benvenuto nella nostra applicazione.",
        "Mi piace imparare nuove tecnologie.",
        "L'intelligenza artificiale sta crescendo rapidamente.",

        "Olá, como você está?",
        "Eu gosto de aprender novas tecnologias.",
        "Bem-vindo ao nosso aplicativo.",
        "A inteligência artificial está evoluindo rapidamente.",
        "Obrigado pelo seu apoio.",

        "Привет, как дела?",
        "Меня зовут Дев.",
        "Добро пожаловать в наше приложение.",
        "Мне нравится изучать новые технологии.",
        "Искусственный интеллект развивается очень быстро."
    ],

    "Targeted_Language":[

        "Hindi","Hindi","Hindi","Hindi","Hindi",
        "Hindi","Hindi","Hindi","Hindi","Hindi",

        "French","French","French","French","French",
        "French","French","French","French","French",

        "English","English","English","English","English",
        "English","English","English","English","English",

        "English","English","English","English","English",

        "English","English","English","English","English",

        "English","English","English","English","English",

        "English","English","English","English","English",

        "English","English","English","English","English",

        "English","English","English","English","English"
    ]


    })

    # ==========================
    # CSV Convert
    # ==========================

    csv = sample_spam_data.to_csv(index=False).encode("utf-8")

    # ==========================
    # Banner
    # ==========================

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#1e3c72,#2a5298);
        padding:12px;
        border-radius:12px;
        text-align:center;
        margin:8px 0;
    ">

    <h3 style="
        color:white;
        margin:0;
    ">
    📥 Don't have a dataset?
    </h3>

    <p style="
        color:#dcdcdc;
        margin:4px 0 0 0;
        font-size:12px;
    ">
    Download sample Food Sentiment dataset 🚀
    </p>

    </div>
    """, unsafe_allow_html=True)
    
    # ==========================
    # Download Button Function
    # ==========================

    def create_download_link(csv, filename, text, cls):
        b64 = base64.b64encode(csv).decode()

        return f"""
        <a class="custom-btn {cls}"
        href="data:file/csv;base64,{b64}"
        download="{filename}">
        {text}
        </a>
        """

    # ==========================
    # CSS
    # ==========================

    st.markdown("""
    <style>

    /* Button Base */

    .custom-btn{
        display:block;
        width:85%;
        margin:auto;
        padding:18px 0;
        border-radius:15px;
        font-weight:bold;
        font-size:18px;
        text-decoration:none;
        text-align:center;
        color:white;
        letter-spacing:0.5px;
        transition:all 0.3s ease;
        box-shadow:0 6px 20px rgba(0,0,0,0.3);
        backdrop-filter:blur(5px);
        animation:glow 2s infinite alternate;
    }

    @keyframes glow{
        from{
            box-shadow:0 0 10px rgba(255,255,255,0.2);
        }
        to{
            box-shadow:0 0 25px rgba(255,255,255,0.6);
        }
    }

    .custom-btn:hover{
        transform:translateY(-4px) scale(1.05);
    }

    /* machine Tranlation Button */

    .translate{
        background:rgba(220,38,38,0.25);
        border:1px solid rgba(220,38,38,0.45);
        box-shadow:0 6px 20px rgba(239,68,68,0.6);
    }

    .translate:hover{
        background:rgba(220,38,38,0.40);
        box-shadow:0 12px 40px rgba(239,68,68,0.7);
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # Layout
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        download_translate_csv()

    with col2:

        st.markdown(
            create_download_link(
                csv,
                "Machine_translate.csv",
                "⬇️ Download Machine Translate Dataset",
                "translate"
            ),
            unsafe_allow_html=True
        )

    

with tab5:

    def download_News_csv():
        con=sqlite3.connect("multi_project.db")

        df=pd.read_sql_query(
            "SELECT * FROM News_classification;",
            con
        )

        csv = df.to_csv(index=False).encode("utf-8")

        st.markdown(
            create_download_link(
                csv,
                "News_Classification_report.csv",
                "📥 Download News Classification Report",
                "report"
            ),
            unsafe_allow_html=True
        )

        con.close()
        
    st.write("### 📰 News Classification Analysis")

    # ==========================
    # Single Prediction
    # ==========================

    st.write("#### 🔍 Single Prediction")

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("### 📄 News Content")


    headline = st.text_area("",placeholder="Type a news headline here...")

    if st.button("Predict Headline"):

        news_category, probability = news_classification(headline)

        if news_category.upper() == "SPORTS":
            st.success(f"🏏 Category : {news_category}")
            st.info(f"📊 Probability : {probability}")
            st.balloons()
            st.snow()

        elif news_category.upper() == "POLITICS":
            st.error(f"🏛️ Category : {news_category}")
            st.info(f"📊 Probability : {probability}")
            st.balloons()
            st.snow()

        elif news_category.upper() == "ENTERTAINMENT":
            st.warning(f"🎬 Category : {news_category}")
            st.info(f"📊 Probability : {probability}")
            st.balloons()
            st.snow()

        elif news_category.upper() == "BUSINESS":
            st.info(f"💼 Category : {news_category}")
            st.info(f"📊 Probability : {probability}")
            st.balloons()
            st.snow()


        elif news_category.upper() == "TECHNOLOGY":
            st.markdown(
                f"""
                <div style="
                    background-color:#00BCD4;
                    padding:15px;
                    border-radius:10px;
                    color:white;
                    font-weight:bold;
                    font-size:18px;">
                    💻 Category : {news_category}
                </div>
                """,
                unsafe_allow_html=True
            )
            st.info(f"📊 Probability : {probability}")
            st.balloons()
            st.snow()

        elif news_category.upper() == "RELIGIOUS":
            st.markdown(
                f"""
                <div style="
                    background-color:#FF9800;
                    padding:15px;
                    border-radius:10px;
                    color:white;
                    font-weight:bold;
                    font-size:18px;">
                    🕉️ Category : {news_category}
                </div>
                """,
                unsafe_allow_html=True
            )
            st.info(f"📊 Probability : {probability}")
            st.balloons()
            st.snow()

        else:
            st.warning(f"Category : {news_category}")
            st.info(f"📊 Probability : {probability}")

    st.divider()

    # ==========================
    # Bulk Prediction
    # ==========================

    st.write("#### 📂 Bulk Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV / Excel / TXT / JSON File",
        type=["csv","xlsx","xls","txt","json"],
        key="bulk_news_file"
    )

    if uploaded_file:

        df = load_file(uploaded_file)

        st.dataframe(df.head())

        if st.button(
            "Run Bulk Prediction",
            key="bulk_news_predict"
        ):

            results = []

            column_name = df.columns[0]

            for headline in df[column_name]:

                news_classifier, probability = news_classification(headline)

                Date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


                results.append([
                    headline,
                    news_classifier,
                    round(probability, 2),
                    Date
                ])

            result_news_df = pd.DataFrame(
                results,
                columns=[
                    "Headline",
                    "News Classification",
                    "Probability",
                    "Date"
                ]
            )

            st.markdown("""
                <style>
                .custom-table th {
                    background-color: #ff4b4b;
                    color: white;
                    text-align: center;
                }
                </style>
                """, unsafe_allow_html=True)

            html_table = result_news_df.to_html(classes="custom-table", index=False)

            st.markdown(html_table, unsafe_allow_html=True)

            csv = result_news_df.to_csv(
                index=False
            )

            st.download_button(
                "⬇ Download Results",
                csv,
                "news_Classification_results.csv",
                "text/csv"
            )

    # ==========================
    # Sample Spam Dataset
    # ==========================

    sample_spam_data = pd.DataFrame({

       "news":[

        "India wins thrilling cricket match against Australia",
        "Government passes new education reform bill",
        "New Bollywood movie breaks box office records",
        "Stock market reaches all-time high this week",
        "Artificial intelligence transforms healthcare industry",
        "Thousands gather for annual religious festival",

        "Football team secures victory in final minutes",
        "Prime Minister addresses nation on economic growth",
        "Famous actor announces upcoming film project",
        "Central bank increases interest rates",
        "Tech company launches next generation smartphone",
        "Temple inauguration ceremony attracts devotees",

        "Olympic athletes begin intensive training camp",
        "Election results spark debate across the country",
        "Music album tops global charts in first week",
        "Inflation rate shows slight decline this month",
        "Cybersecurity experts warn of new online threats",
        "Pilgrimage season begins with large crowds",

        "Star player scores hat-trick in championship game",
        "Opposition criticizes newly proposed tax policy",
        "Celebrity wedding trends across social media",
        "Global economy expected to grow steadily",
        "Researchers develop advanced machine learning model",
        "Religious leaders promote peace and unity",

        "Tennis champion wins grand slam title",
        "Parliament session adjourned after heated arguments",
        "Streaming platform releases anticipated series",
        "Startup raises millions in funding round",
        "Cloud computing adoption continues to grow rapidly",
        "Festival celebrations bring communities together",

        "Team qualifies for world cup after intense match",
        "Foreign policy strategy announced by government",
        "Director reveals teaser of upcoming blockbuster",
        "Oil prices rise due to increased demand",
        "New software update improves system performance",
        "Spiritual event held with traditional rituals",

        "Coach announces squad for upcoming tournament",
        "State elections see record voter turnout",
        "Award show celebrates best performances of the year",
        "Government announces economic stimulus package",
        "Scientists achieve breakthrough in robotics research",
        "Devotees visit shrine during holy occasion",

        "Basketball league finals attract huge audience",
        "Government launches welfare scheme for citizens",
        "Actor signs multi-million dollar movie deal",
        "Cryptocurrency market experiences fluctuations",
        "Electric vehicle technology advances significantly",
        "Religious ceremony conducted with enthusiasm",

        "Athlete breaks national record in sprint event",
        "Political leaders discuss national security issues",
        "New web series gains massive popularity online",
        "Unemployment rate drops significantly",
        "Data scientists create innovative AI solution",
        "Charity event organized by religious organization",

        "Cricket series postponed due to weather conditions",
        "New law proposed to regulate digital media",
        "Film festival showcases international cinema",
        "Tech firms report strong quarterly earnings",
        "Quantum computing project receives major funding",
        "Prayer meetings held across the city",

        "India defeats England in a nail-biting match",
        "Cabinet approves major infrastructure project",
        "Singer launches new album for fans worldwide",
        "Retail sales increase during festive season",
        "Technology conference showcases latest innovations",
        "People participate in sacred pilgrimage journey",

        "Football club wins league title after comeback",
        "Election campaign intensifies ahead of voting",
        "Reality show finale attracts millions of viewers",
        "Investors show confidence in emerging markets",
        "Startup develops smart home automation platform",
        "Monks conduct special meditation session",

        "Fans celebrate historic victory in stadium",
        "Ministers hold meeting on policy reforms",
        "Documentary receives critical acclaim from audience",
        "Company expands operations into international markets",
        "Researchers unveil powerful language model",
        "Community celebrates important religious holiday"
    ]

    })

    # ==========================
    # CSV Convert
    # ==========================

    csv = sample_spam_data.to_csv(index=False).encode("utf-8")

    # ==========================
    # Banner
    # ==========================

    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#1e3c72,#2a5298);
        padding:12px;
        border-radius:12px;
        text-align:center;
        margin:8px 0;
    ">

    <h3 style="
        color:white;
        margin:0;
    ">
    📥 Don't have a dataset?
    </h3>

    <p style="
        color:#dcdcdc;
        margin:4px 0 0 0;
        font-size:12px;
    ">
    Download sample Food Sentiment dataset 🚀
    </p>

    </div>
    """, unsafe_allow_html=True)
    
    # ==========================
    # Download Button Function
    # ==========================

    def create_download_link(csv, filename, text, cls):
        b64 = base64.b64encode(csv).decode()

        return f"""
        <a class="custom-btn {cls}"
        href="data:file/csv;base64,{b64}"
        download="{filename}">
        {text}
        </a>
        """

    # ==========================
    # CSS
    # ==========================

    st.markdown("""
    <style>

    /* Button Base */

    .custom-btn{
        display:block;
        width:85%;
        margin:auto;
        padding:18px 0;
        border-radius:15px;
        font-weight:bold;
        font-size:18px;
        text-decoration:none;
        text-align:center;
        color:white;
        letter-spacing:0.5px;
        transition:all 0.3s ease;
        box-shadow:0 6px 20px rgba(0,0,0,0.3);
        backdrop-filter:blur(5px);
        animation:glow 2s infinite alternate;
    }

    @keyframes glow{
        from{
            box-shadow:0 0 10px rgba(255,255,255,0.2);
        }
        to{
            box-shadow:0 0 25px rgba(255,255,255,0.6);
        }
    }

    .custom-btn:hover{
        transform:translateY(-4px) scale(1.05);
    }

    /* News Classification Button */

    .news{
        background:rgba(220,38,38,0.25);
        border:1px solid rgba(220,38,38,0.45);
        box-shadow:0 6px 20px rgba(239,68,68,0.6);
    }

    .news:hover{
        background:rgba(220,38,38,0.40);
        box-shadow:0 12px 40px rgba(239,68,68,0.7);
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # Layout
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        download_News_csv()

    with col2:

        st.markdown(
            create_download_link(
                csv,
                "News_Classification.csv",
                "⬇️ Download News Classification Dataset",
                "news"
            ),
            unsafe_allow_html=True
        )

    
st.sidebar.image("multi_project.png")


st.sidebar.markdown("## 👋 Welcome")
st.sidebar.write("Explore the NLP Suite powered by LLM.")
st.sidebar.write("====================================")

st.sidebar.markdown("## 🚀 NLP Suite Using LLM")
st.sidebar.write("Perform multiple NLP tasks with AI-powered intelligence.")
st.sidebar.write("====================================")

st.sidebar.markdown("## 🤖 Available Applications")

st.sidebar.write("🌐 Machine Translation")
st.sidebar.write("Translate text into your target language.")

st.sidebar.write("😊 Food Sentiment Analysis")
st.sidebar.write("Analyze food & restaurant reviews.")

st.sidebar.write("📩 Spam Classifier")
st.sidebar.write("Detect Spam or Ham messages.")

st.sidebar.write("📰 News Classification")
st.sidebar.write("Classify news into predefined categories.")

st.sidebar.write("🌍 Language Detection")
st.sidebar.write("Identify the language of any text.")

st.sidebar.write("====================================")

st.sidebar.markdown("## ✨ Features")
st.sidebar.write("✔ AI-Powered Predictions")
st.sidebar.write("✔ Structured LLM Outputs")
st.sidebar.write("✔ Fast & Accurate Results")
st.sidebar.write("✔ Multiple NLP Tasks")
st.sidebar.write("✔ Easy-to-Use Interface")
st.sidebar.write("====================================")

st.sidebar.markdown("## 📌 Supported Tasks")
st.sidebar.write("• Machine Translation")
st.sidebar.write("• Sentiment Analysis")
st.sidebar.write("• Spam Detection")
st.sidebar.write("• News Categorization")
st.sidebar.write("• Language Identification")
st.sidebar.write("====================================")

st.sidebar.markdown("## 📖 How to Use?")
st.sidebar.write("1. Select a task from the dashboard")
st.sidebar.write("2. Enter your text input")
st.sidebar.write("3. Click Predict / Analyze")
st.sidebar.write("4. View AI-generated results")
st.sidebar.write("====================================")

st.sidebar.markdown("## 🎯 Why Choose This NLP Suite?")
st.sidebar.write("• Powered by GPT-4o-mini")
st.sidebar.write("• High Accuracy Predictions")
st.sidebar.write("• Confidence Score Support")
st.sidebar.write("• SQLite Database Integration")
st.sidebar.write("• Modern User Interface")
st.sidebar.write("====================================")

st.sidebar.markdown("## 🧑‍💻 Developer")
st.sidebar.write("Dev Varshney")
st.sidebar.write("AI / ML Engineer 🚀")
st.sidebar.write("====================================")

st.sidebar.markdown("## 📞 Contact")
st.sidebar.write("📱 9058068999")
st.sidebar.write("📧 varshneyd110@gmail.com")
st.sidebar.write("====================================")

st.markdown("""
        <style>
        @keyframes fadeText {
            0% {opacity: 0;}
            5% {opacity: 1;}
            12% {opacity: 1;}
            17% {opacity: 0;}
            100% {opacity: 0;}
        }

        .text-container {
            position: relative;
            height: 40px;
            text-align: left;
            color: #00c6ff;
            font-size: 22px;
            font-weight: bold;
            margin-top: 40px;
            overflow: hidden; /* 🔥 important */
        }

        .text-container span {
            position: absolute;
            width: 100%;
            opacity: 0;
            animation: fadeText 16s linear infinite; /* 🔥 total = 8 × 2s */
        }

        /* Proper spacing */
        .text-container span:nth-child(1) { animation-delay: 0s; }
        .text-container span:nth-child(2) { animation-delay: 2s; }
        .text-container span:nth-child(3) { animation-delay: 4s; }
        .text-container span:nth-child(4) { animation-delay: 6s; }
        .text-container span:nth-child(5) { animation-delay: 8s; }
        .text-container span:nth-child(6) { animation-delay: 10s; }
        .text-container span:nth-child(7) { animation-delay: 12s; }
        .text-container span:nth-child(8) { animation-delay: 14s; }
        </style>

        <div class="text-container">
            <span>🚀 All-in-One NLP Suite Using LLM</span>
            <span>🌐 Translate Text Across Multiple Languages</span>
            <span>😊 Analyze Food & Restaurant Reviews</span>
            <span>📩 Detect Spam and Ham Messages</span>
            <span>📰 Classify News into Smart Categories</span>
            <span>🌍 Detect Languages Instantly</span>
            <span>🤖 Powered by GPT-4o-mini & LangChain</span>
            <span>=⚡ Fast, Accurate & Intelligent Predictions</span>
        </div>
        """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #1f4037, #99f2c8);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-top: 40px;
    ">
        <h4>🤖 NLP Applications</h4>
        <h2>5 Modules</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #141e30, #243b55);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-top: 40px;
    ">
        <h4>🎯 LLM Accuracy</h4>
        <h2>98%+</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #42275a, #734b6d);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-top: 40px;
    ">
        <h4>⚡ AI Powered Tasks</h4>
        <h2>24/7</h2>
    </div>
    """, unsafe_allow_html=True)
