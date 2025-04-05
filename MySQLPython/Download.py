'''Here we will write the command to download mysql on the computer.'''

import requests
from tqdm import tqdm

downloadMysql = requests.get("https://cdn.mysql.com//Downloads/MySQLInstaller/mysql-installer-community-8.0.41.0.msi",stream=True)

totalExpectedBytes = int(downloadMysql.headers["Content-Length"])
progressbar = tqdm(total=totalExpectedBytes,unit_scale=True)
with open("MySQL.msi","wb") as f:
    for chunk in downloadMysql.iter_content(chunk_size=128):
        if chunk:
            f.write(chunk)
            progressbar.update(len(chunk))
progressbar.close()