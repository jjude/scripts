# Convert data from sqlite to text files

### How to use
1. Change sqlite db file name
2. Modify select statement
3. Modify statements in for loop to match the indices of the column you are selecting
4. Issue `carthage update --no-use-binaries` at terminal
5. Change permission for the swift file (`chmod +x main.swift`)
6. Create output directories (`out`)
7. Execute the file (`./main.swift`)
8. Script will create the .md files

_Scripts are for personal, one-off use. They don't contain error handling, or other aspects normally needed for running in production_