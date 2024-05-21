import json

class Team:
    def __init__(self):
        self.business = False
        self.science = False
        self.upper = False
        self.lower = False
        self.members = []
        self.capacity = False

    def add_member(self, participant):
        # Add a member to the team if capacity allows.
        if len(self.members) < 4:
            self.members.append(participant)
            return True
        else:
            print("Cannot add more members, capacity reached.")
            self.capacity = True
            return False

    def update_business(self, status):
        # Update the business status of the team.
        self.business = status

    def update_science(self, status):
        # Update the science status of the team.
        self.science = status

    def update_upper(self, status):
        # Update the upper status of the team.
        self.upper = status

    def update_lower(self, status):
        # Update the lower status of the team.
        self.lower = status

# Opening JSON file
with open('participants.json') as participants:
    # Returns JSON object as a dictionary
    data = json.load(participants)

team_list = []

total_participants = len(data)
print(total_participants)
expected_teams = total_participants // 4  # will need to do some manual assignments because of truncation

def fill_team(team):
    while criteria(team) != 5 and len(team.members) < 4:
        if not find_student(team, criteria(team)):
            break

def find_student(team, selection):
    match selection:
        case 1:  # find an upper year
            for i in data:
                if int(i["Year level"]) > 2:
                    if team.add_member(i):  # add it to the team
                        data.remove(i)  # remove it from the master list
                        update_criteria(team, i)  # update the team's criteria
                        return True
            team.update_upper(True)

        case 2:  # find a business student
            for i in data:
                if i['Faculty'] == "Business":
                    if team.add_member(i):  # add it to the team
                        data.remove(i)  # remove it from the master list    
                        update_criteria(team, i)  # update the team's criteria
                        return True
            team.update_business(True)

        case 3:  # find a science student
            for i in data:
                if i['Faculty'] == "Science":
                    if team.add_member(i):  # add it to the team
                        data.remove(i)  # remove it from the master list
                        update_criteria(team, i)  # update the team's criteria
                        return True
            team.update_science(True)

        case 4:  # find a lower year
            for i in data:
                if int(i["Year level"]) <= 2:
                    if team.add_member(i):  # add it to the team
                        data.remove(i)  # remove it from the master list
                        update_criteria(team, i)  # update the team's criteria
                        return True
            team.update_lower(True)

        case 5:  # exit the loop, all conditions are met
            return False
    return False

def update_criteria(team, participant):
    # Checks participant and updates the team's criteria
    if int(participant["Year level"]) > 2:
        team.update_upper(True)
    else:
        team.update_lower(True)

    if participant['Faculty'] == "Business":
        team.update_business(True)
    elif participant['Faculty'] == "Science":
        team.update_science(True)

def criteria(team):
    if not team.upper:
        return 1
    elif not team.business:
        return 2
    elif not team.science:
        return 3
    elif not team.lower:
        return 4
    return 5

# Process
# - Fill teams one by one
# - Run the fill teams function while we still have creates teams < expected_teams
# - Keep filling the team with desired applicants until all criteria is met
# - If all criteria is met, then proceed to next team.

for _ in range(expected_teams):
    new_team = Team()
    fill_team(new_team)
    team_list.append(new_team)

# Add remaining participants to teams
for team in team_list:
    while not team.capacity and data:
        participant = data[-1]  # Get the last participant
        if team.add_member(participant):  # Try to add to the team
            data.pop()  # Remove from data if successfully added

# Print teams and remaining participants
for team in team_list:
    print("Team: ")
    for participant in team.members:
        print(participant)
    print(" ----- ")

if data:
    print("Remaining participants: ")
    for participant in data:
        print(participant)
