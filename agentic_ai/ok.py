from flask import Flask, render_template, request
import google.generativeai as genai

# 🔑 Configure Gemini API key
GOOGLE_API_KEY = "YOUR_API_KEY"
genai.configure(api_key="AIzaSyC0pnHWcKL1rv6YLykJyFPTDLrLKFUBLsU")

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    error = None

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if not question:
            error = "Please enter a question."
        else:
            try:
                response = model.generate_content(question)
                answer = response.text
            except Exception as e:
                error = f"⚠️ Error: {e}"

    return render_template("index.html", answer=answer, error=error)

if __name__ == "__main__":
    app.run(debug=True)
