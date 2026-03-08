# Excel Formula Generator Prompts

## Module 07: AI for Daily Productivity — Code and Examples

---

A comprehensive collection of 50+ prompts for generating Excel formulas, Google Sheets functions, VBA macros, and Google Apps Script. Organized by category for quick reference.

---

## How to Use These Prompts

1. Copy the prompt
2. Replace the bracketed `[PLACEHOLDER]` values with your actual data references
3. Paste into your AI tool (ChatGPT, Claude, Gemini, etc.)
4. Test the generated formula with your data
5. Ask follow-up questions if the formula needs adjustment

---

## Category 1: Lookup and Reference (Prompts 1-8)

### Prompt 1: Basic VLOOKUP

```
Write an Excel VLOOKUP formula.

Lookup value: Cell [A2]
Table array: Sheet "[SHEET NAME]", range [A:D]
Return column: [3] (third column of the table)
Match type: Exact match

Also provide the XLOOKUP alternative if using Excel 365.
Explain the difference and when to prefer each.
```

### Prompt 2: INDEX-MATCH (Two-Way Lookup)

```
Write an INDEX-MATCH formula for a two-way lookup.

I need to find a value at the intersection of:
- Row identifier: [VALUE IN CELL A1] — matched against Column [A]
- Column identifier: [VALUE IN CELL B1] — matched against Row [1]
- Data range: [B2:Z100]

The formula should work even if rows or columns are reordered.
```

### Prompt 3: XLOOKUP with Multiple Criteria

```
Write an XLOOKUP formula that matches on multiple criteria.

I need to find the value where:
- Column A matches [CRITERIA 1]
- Column B matches [CRITERIA 2]

Return the value from Column [C].
Data range: rows 2 to 1000.

If Excel 365 XLOOKUP is not available, provide a
SUMPRODUCT or INDEX-MATCH-MATCH alternative.
```

### Prompt 4: Fuzzy Match / Approximate Lookup

```
Write a formula to find the closest match (not exact).

Lookup value: [CELL REFERENCE] (a number)
Lookup range: [COLUMN REFERENCE] (sorted ascending)
Return column: [COLUMN REFERENCE]

I need the closest value that does NOT exceed my lookup value.
Explain how approximate match works in VLOOKUP vs XLOOKUP.
```

### Prompt 5: Reverse VLOOKUP (Lookup Left)

```
I need to look up a value in Column [D] and return the
corresponding value from Column [A] (which is to the LEFT
of the lookup column).

VLOOKUP cannot look left. Provide solutions using:
1. INDEX-MATCH
2. XLOOKUP
3. CHOOSE (workaround for older Excel versions)
```

### Prompt 6: Multiple Results from Lookup

```
I have a list where Column A has a category and Column B has values.
Some categories appear multiple times.

Write a formula that returns ALL values from Column B where
Column A equals [CRITERIA].

List the results vertically starting in cell [D2].
Provide solutions for:
1. Excel 365 (using FILTER function)
2. Older Excel (using SMALL + IF array formula)
```

### Prompt 7: Cross-Workbook Reference

```
Write a formula that references data from another workbook.

Source workbook: [FILENAME.xlsx]
Source sheet: [SHEET NAME]
Source range: [RANGE]
Currently: [OPEN / CLOSED] (this affects the formula syntax)

I need to pull [DESCRIBE WHAT DATA] from the source workbook
into my current workbook at cell [CELL REFERENCE].
```

### Prompt 8: Dynamic Array SORT and FILTER

```
Write Excel 365 dynamic array formulas to:
1. FILTER Column [A:C] where Column [B] equals [CRITERIA]
2. SORT the filtered results by Column [C] descending
3. Return only UNIQUE values from the result
4. Combine all three into a single formula

Data range: [A2:C500]
```

---

## Category 2: Conditional Aggregation (Prompts 9-16)

### Prompt 9: SUMIFS with Multiple Conditions

