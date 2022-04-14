def get_entry_from_collection(data, entry_id):
    for item in data["items"]:
        if item["id"] == entry_id:
            return item
    return "Record not found"
