#  pip install wget
import wget, os,zipfile
destino =  os.path.join(".",'dados')
os.makedirs(destino,exist_ok=True)
os.chdir(destino)

url="http://networksciencebook.com/translations/en/resources/networks.zip"
# http://networksciencebook.com/translations/en/resources/data.html
arquivo = 'networks.zip'
if not os.path.isfile(arquivo):
    wget.download(url)
with zipfile.ZipFile(arquivo, 'r') as zip:
   
    zip.extractall()
    print('Done!')