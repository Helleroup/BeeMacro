import sqlite3

# The local function to get the path of the database
def getPath(db):

    dbs = {
        'user': './data/user.db', # User database
        'game': './data/game.db', # Game database
    }

    # Loop through the database dictionary, looking for a match
    success = False
    for file, path in dbs.items():
        if file == db:
            success = True
            return path

    # Prints error message if no match is found
    if not success:
        print('Error: Invalid database')

# Function to get all data from a table in the database, structured as a dictionary
def get(db, table):

    # Establish a connection to the database and enable row factory to make rows behave like dictionaries
    conn = sqlite3.connect(getPath(db))
    conn.row_factory = sqlite3.Row

    # Create a cursor object to execute SQL commands and fetch all rows from the specified table including the rowid
    cursor = conn.cursor()
    cursor.execute(f'SELECT rowid, * FROM {table}')
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

     # Create a dictionary where each key is the index and the value is a dictionary of the row data including the rowid.
    tableDict = {
        i + 1: {**{key: row[key] for key in row.keys()}, 'rowid': row['rowid']}
        for i, row in enumerate(rows)
    }

    # Return the dictionary
    return tableDict

# Function to add a new row to the selected database
def addRow(db, table, data):

    # Establish a connection to the database and create a cursor object
    conn = sqlite3.connect(getPath(db))
    cursor = conn.cursor()

    # Format the data to be compatible with sqlite
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))

    # Add the row to the table
    cursor.execute(f'INSERT INTO {table} ({columns}) VALUES ({placeholders})', tuple(data.values()))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Function to edit a specific cell from the selected database
def editCell(db, table, rowid, column, data):

    # Establish a connection to the database and create a cursor object
    conn = sqlite3.connect(getPath(db))
    cursor = conn.cursor()

    # Edit the cell in the table, where the rowid and column match
    cursor.execute(f'UPDATE {table} SET {column} = ? WHERE rowid = ?', (data, rowid))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

# Function to remove a specific row from the selected database
def removeRow(db, table, rowid):

    # Establish a connection to the database and create a cursor object
    conn = sqlite3.connect(getPath(db))
    cursor = conn.cursor()

    # Delete the row in the table, where the rowid matches
    cursor.execute(f'DELETE FROM {table} WHERE rowid = ?', (rowid,))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()
