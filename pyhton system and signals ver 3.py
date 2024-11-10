import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap, MarkerCluster

# Function to preprocess the data from CSV file
def preprocess_earthquake_data(csv_file):
    
    df = pd.read_csv(csv_file)
    
    df['time'] = pd.to_datetime(df['time'], errors='coerce')  
    
    print("First 5 rows of the data:")
    print(df.head())
    
    return df

# Function to plot earthquake magnitudes over time
def plot_magnitude_trend(df):
    plt.figure(figsize=(10,6))
    df.groupby(df['time'].dt.year)['mag'].mean().plot()
    plt.title('Average Earthquake Magnitude Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average Magnitude')
    plt.grid(True)
    plt.show()

# Function to plot earthquake depth vs magnitude
def plot_depth_vs_magnitude(df):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='depth', y='mag', data=df)
    plt.title('Earthquake Depth vs Magnitude')
    plt.xlabel('Depth (km)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

# Function to plot earthquake frequency by magnitude
def plot_earthquake_frequency(df):
    plt.figure(figsize=(10,6))
    sns.histplot(df['mag'], bins=10, kde=False)
    plt.title('Earthquake Frequency by Magnitude')
    plt.xlabel('Magnitude')
    plt.ylabel('Number of Earthquakes')
    plt.grid(True)
    plt.show()

# Function to create a heatmap of earthquake locations
def create_earthquake_heatmap(df):
    earthquake_map = folium.Map(location=[0, 0], zoom_start=2)
    
    heat_data = [[row['latitude'], row['longitude']] for index, row in df.iterrows() if not pd.isnull(row['latitude']) and not pd.isnull(row['longitude'])]
    
    HeatMap(heat_data).add_to(earthquake_map)
    
    return earthquake_map

# Function to create a clustered earthquake map
def create_earthquake_cluster_map(df):
    earthquake_map = folium.Map(location=[0, 0], zoom_start=2)
    
    marker_cluster = MarkerCluster().add_to(earthquake_map)
    
    for index, row in df.iterrows():
        if not pd.isnull(row['latitude']) and not pd.isnull(row['longitude']):
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=f"Location: {row['place']}<br>Magnitude: {row['mag']}<br>Depth: {row['depth']} km"
            ).add_to(marker_cluster)
    
    return earthquake_map

# Function to create an interactive map of earthquakes with additional information 
def create_earthquake_map(df):
    
    earthquake_map = folium.Map(location=[0, 0], zoom_start=2)
    
    for index, row in df.iterrows():
        if not pd.isnull(row['latitude']) and not pd.isnull(row['longitude']):
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=row['mag'] * 2,
                color='red' if row['mag'] >= 5 else 'orange',
                fill=True,
                fill_opacity=0.6,
                popup=f"Location: {row['place']}<br>mag: {row['mag']}<br>Depth: {row['depth']} km"
            ).add_to(earthquake_map)
    
    return earthquake_map

#Main system with all the working functions and plots, CSV file is also located here
if __name__ == "__main__":
    
    csv_file = r"C:\Users\knars\Downloads\query.csv"  
    
    df_earthquakes = preprocess_earthquake_data(csv_file)
    
    print(df_earthquakes.describe())
    
    plot_magnitude_trend(df_earthquakes)
    
    plot_depth_vs_magnitude(df_earthquakes)
    
    plot_earthquake_frequency(df_earthquakes)
    
    earthquake_map = create_earthquake_map(df_earthquakes)
    earthquake_map.save("earthquake_map.html")
    print("Earthquake map saved as 'earthquake_map.html'")
    
    earthquake_map = create_earthquake_heatmap(df_earthquakes)
    earthquake_map.save("earthquake_heatmap.html")
    print("Earthquake map saved as 'earthquake_heatmap.html'")
    
    earthquake_map = create_earthquake_cluster_map(df_earthquakes)
    earthquake_map.save("earthquake_cluster.html")
    print("Earthquake map saved as 'earthquake_cluster.html'")
    
real_data_file = r"C:\Users\knars\Downloads\query.csv"   

#testing functions -->
def test_preprocess_earthquake_data():
    df = preprocess_earthquake_data(real_data_file)
    assert 'time' in df.columns, "Data should contain a 'time' column."
    assert pd.api.types.is_datetime64_any_dtype(df['time']), "Column 'time' should be in datetime format."

def test_plot_magnitude_trend():
    df = preprocess_earthquake_data(real_data_file)
    try:
        plot_magnitude_trend(df)
    except Exception as e:
        assert False, f"plot_magnitude_trend() raised an exception {e}"

def test_plot_depth_vs_magnitude():
    df = preprocess_earthquake_data(real_data_file)
    try:
        plot_depth_vs_magnitude(df)
    except Exception as e:
        assert False, f"plot_depth_vs_magnitude() raised an exception {e}"

def test_create_earthquake_heatmap():
    df = preprocess_earthquake_data(real_data_file)
    heatmap = create_earthquake_heatmap(df)
    assert heatmap is not None, "Heatmap creation should not return None."
    assert len(heatmap._children) > 0, "Heatmap should contain data points."
