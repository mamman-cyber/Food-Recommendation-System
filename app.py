from flask import Flask, render_template, request
from logic import recommend_meals
from data_processor import load_data, clean_data

app = Flask(__name__)

# Load and clean dataset at startup
try:
    df = load_data('data/meals_data.csv')
    df = clean_data(df)
except Exception as e:
    print(f"Startup error: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    error = None
    
    if request.method == 'POST':
        # Get dietary preferences from form
        dietary_preferences = request.form.getlist('dietary')
        
        # Validate input
        if not dietary_preferences:
            error = "Please select at least one dietary preference to find meals."
        else:
            recommendations = recommend_meals(dietary_preferences, df)
            if not recommendations:
                error = "No meals match your selected preferences. Try different combinations."
    
    return render_template('index.html', recommendations=recommendations, error=error)

if __name__ == '__main__':
    app.run(debug=True)