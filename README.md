# Options Lifecycle Reconciliation & Break Analysis (Simulated OCC/CDCC Workflow)

This project simulates the daily operational workflows performed in an Options Clearing team, including reconciliation of expected vs actual positions, break identification, expiration processing, and assignment logic. It mirrors the accuracy‑critical tasks carried out in brokerage operations, where every position must match what it should and discrepancies must be caught before they impact clients.

The goal of this project is to demonstrate how operational analysts protect client assets by ensuring the integrity of the options book, resolving breaks early, and improving the processes that support daily clearing activities.

---

## Key Features

### **Reconciliation**
- Compare expected vs actual option positions  
- Identify quantity mismatches (“breaks”)  
- Quantify break amounts and isolate root causes  

### **Break Analysis**
- Automated break detection using SQL and Python  
- Summary statistics for break patterns  
- Manual review model in Excel with conditional formatting  

### **Expiration Processing**
- Determine which contracts expired vs remained active  
- Join position data with expiration records  
- Prepare data for settlement and post‑expiration workflows  

### **Assignment Handling**
- Simulate OCC/CDCC assignment events  
- Adjust quantities based on assignment records  
- Validate updated positions  

### **Tools Used**
- **SQL** for validation, joins, and discrepancy detection  
- **Python** for automated reconciliation and break analysis  
- **Excel** for manual review, pivot tables, and reconciliation modeling  

---

---

## Data Overview

### **positions_expected.csv**
Expected option positions before reconciliation.

### **positions_actual.csv**
Actual positions pulled from a simulated clearing system.

### **expirations.csv**
Indicates which contracts expired on the cycle date.

### **assignments.csv**
Simulated OCC/CDCC assignment events.

These datasets are intentionally small for demonstration purposes but structured to reflect real operational workflows.

---

## SQL Queries

### **reconcile_positions.sql**
Compares expected vs actual quantities and calculates break amounts.

### **find_breaks.sql**
Filters reconciliation results to show only mismatches.

### **expiration_processing.sql**
Joins positions with expiration status for lifecycle processing.

---

## Python Scripts

### **reconcile.py**
Automates reconciliation and prints break results.

### **expiration_logic.py**
Processes expiration data and merges it with positions.

### **break_analysis.py**
Provides summary statistics for break patterns.

---

## Excel Reconciliation Model

The Excel workbook includes:
- Pivot tables comparing expected vs actual quantities  
- Conditional formatting to highlight breaks  
- Tabs for reconciliation, expirations, and assignments  
- A manual review workflow similar to real clearing processes  

This mirrors how many brokerage operations teams validate data before settlement.

---

## Purpose of This Project

This project was created to demonstrate the core skills required in an Options Clearing role:

- Accuracy and attention to detail  
- Comfort working with large datasets  
- Curiosity when something “looks off”  
- Early escalation of discrepancies  
- Clear documentation of operational workflows  
- Ability to reconcile multi‑source data  
- Understanding of the options lifecycle (expiration, assignment, reconciliation)

It reflects how operational analysts protect client assets by ensuring the options book is accurate and breaks are resolved before they reach clients.

---

## How to Run

### **1. Load the datasets**
All CSV files are located in `/data`.

### **2. Run Python scripts**

## Project Structure


### **3. Review SQL queries**
Open the `.sql` files in any SQL editor.

### **4. Explore the Excel model**
Open `excel/reconciliation_model.xlsx` to manually review breaks.

---

## Suggested GitHub Topics
Add these to your repo for visibility:

`options-clearing`  
`reconciliation`  
`sql`  
`python`  
`operations`  
`brokerage`  
`data-validation`  
`financial-operations`  

---

## Contact
Created by **Mandie Dunwoody**  
For demonstration of operational accuracy, reconciliation workflows, and options lifecycle understanding.

