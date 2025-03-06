# Car Advertisement Data Analysis App

This is a Streamlit web application that provides an interactive analysis of car advertisement data, specifically using the `vehicles_us.csv` dataset. The application allows users to explore the distribution of car prices, and the relationship between price and mileage, along with the condition of the car.

## Features

*   **Data Loading and Preprocessing:**
    *   Loads the `vehicles_us.csv` dataset.
    *   Handles missing values in `paint_color`, `is_4wd`, `model_year`, and `cylinders` columns.
    *   Converts the `is_4wd`, `model_year` and `cylinders` columns to appropriate data types.
*   **Price Filtering:**
    *   A checkbox allows users to filter the data to show only cars priced under $50,000.
*   **Price Distribution Histogram:**
    *   Displays a histogram visualizing the distribution of car prices, with the option to filter based on the price checkbox.
*   **Price vs. Mileage Scatterplot:**
    *   Displays a scatterplot showing the relationship between car price and mileage.
    *   The scatterplot's points are colored by the car's condition.
    *   Can be filtered based on the price checkbox.
* **Clear Chart labels**: the charts have their axis labeled.

## Getting Started

### Prerequisites

*   Python 3.7+
*   Libraries: `streamlit`, `pandas`, `plotly`

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Vearanos/Caradvertisement.git
    cd Caradvertisement
    ```

2.  **Install the required packages:**
    ```bash
    pip install streamlit pandas plotly
    ```

### Running the App

1.  **Navigate to the directory:**
    ```bash
    cd Caradvertisement
    ```
2.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
3.  This command will start a local server and open the app in your default web browser.

### Data

*   The app uses the `vehicles_us.csv` file, which should be in the same directory as `app.py`.

## Usage

Once the app is running in your browser, you can:

*   **Filter by Price:** Check the box to filter the data and visualizations to only show cars priced under $50,000.
*   **View Price Distribution:** Examine the histogram to see how car prices are distributed.
*   **Explore Price vs. Mileage:** Use the scatterplot to analyze the relationship between a car's price and its mileage, taking into account the condition of the car.

## Contributing

Contributions to this project are welcome! If you'd like to contribute:

1.  Fork the repository.
2.  Create a new branch for your changes.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## Author

Chase Summerhays
[https://github.com/Vearanos/Caradvertisement.git]
