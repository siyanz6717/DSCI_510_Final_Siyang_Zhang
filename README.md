# Analyzing the Disparity Between Cost of Living and Quality of Life

## Team Members
* **Name**: Siyang Zhang
* **USC Email**: szhang19@usc.edu
* **USC ID**: 9033653228
* **GitHub Username**: siyanz6717

## Project Overview
In the post-pandemic era, the decoupling of work and location has led to a surge in digital nomadism, prompting individuals to seek locations that offer high living standards at a reasonable cost. However, a higher cost of living does not necessarily guarantee a superior quality of life. This project aims to solve the problem of identifying "undervalued" cities—locations where the quality of life exceeds what the cost of living would quantitatively predict.

We collect data by scraping **Numbeo.com**, extracting indices for Cost of Living, Rent, Safety, Healthcare, and Pollution for 285 cities. By merging and analyzing these datasets, we calculate a custom "Geo-Arbitrage Score" to rank global cities based on their value proposition. The analysis also includes regional segmentation and outlier detection to investigate whether expensive cities are inherently safer or better to live in.

## Project Structure
```
DSCI_510_Final_Siyang_Zhang/
├── README.md
├── requirements.txt
├── data/
  ├── processed/
  └── raw/
├── project_proposal.pdf
├── results/
  ├── analysis_summary.txt
  ├── bar_top_10_value.png
  ├── heatmap_correlation.png
  ├── scatter_cost_quality.png
  └── final_report.pdf
└── src/
  ├── clean_data.py
  ├── get_data.py
  ├── run_analysis.py
  ├── utils/
  └── visualize_results.ipynb
```

## Installation, Setup, and Execution

### Prerequisites
Ensure you have `Python 3.8+` installed as well as the libraries in `requirement.txt`.

### Create a Virtual Environment
Run the following command in your terminal to create a virtual environment named `venv`:

```bash
python3 -m venv venv
```

### Install Required Libraries
Once the virtual environment is activated, install all external libraries (`Requests`, `BeautifulSoup`, `Pandas`, `Matplotlib`, `Seaborn`) using the requirements file.

### Create folders using the same structure in the repo
You will need to create the same directory as the repo does in order to run the script.

### Run the script
Run the script in order of `get_daya.py`, `clean_data.py`, `run_analysis.py`, `visualize_results.ipynb` using `CMD` or `Git Bash`.

#### Data Collection
Run the scraper to fetch raw data from Numbeo using `CMD` or `Git Bash`. 

```Bash
python src/get_data.py
```

#### Data Cleaning
Run the cleaning script to process the raw files using `CMD` or `Git Bash`.

```Bash
python src/clean_data.py
```

#### Analysis
Run the analysis script to calculate the "Geo-Arbitrage Score" and perform statistical analyses using `CMD` or `Git Bash`.

```Bash
python src/run_analysis.py
```
#### Visualization
Run the visualization script to generate charts using `CMD` or `Git Bash`. 
```Bash
python src/visualize_results.py
```

### Results
After running the code, you can check results in `results` folder.



