# Covid-dataset
Authors: 
Dino Azizovic, Shaheer Waqar, Alexander Schäfer

## Requirements
Python 3.10
Used Librarys:
- Plotly 5.15.0
- Dash 2.11.1
- Pandas 2.0.3
  
## Installation
1. Download the repository from GitHub.
2. Open the repository in your Python supported IDE
3. Install the Librarys through requirements

   ```pip install -r requirements.txt```
5. Run through the IDE -> a Localhost adress will be generated in the console

## Motivation
We wanted to show the impact of the global Covid-19 Pandemic based on collected Data over the last 4 Years. For that we choose a Dataset from the [Our World in Data](https://ourworldindata.org/coronavirus). 
The Dataset had an overwhelming amount of options too choose from where we at the end decided to include the Data only from the Columns of "Total Cases, Total Deaths, Population, Fully Vacinations, Total Cases Per Million and Total Deaths Per Million.

## Function
The Graphs are Variable Drawn based on the choosing of the Costumer. 

For that the Webbased Application uses a Dropdown Menu to choose the country the Data is from and a Checklist to choose the wished data that the customer wants to see.

## Data Processing 
For processing and cleaning the data and removing null values and unwanted columns, Pandas library was used to make changes to the existing csv file.
## Front-End
  In the frontend, we built an intuitive and interactive interface using Dash and Bootstrap. Users can easily navigate through dropdown menus and checkboxes to select specific countries and data points. Dynamic line charts visualize the progression of COVID-19 cases and vaccination impact. Engaging card components with animations provide concise information about the epidemic and its global impact. Our frontend offers a seamless and informative experience for exploring COVID-19 data.
## Back-End
The main part of the Back-End is the generation of the Multilayered Graphs based on the options choosen of the Checkboxes. 

For that we choose to use a For-Loop that itterates over the Dataset based on the choosen Country from the Dropdown Box.

After the Data is properly selected we create a Trace with the plotly.graph_objs Library (shortened to go).
A Trace is the basic Drawing that is later then shown on the Graph. We create the Lines for the different Datapoints choosen over the Checkbox and then append the results in a Traces List.

The Traces list is then used to generate a Figure together with a custom Layout that decides the x- and y-axes as well as the title.

afterwards the Figure is returned to the HTML Output call for the Graph to show the different figures. 

## Sources
Dataset: [Our World in Data](https://ourworldindata.org/coronavirus), last seen: 05/07/2023

Dash + Plotly Information: [Plotly](https://dash.plotly.com)
