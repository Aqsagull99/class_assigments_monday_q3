# Enhanced Personal Finance Tracker with Budgeting and Reporting

A comprehensive command-line personal finance tracker with budgeting, reporting, and data export capabilities.

## New Features

### 1. Budget Management System
- Set spending limits for categories
- Track budget utilization with color-coded warnings
- View remaining budget amounts

### 2. Advanced Transaction Filtering
- Filter by transaction type (income/expense)
- Filter by category
- View recent transactions (last 7 days)

### 3. Reporting Features
- Generate monthly financial reports
- View spending by category
- See income vs. expense breakdowns

### 4. Data Export
- Export all transactions to CSV format
- Easy import into spreadsheets or other tools

### 5. Enhanced Error Handling
- Better input validation
- Graceful error recovery
- Clear error messages

## Color Coding System

The application now includes additional color codes for budget tracking:

- **Budget Status**:
  - Safe (<70% used): Green
  - Warning (70-90% used): Yellow
  - Danger (>90% used): Red

- **New UI Elements**:
  - Warning messages: Bright Yellow
  - Budget displays: Contextual colors
  - Report headers: Special formatting

## How to Use the New Features

### Setting Up Budgets
1. Go to "Budget Management" in the main menu
2. Choose "Add New Budget"
3. Enter category name and spending limit

### Generating Reports
1. Go to "Generate Reports" in the main menu
2. Select report type (monthly or recent transactions)
3. For monthly reports, enter year and month

### Exporting Data
1. Go to "Export Data" in the main menu
2. Enter filename (or press Enter for default)
3. Data will be saved as CSV

## Requirements

- Python 3.11.9
- colorama library (`pip install colorama`)

## Running the Application

```bash
python finance_tracker.py
