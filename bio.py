from pyrogram import Client
import time
import schedule
import requests
from datetime import datetime
import pytz


api_id = 
api_hash = ""
def timezone():
        tz_te = pytz.timezone('Asia/Tehran')
        datetime_te = datetime.now(tz_te)
        IranDatetime = datetime_te.strftime("%Y/%m/%d %H:%M")
        my_bio = "The text u want: {}".format(IranDatetime)
        with Client("OkBye", api_id, api_hash) as app:
            app.update_profile(bio = my_bio)

schedule.every(1).seconds.do(timezone)
while True:
    schedule.run_pending()
    time.sleep(1)
