import pdfplumber
import csv

def pdf_to_csv(pdf_path, csv_path):
    with pdfplumber.open(pdf_path) as pdf, open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    writer.writerow(row)
    print(f"CSV file saved as: {csv_path}")

# Example usage
pdf_to_csv("input.pdf", "output.csv"