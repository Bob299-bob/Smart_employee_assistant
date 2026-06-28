# 🏢 Smart Employee Entry & Assistance System

An end-to-end **AI-powered Smart Office System** that automates employee entry, security validation, authentication, and internal office assistance using **Computer Vision, Deep Learning, and LLM-based RAG chatbot**.

---

## 🚀 Overview

This project simulates a real-world **intelligent organization ecosystem**, where multiple AI modules work together to handle:

* Entry gate intelligence 🚪
* Security validation 😷
* Employee authentication 🔐
* Office navigation 🏢
* AI-powered knowledge assistant 🤖

The system is designed to improve **security, efficiency, and employee experience** in modern workplaces.

---

## 🧠 System Architecture / Flow

```
🚗 Vehicle Detection (Optional Layer)
        ↓
😷 Face Mask Detection (CNN)
        ↓
🔐 Authentication System (Login/Signup - FastAPI)
        ↓
🏢 Organization Intelligence System (LSTM/RNN)
        ↓
🤖 RAG-Based AI Chatbot (Ask Anything Assistant)
```

---

## ⚙️ Features

### 🚗 Vehicle Detection System

* Detects vehicle presence at entry gate
* Used for optional parking/entry analytics
* Does not block entry flow

---

### 😷 Face Mask Detection

* CNN-based real-time detection
* Ensures safety compliance
* Allows/restricts entry based on mask status

---

### 🔐 Authentication System

* Secure Login/Signup using FastAPI
* Session-based access control
* Only authorized employees can access system

---

### 🏢 Organization Intelligence System

* Structured office knowledge system
* Acts as virtual office map
* Includes:

  * Departments
  * Floor mapping
  * Cabin locations
  * Navigation guidance

---

### 🤖 RAG-Based AI Chatbot

* Retrieval-Augmented Generation system
* Answers organization-specific queries
* Examples:

  * “Where is HR department?”
  * “How do I access admin office?”
  * “What are office timings?”

---

## 🛠️ Tech Stack

**Computer Vision**

* CNN (Face Mask Detection)
* Object Detection (Vehicle Detection)

**AI / NLP**

* RAG (Retrieval-Augmented Generation)
* LSTM / RNN (Organization Intelligence)
* FAISS (Vector Search)

**Backend**

* FastAPI

**Frontend**

* Streamlit

**Database**

* SQLite (modular & scalable)

**Frameworks**

* PyTorch / TensorFlow
* (Optional) LangChain

---

## 📁 Project Structure

```
Smart-Office-System/
│
├── backend/
│   ├── main.py
│   ├── auth/
│   ├── rag_system/
│   └── models/
│
├── frontend/
│   ├── app.py (Streamlit UI)
│
├── models/
│   ├── cnn_mask_model/
│   ├── vehicle_detection_model/
│
├── data/
│   ├── org_documents/
│
├── database/
│   └── database.db
│
├── requirements.txt
└── README.md
```

---

## 🚀 How It Works

1. User enters the organization premises
2. System checks vehicle presence (optional layer)
3. Face mask detection is performed
4. User logs in via authentication system
5. System loads organization intelligence
6. User interacts with AI chatbot (RAG system)

---

## ⚠️ Challenges Faced

* Integrating CV + NLP pipelines in real-time
* Optimizing Streamlit performance for inference
* Improving RAG accuracy for domain-specific answers
* Handling model size and deployment constraints
* Managing session-based authentication flow

---

## 💡 Future Improvements

* Face recognition-based auto login
* IoT-based gate control integration
* Live CCTV anomaly detection
* Voice-enabled AI assistant
* Multi-floor digital twin of organization

---

## 📌 Key Highlights

✔ Multi-AI system integration
✔ Real-time security pipeline
✔ Enterprise-like workflow simulation
✔ RAG-based intelligent assistant
✔ Modular and scalable architecture

---

## 🏁 Outcome

This project demonstrates how multiple AI systems can be combined into a **single intelligent workplace ecosystem**, transforming traditional office operations into a smart, automated experience.

---

## 🔖 License

This project is for educational and portfolio purposes.

---

## 👨‍💻 Author

**Boby Gupta**

---

## 🌟 Show Your Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🧠 Share it with others

---

## 🔖 Tags

#ArtificialIntelligence #MachineLearning #DeepLearning #ComputerVision #RAG #LLM #FastAPI #Streamlit #Python #AIProjects #SmartOffice #Automation #NLP #MLOps #GenerativeAI

---

