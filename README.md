# Food Recommendation Expert System

## Project Description
This project implements a Boolean filtering-based expert system for recommending meals based on user-selected dietary preferences (e.g., vegan, gluten-free, low-carb). It features an enhanced Flask web interface with Bootstrap 5.3.0 styling, including responsive design, tooltips, and visual feedback for a user-friendly experience. The system uses a static CSV dataset simulating data from food APIs like Spoonacular or Edamam and is designed for educational purposes.

## Setup Instructions

Follow these steps to set up and run the Food Recommendation Expert System on your computer. These instructions are designed for Windows, Mac, or Linux users with no prior experience in Python or Flask.

### Prerequisites
- **Python 3.10 or higher**:
  - Download and install from [python.org](https://www.python.org/downloads/).
  - **Windows**: Check “Add Python to PATH” during installation.
  - Verify: Open a terminal (Command Prompt, Terminal, or Git Bash) and run:
    ```bash
    python --version
    ```
    You should see `Python 3.x.x`.
- **Git** (optional, for cloning):
  - Download from [git-scm.com](https://git-scm.com/downloads) or install via package manager (e.g., `brew install git` on Mac, `sudo apt-get install git` on Linux).
- **Text Editor** (recommended):
  - Use [Visual Studio Code](https://code.visualstudio.com/) or any text editor (e.g., Notepad).

### Step-by-Step Setup
1. **Clone or Download the Repository**:
   - **Option 1: Clone with Git**:
     - Open a terminal and run:
       ```bash
       git clone https://github.com/mamman-cyber/Food-Recommendation-System.git
       cd Food-Recommendation-System
       ```
   - **Option 2: Download ZIP**:
     - Visit [https://github.com/mamman-cyber/Food-Recommendation-System](https://github.com/mamman-cyber/Food-Recommendation-System).
     - Click “Code” > “Download ZIP,” extract to a folder (e.g., `Food-Recommendation-System`).
     - Open a terminal and navigate to the folder:
       ```bash
       cd path/to/Food-Recommendation-System
       ```

2. **Create a Virtual Environment**:
   - In the `Food-Recommendation-System` folder, run:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **Mac/Linux**:
       ```bash
       source venv/bin/activate
       ```
   - Your terminal should show `(venv)`.

3. **Install Dependencies**:
   - Ensure `requirements.txt` is in the folder.
   - Run:
     ```bash
     pip install -r requirements.txt
     ```
   - This installs Flask and pandas. You’ll see installation messages.

4. **Run the Application**:
   - In the same terminal (with `(venv)` active), run:
     ```bash
     python app.py
     ```
   - You should see:
     ```
     * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
     ```
   - Open a web browser (Chrome, Firefox, etc.) and go to `http://localhost:5000`.

5. **Use the Application**:
   - The webpage displays:
     - A green header with the title “Food Recommendation Expert System.”
     - Checkboxes for dietary preferences (e.g., Vegan, Gluten-Free) with tooltips (hover for descriptions).
     - A “Get Meals” button.
   - Select preferences (e.g., Vegan, Gluten-Free), click “Get Meals,” and view recommended meals.
   - If no meals match or no preferences are selected, an error message appears.
   - Press `CTRL+C` in the terminal to stop the app.

### Troubleshooting
- **Python not found**:
  - Ensure Python is installed and added to PATH. Run `python --version`.
  - Use `python3` instead of `python` on Mac/Linux if needed.
- **ModuleNotFoundError: No module named 'flask'**:
  - Confirm you’re in the virtual environment (`(venv)` in terminal).
  - Re-run `pip install -r requirements.txt`.
- **Port already in use**:
  - If `http://localhost:5000` fails, another app may use port 5000. Stop other Flask apps or run:
    ```bash
    python app.py --port 5001
    ```
    Then visit `http://localhost:5001`.
- **Page shows raw code**:
  - Don’t open `index.html` directly in a browser. Run `python app.py` and visit `http://localhost:5000`.
- For other issues, contact the team or check Flask documentation.


## Dataset Sources
- `data/meals_data.csv`: A sample dataset simulating data from Spoonacular or Edamam APIs, containing meal names, ingredients, dietary tags, and calories.
- Potential sources: [Spoonacular Food API](https://spoonacular.com/food-api), [Edamam Recipe API](https://developer.edamam.com/edamam-recipe-api), [USDA Nutrition Database](https://fdc.nal.usda.gov/).

## Test Cases
- **Test Case 1**: Input: Vegan, Gluten-Free → Output: Grilled Veggie Salad, Quinoa Bowl
- **Test Case 2**: Input: Low-Carb, High-Protein → Output: Keto Beef Bowl
- **Test Case 3**: Input: None → Output: Error ("Please select at least one dietary preference")


## Team Members
- Mamman Cyber (mamman oliver yelwa vug/sen/22/8261): Primary developer and project lead.
- kennedy: Assisted with testing and validation.
- Akudigwe kingdavid vug/sen/22/8261: Supported documentation and project coordination.

## Contributions
- Mamman Cyber: Designed and implemented the entire system, including dataset handling (`data_processor.py`, `meals_data.csv`), Boolean filtering logic (`logic.py`), Flask UI with Bootstrap styling (`app.py`, `index.html`, `styles.css`), and documentation (`README.md`).
- kennedy: Tested the application with various inputs to ensure functionality, including edge cases like no dietary preferences selected.
- Akudigwe kingdavid: Reviewed documentation for clarity and assisted in coordinating project tasks.


**Disclaimer**: This system is for educational purposes only bulit by 300lvl veritas software engineering student as their SEN312 project. Consult a nutritionist for dietary advice.
