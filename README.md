# InvestIQ

This repository contains InvestIQ, a Python-based stock recommendation system that analyzes financial data and identifies the best stocks based on predefined criteria.

## Features

- Fetch financial data for various stocks.
- Analyze multiple financial metrics to rank stocks.
- Flexible scoring system for determining the "best" stock.
- Supports easy customization and extension.

## Installation

### Prerequisites

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) (for managing dependencies and virtual environments)

### Installing Poetry

If you don't have Poetry installed, follow these steps:

1. **Install Poetry:**

   You can install Poetry using the following command:

   ```bash
   pip install poetry
   ```
2. **Verify Installation:**

   You can verify the installation by running the following command:

   ```bash
   poetry --version
   ```
### Install Dependencies:**

   You can install the project dependencies by running the following command:

   ```bash
   poetry install
   ```
### Running the Project:**

   You can run the project by executing the following command:

   ```bash
   poetry run python app.py --stock_symbols "AAPL,GOOGL,MSFT"
   ```
