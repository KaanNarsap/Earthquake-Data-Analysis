Python Proposal Kaan Narsap 5716357

This project aims to analyze and visualize global earthquake data using the Geological Survey Data. By collecting, processing, and analyzing real-time and historical earthquake data, the project will explore seismic patterns such as earthquake frequency, magnitude distribution, depth variation, and geographical clustering. The outcome will be a set of visualizations that help understand global seismic activity and highlight regions of high seismic risk.

Data Collection:
  Retrieve earthquake data (magnitude, depth, location, time) for a defined time range (e.g., last 20 years or real-time).

Data Analysis:
 Analyze the distribution of earthquake magnitudes and depths.
    Investigate the frequency of seismic events over time.
    Identify geographic regions with a high occurrence of earthquakes.

Geospatial Visualization: Create interactive maps that display:
Earthquake locations overlaid on a world map.
    Regions with a high frequency of earthquakes.
    Patterns between earthquake depth and magnitude.

Temporal Visualization: 
  Show trends over time, such as changes in earthquake activity, and compare year-on-year seismic activity.
  
Seismic Risk Identification: 
Based on the analyzed data, identify and highlight areas that are most prone to high-magnitude earthquakes and assess potential seismic risk zones.

# Earthquake Data Analysis

This project analyzes earthquake data from a CSV file, providing insights into various aspects of earthquakes, such as magnitude trends over time, depth vs. magnitude, frequency distribution, and visualizations on interactive maps.

## Features

- **Magnitude Trend Analysis:** Plotting average earthquake magnitudes over time.
- **Depth vs. Magnitude Analysis:** Scatterplot to visualize the relationship between depth and magnitude.
- **Frequency Distribution:** Histogram of earthquake frequency by magnitude.
- **Interactive Map Visualizations:** Heatmap, clustered map, and detailed circle marker map displaying earthquake locations.

## How to Run

1. **Requirements:** Make sure you have Python installed along with the required libraries: `pandas`, `matplotlib`, `seaborn`, and `folium`.
2. **Install Dependencies:** Run the following to install necessary packages:
   ```bash
   pip install pandas matplotlib seaborn folium

Run the Program:

    Place your earthquake data CSV file in a known location. Specify its path in the csv_file variable in the script.

Outputs:

    The program generates visualizations and saves interactive map files:
        Magnitude Trend Plot
        Depth vs. Magnitude Scatter Plot
        Frequency Distribution Histogram
    Saved HTML map files:
        earthquake_map.html (Detailed map with circle markers)
        earthquake_heatmap.html (Heatmap of earthquake locations)
        earthquake_cluster.html (Clustered earthquake map)

Input Requirements

    CSV Data File: The file should contain columns for latitude, longitude, place, mag (magnitude), depth, and time.

Additional Information

    Data Preprocessing: The script preprocesses the data, handling missing values and converting time fields.
    Map Visualizations: Interactive maps are saved as HTML files for easy viewing.

This README provides a comprehensive guide to understanding, running, and exploring the outputs of your earthquake data analysis project. Let me know if you’d like to add more details.



Test functions: 
![image](https://github.com/user-attachments/assets/031e2ff2-fcc5-4405-b14b-530bae2710ec)
