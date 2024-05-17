# Housecall Pro Assignment
Housecall Pro technical assignment


### Solution 

The task is to divide Google Analytics export data into two separate JSON files: visits.json and hits.json, each formatted in line-delimited JSON. The input data is in a nested JSON format, with "hits" nested within "visits". The script processes this data, extracting and transforming it into a flat structure suitable for relational-style tables.

Here is a step-by-step explanation of the logic implemented in the script:

Imports and Function Definitions:

- 1. Import necessary libraries: json, gzip, sys, and datetime.
Define a function to_iso8601 to convert timestamps into ISO8601 format.


- 2. Main Function:

Initialize two lists: visits and hits to store the processed visit and hit records.
Open the input file, which is expected to be gzipped, in read-text mode with UTF-8 encoding.

- 3. Reading and Processing the Input File:

Iterate over each line in the input file. Each line represents a single visit record in JSON format.
Parse the JSON line into a Python dictionary.

- 4. Extract and Transform Visit Data:
Create a visit_record dictionary with the following fields extracted and transformed:
  full_visitor_id: Directly from the visit record.
  visit_id: Directly from the visit record.
  visit_number: Directly from the visit record, converted to an integer.
  visit_start_time: Converted from a timestamp to ISO8601 format using the to_iso8601 function.
  browser: Extracted from the device sub-record.
  country: Extracted from the geoNetwork sub-record.


- 5. Extract and Transform Hit Data:

  Iterate over the hits array within the visit record.
  For each hit, calculate the hit_timestamp by adding the hit's time value (in milliseconds) to the visit's visitStartTime.
  Create a hit_record dictionary with the following fields:
  hit_number: Directly from the hit record, converted to an integer.
  hit_type: Directly from the hit record.
  hit_timestamp: Converted from a timestamp to ISO8601 format using the to_iso8601 function.
  page_path: Extracted from the page sub-record,
  or an empty string if not present.
  - page_title: Extracted from the page sub-record, or an empty string if not present.
  - hostname: Extracted from the page sub-record, or an empty string if not present.
  - Append the hit_record to the hits list.

- 6. Write Output Files:

Open visits.json for writing. Write each visit_record from the visits list to the file in line-delimited JSON format.
Open hits.json for writing. Write each hit_record from the hits list to the file in line-delimited JSON format.

- 7. Entry Point Check:

Check if the script is run with exactly one command-line argument (the input file path). If not, print a usage message and exit with an error code.
Call the main function with the input file path provided as a command-line argument.

<br>
<hr>

### How to use 

First, is needed to have a .gz file with in the same directory of **main.py**, the script accepts the .gz file to generate properly output. 
usage example: 

```python

python main.py ga_sessions.gz

```

All the dependencies and packages used in this solution are python native libraries. 
<br>

<br>
