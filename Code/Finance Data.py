import pandas as pd
import os
import datetime

path = ""
sheet_name = "Sheet1"

df = pd.DataFrame()
for i in os.listdir(path):
 for j in os.listdir(str(path + "\\" + i)):
  td = pd.read_excel(str(path + "\\" + i + "\\" + j),sheet_name=sheet_name)
  td = td.loc[(~td["DATE"].isin(["?????","March","Multiple"]))]
  td["DATE"] = td.apply(lambda x: datetime.datetime.strptime(str(x["DATE"]),"%Y-%m-%d %H:%M:%S") if type(x["DATE"]) == "Timestamp" else x["DATE"],axis=1)
  td["DATE"] = td.apply(lambda x: datetime.datetime.strptime(str(x["DATE"]),"%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y"),axis=1)
  df = pd.concat([df,td])