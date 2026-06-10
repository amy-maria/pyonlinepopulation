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
    # clear any previous charts
    plt.clf()

    file_path = 'data.csv'
    population_data = online_population(file_path)


def plot_population_by_continent(population_by_continent):
    # loop over each continent and plot each continent and population by year
    for continent in population_by_continent:
        years = population_by_continent[continent]['years']
        population_continent = (
            population_by_continent[continent]['population'])

    # create a plot for each continent
        plt.plot(years, population_continent,
                 label=continent, alpha=0.5, marker='+')
        plt.legend()


# create ploy labels outside of function
    plt.title("Online Population by Continent")
    plt.xlabel("Year")
    plt.ylabel("Population (in billions)")
    plt.grid(True)
    plt.tight_layout()

# New for Flask
# Save the plot to an in-memory buffer instead of a file on disk
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

# Encode the image to base64 string so HTML/JS can read it instantly
    img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
    plt.close()

# create file path
# file_path = 'data.csv'
# population_by_continent = online_population(file_path)
# plot_population_by_continent(population_by_continent)

    return jsonify({"chart_image": f"data:image/png;base64,{img_base64}"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# plt.show()
