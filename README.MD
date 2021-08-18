Activate Python Virtual Environment
c:\users\brend\appdata\local\programs\python\python39\python.exe -m pipenv shell

Run
python main.py






arcgit clone [itemeId] [type]

    Creates a folder in the user's current directory, and pull the item's data
    Creates a copy of the item in AGOL and stores it in user's AGOL home folder.
    Creates a arcgit file that stores the itemId of the clone and original item
    
    cloneId : Id of the AGOL Item.

    ex:
    arcgit clone -c9b3dbb892442463ab065efcb96dcd81c -dashboard

    dashboard folder structure
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


arcgit push

    Can only run if there is an arcit file in the current directory.
    Pushes changes to AGOL cloned items (aka push local changes to cloned item in AGOL)


arcgit pull

    Can only run if there is an arcit file in the current directory.
    Pull json data from AGOL cloned items (aka push AGOL changes to local directory).



arcgit merge

    Can only run if there is an arcgit file in the current directory.
    If there are local changes that haven't been pushed to AGOL, FAIL (ask the user to first push there changes).
    If there are no local changes that haven't been pushed to AGOL, PUSH local JSON to original item data








Resources:
- https://towardsdatascience.com/how-to-build-and-publish-command-line-applications-with-python-96065049abc1