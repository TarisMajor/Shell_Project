import sqlite3
from rich.text import Text
from rich import print


db_path = './P01/ApiStarter/data/filesystem.db'  

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
    
    def get_dir_id(db_path, name):
        """
        Gets directory id in the SQLite database.

        Parameters:
            db_path (str): Path to the SQLite database.
            name (str): Name of the directory to search for.

        Returns:
            int: Directory ID
        """
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
    
        cursor.execute("SELECT id FROM directories WHERE name=?", (name,))
        dir_id = cursor.fetchone()
    
        did = int
        # Fetch the result
    
        for id in dir_id:
            did = id

        # Close the connection
        cursor.close()
        conn.close()
        
        return did
        
    
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

    def dir_exists(db_path, name):
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
        cursor.execute("SELECT EXISTS(SELECT 1 FROM directories WHERE name=?)", (name,))
    
        # Fetch the result
        exists = cursor.fetchone()[0] == 1  # returns True if exists, False otherwise

        return exists

    def get_listing(db_path, dir_id):
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to check if the file exists
        cursor.execute(f'SELECT name FROM files WHERE  pid = "{dir_id}"')
        files = cursor.fetchall()
        
        files = [file[0] for file in files]
        
        files = "\t".join(files)
        
        # Query to check if the file exists
        cursor.execute(f'SELECT name FROM directories WHERE pid = "{dir_id}"')
        directories = cursor.fetchall()
        
        directories = [directory[0] for directory in directories]
        
        directories = "\t".join(directories)

        directories = Text(directories)
        files = Text(files)
        directories.stylize("cyan")
        files.stylize("white")
        
        listing = directories + "\t" + files
                
        return listing
        
