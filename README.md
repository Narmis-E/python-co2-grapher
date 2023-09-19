# Python CO2 Grapher

Python CO2 Grapher is a simple Python program designed for an engineering project. It leverages the Our World In Data ([OWID](https://github.com/owid/co2-data)) dataset on CO2 emissions to generate informative and visually appealing graphs.
Features

- User-friendly interface: Input your desired country, start year, and end year to visualize CO2 emissions trends.
- Multiple graph types: Choose between line, scatter, and column graphs to display the data.
- Customizable: Save your generated graphs as image files with custom filenames.
- Dataset Inclusivity: Ensures your input is within the dataset's range.

## How to Use:

Clone the Repository:
```
git clone https://github.com/Narmis-E/python-co2-grapher.git
```
Install Dependencies:
Ensure you have the required Python libraries installed. You can do this with pip:
```
pip install pandas matplotlib
```
Run the Program:
```
python main.py
```
Follow the Prompts:
- Enter the desired country (please use proper capitalization).
- Specify the start and end years.
- Select a graph type (line, scatter, or column).
- Choose to save the graph as an image or exit the program.

    Explore Your Graph:
    A graph of CO2 emissions for the selected country and years will be displayed. Customize the graph type and save it as an image for your needs.

### Here's some examples of graphs produced by our program:

**Line Graph:**
![image](https://github.com/Narmis-E/python-co2-grapher/assets/109248529/159b14d5-1009-49db-9926-b0fe9092046c)

**Scatter:**
![image](https://github.com/Narmis-E/python-co2-grapher/assets/109248529/1c2faa53-9c3a-43a9-91fa-0bfd21b905bb)

**Bar:**
![image](https://github.com/Narmis-E/python-co2-grapher/assets/109248529/25aea863-6ffd-4fcb-b615-f13fb10f59e2)

## Limitations

Given the time constraints of the project, this program is relatively simple in its approach. With more time, the program would be able to use mroe data from the OWID dataset, perhaps analysing CO2 data per capita or CO2 growth %.
This progran is also made with the command line in mind, and we did not have enough time to conturct a graphical interface to make use of our program.

