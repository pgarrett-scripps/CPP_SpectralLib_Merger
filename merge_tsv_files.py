import tkinter as tk
from tkinter import filedialog


def merge_tsv_files():
    root = tk.Tk()
    root.withdraw()

    # Ask the user to select multiple TSV files
    file_paths = filedialog.askopenfilenames(filetypes=[("TSV Files", "*.tsv")], multiple=True, title="Select Input TSV Files")
    if not file_paths:
        print("No files selected. Exiting.")
        return

    # Ask the user to choose a location to save the merged TSV file
    save_path = filedialog.asksaveasfilename(defaultextension=".tsv", filetypes=[("TSV Files", "*.tsv")], title="Save Merged TSV File")
    if not save_path:
        print("No save location selected. Exiting.")
        return

    seen = set()
    header_written = False

    with open(save_path, 'w') as of:
        for file_path in file_paths:
            with open(file_path, 'r') as f:
                curr_peptide_charge = None
                for i, line in enumerate(f):
                    if i == 0:
                        # Write the header line only once
                        if not header_written:
                            of.write(line)
                            header_written = True
                        continue

                    line_elements = line.strip().split('\t')
                    peptide, charge, unmod_peptide = line_elements[0], int(line_elements[1]), line_elements[4]

                    # Check if we have encountered a new peptide and charge combination
                    if curr_peptide_charge and curr_peptide_charge != (peptide, charge):
                        seen.add(curr_peptide_charge)
                        curr_peptide_charge = (peptide, charge)
                    elif not curr_peptide_charge:
                        curr_peptide_charge = (peptide, charge)

                    # Check for 'K' in unmod_peptide and if (peptide, charge) is not in seen
                    if 'K' in unmod_peptide and curr_peptide_charge not in seen:
                        of.write(line)

                # Add the last encountered peptide and charge to seen
                if curr_peptide_charge:
                    seen.add(curr_peptide_charge)

    print(f"Merged TSV file saved to: {save_path}")


if __name__ == "__main__":
    merge_tsv_files()
