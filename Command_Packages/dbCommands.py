import sqlite3

class DbCommands:

    def get_Content(db_path, file_id, dir_id):
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to check if the file exists
        cursor.execute(f'SELECT contents FROM files WHERE id = "{file_id}" AND pid = "{dir_id}"')
        content = ' '.join(map(str, cursor.fetchall())) 
    
        # Close the connection
        cursor.close()
        conn.close()
        return content
    
    def get_file_and_dir_id(db_path, name):
        """
        Check if a file exists in the SQLite database.

        Parameters:
            db_path (str): Path to the SQLite database.
            file_name (str): Name of the file to search for.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to check if the file exists
        cursor.execute("SELECT id FROM files WHERE name=?", (name,))
        file_id = cursor.fetchone()
    
        cursor.execute("SELECT pid FROM files WHERE name=?", (name,))
        dir_id = cursor.fetchone()
    
        fid = int
        did = int
        # Fetch the result
    
    
        for id in file_id:
            fid = id
        
        for id in dir_id:
            did = id

        # Close the connection
        cursor.close()
        conn.close()

        return [fid, did]
    
    def file_exists(db_path, name):
        """
        Check if a file exists in the SQLite database.

        Parameters:
            db_path (str): Path to the SQLite database.
            file_name (str): Name of the file to search for.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to check if the file exists
        cursor.execute("SELECT EXISTS(SELECT 1 FROM files WHERE name=?)", (name,))
    
        # Fetch the result
        exists = cursor.fetchone()[0] == 1  # returns True if exists, False otherwise

        return exists

