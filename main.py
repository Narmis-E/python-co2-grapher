#!/usr/bin/python
# Import libraries for CSV data manipulation and data visualization
import pandas as pd
import matplotlib.pyplot as plt

def welcome_message():
    print("CO2 Emissions Visualization Program")
    print("-----------------------------------")

def get_country(dataset):
    unique_countries = dataset['country'].unique()
    while True:
        country = input("Enter a country: ").title()
        if country in unique_countries:
            return country
        else:
            print(f"{country} is not in the dataset\n")

def get_years(dataset, country):
    valid_years = dataset[dataset['country'] == country]['year']
    min_year = int(valid_years.min())
    max_year = int(valid_years.max())
    
    while True:
        while True:
            try:
                start_year = int(input(f"Enter the start year (min {min_year}): "))
            except:
                print("Please enter a number.")
                continue
            break

        if start_year < min_year or start_year > max_year:
            print(f"{start_year} is not in the dataset or out of range\n")
            continue

        while True:
            try:
                end_year = int(input(f"Enter the end year (max {max_year}): "))
            except:
                print("Please enter a number.")
                continue
            break

        if end_year <= start_year or end_year > max_year:
            print("End year must be greater than start year and within the dataset's range.\n")
            continue
        return start_year, end_year

def create_plot(dataset, country, start_year, end_year):
    filtered_data = dataset[dataset['country'] == country]
    filtered_data = filtered_data[(filtered_data['year'] >= start_year) & (filtered_data['year'] <= end_year)]
    filtered_data['year'] = filtered_data['year'].astype("int")

    print("-------------------------------")
    print("Line: 1")
    print("Scatter: 2")
    print("Column: 3")

    while True:
            try:
                graph_choice = int(input("Please select a type of graph: "))
            except:
                print("Please enter a number.")
                continue
            break

    match graph_choice:
        case 1:
            plt.plot(filtered_data['year'], filtered_data['co2'], marker='.', markersize=15)
        case 2:
            plt.scatter(filtered_data['year'], filtered_data['co2'], s=100)
        case 3:
            plt.bar(filtered_data['year'], filtered_data['co2'])
            
    plt.xlabel("Time (Year)")
    plt.ylabel("CO2 Emissions (Million Tons)")
    plt.title(f"{country} CO2 Emissions ({start_year}-{end_year})")
    figure = plt.gcf()
    plt.show()
    plt.close()
    save_choice = input("Do you wish to save the graph as an image? [Y/n]: ")
    if (save_choice == 'y' or save_choice == ''):
        figure_name = input("Enter a name for your graph: ")
        figure.savefig(f'{figure_name}.png')
    else:
        print("Exiting")

def main():
    dataset = pd.read_csv("owid-co2-data.csv")
    print(dataset)
    welcome_message()
    country = get_country(dataset)
    start_year, end_year = get_years(dataset, country)
    create_plot(dataset, country, start_year, end_year)

main()