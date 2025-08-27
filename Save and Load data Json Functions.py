def save_data():
    data = {
        "NA_total": NA_total,
        "A_total": A_total,
        "M_total": M_total,
        "E_total": E_total
    }
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"NA_total": 0, "A_total": 0, "M_total": 0, "E_total": 0}

saved_data = load_data()