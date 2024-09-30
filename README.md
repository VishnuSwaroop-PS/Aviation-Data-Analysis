# Aviation Data Analysis Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Project Structure](#project-structure)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Data Processing Pipeline](#data-processing-pipeline)
8. [Web Interface](#web-interface)
9. [Analysis and Insights](#analysis-and-insights)
10. [Contributing](#contributing)
11. [License](#license)

## Project Overview

This Aviation Data Analysis project is designed to process, analyze, and visualize flight delay data. It provides insights into various factors affecting flight delays, including airlines, days of the week, and departure times. The project includes a data processing pipeline, a MySQL database for storage, and a Flask web application for displaying the analysis results.

## Features

- Data cleaning and preprocessing of raw aviation data
- MySQL database integration for efficient data storage and retrieval
- Comprehensive data analysis using Python (pandas, matplotlib, seaborn)
- Interactive web interface built with Flask and Tailwind CSS
- Visualizations including histograms, box plots, and bar charts
- Statistical analysis (ANOVA) to compare delays across airlines

## Tech Stack

- Python 3.7+
- Flask
- MySQL
- Pandas
- Matplotlib
- Seaborn
- Tailwind CSS
- Node.js (for Tailwind CSS processing)

## Project Structure

```
Aviation Data Analysis/
│
├── .venv/                   # Virtual environment directory
├── node_modules/            # Node.js modules (for Tailwind CSS)
├── plots/                   # Directory to store generated plots
├── templates/
│   └── index.html           # HTML template for the Flask app
├── .gitignore
├── app.py                   # Main Flask application
├── aviation_data.csv        # Raw input data
├── cleaned_flight_data.csv  # Cleaned data output
├── create_db.py             # Script to create MySQL database
├── data_analysis.py         # Data analysis and plot generation script
├── load_csv_into_mysql.py   # Script to load data into MySQL
├── package-lock.json        # Node.js package lock file
├── package.json             # Node.js package file
├── processing_aviation_data.py  # Data cleaning and preprocessing script
├── requirements.txt         # Python dependencies
└── tailwind.config.js       # Tailwind CSS configuration
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/VishnuSwaroop-PS/Aviation-Data-Analysis.git
   cd aviation-data-analysis
   ```

2. Set up a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up MySQL:
   - Ensure MySQL Server is installed and running
   - Update the MySQL connection details in `create_db.py`, `load_csv_into_mysql.py`, and `data_analysis.py` if necessary

5. (Optional) Install Node.js dependencies for Tailwind CSS:
   ```
   npm install
   ```

## Usage

1. Process the raw data:
   ```
   python processing_aviation_data.py
   ```

2. Create the MySQL database:
   ```
   python create_db.py
   ```

3. Load the cleaned data into MySQL:
   ```
   python load_csv_into_mysql.py
   ```

4. Generate analysis plots:
   ```
   python data_analysis.py
   ```

5. Run the Flask application:
   ```
   python app.py
   ```

6. Open a web browser and navigate to `http://localhost:5000` to view the analysis dashboard.

## Data Processing Pipeline

1. `processing_aviation_data.py`: Cleans and preprocesses the raw data from `aviation_data.csv`, producing `cleaned_flight_data.csv`.
2. `create_db.py`: Sets up the MySQL database schema.
3. `load_csv_into_mysql.py`: Loads the cleaned data into the MySQL database.
4. `data_analysis.py`: Performs data analysis and generates visualizations.

## Web Interface

The Flask application (`app.py`) serves a web interface that displays various visualizations and insights derived from the aviation data. The interface is styled using Tailwind CSS for a responsive and modern design.

## Analysis and Insights

The project provides several key insights into flight delays:

- Distribution of flight delays
- Average delays by day of the week
- Comparison of delays across airlines
- Correlation between departure time and delay duration
- Statistical analysis of delay differences between airlines

For detailed explanations of each visualization, refer to the comments in the `index.html` template.

## Contributing

Contributions to this project are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Create a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

For any questions or issues, please open an issue on the GitHub repository.
