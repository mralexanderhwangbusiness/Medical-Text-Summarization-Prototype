# Medical Text Summarization API

## 📌 Prerequisites
- **Python 3.9+**
- **Docker** (optional, for containerized deployment)

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone <repository-url>
cd Medical-Text-Summarization-Prototype
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
- Create a `.env` file in the root directory.
- Add your OpenAI API key:
  ```
  OPENAI_API_KEY=your_openai_api_key
  ```

## 🚀 Running the Application

### **Running Locally**
1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
2. Access the API documentation at:
   👉 [http://localhost:8000/docs](http://localhost:8000/docs)

### **Using Docker**
1. **Build the Docker Image**
   ```bash
   docker build -t medical-text-summarization .
   ```
2. **Run the Docker Container**
   ```bash
   docker run -p 8000:8000 medical-text-summarization
   ```

## 📡 API Endpoints

### **1️⃣ Health Check**
```http
GET /health
```
🔹 **Response:**
```json
{"status": "OK"}
```

### **2️⃣ Summarize Medical Text**
```http
POST /summarize
```
🔹 **Request Body:**
```json
{
  "text": "71-year-old male with hypertension and chest pain."
}
```
🔹 **Response:**
```json
{
  "summary": "71-year-old male with hypertension and chest pain. Admitted for observation."
}
```

## 🧪 Testing
### **Run All Tests Using Pytest with logs**
```bash
pytest -s --log-cli-level=INFO
```
🔹 **Test results will be stored in the `test_results` directory.**

## 🙌 Acknowledgements
- **OpenAI** for providing the GPT-4 model.
- **FastAPI** for the web framework.

