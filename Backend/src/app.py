import streamlit as st
from evaluateYolo import prevehicle
from evaluateCNN import predict
from evaluateLSTM import evaluate
from evaluateRAG import extract_pdf,search,rag_system,retrieve_system,prerag,data_chunk
import requests

st.markdown("""
<style>

/* MAIN BACKGROUND (NEW MODERN GRADIENT) */
.main {
    background: linear-gradient(135deg, #0f172a, #1e1b4b, #0b1220);
    color: white;
}

/* Optional animated feel */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b, #0b1220);
    background-size: 300% 300%;
    animation: gradientMove 12s ease infinite;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Cards effect */
.block-container {
    padding: 2rem 3rem;
}

/* Glass effect for widgets */
.stTextInput > div > div > input,
.stFileUploader,
.stTabs {
    background: rgba(255, 255, 255, 0.06) !important;
    border-radius: 12px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: white;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #8b5cf6, #06b6d4);
    color: white;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #06b6d4, #8b5cf6);
    transform: scale(1.05);
}

/* Headings */
h1 {
    text-align: center;
    color: #a78bfa;
    font-size: 38px;
}

h3 {
    color: #22d3ee;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Smart Employee Assistance System",
    page_icon="🏢",
    layout="wide"
)

# Session State
if "vehicle_verified" not in st.session_state:
    st.session_state.vehicle_verified = False

if "mask_verified" not in st.session_state:
    st.session_state.mask_verified = False

if "chatbot_completed" not in st.session_state:
    st.session_state.chatbot_completed = False

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# Header
st.title("🏢 Smart Employee Assistance & Security System")

st.markdown("---")

# STEP 1
st.subheader("🚗Vehicle Verification")

if not st.session_state.vehicle_verified:

    vehicle_image = st.file_uploader(
        "Upload Vehicle Image",
        type=["jpg", "jpeg", "png"],
        key="vehicle"
    )

    if vehicle_image:

        st.image(vehicle_image, width=500)
        if st.button("Detect Vehicle"):
            result, confidences, texts = prevehicle(vehicle_image)
            st.success("Detection Completed ✅")
            st.write("📌 Detected Plates:")
            st.write(texts)
            st.write("📊 Confidence:")
            st.write(confidences)
            st.session_state.vehicle_verified = True
            
else:
    st.success("Vehicle Verification Completed ✅")


st.markdown("---")

# STEP 2
if st.session_state.vehicle_verified:
    st.subheader(" Face Mask Detection")
    if not st.session_state.mask_verified:
        face_image = st.file_uploader(
            "Upload Face Image",
            type=["jpg", "jpeg", "png"],
            key="face"
        )
        if face_image:
            st.image(face_image, width=400)
            if st.button("Check Mask"):
                confidence, img = predict(face_image)
                st.success("Prediction Done ✅")
                st.write(f"Confidence: {confidence:.2f}")
                if confidence >= 80:
                    st.error("❌ No Mask Detected")
                elif confidence <= 20:
                    st.success("✅ Mask Detected")
                    st.session_state.mask_verified = True
                else:
                    st.warning("⚠ Please Upload Clear Image")
    else:
        st.success("Mask Verification Completed ✅")

st.markdown("---")

# STEP 3
if st.session_state.mask_verified:

    st.subheader("🤖 Navigation Assistant")

    st.write(
        "Ask where you want to go inside the organization."
    )

    query = st.text_input(
        "Destination Query",
        placeholder="I want to go to HR Department"
    )

    if st.button("Get Directions"):
        answer=evaluate(query)
        st.write(answer)
        st.session_state.chatbot_completed = True
        
st.markdown("---")

API_URL = "http://127.0.0.1:8000"

if st.session_state.chatbot_completed:
    st.subheader(" Employee Authentication")
    auth_tab1, auth_tab2 = st.tabs(
        ["Login", "Sign Up"]
    )

    # ---------------- LOGIN ----------------
    with auth_tab1:

        email = st.text_input(
            "Email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_pass"
        )

        if st.button("Login"):

            payload = {
                "email": email,
                "password": password
            }

            response = requests.post(
                f"{API_URL}/login",
                json=payload
            )

            data = response.json()

            if data.get("message") == "Login success":

                st.success("Login Successful ✅")

                st.session_state.authenticated = True
                st.session_state.user_name = data.get("name")
                st.session_state.user_email = data.get("email")
                

            else:
                st.error("Invalid Credentials ❌")

    # ---------------- SIGNUP ----------------

    with auth_tab2:

        name = st.text_input(
            "Name",
            key="signup_name"
        )

        signup_email = st.text_input(
            "Email",
            key="signup_email"
        )

        signup_pass = st.text_input(
            "Password",
            type="password",
            key="signup_pass"
        )

        if st.button("Create Account"):

            payload = {
                "name": name,
                "email": signup_email,
                "password": signup_pass
            }

            response = requests.post(
                f"{API_URL}/signup",
                json=payload
            )

            data = response.json()

            if "Thankyou" in data.get("message", ""):

                st.success(data["message"])

                st.session_state.authenticated = True
                st.session_state.user_name = name
                st.session_state.user_email = signup_email

                st.rerun()

            else:
                st.warning(data["message"])

st.markdown("---")

# STEP 5
if st.session_state.authenticated:
    col1,col2=st.columns(2)
    with col1:
        st.subheader("📚 Document Brain")
        pdf_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

        question = st.text_input(
        "Ask Question From Document"
    )

        if st.button("Ask Document Brain"):

            data=extract_pdf(pdf_file)
            chunk=data_chunk(data)
            index=rag_system(chunk)
            query=question
            result=retrieve_system(query,index,chunk)
            search_result=search(query)
            final=prerag(query,result,search_result)
            st.write(final)
    with col2:
        st.subheader('Search anything')
        text=st.text_input('Type and Press Enter')
        if st.button('Get Info'):
            sea_result=search(text)
            st.write(sea_result)