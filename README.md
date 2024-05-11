# Seminar


# Installation

## Requirements

- Python 3.10+

## Installation

To install the requirements:
```
pip install -r requirements.txt
```


# Project Structure

The project is structured as follows:

- root/: Contains core project files.
  - `.gitignore`: Configuration file to instruct Git on which files to ignore.
  - `README.md`: Project description and instructions.
  - `main_dtw_erp.py`: Script for ERP/DTW testing of CSV files from `./data/`.
  - `main_twed.ipynb`: Jupyter notebook for testing TWED coding.
  - `utils.py`: Utility functions used throughout the project.

- src/: Contains the main source files of the project.
  - `DTW_Code.py`: Functions for Dynamic Time Warping (DTW) algorithms.
  - `ERP_Code.py`: Functions for Edit Distance with Real Penalty (ERP) algorithms.

- tests/: Contains test scripts for the project.
  - `main_tester.py`: Main test script to run tests on the project’s functionalities.

- data/: Contains dataset files used in the project.
  - `serie_A.csv`: Time-series data for series A.
  - `serie_B.csv`: Time-series data for series B.
