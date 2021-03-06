
import requests
import json

print("-" * 40)
print("These are Most Popular Videos on YouTube")
print("-" * 40)

# Get the feed
r = requests.get("http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?v=2&alt=jsonc")
r.text

# Convert it to a Python dictionary
data = json.loads(r.text)

# Loop through the result.
for item in data['data']['items']:
    print("Video Title: %s" % (item['title']))

    print("Video Category: %s" % (item['category']))

    print("Video ID: %s" % (item['id']))

    print("Video Rating: %f" % (item['rating']))

    print("Embed URL: %s" % (item['player']['default']))

print()
