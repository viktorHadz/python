Student Survey Report Generator
A Python tool that transforms student survey data into professional, publication-ready reports with charts and insights.
What it does
Takes a CSV file of student survey responses and automatically generates:

A comprehensive Word document with charts for each question
Professional formatting with color-coded categories
Data tables with counts and percentages
Visual charts (bar/horizontal based on response length)
Executive summary and insights

Perfect for academic institutions analyzing student feedback, transitions, or satisfaction surveys.
Quick Start
bash# Clone and setup
git clone https://github.com/viktorHadz/python.git
cd python
pip install pandas matplotlib python-docx

# Run with your survey data
python survey_report_generator.py
Make sure your CSV file is named transitions.csv or update the file path in the script.
What makes it special

Smart chart selection: Automatically chooses horizontal/vertical charts based on response length
Categorized analysis: Groups related questions together (Demographics, Academic Skills, etc.)
Professional styling: Uses academic color palette and consistent formatting
Configurable: Easy to adjust colors, categories, and styling via survey_config.py

Example Output
The tool generates reports like this:

Executive summary with key statistics
Questions grouped by category (Course Background, Learning Preferences, etc.)
Each question gets a data table + chart + key insights
Professional Word document ready for sharing

Built with

Python 3.8+
pandas for data processing
matplotlib for charts
python-docx for Word document generation

Why I built this
Created this while working on student experience analysis. Got tired of manually creating charts and formatting reports, so I automated the whole process. Now it takes seconds instead of hours to generate professional survey reports.

Part of my Python portfolio - feel free to check out my other projects!
