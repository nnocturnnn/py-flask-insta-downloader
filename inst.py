import os


profile = "nnnocturn"
lol = "2018, 5, 31"
kek = "2017, 5, 21"
os.system(f"Instaloader  --post-filter=\"date_utc <= datetime({lol}) and date_utc >= datetime({kek})\" --no-metadata-json --no-videos {profile}")