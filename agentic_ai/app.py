from flask import Flask, request, render_template
import google.generativeai as genai

app = Flask(__name__)

# 🔑 API Key
GOOGLE_API_KEY = "AIzaSyBTyLAoKjXxDJQVLaNR0BQWADs3eZ7C0xg"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        if question:
            response = model.generate_content(question)
            answer = response.text
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
