# bolt-team-sorter

Currently still in testing phase!

How to test:
- clone the repository
- run $ python3 main.py
You should see an output of a list of teams each containing 4 students

Project Idea: 
Automate the process of assigning teams for club events. Takes a list of students stored in json format with attributes Year, Name, Faculty, and Student ID, and assigns them to a team which requires: 1 upper and lower year, and 1 business and science student. 

Currently using a list of 32 generated students stored in participants.json, but the idea is to be able to collect participant info from an excel sheet and convert it into json format:
- converting excel table to json: https://learn.microsoft.com/en-us/office/dev/scripts/resources/samples/get-table-data

The program will output a list of Teams, and assumes that the list of participants inputted is a multiple of 4. The user will have sort at most 3 students if there is an uneven number. 

Next Steps:
(Not implemented Yet)
- convert the returned list of Teams into a json to be converted back into an excel table: https://www.howtogeek.com/775651/how-to-convert-a-json-file-to-microsoft-excel/
- implement an interactive frontend to make it more user-friendly
- make the criteria for each team customizable
