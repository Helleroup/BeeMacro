import sqlite3

def getPath(db):
    dbs = {
        'user': './data/user.db',
        'game': './data/game.db',
    }
    success = False
    for file, path in dbs.items():
        if file == db:
            success = True
            return path
    if not success:
        print('Error: Invalid database')

def get(db, table):

    conn = sqlite3.connect(getPath(db))
    conn.row_factory = sqlite3.Row  # Enable row factory to access columns by name
    cursor = conn.cursor()

    cursor.execute(f'SELECT rowid, * FROM {table}')

    rows = cursor.fetchall()

    #tableDict = {row['rowid']: {key: row[key] for key in row.keys() if key != 'rowid'} for row in rows}

    conn.close()

    #tableDict = {i + 1: {key: row[key] for key in row.keys() if key != 'rowid'} for i, row in enumerate(rows)}
    tableDict = {
        i + 1: {**{key: row[key] for key in row.keys()}, 'rowid': row['rowid']}
        for i, row in enumerate(rows)
    }

    return tableDict

def removeRow(db, table, rowid):
    conn = sqlite3.connect(getPath(db))
    cursor = conn.cursor()

    cursor.execute(f'DELETE FROM {table} WHERE rowid = ?', (rowid,))
    conn.commit()
    conn.close()

def editRow(db, table, rowid, column, data):
    conn = sqlite3.connect(getPath(db))
    cursor = conn.cursor()

    cursor.execute(f'UPDATE {table} SET {column} = ? WHERE rowid = ?', (data, rowid))
    conn.commit()
    conn.close()

def addRow(db, table, data):
    conn = sqlite3.connect(getPath(db))
    cursor = conn.cursor()

    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' * len(data))
    cursor.execute(f'INSERT INTO {table} ({columns}) VALUES ({placeholders})', tuple(data.values()))
    conn.commit()
    conn.close()
