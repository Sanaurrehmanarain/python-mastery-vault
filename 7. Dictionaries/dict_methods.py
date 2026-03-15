bio = {
	"name": "Sana",
	"last_name": "Rehman",
	"cast": "Arain",
	"city": "Braga",
	"height": 172,
	"weight": 88
}

bio.get("name") 
bio.pop("cast")
bio["middle_name"] = "Ur" # add middle name at the end of dict
bio.update({"d.o.b": "17 sep 1988"}) # add d.o.b at the end of the dict
bio["name"] = "Atta" # change the name from sana to atta
bio.clear()
del bio

bio.keys() # show the keys
bio.values() # show the values
bio.items() # show both keys and values
bio.popitem() # del the last key value item

# Adding Multiple Items
bio1 = {}
bio1.update({"name": "Maha", "city": "Porto", "height": 152, "weight": 68})

# Removing Multiple Items
keys_to_remove = ["city", "weight"]
for key in keys_to_remove:
    bio.pop(key, None)  # Use `None` to avoid KeyError if the key doesn't exist








