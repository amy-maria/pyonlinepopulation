import matplotlib.pyplot as plt
from flask import Flask, jsonify, render_template
import csv
import io
import base64
import os
import matplotlib
# Agg backend to generate plots without a new window
matplotlib.use("Agg")

app = Flask(__name__)

# ... your routes go here ...


def online_population(file_path):
    population_by_continent = {}
    if not os.path.exists(file_path):
        return population_by_continent

    with open(file_path, 'r') as data_csvfile:
        data_csvreader = csv.DictReader(data_csvfile)

        for line in data_csvreader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])

        # check to see if continent is not in the dictionary
        # add continent, year, population if it doesn't exist
            if continent not in population_by_continent:
                population_by_continent[continent] = {
                    'years': [], 'population': []}
            # if continent exists, append the year, population
            population_by_continent[continent]['years'].append(year)
            population_by_continent[continent]['population'].append(population)

    return population_by_continent

# --- Web Routes ---


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chart")
def get_chart():
    try:
        # clear any previous charts
        plt.clf()

        file_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'data.csv')
        if not os.path.exists(file_path):
            return jsonify({"error": f"Critical Error: Data file '{file_path}' was not found in the project directory."}), 404

        population_data = online_population(file_path)

        # Check if your CSV parser returned an empty dictionary
        if not population_data:
            return jsonify({"error": "Data file found, but the parsed dictionary is empty. Check your CSV column headers."}), 400

        # 2. Map line data points
        for continent in population_data:
            years = population_data[continent]['years']
            population_continent = population_data[continent]['population']
            plt.plot(years, population_continent,
                     label=continent, alpha=0.7, marker='+')

        # 3. Apply labels and structural layouts
        plt.title("Online Population by Continent")
        plt.xlabel("Year")
        plt.ylabel("Population (in billions)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()

        # 4. Stream and translate to base64
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)

        img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')

        # Successful return statement
        return jsonify({"chart_image": f"data:image/png;base64,{img_base64}"})

    except Exception as e:
        # If ANY structural processing error happens, pass the error string back to the browser safely
        return jsonify({"error": f"Internal Application Error: {str(e)}"}), 500
    finally:
        plt.close()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
