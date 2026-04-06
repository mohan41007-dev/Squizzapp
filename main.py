import json
import os
from src.logic import QuizLogic
from src.ui import QuizUI

def run_app():
    # 1. Locate the data file
    # We use join to make sure it works on both Windows and Mac
    data_path = os.path.join("data", "questions.json")

    # 2. Load the questions from the JSON file
    try:
        with open(data_path, "r") as file:
            questions_data = json.load(file)
    except FileNotFoundError:
        print("Error: Could not find questions.json in the data folder!")
        return

    # 3. Initialize the 'Brain' (Logic) with the data
    brain = QuizLogic(questions_data)

    # 4. Initialize the 'Face' (UI) and give it the Brain
    app = QuizUI(brain)

    # 5. Keep the app running
    app.mainloop()

if __name__ == "__main__":
    run_app()