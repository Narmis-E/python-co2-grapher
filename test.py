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
    
    # Set valid years equal to the years each country has
    valid_years = dataset[dataset['country'] == country]['year']
    
    # Get min and max years from valid_years
    min_year = int(valid_years.min())
    max_year = int(valid_years.max())

    while country:
        start_year = 0
        end_year = 0
        start_year = int(input(f"Enter the start year (min {min_year}): "))
        if (start_year < min_year or start_year > max_year): 
            print(f"{start_year} is not in the dataset\n")
            continue

        end_year = int(input(f"Enter the end year (max {max_year}): "))
        if (end_year < start_year):
            print("End year must be greater than start year.")
            continue

        if (end_year > max_year or end_year < min_year):
            print(f"{end_year} is not in the dataset\n")
            continue
        break    

    # Filter the dataset for the selected country and years
    filtered_data = dataset[dataset['country'] == country]
    filtered_data = filtered_data[(filtered_data['year'] >= start_year) & (filtered_data['year'] <= end_year)]

    # Convert the 'year' column to integers and then to strings
    filtered_data['year'] = filtered_data['year'].astype("int")

    # Create a basic line chart using Matplotlib to visualize CO2 emissions over time
    plt.plot(filtered_data['year'], filtered_data['co2'])

    # Customize the chart (e.g., labels, titles, legends)
    plt.xlabel("Time (Year)")
    plt.ylabel("CO2 Emissions (Million Tons)")
    plt.title(f"{country} CO2 Emissions ({start_year}-{end_year})")

    # Show the chart
    plt.show()

# Execute the main function
main()
