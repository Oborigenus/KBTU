import json, os

DEFAULT_SETTINGS={"sound":True,"difficulty":"normal","car_color":"red"}


def load_settings():
    if not os.path.exists("settings.json"):
        return DEFAULT_SETTINGS
    with open("settings.json") as f:
        return json.load(f)


def save_settings(s):
    with open("settings.json","w") as f:
        json.dump(s,f,indent=4)


def load_scores():
    if not os.path.exists("leaderboard.json"):
        return []
    with open("leaderboard.json") as f:
        return json.load(f)


def save_score(name, score, distance):
    data = load_scores()
    data.append({"name":name,"score":score,"distance":distance})
    data = sorted(data,key=lambda x:x["score"],reverse=True)[:10]
    with open("leaderboard.json","w") as f:
        json.dump(data,f,indent=4)
