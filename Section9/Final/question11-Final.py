# 11. برنامه ای بنویسید که تغییرات یک فایل را از نظر محتوا مدیریت کند و در صورت تغییر محتوا، فایل را چاپ کند.

import datetime
import os

def file_content_changer(file_path, new_content):
    now = datetime.datetime.now()
    date_time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_content = f.read()
    except FileNotFoundError:
        original_content = ""

    if original_content != new_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"{date_time_string}: محتوای فایل تغییر کرد:")  # File content changed:
        with open(file_path, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print(f"{date_time_string}: محتوای فایل تغییری نکرد.") 

file_path = "example.txt"
new_content = "این یک محتوای جدید است."  # This is a new content.
file_content_changer(file_path, new_content)
