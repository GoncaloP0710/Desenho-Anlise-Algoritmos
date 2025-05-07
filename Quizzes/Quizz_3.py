# You have a list of tasks that need to be performed. Each task requires a minimum amount of work. You also have a list of teams that can output a certain amount of work. Each team can be assigned to one task, if their work output is equal or larger than the work required for that task.

# Define function max_tasks, that receives a list of tasks (ie, their minimum amount of work) and a list of teams (ie, their work output), and return the maximum number of tasks that can be assigned to an available team.

def max_tasks(tasks, teams):
    # Sort the tasks and teams in ascending order
    tasks.sort()
    teams.sort()

    # Initialize variables to keep track of the number of tasks assigned and the current team index
    assigned_tasks = 0
    team_index = 0

    # Iterate through each task
    for task in tasks:
        while team_index < len(teams) and teams[team_index] < task:
            # If the current team's work output is less than the task's minimum work, move to the next team
            team_index += 1
        # Check if there are still teams available to assign to the task
        if team_index < len(teams):
            # If the current team's work output is greater than or equal to the task's minimum work, assign the task to the team
            if teams[team_index] >= task:
                assigned_tasks += 1  # Increment the count of assigned tasks
                team_index += 1  # Move to the next team for the next task

    return assigned_tasks  # Return the total number of tasks that can be assigned


tasks = [250,490,328,149,495,325,1314,360,333,418,430,458]
teams = [376,71,228,110,215,410,363,135,508,268,494,288,24,362,20,5,247,
  118,152,393,458,354,201,188,425,167,220,114,148,43,403,385,512,459,71,
  425,142,102,361,102,232,203,25,461,298,437,252,364,171,240,233,257,305,
  346,307,408,163,216,243,261,137,319,33,91,116,390,139,283,174,409,191,
  338,123,231,101,458,497,306,400,513,175,454,273,88,169,250,196,109,505,
  413,371,448,12,193,396,321,466,526,276,276,198,260,131,322,65,381,204,
  32,83,431,81,108,366,188,443,331,102,72,496,521,502,165,439,161,257,324]
print(max_tasks(tasks, teams))


# You are playing a 2D video game where there are many rectangle-shaped alien ships that must be destroyed
# You have a lazer at the ground that can shoot vertically, destroying any ship that lies of that column. You need to destroy the entire alien fleet with the smaller number of lazer shoots possible.
# Define function min_lazer_shoots that receives a list of pairs [x0,x1] representing the x-coordinates of each alien ship (ie, where it begins and where it ends), and returns the minimum number of shoots needed to destroy the entire fleet.


def min_lazer_shots(intervals):
    # Sort the intervals based on their starting points
    intervals.sort(key=lambda x: x[0])

    # Iterate through the intervals and get the number that catches the most ships
    shots = []
    for start, end in intervals:
        # If the shots list is empty or the current interval does not overlap with the last shot, add a new shot
        if not shots or start > shots[-1]:
            shots.append(end)
        else:
            # Update the last shot to the minimum of the current end and the last shot
            shots[-1] = min(shots[-1], end)

    # Return the number of shots needed
    return len(shots)


ships = [[1,2],[2,3],[3,4],[4,5]]
print(min_lazer_shots(ships))
ships = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
print(min_lazer_shots(ships))


# Define function smallest_unique_letters that receives a string s of letters and returns the smallest lexicographic string with  the unique letters of s (ie, without letter repetitions)

def smallest_unique_letters(s):

    str = s
    solution = []

    # Sort the unique letters in lexicographic order
    for letter in str:
        if letter not in solution:
            for i in range(len(solution)):
                if (ord(solution[-1]) > ord(letter) and solution[-1] in str):
                    solution.pop()
            solution.append(letter)
            str = str.replace(letter, "", 1)
            

    return ''.join(solution)

print(smallest_unique_letters("bcabc"))
print(smallest_unique_letters("thesqtitxyetpxloeevdeqifkz"))
