# Merge TSV Files Utility

This Python script allows you to merge multiple TSV (Tab-Separated Values) files into a single output TSV file, filtering lines based on specific criteria. It utilizes the Tkinter library for a basic graphical user interface (GUI) to select input files and choose a location to save the merged file.

## Prerequisites

Before using this script, ensure that you have the following prerequisites installed on your system:
- Python 3.x
- Tkinter library (usually comes pre-installed with Python)

## Usage

1. Save the script to your computer with a `.py` extension, for example, `merge_tsv.py`.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```
   python merge_tsv.py
   ```

4. The script will open a file dialog window for you to select multiple TSV input files. You can select one or more files by holding down the Ctrl key (Cmd key on macOS) while clicking on the files.

5. After selecting the input files, the script will open another file dialog window for you to choose a location and name for the merged TSV file. By default, the merged file will have a `.tsv` extension.

6. Click the "Save" button to merge the selected files. The script will filter and merge the lines from the input files based on specific criteria (explained below).

7. Once the merge is complete, the script will display a message indicating where the merged TSV file has been saved.

## Criteria for Merging

The script reads the selected TSV files and performs the following filtering and merging based on specific criteria:

- It skips the header line from each input file but writes it only once to the merged file.
- It checks for lines in which the peptide starts with '_(' and contains the letter 'K' in the unmodified peptide.
- It ensures that only one line with the same peptide and charge combination is included in the merged file.
- The merged TSV file will contain only the lines that meet these criteria.

## Notes

- If you do not select any input files or cancel the file dialogs, the script will exit without merging any files.
- The script assumes that the input files are in the TSV format with tab-separated values.
- If you encounter any issues or have questions, please refer to the code or consult the script's developer for assistance.

Feel free to modify the script or integrate it into your projects as needed. Enjoy using the TSV file merging utility!