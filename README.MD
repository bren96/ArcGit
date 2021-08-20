# ArcGit

Software is never written correctly the first time, and neither are services, maps, and apps for ArcGIS Online.

ArcGit is a version control Python library for ArcGIS Online content. ArcGit uses the ArcGIS REST API and ArcGIS API for Python. This library can help developers manage versioning of content in ArcGIS Online for branching, testing and design iteration.

Use cases:

1. Test and Iterate AGOL hosted products across multiple users/teams.

2. Merge and review changes to customer-facing AGOL services, maps, and apps without breaking active configurations.

3. Edit the JSON of your AGOL content locally from your favorite code editor.

4. Programmatically manage and apply changes to versioned AGOL content.

Imagine you have customers actively using a dashboard. You want to make changes or improvements to the dashboard, such as adding a new layer to the map, including more attributes in a popup, or trying out a new layer symbology.

Sadly, you can't replace the web-map currently used in the dashboard without fully deleting all the configurations to the web-map (dashboard selectors, charts, indicators, etc.) -> :confounded:

Imagine if it was just as simple as:
```python
import arcgit

clone = arcgit.clone(itemId)

# make your changes -> push to clone in AGOL
clone.push()

# merge the changes to the original item
clone.merge(itemId)
```

# Installation

Install to your local python environment:
```python
pip install arcgit
```

In your project's root directory, add your AGOL login credentials to AGOL_CONFIG.py:
```python
agol_config = {
    'orgUrl': '',
    'username': '',
    'password': '',
    'token' : ''
}
```

## Usage

Dashboard Example:

1. Clone a dashboard using it's itemId. This creates a folder locally called Dashboard-{itemId} containing json files for that AGOL item and a log tracking changes between the item and the clone.

2. Push local changes to the cloneId for testing.

3. Pull changes to sync your local directory.

4. Repeat steps 2 & 3 until ready for merge.

5. Merge changes from the clone to the original item. Optionally delete the clone after merging.


### Clone

#### arcgit.clone(itemID, cloneId, itemType outputFolder)

Clone an item in AGOL, and store a copy of the description.json and data.json in a local directory.

If in the clone's local directory, a clone object can be created by calling `argit.clone()`.

To load an existing clone in AGOL, pass the clone's id to the cloneId argument.

itemId
- Id of the AGOL Item you wish to clone
- String
- Optional

cloneId
- Id of the cloned AGOL Item (if a clone already exists)
- String
- Optional

itemType
- Type of AGOL item (ex: 'dashboard', 'map', 'service'). This will change how the locally stored directory is structured. Read [Item Folder Structure](#item-folder-structure) for more information.
- String
- Optional

outputFolder
- Path to output directory. If null, will default to current directory.
- String
- Optional

### Item Folder Structure
To make it easier to clone AGOL app item's, there are templates for different folder structures.

#### Dashboard Folder Structure
```
├── Dashboard_{itemId}
│   ├── Description.JSON
│   ├── Data.JSON
│   └── Maps
|       ├── ...
│       └── Map_{itemId}
│           ├── Description.JSON
│           ├── Data.JSON
│           └── Layers
|               ├── ...
│               └── Layer_{itemId}
│                   ├── Description.JSON
│                   └── Data.JSON
```


### Push
```python
# pushing via clone class
clone = arcgit.clone(itemId)
clone.push()

# if pushing form local clone directory
arcgit.push()
```


### Pull
```python
# pulling via clone class
clone = arcgit.clone(itemId)
clone.pull()

# if pulling from local clone directory
arcgit.pull()
```


### Merge
```python
# merging via clone class
clone = arcgit.clone(itemId)
clone.merge()

# if merging directly within AGOL
arcgit.merge(itemId, cloneId)
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
This library uses the ArcGIS REST API and ArcGIS API for Python by ESRI. This project is not affiliated or directly supported by ESRI. No modifications have been made to ESRI's software. For more information, please refer to ESRI's [license information](https://pypi.org/project/arcgis/).

Otherwise, feel free to do whatever you want with this code, but consider [buying me a cup of coffee](https://www.buymeacoffee.com/bren9966).



# Resources:
- https://towardsdatascience.com/how-to-build-and-publish-command-line-applications-with-python-96065049abc1