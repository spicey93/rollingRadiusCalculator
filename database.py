import sqlite3
import csv
import tyre_calculator as t_calc

# PREPARE DATA FOR DATABASE
# -------------------------------
# Empty array to store data
data = []

# Open CSV file and add to array
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(row)


# Create and populate 'sizes' table in sizes.db
def seed_database():
    con = sqlite3.connect("sizes.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sizes
    (size text, circumference real)""")
    for row in data:
        tyre_size = row[0]
        circum = row[1]
        cur.execute(f"INSERT INTO sizes VALUES ('{tyre_size}', {circum})")
    con.commit()
    con.close()


# Delete the size table if there are duplicate values
def delete_size_table():
    con = sqlite3.connect("sizes.db")
    cur = con.cursor()
    cur.execute("DROP TABLE sizes")
    con.commit()
    con.close()


# Query the database for tyre sizes with a similar rolling radius value
def find_similar_sizes(rolling_radius):
    con = sqlite3.connect("sizes.db")
    cur = con.cursor()
    info = cur.execute("SELECT * FROM sizes")
    # Create empty array to append too
    similar_sizes = []
    for row in info:
        # If we find a similar size tyre
        if t_calc.is_within_range(row[1], rolling_radius):
            # Add a formatted string to the list
            similar_sizes.append(
                f"{row[0]} | {(row[1] / rolling_radius) * 100 - 100:.2f}% | {int(row[1] - rolling_radius)}mm")
    con.commit()
    con.close()
    return similar_sizes
