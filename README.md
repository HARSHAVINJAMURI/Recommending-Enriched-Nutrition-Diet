# Recommending Enriched Nutrition Diet

**Health is Wealth**

## Overview

The "Recommending Enriched Nutrition Diet" project is a web-based application designed to provide users with personalized diet recommendations. By inputting specific health parameters, users receive tailored nutrition plans to enhance their well-being.

## Features

- **Personalized Diet Plans**: Users receive diet suggestions based on their individual health metrics.
- **BMI Calculation**: The application calculates the Body Mass Index (BMI) to assess weight categories.
- **Health Issue-Based Recommendations**: Offers dietary advice tailored to specific health concerns.

## Installation

To set up the application locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HARSHAVINJAMURI/Recommending-Enriched-Nutrition-Diet.git
   cd Recommending-Enriched-Nutrition-Diet
2. **Set Up a Virtual Environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   
## Usage
1. Run the Application:
   ```bash
   python app.py
    ```
2. Access the Web Interface: Open your browser and navigate to http://127.0.0.1:5000/ to interact with the application.

## Requirements
- The application relies on the following Python packages:

  - Flask==2.2.5
  - pandas==2.0.3
  - openpyxl==3.1.2
  - numpy==1.24.3
- These are specified in the requirements.txt file.

## Tech Stack
- Frontend: HTML
- Backend: Python (Flask)
- Data Processing: pandas, numpy
- Data Storage: Excel files (dataset.xlsx, dataset0.xlsx)
  
## Project Structure
Recommending-Enriched-Nutrition-Diet/
```bash
- ├── app.py
- ├── dataset.xlsx
- ├── dataset0.xlsx
- ├── index.html
- ├── index1.html
- ├── index2.html
- ├── index3.html
- ├── requirements.txt
- ├── result.html
- └── result0.html
```
- app.py: Main application file containing the Flask server and route definitions.
- dataset.xlsx & dataset0.xlsx: Datasets containing nutritional information.
- index.html and other HTML files: Frontend templates for various pages.
- requirements.txt: List of required Python packages.

## Future Enhancements
- User Authentication: Implement user login and profile management.
- Expanded Database: Incorporate a broader range of health conditions and dietary recommendations.
- Interactive Features: Add charts and visualizations for better user engagement.
## Contributing
- Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## License
- This project is open-source and available for free.
