from opplast import Upload


upload = Upload(
    # use r"" for paths, this will not give formatting errors e.g. "\n"
    r"C:\Users\Subodh Maharjan\AppData\Roaming\Mozilla\Firefox\Profiles\b4kta5m0.Selenium",
)
 
was_uploaded, video_id = upload.upload(
    r"C:\Users\Subodh Maharjan\Desktop\new_uploader_modules\opplast-1.0.14\3_xqc.mp4",
    title="s2",
    description="s22",
    thumbnail=r"C:\Users\Subodh Maharjan\Desktop\new_uploader_modules\opplast-1.0.14\14.png",
    tags=["these", "are", "my", "tags"],
    only_upload=False # If True will not set title, description or anything else. 
    # Might be useful if you want to do it manually or by using the YouTube API.
)

if was_uploaded:
    print(f"{video_id} has been uploaded to YouTube")

upload.close()