```
Write a SUMIFS formula to sum Column [E] where:
- Column [A] equals [VALUE1]
- Column [B] is greater than [VALUE2]
- Column [C] contains the text "[PARTIAL TEXT]"
- Column [D] is between [DATE1] and [DATE2]

Data range: rows 2 to [LAST ROW].
```

### Prompt 10: COUNTIFS with Date Ranges

```
Write a COUNTIFS formula to count records where:
- Date column [A] is within the current month
- Status column [B] is not "Cancelled"

The formula should automatically use the current month
without me updating it manually.
```

### Prompt 11: AVERAGEIFS

```
Write an AVERAGEIFS formula to calculate the average of Column [D]
where:
- Column [A] is "[CATEGORY]"
- Column [B] is not blank
- Column [C] is greater than [MINIMUM VALUE]

Data range: rows 2 to 5000.
```

### Prompt 12: MAXIFS and MINIFS

```
Write formulas to find:
1. The highest value in Column [D] where Column [A] = "[CATEGORY]"
2. The lowest value in Column [D] where Column [A] = "[CATEGORY]"
3. The date (Column [B]) when the maximum occurred

For Excel versions without MAXIFS/MINIFS, provide alternatives.
```

### Prompt 13: Conditional Sum with OR Logic

```
Write a formula to sum Column [E] where Column [A] equals
EITHER "[VALUE1]" OR "[VALUE2]" OR "[VALUE3]".

SUMIFS uses AND logic by default. Show me how to use OR logic with:
1. SUMPRODUCT approach
2. Multiple SUMIFS added together
3. SUM with IF array formula
```

### Prompt 14: Running Total / Cumulative Sum

```
Write a formula for a running total (cumulative sum) in Column [C].

Values to sum are in Column [B], starting at B2.
The formula in C2 should show the sum of B2.
The formula in C3 should show the sum of B2:B3.
And so on.

Make the formula copiable down the column.
Also provide a version that resets the running total when
Column [A] (category) changes.
```

### Prompt 15: Weighted Average

```
Write a formula for a weighted average.

Values are in Column [B] (e.g., grades: 85, 92, 78).
Weights are in Column [C] (e.g., weight: 30%, 40%, 30%).
Data range: rows 2 to [LAST ROW].

Use SUMPRODUCT for this calculation.
Also handle the case where weights do not sum to 100%.
```

### Prompt 16: Percentile and Rank

```
Write formulas to:
1. Find the 90th percentile of values in Column [B]
2. Rank each value in Column [B] (1 = highest)
3. Calculate the percentile rank of each value
4. Find the median of Column [B] where Column [A] = "[CATEGORY]"

Data range: B2:B[LAST ROW].
```

---

## Category 3: Text Manipulation (Prompts 17-24)

### Prompt 17: Extract Parts of a Name

```
Column A has full names in the format "[FIRST] [LAST]".
Some have middle names: "[FIRST] [MIDDLE] [LAST]".

Write formulas to extract:
- First name into Column B
- Last name into Column C
- Middle name into Column D (blank if none)

Handle edge cases: single names, names with suffixes (Jr., III).
```

### Prompt 18: Email Address Generator

```
Column A: First Name
Column B: Last Name
Column C: Company Domain (e.g., "company.com")

Write formulas to generate email addresses in these formats:
1. first.last@domain.com (Column D)
2. firstinitiallast@domain.com (Column E)
3. first@domain.com (Column F)

Convert all to lowercase. Handle names with spaces or special characters.
```

### Prompt 19: Phone Number Formatting

```
Column A has phone numbers in inconsistent formats:
- "1234567890"
- "(123) 456-7890"
- "123-456-7890"
- "+1 123 456 7890"

Write a formula that standardizes ALL these to "(123) 456-7890" format.
Handle international prefixes (strip +1).
```

### Prompt 20: Text Extraction with REGEX (Google Sheets)

```
Write Google Sheets REGEXEXTRACT formulas to extract:

1. All numbers from a text string (e.g., "Order #12345 placed" → "12345")
2. Email address from a text block
3. URL from a text block
4. Date in any format from a text block
5. Dollar amount from a text (e.g., "Total: $1,234.56" → "1234.56")

Provide the REGEXEXTRACT formula with the appropriate regex pattern.
```

