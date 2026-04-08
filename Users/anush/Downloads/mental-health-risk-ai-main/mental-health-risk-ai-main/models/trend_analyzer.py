import json
import os
from datetime import datetime

FILE = "risk_history.json"

def load_history():

    if not os.path.exists(FILE):
        return []

    with open(FILE,"r") as f:
        return json.load(f)

def save_history(history):

    with open(FILE,"w") as f:
        json.dump(history,f)

def update_risk(current_risk):
    
    history = load_history()

    # calculate average of last 5 risks
    risks = [entry["risk"] for entry in history[-5:]]

    if len(risks) > 0:
        avg = sum(risks) / len(risks)
    else:
        avg = 0

    final_risk = current_risk + avg * 0.25
    final_risk = min(final_risk, 1)

    # save FINAL risk instead of current risk
    history.append({
        "risk": final_risk,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })


    history = history[-20:]
    save_history(history)

    return final_risk