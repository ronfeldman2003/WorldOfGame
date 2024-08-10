from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    score_points = (difficulty*3)+5
    try:
        file = open(SCORES_FILE_NAME, "r")
        score_current = int(file.read())
        file.close()
        file = open(SCORES_FILE_NAME, "w")
        file.write(str(score_current+score_points))
    except FileNotFoundError:
        file = open(SCORES_FILE_NAME, "w")
        file.write(str(score_points))