### Prompt 21: Data Cleaning — Standardize Text

```
Write formulas to clean messy text data:

1. Remove all extra spaces (multiple spaces to single): Column [A]
2. Remove non-printable characters: Column [A]
3. Standardize capitalization to Proper Case: Column [A]
4. Remove leading/trailing spaces: Column [A]
5. Replace line breaks with spaces: Column [A]
6. Remove all special characters (keep only letters, numbers, spaces): Column [A]

Combine all cleaning steps into a single nested formula.
```

### Prompt 22: Split Delimited Text

```
Column A contains comma-separated values:
Example: "apple, banana, cherry, date"

Write formulas to split these into separate columns:
- Column B: First item
- Column C: Second item
- Column D: Third item
- etc.

Provide solutions for:
1. Fixed number of items
2. Variable number of items (using TEXTSPLIT in Excel 365)
3. Google Sheets equivalent
```

### Prompt 23: Concatenation with Conditions

```
Combine values from multiple columns into one cell:

Column A: First Name
Column B: Middle Name (sometimes blank)
Column C: Last Name
Column D: Suffix (sometimes blank)

Result format: "Last, First Middle Suffix"
Skip blank fields gracefully (no extra spaces or commas).

Provide solutions using:
1. CONCATENATE
2. TEXTJOIN (Excel 365)
3. Ampersand (&) operator
```

### Prompt 24: Find and Replace with Formulas

```
Column A has product codes like "PROD-2024-001-NA".

Write formulas to:
1. Replace "NA" with "North America" in the code
2. Replace the year portion with the current year
3. Increment the sequence number by 1
4. Extract each segment into separate columns
```

---

## Category 4: Date and Time (Prompts 25-32)

### Prompt 25: Business Days Calculations

```
Write formulas to:
1. Calculate business days between [START DATE] and [END DATE]
   (excluding weekends)
2. Same but also exclude holidays (holiday list in Column [H])
3. Add [N] business days to a date
4. Determine if a date is a business day

Use NETWORKDAYS and WORKDAY functions.
```

### Prompt 26: Age / Tenure Calculation

```
Column A: Date of Birth / Start Date
Column B: [TODAY or specific end date]

Write formulas to calculate:
1. Age/tenure in complete years
2. Age/tenure in years and months (e.g., "3 years, 7 months")
3. Age/tenure in total months
4. Age/tenure in total days
5. Next birthday/anniversary date
```

### Prompt 27: Date Grouping

```
Column A has dates. Write formulas to extract:
1. Year (Column B)
2. Quarter as "Q1", "Q2", etc. (Column C)
3. Month name (Column D)
4. Week number (Column E)
5. Day of week name (Column F)
6. Fiscal year (starting [MONTH]) (Column G)
7. Fiscal quarter (starting [MONTH]) (Column H)
```

### Prompt 28: Dynamic Date References

```
Write formulas (no hardcoded dates) for:
1. First day of current month
2. Last day of current month
3. First day of current quarter
4. Last day of current quarter
5. First day of current year
6. Same date last year
7. First Monday of current month
8. Last business day of previous month
```

### Prompt 29: Time Calculations

```
Column A: Start Time (format: HH:MM AM/PM)
Column B: End Time (format: HH:MM AM/PM)

Write formulas to:
1. Calculate duration in hours and minutes
2. Handle overnight shifts (end time < start time)
3. Calculate total hours worked per week (sum column)
4. Flag if overtime (>8 hours in a day or >40 hours in a week)
5. Calculate pay at [RATE] per hour with 1.5x for overtime
```

### Prompt 30: Date-Based Conditional Logic

