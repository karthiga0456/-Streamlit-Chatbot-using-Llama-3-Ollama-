Streamlit Chatbot using Llama 3 (Ollama)




Overview
This project is a Chatbot built using Streamlit and Llama 3 from Ollama. It provides a simple web-based UI for interacting with the chatbot.

🚀 Features
✅ Uses Llama 3 from Ollama for local inference
✅ Built with Streamlit for an interactive UI
✅ No external API keys required – runs locally
✅ Lightweight and easy to set up

📌 Installation
1️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/karthiga0456/-Streamlit-Chatbot-using-Llama-3-Ollama-.git
cd Streamlit-Chatbot-using-Llama-3-Ollama

2️⃣ Set Up a Virtual Environment
sh
Copy
Edit
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate     # On Windows

3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt

4️⃣ Install Ollama and Llama 3 Model
sh
Copy
Edit
ollama pull llama3

5️⃣ Run the Streamlit App
sh
Copy
Edit
streamlit run app.py
🖥️ Usage
1️⃣ Open the Streamlit app in your browser.
2️⃣ Enter your question in the chat input box.
3️⃣ The Llama 3 model will generate a response.

🔧 Configuration
If you want to modify the chatbot, edit app.py.
Change the model in app.py if you have a different Ollama model installed.
📜 License
This project is licensed under the MIT License.
