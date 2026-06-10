import csv

import matplotlib.pyplot as plt

def online_population(file_path):
  population_by_continent={}
  
  with open(file_path, 'r') as data_csvfile:
    data_csvreader=csv.DictReader(data_csvfile)
    
    for line in data_csvreader:
      continent=line['continent']
      year=int(line['year'])
      population=int(line['population'])

    #check to see if continent is not in the dictionary 
    #add continent, year, population if it doesn't exist
      if continent not in population_by_continent:
          population_by_continent[continent]={'years':[], 'population':[]} 
      #if continent exists, append the year, population
      population_by_continent[continent]['years'].append(year)  
      population_by_continent[continent]['population'].append(population)
      
  return population_by_continent
    
def plot_population_by_continent(population_by_continent):
  #loop over each continent and plot each continent and population by year
    for continent in population_by_continent:
      years=population_by_continent[continent]['years']
      population_continent=(population_by_continent[continent]['population'])
      
    #create a plot for each continent
      plt.plot(years, population_continent, label=continent, alpha=0.5, marker='+')
      plt.legend()

#create ploy labels outside of function
plt.title("Online Population by Continent")
plt.xlabel("Year")
plt.ylabel("Population (in billions)")
plt.grid(True)
plt.tight_layout()

#create file path
file_path='data.csv'
population_by_continent= online_population(file_path)
plot_population_by_continent(population_by_continent)

plt.show()
