import sqlite3
from rich.text import Text
from rich import print
from .sqliteCRUD import SqliteCRUD
from prettytable import PrettyTable


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
        
        listing = directories + "\n" + files
                
        return listing
    
    
    
    def get_long_listing(db_path, dir_id, flags):
         # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Query to check if the file exists
        cursor.execute(f'SELECT name FROM files WHERE  pid = "{dir_id}"')
        file_names = cursor.fetchall()
        file_names = list(file_names)
        
         # Query to check if the file exists
        cursor.execute(f'SELECT name FROM directories WHERE pid = "{dir_id}"')
        directory_names = cursor.fetchall()
        
        file_names = [name[0] for name in file_names]
        directory_names = [directory[0] for directory in directory_names]
        
        table = []
        
        for name in directory_names:
            
            temp_table = []
            # Gets the directory permissions
            cursor.execute('SELECT read_permission, write_permission, execute_permission, world_read, world_write, world_execute FROM directories WHERE name = ?', (name,))
            directory_permissions = cursor.fetchone()
            
            directory_permissions = list(directory_permissions)
            temp_perm = 'd'
            
            # Iterate over each character in the input string
            for index, char in enumerate(directory_permissions):
                if index % 3 == 0:  # Positions 0, 3, 6, ... get 'r'
                    if char == 1:
                        temp_perm += 'r'
                    else:
                        temp_perm += '-'
                elif index % 3 == 1:  # Positions 1, 4, 7, ... get 'w'
                    if char == 1:
                        temp_perm += 'w'
                    else:
                        temp_perm += '-'
                elif index % 3 == 2:  # Positions 2, 5, 8, ... get 'x'
                    if char == 1:
                        temp_perm += 'x'
                    else:
                        temp_perm += '-'
            directory_permissions = temp_perm
            
            # Default directory size
            directory_size = 4096
            
            if 'h' in flags:
                if directory_size >= 1000:
                    directory_size =  f"{directory_size / 1000:.1f}k"
                str(directory_size)
            else: 
                directory_size = str(directory_size)
            
            cursor.execute(f'Select created_at, modified_at FROM directories WHERE name = ?', (name,))
            directory_dates = cursor.fetchone()
            directory_dates = list(directory_dates)
            
            if 'l' in flags:                        
                temp_table.insert(len(temp_table), directory_permissions)
                temp_table.insert(len(temp_table), directory_size)
                temp_table.extend(directory_dates)
            temp_table.insert(len(temp_table), name)
            
            table.append(temp_table)
        
        
        for name in file_names:
            
            temp_table = []
            # Gets the file permissions
            cursor.execute('SELECT read_permission, write_permission, execute_permission, world_read, world_write, world_execute FROM files WHERE name = ?', (name,))
            file_permissions = cursor.fetchone()
            # file_permissions = ''.join(map(str, file_permissions))
            file_permissions = list(file_permissions)
            temp_perm = '-'
            
            # Iterate over each character in the input string
            for index, char in enumerate(file_permissions):
                if index % 3 == 0:  # Positions 0, 3, 6, ... get 'r'
                    if char == 1:
                        temp_perm += 'r'
                    else:
                        temp_perm += '-'
                elif index % 3 == 1:  # Positions 1, 4, 7, ... get 'w'
                    if char == 1:
                        temp_perm += 'w'
                    else:
                        temp_perm += '-'
                elif index % 3 == 2:  # Positions 2, 5, 8, ... get 'x'
                    if char == 1:
                        temp_perm += 'x'
                    else:
                        temp_perm += '-'
            file_permissions = temp_perm
            
            # Gets the file size
            cursor.execute(f'SELECT size FROM files WHERE name = ?', (name,))
            file_size = cursor.fetchone()
            
            if 'h' in flags:
                file_size = int(''.join(map(str, file_size)))
                
                if file_size >= 1000:
                    file_size =  f"{file_size / 1000:.1f}k"
                str(file_size)
            else:
                file_size = ''.join(map(str, file_size))
            
            cursor.execute(f'Select creation_date, modified_date FROM files WHERE name = ?', (name,))
            file_dates = cursor.fetchone()
            file_dates = list(file_dates)
            #file_dates = [item for tup in file_dates for item in tup]
             
            if 'l' in flags:           
                temp_table.insert(len(temp_table), file_permissions)
                temp_table.insert(len(temp_table), file_size)
                temp_table.extend(file_dates)            
            temp_table.insert(len(temp_table), name)
            table.append(temp_table)
            
        if 'l' in flags:    
            table = '\n'.join(['\t'.join(sublist) for sublist in table])
        else:
            table = '\t'.join(['\t'.join(sublist) for sublist in table])
    
        return(table)
        

        # for dir in directory_names:
        #     table.append(dir)
        # table.append("\n")
            
        # for file in files:
        #     table.append(file)
        # table.append("\n")
        # #table.add_rows(files_info)
        
        #return table
    
    def get_row_number_by_name(table, name):
        for i, row in enumerate(table.rows):
            if row[0] == name:  # Assuming the name is in the first column
                return i
        return -1  # Return -1 if the name is not found