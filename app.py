from flask import Flask, render_template, request, redirect, url_for

# Tell Flask to look for templates and static files in the current folder
app = Flask(__name__, template_folder=".", static_folder=".")

# In-memory storage (replace with database later)
transactions = [
    {"date": "2026-07-20", "category": "Sale", "description": "Wheat Harvest", "amount": 2500},
    {"date": "2026-07-18", "category": "Expense", "description": "Fertilizer Purchase", "amount": -800},
    {"date": "2026-07-15", "category": "Sale", "description": "Vegetable Market", "amount": 1200},
]

@app.route("/")
def dashboard():
    revenue = sum(t["amount"] for t in transactions if t["amount"] > 0)
    expenses = sum(-t["amount"] for t in transactions if t["amount"] < 0)
    profit = revenue - expenses
    return render_template("index.html", transactions=transactions, revenue=revenue, expenses=expenses, profit=profit)

@app.route("/income", methods=["GET", "POST"])
def income():
    if request.method == "POST":
        date = request.form["date"]
        category = request.form["category"]
        description = request.form["description"]
        amount = float(request.form["amount"])
        transactions.append({"date": date, "category": category, "description": description, "amount": amount})
        return redirect(url_for("dashboard"))
    return render_template("income.html")

@app.route("/reports")
def reports():
    revenue = sum(t["amount"] for t in transactions if t["amount"] > 0)
    expenses = sum(-t["amount"] for t in transactions if t["amount"] < 0)
    profit = revenue - expenses
    return render_template("reports.html", revenue=revenue, expenses=expenses, profit=profit)

if __name__ == "__main__":
    app.run(debug=True)
