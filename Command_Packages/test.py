import base64
import requests
import sqlite3


db_path = './P01/ApiStarter/data/filesystem.db'  

def encodeIt(plainText):
    # Encode the string as bytes, then to Base64
    encoded = base64.b64encode(plainText.encode("utf-8"))
    # Convert back to string for display
    return encoded


def decodeIt(encodedText):
    # Decode Base64 to original bytes
    decoded = base64.b64decode(encodedText)
    # Convert bytes back to string
    return decoded.decode("utf-8")

def test():
    cwd = "!!!!!9"
    
    cwd = list(cwd)
    cmd = cwd.split(" ")

    if "/" in cwd:
        path = cwd.split("/")
        
    print(path)

if __name__ == "__main__":
    
    # Connect to the SQLite database
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()
    
    # name = 'testls.txt'
    # pid = 3
    # pid = str(pid)
    
    # query = """
    # SELECT EXISTS (SELECT 1 FROM files WHERE name = ? AND pid = ?);
    # """
    # cursor.execute(query, (name, pid))
           
    # exists = cursor.fetchone()[0]
    
    # print(exists)
    
    meh = '77u/VGhlIFByb2plY3QgR3V0ZW5iZXJnIGVCb29rIG9mIEJlb3d1bGY6IEFuIEFuZ2xvLVNheG9uIEVwaWMgUG9lbQoKVGhpcyBlYm9vayBpcyBmb3IgdGhlIHVzZSBvZiBhbnlvbmUgYW55d2hlcmUgaW4gdGhlIFVuaXRlZCBTdGF0ZXMgYW5kCm1vc3Qgb3RoZXIgcGFydHMgb2YgdGhlIHdvcmxkIGF0IG5vIGNvc3QgYW5kIHdpdGggYWxtb3N0IG5vIHJlc3RyaWN0aW9ucwp3aGF0c29ldmVyLiBZb3UgbWF5IGNvcHkgaXQsIGdpdmUgaXQgYXdheSBvciByZS11c2UgaXQgdW5kZXIgdGhlIHRlcm1zCm9mIHRoZSBQcm9qZWN0IEd1dGVuYmVyZyBMaWNlbnNlIGluY2x1ZGVkIHdpdGggdGhpcyBlYm9vayBvciBvbmxpbmUKYXQgd3d3Lmd1dGVuYmVyZy5vcmcuIElmIHlvdSBhcmUgbm90IGxvY2F0ZWQgaW4gdGhlIFVuaXRlZCBTdGF0ZXMsCnlvdSB3aWxsIGhhdmUgdG8gY2hlY2sgdGhlIGxhd3Mgb2YgdGhlIGNvdW50cnkgd2hlcmUgeW91IGFyZSBsb2NhdGVkCmJlZm9yZSB1c2luZyB0aGlzIGVCb29rLgoKCnBhcGVycwlwcHRzCWltYWdlcwlWZWN0b3JzLURpc3RhbmNlX1BvaW50X3RvX2FfTGluZV9maWxlcwlweXRob25fY29kZQlWZWN0b3JzLUFkZGl0aW9uXyZfU3VidHJhY3Rpb25fZmlsZXMJVmVjdG9ycy1Ob3JtYWxpemluZ19maWxlcwlBbGdvcml0aG1pYy1RdWFkVHJlZV8oUHl0aG9uKV9maWxlcwlkYXRhCmdlby5weQlWZWN0b3JzLUFkZGl0aW9uXyZfU3VidHJhY3Rpb24uaHRtbAl0ZXJtaW5vbG9neV9hbmRfdG9waWNzLm1kCVZlY3RvcnMtTm9ybWFsaXppbmcuaHRtbAlzcGF0aWFsX3JlbGF0aW9uc2hpcHMubWQJcXVhZDIudGV4dAlydHJlZV9zcF8yMDIyLnBwdHgJc3RhdGUtZmlwcy5jc3YJVmVjdG9ycy1EaXN0YW5jZV9Qb2ludF90b19hX0xpbmUuaHRtbAlxdWFkdHJlZS56aXAJdG9wb2xvZ2ljYWxfcmVsYXRpb25zLnBuZwpkci14ci14CTQuMWsJMjAyNC0xMC0wNSAwODozNjowNgkyMDI0LTEwLTA1IDA4OjM2OjA2CXBhcGVycwpkci14ci14CTQuMWsJMjAyNC0xMC0wNSAwODozNjowNgkyMDI0LTEwLTA1IDA4OjM2OjA2CXBwdHMKZHIteHIteAk0LjFrCTIwMjQtMTAtMDUgMDg6MzY6MDYJMjAyNC0xMC0wNSAwODozNjowNglpbWFnZXMKZHIteHIteAk0LjFrCTIwMjQtMTAtMDUgMDg6MzY6MDYJMjAyNC0xMC0wNSAwODozNjowNglWZWN0b3JzLURpc3RhbmNlX1BvaW50X3RvX2FfTGluZV9maWxlcwpkci14ci14CTQuMWsJMjAyNC0xMC0wNSAwODozNjowNgkyMDI0LTEwLTA1IDA4OjM2OjA2CXB5dGhvbl9jb2RlCmRyLXhyLXgJNC4xawkyMDI0LTEwLTA1IDA4OjM2OjA2CTIwMjQtMTAtMDUgMDg6MzY6MDYJVmVjdG9ycy1BZGRpdGlvbl8mX1N1YnRyYWN0aW9uX2ZpbGVzCmRyLXhyLXgJNC4xawkyMDI0LTEwLTA1IDA4OjM2OjA2CTIwMjQtMTAtMDUgMDg6MzY6MDYJVmVjdG9ycy1Ob3JtYWxpemluZ19maWxlcwpkci14ci14CTQuMWsJMjAyNC0xMC0wNSAwODozNjowNgkyMDI0LTEwLTA1IDA4OjM2OjA2CUFsZ29yaXRobWljLVF1YWRUcmVlXyhQeXRob24pX2ZpbGVzCmRyLXhyLXgJNC4xawkyMDI0LTEwLTA1IDA4OjM2OjA2CTIwMjQtMTAtMDUgMDg6MzY6MDYJZGF0YQotLXd4LXctCTIuNGsJMjAyNC0wOC0yNiAwMjozNjoxMQkyMDE5LTEwLTE0IDExOjU0OjExCWdlby5weQotcnctLS0tCTYuNWsJMjAyNC0xMC0wMyAyMjoxNzoxMAkyMDIyLTEwLTA3IDIyOjAxOjQ2CVZlY3RvcnMtQWRkaXRpb25fJl9TdWJ0cmFjdGlvbi5odG1sCi1ydy0tLS0JMS4xawkyMDI0LTA4LTI2IDAyOjM4OjE0CTIwMjItMTAtMDcgMjI6MDE6NDYJdGVybWlub2xvZ3lfYW5kX3RvcGljcy5tZAotcnctLS0tCTQuMGsJMjAyNC0xMC0wMyAyMjoxODowMwkyMDIyLTEwLTA3IDIyOjAxOjQ2CVZlY3RvcnMtTm9ybWFsaXppbmcuaHRtbAotcnctLS0tCTUuM2sJMjAyNC0wOC0yNiAwMjozODoxNAkyMDIyLTEwLTA3IDIyOjAxOjQ2CXNwYXRpYWxfcmVsYXRpb25zaGlwcy5tZAotcnctLS0tCTc2LjNrCTIwMjQtMDgtMjYgMDI6Mzg6MTQJMjAyMi0xMC0wNyAyMjowMTo0NglxdWFkMi50ZXh0Ci1ydy0tLS0JMTcwLjRrCTIwMjQtMDgtMjYgMDI6Mzg6MTQJMjAyMi0xMC0wNyAyMjowMTo0NglydHJlZV9zcF8yMDIyLnBwdHgKLXJ3LS0tLQkyLjFrCTIwMjQtMDgtMjYgMDI6MzY6MTAJMjAyMi0xMC0wNyAyMjowMTo0NglzdGF0ZS1maXBzLmNzdgotcnctLS0tCTEwLjdrCTIwMjQtMTAtMDMgMjI6MTc6MzQJMjAyMi0xMC0wNyAyMjowMTo0NglWZWN0b3JzLURpc3RhbmNlX1BvaW50X3RvX2FfTGluZS5odG1sCi1ydy0tLS0JNi41awkyMDI0LTA4LTI2IDAyOjM2OjEwCTIwMjItMTAtMDcgMjI6MDE6NDYJcXVhZHRyZWUuemlwCi1ydy0tLS0JMTI0LjRrCTIwMjQtMDgtMjYgMDI6Mzg6MTQJMjAyMi0xMC0wNyAyMjowMTo0Ngl0b3BvbG9naWNhbF9yZWxhdGlvbnMucG5n'
    
    truin = decodeIt(meh)
    
    print(truin)
