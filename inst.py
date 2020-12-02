import os


post_link = "asaprocky: 2018, 5, 31-2017, 5, 21"
name_date = post_link.split(":")
f_data = name_date[1].split('-')[1]
s_data = name_date[1].split('-')[0]
os.system(f"Instaloader  --post-filter=\"date_utc <= datetime({f_data}) and date_utc >= datetime({s_data})\" --dirname-pattern static/{name_date[0]} --no-metadata-json --no-videos {name_date[0]}")
imgs = os.listdir("static/"+name_date[0]+"/")
for i in imgs:
    if "_id" in i:
        imgs.remove(i)
print(imgs)