import json
import os
import glob

# Step 1: Load all follower files
follower_usernames = set()
follower_files = sorted(glob.glob("followers_*.json"))

for filename in follower_files:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        for entry in data:
            try:
                username = entry["string_list_data"][0]["value"]
                follower_usernames.add(username)
            except (KeyError, IndexError, TypeError):
                continue  # Skip if entry is malformed

# Step 2: Load following file
following_usernames = set()
with open("following.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    following_data = data.get("relationships_following", [])
    print(f"Loaded {len(following_data)} entries from following.json")
    for entry in following_data:
        try:
            username = entry["string_list_data"][0]["value"]
            following_usernames.add(username)
        except (KeyError, IndexError, TypeError):
            continue  # Skip if entry is malformed


# Step 3: Compare
not_following_back = following_usernames - follower_usernames

# Step 4: Output
print(f"Total people you follow: {len(following_usernames)}")
print(f"People not following you back: {len(not_following_back)}\n")

with open("not_following_back.txt", "w", encoding="utf-8") as f:
    for username in sorted(not_following_back):
        f.write(username + "\n")

print("List saved to not_following_back.txt ✅")