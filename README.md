# Analyzing the Disparity Between Cost of Living and Quality of Life

## Team Members
* **Name**: Siyang Zhang
* **USC Email**: szhang19@usc.edu
* **USC ID**: 9033653228
* **GitHub Username**: siyanz6717

## Project Overview
In the post-pandemic era, the decoupling of work and location has led to a surge in digital nomadism, prompting individuals to seek locations that offer high living standards at a reasonable cost. However, a higher cost of living does not necessarily guarantee a superior quality of life. This project aims to solve the problem of identifying "undervalued" cities—locations where the quality of life exceeds what the cost of living would quantitatively predict.

We collect data by scraping **Numbeo.com**, extracting indices for Cost of Living, Rent, Safety, Healthcare, and Pollution for over 500 cities. By merging and analyzing these datasets, we calculate a custom "Geo-Arbitrage Score" to rank global cities based on their value proposition. The analysis also includes regional segmentation and outlier detection to investigate whether expensive cities are inherently safer or better to live in.

## Project Structure
This repository relies on a standard structure where the source code is located in the `src/` directory, and data is managed in the `data/` directory. The `data/raw/` folder contains the initial scraped HTML or CSV files from Numbeo, while `data/processed/` contains the cleaned and merged datasets ready for analysis. The `results/` folder holds the generated visualizations (plots) and the final report.

## Installation and Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed. You will need to create a virtual environment to manage dependencies and avoid conflicts with your system Python.

### 2. Create a Virtual Environment
Run the following command in your terminal to create a virtual environment named `venv`:

```bash
python3 -m venv venv
