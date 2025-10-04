
# IPL Data Analysis

Welcome to the IPL Data Analysis repository! This project is focused on analyzing data from the Indian Premier League (IPL) to uncover interesting insights, trends, and statistics using data science techniques.

## Features

- Data cleaning and preprocessing of IPL datasets
- Exploratory Data Analysis (EDA) on match and player statistics
- Visualizations using Python libraries (Matplotlib, Seaborn, etc.)
- Insights about teams, players, venues, and match outcomes
- Example Jupyter notebooks for step-by-step analysis
- **Streamlit web app** for interactive data exploration (link available in the repository description)

## Dataset Files

The repository includes two key dataset files required for analysis and testing the Streamlit app:
- `matches.csv` – Contains information about each IPL match, including teams, venue, and results.
- `deliveries.csv` – Contains ball-by-ball delivery details for every match.

Make sure both files are present in the `data/` directory before running the app or notebooks.

## Getting Started

### Prerequisites

- Python 3.7 or above
- Recommended: [Anaconda](https://www.anaconda.com/products/distribution) for easy package management
- Required Python packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - jupyter
  - streamlit

Install required packages with:

```bash
pip install pandas numpy matplotlib seaborn jupyter streamlit
````

### Clone the repository

```bash
git clone https://github.com/ErAkhileshSingh/ipl-data-analysis.git
cd ipl-data-analysis
```

### Running the Analysis

Open the Jupyter notebooks in the `notebooks/` directory to explore the data analysis workflow:

```bash
jupyter notebook
```

To launch the Streamlit app for interactive visualizations:

```bash
streamlit run app.py
```

## Data Sources

* IPL match, player, and team statistics sourced from [official IPL website](https://www.iplt20.com/) and public datasets (e.g., Kaggle).

## Project Structure

```
ipl-data-analysis/
├── data/           # Raw and processed IPL data files (matches.csv, deliveries.csv)
├── notebooks/      # Jupyter notebooks for analysis
├── scripts/        # Python scripts for data processing
├── app.py          # Streamlit application file
├── README.md       # Project documentation
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, improvements, or new analyses.

## License

This project is licensed under the MIT License.

## Author

Maintained by [ErAkhileshSingh](https://github.com/ErAkhileshSingh)

---

**Feel free to explore, analyze, and test the Streamlit app using `matches.csv` and `deliveries.csv` available in this repository!**

