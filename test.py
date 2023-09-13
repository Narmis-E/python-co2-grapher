# Import libraries for CSV data manipulation and data visualization
import pandas as pd
import matplotlib.pyplot as plt

# Define the main function
def main():
    # Load the CO2 emissions dataset using Pandas
    dataset = pd.read_csv("owid-co2-data.csv")
    
    # Output a welcome message
    print("Welcome to the CO2 Emissions Visualization Program!")
    unqiue_country = dataset['country'].unique()

    # Prompt the user to input the desired country, start year, and end year
    country = input("Enter the country: ")
    
    while country not in unqiue_country:
        print(f"{country} is not in the dataset\n")
        country = input("Enter the country again: ")
        
    #TODO - make a check for the selected country's start year
    start_year = int(input("Enter the start year: "))

    #TODO - make a check for the selected country's end year
    end_year = int(input("Enter the end year: "))

    # Filter the dataset for the selected country and years
    filtered_data = dataset[dataset['country'] == country]
    filtered_data = filtered_data[(filtered_data['year'] >= start_year) & (filtered_data['year'] <= end_year)]

    # Create a basic line chart using Matplotlib to visualize CO2 emissions over time
    plt.plot(filtered_data['year'], filtered_data['co2'])

    # Customize the chart (e.g., labels, titles, legends)
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions")
    plt.title(f"CO2 Emissions in {country} ({start_year}-{end_year})")

    # Show the chart
    plt.show()

# Execute the main function
main()
