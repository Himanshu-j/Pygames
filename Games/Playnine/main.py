from random import randrange as rrange


def check_state(statedict):
    choice = statedict.get("Choice")
    testno = statedict.get("testno")
    refresh_av = statedict.get("Refresh")
    if refresh_av > 0:
        return True
    elif refresh_av == 0:
        for c in choice:
            if testno == c:
                return True
            else:
                return False


def save_state():
    pass


def start_game(resume_game, statedict):
    if resume_game:
        save_state()
    else:
        Score = play(statedict)
        print(Score)


def play(statedict):
    Refresh_av = statedict.get("Refresh")
    gmsg = "Playing game."
    try:
        choice_av = len(statedict.get("Choice"))
        while Refresh_av >= 0 or choice_av > 0:
            for key in statedict:
                print(key, "=", statedict.get(key))
            result = check_state(statedict)
            if not result:
                return statedict.get("Score")
            print("Press R to refresh or Enter to continue.")
            uinp3 = raw_input()
            if uinp3 == "r" or uinp3 == "R":
                Refresh_av -= 1

                new_testno = rrange(1, 10)
                statedict.update(dict({"Testno.": new_testno}))

                new_refresh = Refresh_av
                statedict.update(dict({"Refresh": new_refresh}))
                continue

            if statedict.get("Refresh") > 0:
                print("Please input your options.")
                uipt1 = raw_input()
                uipt2 = raw_input()

                if not(uipt2):
                    sum = int(uipt1)
                    statedict.get("Choice").remove(sum)
                else:
                    sum = int(uipt1) + int(uipt2)
                    statedict.get("Choice").remove(int(uipt1))
                    statedict.get("Choice").remove(int(uipt2))
                choice_av = len(statedict.get("Choice"))
                if sum == statedict.get("Testno."):

                    new_testno = rrange(1, 10)
                    statedict.update(dict({"Testno.": new_testno}))

                    new_Score = statedict.get("Score") + 1
                    statedict.update(dict({"Score": new_Score}))

                else:
                    return statedict.get("Score")
            elif statedict.get("Refresh") == 0:
                if statedict.get("Testno.") not in statedict.get("Choice"):
                    return statedict.get("Score")
        return statedict.get("Score")
    except Exception as e:
        emsg = e.message
        print("Error while {} Details:{}".format(gmsg, emsg))


def create_setup():
    resume_game = False
    statedict = {"Testno.": rrange(1, 10), "Choice": [1, 2, 3, 4, 5,
                                                               6, 7, 8, 9],
                 "Score": 0, "Refresh": 5}
    start_game(resume_game, statedict)


def new_game():
    create_setup()


if __name__ == "__main__":
    new_game()
