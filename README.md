# 🚀 Chatbot using Google Gemini-Pro and Streamlit

## Overview
This is an AI-powered chatbot built using **Google Gemini-Pro** and **Streamlit**. The chatbot allows users to interact with an AI model and get responses in real-time.

## 🛠️ Technologies Used
- **Python** - Core programming language
- **Streamlit** - Web framework for building the UI
- **Google Generative AI (Gemini-Pro)** - AI model for generating responses
- **dotenv** - For handling environment variables

## 📌 Features
- Interactive chatbot interface
- Supports real-time conversation
- Simple and user-friendly UI
- Uses Google Gemini-Pro for intelligent responses

## 📜 Installation
To run the chatbot locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following line:
     ```sh
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## ▶️ Running the App
Run the following command:
```sh
streamlit run app.py
```

## 🚀 Deployment
### Deploy on Streamlit Cloud
1. Push the code to a **GitHub repository**.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in with GitHub.
3. Select your repository and deploy it.
4. Add the **environment variable (`GOOGLE_API_KEY`)** in Streamlit’s settings.
5. Click **Deploy** and get a shareable link!

## 📌 Contribution
Feel free to contribute to this project by opening **issues** or **pull requests**.

## 📄 License
This project is open-source and available under the **MIT License**.

---
💡 **Developed with ❤️ using Streamlit and Google Gemini-Pro!**
