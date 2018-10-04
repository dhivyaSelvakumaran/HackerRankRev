def countingValleys(n, s):
    currentLevel = 0
    valley = 0
    for step in s:
        if step == 'D':
            currentLevel -= 1
        else:
            if currentLevel == -1:
                valley += 1
            currentLevel += 1
    return valley
