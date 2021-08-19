# ArcGit

ArcGit is a Version Control *helper library for ArcGIS Online content. ArcGit uses the ArcGIS REST API and ArcGIS API for Python. This is a helper library because it *helps developers manage versioning in ArcGIS Online, but is not a full version control library (like Git).

## Installation

Clone this repository.
```
git clone https://github.com/bren96/ArcGit.git
```

Activate Python Virtual Environment (pipenv).
```
python -m pipenv shell
```

Create AGOL_CONFIG.py in home folder.
```
agol_config = {
    'orgUrl': '',
    'user': '',
    'password': '',
    'token' : ''
}
```

Run.
```
python main.py
```

## Usage

### Clone

#### arcgit.clone_dashboard(itemID, *outputFolder)
- Creates a folder in the user's current directory, and pull the item's data
- Creates a copy of the item in AGOL and stores it in user's AGOL home folder.
- Creates a arcgit file that stores the itemId of the clone and original item

```
arcgit.clone_dashboard(c9b3dbb892442463ab065efcb96dcd81c)
```

Dashboard Folder Structure
```
Dashboard_{itemId}
    Description.JSON
    Data.JSON
    Maps
        Map_{itemId}
            Description.JSON
            Data.JSON
            Layer_{itemId}
                Description.JSON
                Data.JSON
```

### Merge
```
arcgit.merge(folderName)
```
- Can only run if there is an arcgit file in the current directory.
- If there are local changes that haven't been pushed to AGOL, FAIL (ask the user to first push there changes).
- If there are no local changes that haven't been pushed to AGOL, PUSH local JSON to original item data


### COMING SOON:

### Push
- Can only run if there is an arcit file in the current directory.
- Pushes changes to AGOL cloned items (aka push local changes to cloned item in AGOL)


### Pull
- Can only run if there is an arcit file in the current directory.
- Pull json data from AGOL cloned items (aka push AGOL changes to local directory).


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
TBD


# Resources:
- https://towardsdatascience.com/how-to-build-and-publish-command-line-applications-with-python-96065049abc1