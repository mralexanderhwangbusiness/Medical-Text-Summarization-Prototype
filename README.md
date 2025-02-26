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
  "text": "71-year-old male with hypertension and chest pain.",
  "mode": "brief"
}
```

### **Modes of Summarization**
#### **1. Brief Mode (`mode=brief`)**
Returns a concise summary of the medical text.

🔹 **Example Request:**
```json
{
  "text": "71-year-old male with hypertension and chest pain.",
  "mode": "brief"
}
```

🔹 **Example Response:**
```json
{
  "summary": "71-year-old male with hypertension and chest pain. Admitted for observation."
}
```

#### **2. JSON Mode (`mode=json`)**
Extracts structured information from the medical text and returns it in JSON format.

🔹 **Example Request:**
```json
{
  "text": "71-year-old male with hypertension and chest pain.",
  "mode": "json"
}
```

🔹 **Example Response:**
```json
{
  "patient_name": "",
  "age": "71",
  "date_of_visit": "",
  "critical_conditions": "hypertension, chest pain",
  "general_summary": "Patient presents with hypertension and chest pain.",
  "discharge_notes": "Admitted for observation."
}
```

## 📜 Logging
The API includes logging functionality to track requests, responses, and errors.

- **INFO Logs**: Logs request mode, input length, processing time, input/output token usage.
- **DEBUG Logs**: Captures the summarized output.
- **ERROR Logs**: Logs errors such as invalid input or failed API requests.

### Example Log Entry:
```
2025-02-26 12:00:00 - INFO - Processing summary request - Mode: json, Input Length: 120 chars
2025-02-26 12:00:01 - INFO - Summary generated in 1.20s | Input Tokens: 50, Output Tokens: 30
2025-02-26 12:00:01 - DEBUG - Summarized Output: {...}
```

## 🧪 Testing
### **Run All Tests Using Pytest with Logs**
```bash
pytest -s --log-cli-level=INFO
```
🔹 **Test results will be stored in the `test_results` directory.**

## 🙌 Acknowledgements
- **OpenAI** for providing the GPT-4 model.
- **FastAPI** for the web framework.

