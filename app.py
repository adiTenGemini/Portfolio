from flask import Flask, render_template

app = Flask(__name__)

profile = {
    "name": "Aditya A Rajan",
    "headline": "Data Scientist — ML, NLP & Analytics",
    "subtitle": "I build machine learning tools, analytics dashboards, and polished data products.",
    "about": "Data scientist with an MSc in Data Science & AI (University of Liverpool). Experienced in ML, NLP, time-series forecasting, and building end-to-end analytics solutions.",
    "stats": [
        {"value": "6+", "label": "Portfolio projects"},
        {"value": "5+", "label": "Notebooks and models"},
        {"value": "1", "label": "Focused portfolio"}
    ],
    "projects": [
        {
            "title": "Player Recommendation Application",
            "description": "A recommender system built to suggest players based on performance and user preference.",
            "meta": "Machine Learning",
            "image": "images/player_recommendation.svg"
        },
        {
            "title": "Customer Churn Prediction",
            "description": "A predictive model for identifying churn risk and improving retention strategies.",
            "meta": "Analytics",
            "image": "images/customer_churn.svg"
        },
        {
            "title": "Customer Reviews Analysis",
            "description": "NLP-driven sentiment analysis to extract product and service insights.",
            "meta": "NLP",
            "image": "images/customer_reviews.svg"
        },
        {
            "title": "Card Fraudulent Detection",
            "description": "An anomaly detection pipeline for spotting fraud in transaction data.",
            "meta": "Data Science",
            "image": "images/card_fraud.svg"
        },
        {
            "title": "Airline Booking Status Predictor",
            "description": "A forecasting solution for booking status and flight demand.",
            "meta": "Predictive Modeling",
            "image": "images/airline_booking.svg"
        },
        {
            "title": "Computation of Lattice Invariants",
            "description": "A research-focused application for mathematical invariant computation.",
            "meta": "Research",
            "image": "images/computation_lattice.svg"
        }
    ],
    "github_url": "https://github.com/adiTenGemini",
    "location": "Liverpool, UK",
    "role": "Data Science Trainee @ Digital Futures",
    "education": "MSc Data Science & AI — University of Liverpool",
    "skills": ["Python", "Pandas", "NumPy", "PyTorch", "scikit-learn", "Postgres", "Tableau", "Django", "JavaScript", "OpenCV"],
    "pinned": [
        {"title": "Player Recommendation Application", "url": "https://github.com/adiTenGemini/Player-Recommendation-Application"},
        {"title": "Application for Computation of Lattice Invariants", "url": "https://github.com/adiTenGemini/Application-for-Computation-of-Lattice-Invariants"},
        {"title": "Customer Churn Prediction", "url": "https://github.com/adiTenGemini/Customer-Churn-Prediction"},
        {"title": "Airline Booking Status Predictor", "url": "https://github.com/adiTenGemini/Airline-Booking-Status-Predictor"},
        {"title": "Customer Reviews Analysis", "url": "https://github.com/adiTenGemini/Customer-Reviews-Analysis"},
        {"title": "Card Fraudulent Detection", "url": "https://github.com/adiTenGemini/Card-Fraudulent-Detection"}
    ],
    "contact_email": "hello@example.com",
    "linkedin_url": "https://www.linkedin.com/in/adityaarajan/"
}

@app.route('/')
def home():
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
