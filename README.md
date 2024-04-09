# Dumpsys Service Info Extractor

This Python script extracts information for each service from a dumpsys file and saves the information as separate text files. It is particularly useful for analyzing system service information in Android environments.

## Prerequisites

- Python 3.x
- `os` and `re` Python libraries

## Usage

1. Ensure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script (`dumpsys_service_info_extractor.py`) using the `cd` command.
4. Run the script using the following command:

```bash
python dumpsys_service_info_extractor.py
```

## Input

- **dumpsys_file**: Path to the dumpsys file from which service information will be extracted. Replace `'YOUR FILE.txt'` with the path to your dumpsys file.

## Output

- The script will create an output folder named after the dumpsys file in the same directory as the script.
- Inside the output folder, it will generate separate text files for each service containing their respective information.

## Script Overview

- The `extract_service_info` function extracts information for each service from the dumpsys file.
- The `write_service_info` function writes the extracted service information to separate text files in the specified output folder.
- The `main` function orchestrates the extraction and writing process.

## Example

Suppose you have a dumpsys file named `system_dump.txt`. Running the script will create an output folder named `system_dump` and generate text files for each service inside that folder.
