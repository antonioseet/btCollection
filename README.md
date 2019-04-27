# btCollection
Collects Bluetooth information (name and address) of discoverable devices nearby into text files.

# current issue(s)
When reading source names file, splits them up by spaces and new lines, we just want to truncate by new lines.
This causes us to have more names than addresses.
    - Problem only occours when reading the file for the initial run.
	-When the problem is fixed, BTnames should match BTnames2. (in terms of spaces in names)
    - Once fixed, we can optimize code to use only one loop instead of two.