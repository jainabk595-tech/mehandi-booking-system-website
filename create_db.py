import sqlite3

# This will CREATE database.db automatically
conn = sqlite3.connect("database.db")

c = conn.cursor()

# Create tables
c.execute("""
CREATE TABLE IF NOT EXISTS designs (
    id INTEGER PRIMARY KEY,
    title TEXT,
    price TEXT,
    image TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS artists (
    id INTEGER PRIMARY KEY,
    name TEXT,
    rating REAL,
    image TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY,
    name TEXT,
    text TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT,
    service TEXT,
    message TEXT
)
""")

# Insert sample data
c.execute("INSERT INTO designs (title,price,image) VALUES ('Bridal Full Hand','₹5000-30000','/static/images/mehendi1.jpg')")
c.execute("INSERT INTO artists (name,rating,image) VALUES ('Neha',4.8,'/static/images/mehendi2.jpg')")
c.execute("INSERT INTO reviews (name,text) VALUES ('Priya','Amazing work!')")

conn.commit()
conn.close()

print("Database created successfully!")
print("tables created successfully")