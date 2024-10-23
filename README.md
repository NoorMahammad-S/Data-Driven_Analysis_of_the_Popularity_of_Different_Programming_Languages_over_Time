# A Data-Driven Analysis of the Popularity of Different Programming Languages over Time

This project explores the popularity of various programming languages over time using data from Stack Overflow. The analysis visualizes the number of posts for different programming languages, helping identify trends and shifts in popularity. The data is either sourced from a provided `.csv` file or fetched directly from Stack Exchange via SQL queries.

![A Data-Driven Analysis of the Popularity of Different Programming Languages over Time](https://github.com/NoorMahammad-S/Data-Driven_Analysis_of_the_Popularity_of_Different_Programming_Languages_over_Time/blob/master/Images/Image.jpg)

## Features
- **Data Handling & Exploration**:
  - Load and preprocess data using Pandas.
  - Clean and reshape data for further analysis.
- **Data Visualization**:
  - Generate line charts for individual languages.
  - Compare the popularity of multiple languages on a single chart.
  - Apply rolling averages to smooth time series data and observe trends.
- **Programming Languages**: Includes analysis for popular programming languages such as Python, Java, and many others.
  
## Requirements
To run this project locally, ensure you have the following dependencies installed:

```bash
pip install pandas matplotlib
```

## Data
The dataset used for this analysis can be either a pre-existing `.csv` file or fetched fresh from Stack Overflow. The `.csv` file should have the following structure:
- **Columns**:
  - `DATE`: The date of the post in `YYYY-MM-DD` format.
  - `TAG`: The programming language tag (e.g., `python`, `java`).
  - `POSTS`: The number of posts on Stack Overflow for that particular language.

## Getting Started
1. **Clone the repository**:
   ```bash
   git clone https://github.com/NoorMahammad-S/Data-Driven_Analysis_of_the_Popularity_of_Different_Programming_Languages_over_Time.git
   ```
2. **Navigate to the project folder**:
   ```bash
   cd Data-Driven_Analysis_of_the_Popularity_of_Different_Programming_Languages_over_Time.git
   ```
3. **Run the Python script**:
   Ensure the data file (`QueryResults.csv`) is available in the directory and run the script to explore the dataset:
   ```bash
   python analyse_popularity.py
   ```

## Script Breakdown

### 1. Data Exploration
The script starts by loading the dataset into a Pandas DataFrame and inspecting its structure (first/last rows, number of rows, and columns).

### 2. Data Cleaning
The date column (`DATE`) is converted to a `datetime` object for easier manipulation. NaN values (missing data) are filled with `0` to avoid issues during visualization.

### 3. Data Reshaping
The dataset is reshaped using the `.pivot()` method to create a table where each language has its own column, making it easier to visualize trends.

### 4. Data Visualization
Using Matplotlib, the script generates various plots to visualize the number of posts over time:
- Single language analysis (e.g., Python or Java).
- Comparison of multiple languages on the same chart.
- Rolling averages to smooth noisy time-series data for better trend observation.

### 5. Plot Customization
Chart aesthetics such as font size, axis labels, and chart size are modified for better readability.

### 6. Rolling Mean
Time series data can fluctuate significantly, so the script also includes rolling mean calculations to help visualize longer-term trends for each language.

## Example Output
![Python Popularity](https://github.com/NoorMahammad-S/Data-Driven_Analysis_of_the_Popularity_of_Different_Programming_Languages_over_Time/blob/master/Images/Python%20Popularity.png)

## Customizing the Script
- **Data Source**: You can replace the provided `.csv` file with fresh data by running an SQL query directly on Stack Exchange.
- **Languages**: Modify the list of languages to focus on different sets of programming languages by filtering or adding new tags.

## Future Improvements
- Fetch live data from Stack Exchange API.
- Add more advanced statistical analyses.
- Interactive visualizations using Plotly or Bokeh.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
