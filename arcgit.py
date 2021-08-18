from AGOL_CONFIG import agol_config

from arcgis.gis import GIS
import requests

import json
import os
import shutil


def login(agol_config):
    # return GIS object using user credentials

    print("Logging into AGOL")

    return GIS(
        url = agol_config['orgUrl'],
        username = agol_config['user'],
        password = agol_config['password']
    )


def request_data(itemId):
    # get request parameters
    baseUrl = 'https://bren96.maps.arcgis.com/sharing/rest/content/items/'
    token = agol_config['token']
    f = 'json'
    
    # build request url
    url = "{}/{}/data?token={}.&f={}".format(baseUrl, itemId, token, f)

    # execute request -> return JSON
    r = requests.get(url)
    return r.json()


def request_metadata(itemId):
    # get request parameters
    baseUrl = 'https://bren96.maps.arcgis.com/sharing/rest/content/items/'
    token = agol_config['token']
    f = 'json'

    # build request url
    url = "{}/{}?token={}.&f={}".format(baseUrl, itemId, token, f)

    #  execute request -> return JSON
    r = requests.get(url)
    return r.json()

def pull_dashboard_data(item, outputPath):
    
    # get item id
    itemId = item.id

    # create folder to store data, use outputPath if defined
    folderName = 'Dashboard_{}'.format(itemId)
    if outputPath:
        folderPath = os.path.join(outputPath, folderName)
    else:
        folderPath = folderName
    if os.path.exists(folderPath):
        errorNote = "Data Pull Failed: Output Folder ({}) already exists".format(folderPath)
        return {'success': False, 'data': errorNote}
    os.mkdir(folderPath)

    # write dashboard data to file
    dashboardData = request_data(itemId)
    filePath = os.path.join(folderPath, "Data.json")
    with open(filePath, 'x') as dataFile:
        dataFile.write(json.dumps(dashboardData, indent=4))

    # write dashboard metdata to file
    dashboard_metadata = request_metadata(itemId)
    filePath = os.path.join(folderPath, 'Description.json')
    with open(filePath, 'x') as dataFile:
        dataFile.write(json.dumps(dashboard_metadata, indent=2))

    print('Pulled Item Data to {}'.format(folderPath))
    return {'success': True, 'data': folderPath}


def clone_dashboard(itemId, *outputFolder):

    # login to AGOL
    gis = login(agol_config)

    # clone in AGOL
    print('Cloning Item')
    item = gis.content.get(itemId)
    clonedItem = gis.content.clone_items(
        items = [item],
        search_existing_items = False
    )

    if len(clonedItem) == 0:
        # check if clone item list returns none
        print("Cloning Failed: No AGOL item Created")
        return None
    else:
        print("Cloning Successfull")
        
        
    # pull item data
    dataPull = pull_dashboard_data(clonedItem[0], outputFolder)
    if dataPull['success']:
        dataFolder = dataPull['data']
    else:
        print(dataPull['data'])
        return None 
        
        
    # create arcgit in data folder, add original item id
    arcgitPath = os.path.join(dataFolder, 'arcgit.json')
    save_to_arcgit(
        arcgitPath,
        {
            'itemId': itemId,
            'clonedId': clonedItem[0].id
        }
    )

    # get list of dashboard maps
    # for each map, request data, store locally
    # for each map, get list of layers
    # for each layer, request data, store locally
        
        


def save_to_arcgit(filePath, dict):
    # read in JSON to dictionary
    if os.path.exists(filePath):
        currentDict = json.load(open(filePath))
    else:
        # if there is no filepath, return empty dictionary
        currentDict = {}
        
    # update dictionary with records to append
    currentDict.update(dict)

    # write updated dictionary to arcgit
    print("Saving to arcgist.JSON")
    with open(filePath, 'w') as arcgitFile:
        arcgitFile.write(json.dumps(currentDict, indent=2))


def post_data(itemId, cloneMetadata, cloneData):
    # login to AGOL
    gis = login(agol_config)

    item = gis.content.get(itemId)
    item.update(
        # item_properties = cloneMetadata,
        data = cloneData
    )

def merge(folderName):
    # look for an arcgit.json in folderName
    arcgitPath = os.path.join(folderName, 'arcgit.json')
    if os.path.exists(arcgitPath):
        # open arcgit, read into python dictionary
        with open(arcgitPath) as arcgitFile:
            arcgit = json.load(arcgitFile)
        
        # get clone and original item id
        cloneId = arcgit['clonedId']
        ogId = arcgit['itemId']
        
        # get clone data & metadata
        cloneMetadata = request_metadata(cloneId)
        cloneData = request_data(cloneId)

        # set original item data & metadata 
        post_data(ogId, cloneMetadata, cloneData)

        print('Clone is now merged with Original Item')

    else:
        print('Error: no arcgit.json found in {}'.format(arcgitPath))