```
Write formulas for a project tracker:

Column A: Task Name
Column B: Start Date
Column C: Due Date
Column D: Status (Not Started / In Progress / Complete)

Create formulas for:
1. Column E: Days remaining until due (negative if overdue)
2. Column F: Status indicator:
   - "Overdue" if past due and not complete
   - "Due Today" if due today
   - "Due This Week" if due within 7 days
   - "On Track" if due later
   - "Complete" if status is Complete
3. Column G: RAG status (Red/Amber/Green) based on above
```

### Prompt 31: Month-over-Month and Year-over-Year

```
I have monthly data:
Column A: Date (first of each month)
Column B: Revenue

Write formulas to calculate:
1. Month-over-Month change (absolute)
2. Month-over-Month change (percentage)
3. Year-over-Year change (same month last year)
4. 3-month moving average
5. 12-month rolling total
6. Best month ever (and which month it was)
```

### Prompt 32: Recurring Date Generation

```
Write formulas to generate a series of recurring dates:

Starting from: [START DATE]
Recurrence: [DAILY / WEEKLY / BIWEEKLY / MONTHLY / QUARTERLY / ANNUALLY]
Number of occurrences: [N]

Handle month-end dates correctly
(e.g., monthly from Jan 31 should go to Feb 28/29, not error).
Also generate:
- Every 2nd Tuesday
- Last Friday of each month
- First business day of each month
```

---

## Category 5: Financial Formulas (Prompts 33-38)

### Prompt 33: Loan Amortization

```
Create a complete loan amortization schedule in Excel.

Inputs:
- Loan amount: Cell [B1]
- Annual interest rate: Cell [B2]
- Loan term (years): Cell [B3]

Provide formulas for:
1. Monthly payment (PMT function)
2. For each month: Payment #, Payment Amount, Principal, Interest, Balance
3. Total interest paid over the life of the loan
4. Payoff date

Start the schedule at row 6 with headers in row 5.
```

### Prompt 34: Investment Growth

```
Write formulas to calculate:
1. Future value of [AMOUNT] invested for [YEARS] at [RATE] annually
2. Same but with monthly contributions of [AMOUNT]
3. How long until investment reaches [TARGET] at [RATE]
4. Required monthly contribution to reach [TARGET] in [YEARS] at [RATE]
5. Effective annual rate from a nominal rate with [N] compounding periods

Use FV, NPER, PMT, and RATE functions.
```

### Prompt 35: Break-Even Analysis

```
Create a break-even analysis spreadsheet:

Fixed costs: Cell [B1]
Variable cost per unit: Cell [B2]
Price per unit: Cell [B3]

Calculate:
1. Break-even quantity
2. Break-even revenue
3. Margin of safety (at [PROJECTED UNITS] sold)
4. Contribution margin per unit
5. Contribution margin ratio
6. Profit/loss at various volumes (create a data table: 100 to 10,000 units)
```

### Prompt 36: Depreciation Schedules

```
Write formulas for different depreciation methods:

Asset cost: [AMOUNT]
Salvage value: [AMOUNT]
Useful life: [YEARS]

Calculate annual depreciation using:
1. Straight-line (SLN function)
2. Double-declining balance (DDB function)
3. Sum-of-years digits (SYD function)
4. Units of production method

Create a schedule showing annual depreciation and book value for each method.
```

### Prompt 37: Currency Conversion

```
I have sales data in multiple currencies:
Column A: Amount
Column B: Currency code (USD, EUR, GBP, JPY, etc.)

Exchange rates are in a reference table on Sheet "Rates":
Column A: Currency code
Column B: Exchange rate to USD

Write a formula to convert all amounts to USD in Column C.
Handle missing exchange rates with an error message.
```

### Prompt 38: Percentage Calculations

```
Write formulas for common percentage calculations:

1. Percentage of total: [VALUE] as % of [TOTAL] in each row
2. Percentage change: From [OLD VALUE] to [NEW VALUE]
3. Markup percentage: Cost [C] to price [P]
4. Discount: Original price minus [X]% discount
5. Tax calculation: Subtotal + [TAX RATE]
6. Compound growth rate over [N] periods
7. Percentage contribution of each row to group total
   (grouped by Column [A])
```

