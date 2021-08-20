### COMING SOON:

### Clone
- Creates a folder in the user's current directory, and pull the item's data
- Creates a copy of the item in AGOL and stores it in user's AGOL home folder.
- Creates a arcgit file that stores the itemId of the clone and original item

### Merge
- Can only run if there is an arcgit file in the current directory.
- If there are local changes that haven't been pushed to AGOL, FAIL (ask the user to first push there changes).
- If there are no local changes that haven't been pushed to AGOL, PUSH local JSON to original item data

### Push
- Can only run if there is an arcit file in the current directory.
- Pushes changes to AGOL cloned items (aka push local changes to cloned item in AGOL)


### Pull
- Can only run if there is an arcit file in the current directory.
- Pull json data from AGOL cloned items (aka push AGOL changes to local directory).