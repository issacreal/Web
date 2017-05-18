# -*-coding:UTF-8 -*-

import os
import sys
import logging
import requests
import shutil
import bs4
import pandas as pd
import urllib.request, urllib.parse, urllib.error
from datetime import datetime

loggingOutputFile = 'log.txt'
logFormat = '%(asctime)s - [%(levelname)s] - %(message)s'
dateFormat = '%Y-%m-%d-%H:%M:%S'

RESET_COLOR     = '\033[1;0m'
WARNING_COLOR   = '\033[1;33m'
ERROR_COLOR     = '\033[1;41m'

# -----------------------------------------------------------------------------
# set log format
logging.basicConfig(filename='',
                    filemode='w',
                    level=logging.DEBUG, format=logFormat, datefmt=dateFormat)
logging.addLevelName(logging.WARNING, "%s%s%s" % (WARNING_COLOR, logging.getLevelName(logging.WARNING), RESET_COLOR))
logging.addLevelName(logging.ERROR, "%s%s%s" % (ERROR_COLOR, logging.getLevelName(logging.ERROR), RESET_COLOR))
# logging.disable(logging.DEBUG)
# logging function:
#   logging.debug()     ->  logging.DEBUG
#   logging.info()      ->  logging.INFO
#   logging.warning()   ->  logging.WARNING
#   logging.error()     ->  logging.ERROR
#   logging.critical()  ->  logging.CRITICAL
# -----------------------------------------------------------------------------

def CreateReportFolder(folderName):
    logging.debug("CreateReportFolder folderName: %s" % (folderName))
    relativePath = os.path.join(folderName)

    shutil.rmtree(folderName, ignore_errors=True)
    os.makedirs(relativePath)
    logging.info("CreateReportFolder path: %s" % (relativePath))
    return relativePath

def IsNeedToDownload(checkDownloadFile, downloadExtension):
    result = False
    file_name, extension = os.path.splitext(checkDownloadFile)
    logging.debug('filename: %s ext: %d' % (file_name, len(extension)))
    if len(extension) != 0 and extension.strip('.') in downloadExtension:
        result = True
    return result

def GetFileFromLink(downloadUrl, downloadExtension):
    downloadFileList = []
    folderName = datetime.now().strftime("%Y-%m-%d") + '_failLog'
    downloadedFolder = CreateReportFolder(folderName)
    logging.info("Download Url: %s dest: %s" % (downloadUrl, downloadedFolder))

    try:
        res = requests.get(downloadUrl)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # elems = soup.select('td > a')
        elems = soup.select('a')
        for eachlinkIndex in range(len(elems)):
            fileName = elems[eachlinkIndex].get('href')
            logging.info('eachlinkIndex: %d -> %s' % (eachlinkIndex, fileName))
            if IsNeedToDownload(fileName, downloadExtension):
                downloadFileList.append(fileName)
    except Exception as exc:
        logging.error('There was a problem: %s' % (exc))
    return downloadFileList, downloadedFolder

def DownloadFile(downloadUrl, fileList, destFolder):
    finishDownloadCount = 0
    for eachFileName in fileList:
        fileLink = urllib.parse.urljoin(downloadUrl, eachFileName)
        destorigFileName = os.path.join(destFolder, eachFileName)
        try:
            logging.info('Downloading: %s -> %s' % (fileLink, destorigFileName))
            urllib.request.urlretrieve(fileLink, destorigFileName)
        except Exception as err:
            logging.error('Download Fail in link: %s err: %s' % (fileLink, err))
            continue
    return finishDownloadCount

# ----- start to estimate -----
def main():
	  targetUrl = "http://www.tse.com.tw/ch/trading/indices/MI_5MINS_HIST/MI_5MINS_HIST.php"
	  logging.debug("Target: %s"  % targetUrl)
	  
	  year    = '101'
	  month   = '03 '

	  payload = {
	   'myear': year,
	   'mmon' : month
	  }
	  
	  res = requests.post(targetUrl, data = payload)	
	  soup = bs4.BeautifulSoup(res.text, 'html.parser')
	  tb = soup.select('#contentblock > td > table')[2].select('tr')

	  #df = pd.read_html(tb.prettify('utf-8'), encoding= 'utf-8', skiprows = [0]) 
	  #print(tb.prettify('utf-8'))
	  print(tb[5])
	  #res = requests.get(targetUrl)
	  
	  #logging.info("%s", res.text)
	  
	  #logging.info("%s", res.url)
	 
	  """ 



	  
	  
    url = 'http://www.twse.com.tw/ch/trading/exchange/MI_5MINS_INDEX/MI_5MINS_INDEX.php'
  myear:106
mmon:03


	  
    logging.debug("%s %d" % (sys.argv, len(sys.argv)))
    if len(sys.argv) < 2:
        logging.error('Please input the url you need')
    else:
        urlFromUser = sys.argv[1]
        downloadExtension = sys.argv[2:]
        logging.debug('downloadExtension %s' % (downloadExtension))
        #downloadFileList, downloadedFolder = GetFileFromLink(urlFromUser, downloadExtension)
        #successfulCount = DownloadFile(urlFromUser, downloadFileList, downloadedFolder)
        #logging.info('Download file = %s done: %d' % (downloadFileList, successfulCount))
  
    """
    #logging.debug('test')
    

if __name__ == '__main__':
    main()
