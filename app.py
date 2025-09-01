from flask import Flask, render_template, request
app = Flask(__name__)

def evaluate_grade(score):
    """Return grade, emoji, and suggestion"""
    if score < 0 or score > 100:
        return "Invalid input ⚠️", "", "Grade must be between 0 and 100."
    
    if score >= 90:
        return "A+ 🌟", "Excellent work!", "Keep up the amazing effort!"
    elif score >= 80:
        return "A ✅", "Very Good!", "You are doing great, aim for A+!"
    elif score >= 70:
        return "B 👍", "Good!", "Some improvement needed to reach top grades."
    elif score >= 60:
        return "C 🙂", "Average", "Focus a bit more on weak areas."
    elif score >= 50:
        return "D ⚠️", "Below Average", "Work harder, you can improve!"
    else:
        return "F ❌", "Failed", "Don't give up! Seek help and try again."

@app.route("/", methods=["GET", "POST"])
def home():
    grade_result = ""
    emoji = ""
    suggestion = ""
    if request.method == "POST" :
        try:
            user_score = float(request.form.get("score"))
            grade_result, emoji, suggestion = evaluate_grade(user_score)
        except ValueError:
            grade_result = "❌ Please enter a valid number!"
    return render_template("index.html", grade=grade_result, emoji=emoji, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)