---

## Category 6: Data Analysis (Prompts 39-44)

### Prompt 39: Pivot Table Alternative with Formulas

```
My data has:
Column A: Category
Column B: Subcategory
Column C: Date
Column D: Value

Create a formula-based summary table that shows:
- Rows: Each unique Category
- Columns: Each month
- Values: Sum of Value

Use SUMPRODUCT or SUMIFS to create this cross-tabulation.
Handle missing combinations with 0 instead of error.
```

### Prompt 40: Outlier Detection

```
Column [B] has numerical data (rows 2 to [LAST ROW]).

Write formulas to:
1. Calculate Q1 (25th percentile), Q3 (75th percentile), and IQR
2. Calculate lower fence (Q1 - 1.5*IQR) and upper fence (Q3 + 1.5*IQR)
3. Flag each row as "Outlier" or "Normal" in Column [C]
4. Count the number of outliers
5. Calculate mean and standard deviation WITH and WITHOUT outliers
```

### Prompt 41: Correlation and Trend

```
Column [B]: Independent variable (e.g., advertising spend)
Column [C]: Dependent variable (e.g., sales)
Rows 2 to [LAST ROW].

Write formulas to:
1. Calculate the Pearson correlation coefficient
2. Create a linear regression equation (slope and intercept)
3. Calculate R-squared (coefficient of determination)
4. Predict the dependent variable for a given independent value
5. Calculate the standard error of the regression
```

### Prompt 42: Frequency Distribution

```
Column [A] has numerical data (e.g., exam scores, 0-100).

Create a frequency distribution:
1. Define bins: 0-10, 11-20, 21-30, ..., 91-100
2. Count frequency in each bin using FREQUENCY function
3. Calculate percentage of total for each bin
4. Calculate cumulative frequency
5. Calculate cumulative percentage
6. Identify the mode and modal class
```

### Prompt 43: Pareto Analysis (80/20 Rule)

```
Column A: Category (e.g., product name)
Column B: Value (e.g., revenue)

Create a Pareto analysis:
1. Sort categories by value descending
2. Calculate cumulative sum
3. Calculate cumulative percentage
4. Identify which categories make up 80% of the total
5. Flag them as "Vital Few" (top 80%) vs "Trivial Many"
6. Count how many categories represent the Vital Few

Provide all formulas assuming data is already sorted.
```

### Prompt 44: Cohort Analysis

```
I have customer data:
Column A: Customer ID
Column B: First Purchase Date
Column C: Transaction Date
Column D: Transaction Amount

Create formulas for a monthly cohort analysis:
1. Assign each customer to a cohort based on their first purchase month
2. For each cohort, calculate:
   - Number of customers acquired
   - Retention rate by month (Month 1, Month 2, ..., Month 12)
   - Revenue per cohort per month
   - Average revenue per customer per cohort

Build the cohort table with months as columns and cohorts as rows.
```

---

## Category 7: VBA Macro Prompts (Prompts 45-50)

### Prompt 45: Data Cleaning Macro

```
Write a VBA macro that cleans data in the active sheet:

1. Remove all blank rows
2. Trim spaces from all text cells
3. Convert all text to proper case in Column [C]
4. Standardize date format to MM/DD/YYYY in Column [A]
5. Replace "N/A", "NA", "n/a", "#N/A" with empty cells
6. Remove duplicate rows based on Column [A]
7. Sort by Column [A] ascending
8. Auto-fit all column widths
9. Display a message box with count of rows cleaned/removed

Include error handling and a progress indicator.
```

### Prompt 46: Auto-Report Generator

```
Write a VBA macro that generates a formatted report:

Source data: Sheet "Data", columns A through [LAST COLUMN]
Report output: New sheet named "Report_[YYYY-MM-DD]"

The macro should:
1. Copy data to the new sheet
2. Create a summary section at the top with:
   - Total rows
   - Sum of Column [E]
   - Average of Column [E]
   - Count of unique values in Column [A]
3. Apply table formatting (professional look)
4. Add a chart (Column chart of Column [A] vs Column [E])
5. Set print area and page orientation
6. Protect the sheet (with password "[PASSWORD]")
7. Save the workbook

Include comments and error handling.
```

