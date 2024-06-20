import ftplib
from ftplib import FTP
from datetime import datetime

def is_file(filename: str) -> bool:
    try:
        ftp.size(filename)
        return True
    except ftplib.error_perm as e:
        return False


start = datetime.now()
ftp = FTP('ftp.dlptest.com')
ftp.login('dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')

# Get All Files
files = ftp.nlst()

print(files)
files = files[:5]
# Print out the files
for file in files:
    print("Downloading..." + file)
    if is_file(file):
        ftp.retrbinary("RETR " + file, open(file, 'wb').write)

ftp.close()

end = datetime.now()
diff = end - start