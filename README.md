# Student Survey Report Generator

A Python tool that transforms survey csv data for students who've just joined university into a reports with charts and insights.

## What it does

Takes a CSV file of student survey responses and automatically generates:
- A comprehensive Word document with charts for each question
- Professional formatting with color-coded categories
- Data tables with counts and percentages
- Smart Visual charts (bar/horizontal based on response length)
- Executive summary and insights

Perfect for academic institutions analyzing student feedback, transitions, or satisfaction surveys.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/viktorHadz/python.git
cd python
pip3 install pandas matplotlib python-docx

# Run with your survey data
python3 survey_report_generator.py
```

Make sure your CSV file is named `transitions.csv` or update the file path in the script.

## Features at a Glance

 **Smart Automation**: Detects response types and chooses optimal chart formats  
 **Professional Output**: Publication-ready Word documents with consistent styling  
 **Academic Design**: Color-coded categories with professional formatting  
 **Highly Configurable**: Easy customization of colors, categories, and layouts  
 **Comprehensive Analysis**: Data tables, charts, and insights for every question  

## Sample Output Preview

Here's what you get:
```
Enhanced_Survey_Report.docx
├── Executive Summary (response counts, key highlights)
├── Course & Academic Background (6 questions analyzed)
├── Learning & Assessment Preferences (7 questions analyzed)  
├── Transition Concerns (7 questions analyzed)
├── Demographics (6 questions analyzed)
└── Support & Services (2 questions analyzed)
```

Each section includes data tables, professional charts, and key insights automatically generated.

## Built with

- **Python 3.8+** (tested on Linux/Pop!_OS)
- **pandas** for data processing
- **matplotlib** for charts
- **python-docx** for Word document generation

## Development Environment

Developed and tested on Pop!_OS (Ubuntu-based) using Python 3. Should work on any Linux distro or system with Python 3.8+.

## Why I built this

Created this while working on student experience analysis. Got tired of manually creating charts and formatting reports in excel and word, so I automated the whole process. Now it takes seconds instead of hours to generate professional survey reports :D

---

*Part of my Python portfolio - feel free to check out my other projects!*
