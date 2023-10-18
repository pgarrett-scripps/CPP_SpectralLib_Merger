import pandas as pd
import tkinter as tk
from tkinter import filedialog


def merge_tsv_files():
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select multiple TSV files
    file_paths = filedialog.askopenfilenames(filetypes=[("TSV Files", "*.tsv")])
    if not file_paths:
        print("No files selected. Exiting.")
        return

    # Initialize an empty list to store DataFrames
    dfs = []

    # Read each selected TSV file into a DataFrame and append it to the list
    for file_path in file_paths:
        df = pd.read_csv(file_path, sep='\t')
        dfs.append(df)

    # Merge the DataFrames (assuming they have the same columns)
    merged_df = pd.concat(dfs, ignore_index=True)

    # Ask the user to choose a location to save the merged TSV file
    save_path = filedialog.asksaveasfilename(defaultextension=".tsv", filetypes=[("TSV Files", "*.tsv")])
    if not save_path:
        print("No save location selected. Exiting.")
        return

    # Save the merged DataFrame to the selected location
    merged_df.to_csv(save_path, sep='\t', index=False)

    print(f"Merged TSV file saved to: {save_path}")


if __name__ == "__main__":
    merge_tsv_files()
