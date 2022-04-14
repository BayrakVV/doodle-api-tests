def get_entry(set, id):
    for i in set["items"]:
        if i["id"] == id:
            return i
    return "Record not found"
