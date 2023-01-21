import os
import csv
import re

folder_path = "./TonyCSVs"

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
        with open(file_path, "w", newline='') as f:
            writer = csv.writer(f)
            for row in rows:
                new_row = [re.sub(r'\([^()]*\)', '', val).replace(" Ltd.",
                                                                  "").replace(" LLC",
                                                                              "").replace(" L.L.C.",
                                                                                          "").replace(" & Co.",
                                                                                                      "").replace(" Inc.",
                                                                                                                  "").replace(" Inc",
                                                                                                                              "").replace(" (", "(").strip() for val in row]
                writer.writerow(new_row)