### Prompt 47: Email Automation Macro

```
Write a VBA macro that sends personalized emails from Excel:

Data in Sheet "Contacts":
- Column A: Recipient Name
- Column B: Email Address
- Column C: Company
- Column D: Custom Field 1
- Column E: Send? (YES/NO)

Email template:
Subject: "[SUBJECT WITH [NAME] PLACEHOLDER]"
Body: [PROVIDE YOUR EMAIL TEMPLATE WITH PLACEHOLDERS]

The macro should:
1. Loop through rows where Column E = "YES"
2. Create email using Outlook
3. Replace placeholders with actual data
4. Option to send immediately or save as draft
5. Log sent status in Column F with timestamp
6. Show progress bar during execution

Include Outlook object model references and error handling.
```

### Prompt 48: Data Import and Consolidation Macro

```
Write a VBA macro that:

1. Opens all .xlsx files in folder "[FOLDER PATH]"
2. For each file, copies data from Sheet "[SHEET NAME]",
   range A2 to the last row (skipping headers)
3. Pastes all data into the active workbook's Sheet "Consolidated"
4. Adds a column with the source filename
5. Removes any duplicate rows
6. Sorts by Column [A]
7. Creates a summary showing count of records per source file
8. Closes all source files without saving

Handle:
- Files with different column orders (match by header name)
- Protected files (skip and log)
- Empty files (skip and log)
- Progress indicator for large batches
```

### Prompt 49: Interactive Dashboard Macro

```
Write VBA macros for an interactive dashboard:

1. Macro "FilterByRegion":
   - Linked to a dropdown (Cell [B1]) with region names
   - Filters the data table by the selected region
   - Updates all charts to reflect the filtered data
   - Updates summary KPIs

2. Macro "FilterByDateRange":
   - Uses start date (Cell [D1]) and end date (Cell [E1])
   - Filters the data table by the date range
   - Updates all charts and KPIs

3. Macro "ResetFilters":
   - Clears all filters
   - Resets dropdown to "All"
   - Resets dates to current month
   - Refreshes everything

4. Macro "ExportDashboard":
   - Exports the dashboard sheet as a PDF
   - Names the file with current date
   - Opens the PDF after export

Include worksheet event triggers for automatic updates.
```

### Prompt 50: Scheduled Task Automation

```
Write a VBA macro system that automates recurring tasks:

1. Macro "DailyRefresh":
   - Refreshes all data connections
   - Recalculates all formulas
   - Updates date stamp in Cell [A1]
   - Runs every day when the workbook opens (Workbook_Open event)

2. Macro "WeeklyBackup":
   - Saves a copy of the workbook with date in filename
   - To folder "[BACKUP PATH]"
   - Keeps only the last 4 backups (deletes older ones)
   - Runs every Monday (check date on open)

3. Macro "MonthlyReport":
   - On the 1st of each month, generates last month's report
   - Calls the AutoReportGenerator macro with previous month's parameters
   - Emails the report to "[DISTRIBUTION LIST]"
   - Logs the execution in a "Run History" sheet

Include scheduling logic using Workbook_Open and Application.OnTime.
Error handling that logs failures without crashing.
```

---

## Quick Reference: Prompt Enhancement Tips

When using any of these prompts, improve the output by adding:

```
Additional instructions:
- Explain each function used in plain English
- Include IFERROR wrapper for error handling
- Show me what the formula looks like in the formula bar
- Provide a Google Sheets version if syntax differs
- Test cases: What should the formula return for these example values?
  - Example 1: [INPUT] → Expected: [OUTPUT]
  - Example 2: [INPUT] → Expected: [OUTPUT]
- Handle these edge cases: [BLANKS, ZEROS, TEXT IN NUMBER COLUMNS, ETC.]
```
