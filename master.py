 
from cmath import e
import pathlib
import subprocess
import os 
import glob
import json
from opplast import Upload
import shutil
 
def cleaner(streamer_name):
    shutil.rmtree('./act_thumbnails/'+streamer_name)
    path = os.path.join('.', './act_thumbnails/'+streamer_name)
    os.mkdir(path)
    shutil.rmtree('./output/'+streamer_name)
    path = os.path.join('.', './output/'+streamer_name)
    os.mkdir(path)
    shutil.rmtree('./thumbnails_bg/'+streamer_name)
    path = os.path.join('.', './thumbnails_bg/'+streamer_name)
    os.mkdir(path)
    shutil.rmtree('./'+streamer_name)
    path = os.path.join('.', './'+streamer_name)
    os.mkdir(path)
 


 
def upload_to_yt(streamer_name):
    os.chdir("C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\output\\"+streamer_name)
    files = glob.glob("./*")
    files.sort(key=os.path.getmtime)
    
    os.chdir("..")
    os.chdir("..")
    os.chdir("C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\act_thumbnails\\"+streamer_name)
    img_files = glob.glob("./*")
    os.chdir("..")
    os.chdir("..")
    f=open('./hashtags.json')
    hash_json=json.load(f)
    streamer_hash=hash_json[streamer_name]["hashtags"]
    description = hash_json[streamer_name]["des"]+" "+streamer_hash
    tagers=hash_json[streamer_name]["tags"]
    mozi_id=hash_json[streamer_name]["mozi_id"]
     
    # description="balls"
    for i in range(len(files)):
       
        
        if(img_files[i]!=" "):
            
            img_files_name=os.path.basename(img_files[i]).split('.')
            video_name_yt=img_files_name[0].replace('_',' ')
            if(video_name_yt==" "):
                video_name_yt=streamer_name
            video_name_yt= video_name_yt+ " - " +streamer_name+ " Stream Highlights"
            print(video_name_yt)
            video_name_yt=video_name_yt.upper()
            upload = Upload(
        # use r"" for paths, this will not give formatting errors e.g. "\n"
            mozi_id,
            )

            repeat=True
            while(repeat):
                try:
                    was_uploaded, video_id = upload.upload(
                    "C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\output\\"+streamer_name+"\\"+os.path.basename(files[i]),
                    title=video_name_yt,
                    description=description,
                    thumbnail="C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\act_thumbnails\\"+streamer_name+"\\"+img_files[i],
                    tags=tagers,
                    only_upload=False # If True will not set title, description or anything else. 
                    # Might be useful if you want to do it manually or by using the YouTube API.
                    )
                    repeat=False
                except :
                    repeat=True
                    
                    print("Bad upload Trying Again")


            if was_uploaded:
                print(f"{video_id} has been uploaded to YouTube")

            upload.close()

    cleaner(streamer_name)


if __name__ == "__main__":
   pass
 