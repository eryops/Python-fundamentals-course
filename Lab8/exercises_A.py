class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)

    def __repr__(self):
        return f'name: {self.name} members: {self.members}'

class Team:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []

    def add_member(self, member):
        self.members.append(member)

    def __repr__(self):
        return f'name: {self.name} members: {self.members}'

badTeam1 = BadTeam('Bad Team 1')
badTeam2 = BadTeam('Bad Team 2')

badTeam1.add_member('Jonas')

print(badTeam1)
print(badTeam2)

team1 = Team('Team 1')
team2 = Team('Team 2')

team1.add_member('Jonas')

print(team1)
print(team2)