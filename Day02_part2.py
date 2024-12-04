input = open("input.txt", "r")

# Function to compare 2 levels, dynamic to the reports interval direction
def isLevelOkay(direction, level1, level2):

    difference = int(level1) - int(level2)

    if direction == "ascending":
        difference = difference * -1
        return(difference <= 3 and difference >= 1)
    if direction == "descending":
        return(difference <= 3 and difference >= 1)

# Create a list of reports where each report is a list of levels
data = []
for line in input:
    data.append(line.split())

# If a report is deemed safe, increase safeCount by 1
safeCount = 0

# Debug variables
isSafeTriggered = 0
thisLevelsBad = 0
theNextLevelsBad = 0
reportsAnalyzed = 0


for report in data: # pulls each report from the list of reports

    reportsAnalyzed += 1 # debug
    isSafe = True # opted to assume each report is safe since I only need to detect one error to deem a report unsafe
    didDampen = False # if didDampen is True when attempting to dampen a report (2nd dampen), report will be unsafe
    direction = '' # Used to store direction

    dampenCount = 0 # initially debug, but now a fail safe for didDampen

    # Determine if report is increasing or decreasing
    if int(report[0]) == int(report[1]): # If first 2 levels are the same,  it can be dampened
        didDampen = True
        dampenCount += 1 # I shouldn't need these two lines, but they somehow make a difference
        if int(report[1]) > int(report[2]): direction = "descending"
        else: direction = "ascending"

    elif int(report[0]) > int(report[1]): direction = "descending"
    else: direction = "ascending"

    for level in range(len(report) - 1):
        if not isLevelOkay(direction, report[level], report[level + 1]): # check if level is ok

            isSafe = False # Assume level's unsafe. If dampened, then rectified
            isSafeTriggered += 1 # debug

            if dampenCount >= 2 or didDampen: break # if report is already dampened, break the loop, isSafe will be false, report won't be counted

            if level > 0: # index out of bounds check to test dampening current level in the report
                if isLevelOkay(direction, report[level - 1], report[level + 1]): # Check previous level against next level to see if current level is the problem
                    didDampen = True
                    dampenCount += 1
                    thisLevelsBad += 1 # debug
                    isSafe = True # rectify

            if level < len(report) - 2: # index out of bounds check
                if isLevelOkay(direction, report[level], report[level + 2]): # Checking current level against 2 levels ahead
                    didDampen = True
                    dampenCount += 1
                    theNextLevelsBad += 1 # debug
                    isSafe = True # rectify
                    level += 1 # if next level is the problem, need to skip it in the loop

    if isSafe and dampenCount <= 1:
        safeCount += 1

print("reportsAnalyzed = " + str(reportsAnalyzed))
print("isSafeTriggered = " + str(isSafeTriggered))
print("thisLevelsBad = " + str(thisLevelsBad))
print("theNextLevelsBad = " + str(theNextLevelsBad))
print(safeCount)





