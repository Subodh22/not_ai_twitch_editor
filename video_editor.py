from asyncio import futures
from logging import StreamHandler
from math import comb
import re

from aiohttp import streamer
import moviepy.editor
import site
from moviepy.editor import VideoFileClip,TextClip,CompositeVideoClip,concatenate_videoclips
import os,shutil
import concurrent.futures
import subprocess
from numpy import clip
import glob
import json

 

def video_namer(video_name,streamer_name):
   
   video_title=video_name.split(streamer_name)
   if(len(video_title)>2):
        
        title=streamer_name+video_title[-1]

   else:
     title=video_title[-1]
   title=title.split(".")
   title=title[0]
   title=title.replace('_',' ')
   
   return title

def text_adder_ffmpeg(steam):
   streamer_name=steam[0]
   video_name=steam[1]
   title=video_namer(video_name,streamer_name)
#    print(title)
   title_pic_name=title.replace(' ',"_")
    
   subprocess.run("""ffmpeg -nostdin -ss 00:00:05 -i """+'./'+streamer_name+'/'+video_name+""" -frames:v 1 -q:v 2 """+'./thumbnails_bg/'+streamer_name+'/'+title_pic_name+'.jpg',shell=True)
   subprocess.run("""ffmpeg -nostdin -i """+'./'+streamer_name+'/'+video_name+""" -vf drawtext="fontfile=./font/arial.ttf: text="""+title+""": fontcolor=white: fontsize=80: x=50: y=50" """+'./changed_name/'+video_name  ,shell=True)
   print("working")

def combine_ffmpeg(number,streamer_name):
    video_name=str(number)+'_'+streamer_name
    subprocess.run('ffmpeg -nostdin -f concat -i ./changed_name/mylist.txt -c copy ./output/'+streamer_name+'/'+video_name+'.mp4',shell=True)

   


def main(reser,z,streamer_name,vids_array):
    
    print(streamer_name)
    with concurrent.futures.ProcessPoolExecutor() as executer:
        net=[(streamer_name,z)for z in reser]
        executer.map(text_adder_ffmpeg,net)
    # txt_command=subprocess.run('(for %i in (./changed_name/*.mp4) do @echo file %i) > ./changed_name/mylist.txt',shell=True)
    
    os.chdir("./changed_name")
    files = glob.glob("./*")
    files.sort(key=os.path.getmtime)
    print(files)
    os.chdir("..")
    
    for i in range(len(files)):
        f =open('./changed_name/mylist.txt','a')
        j=i+1
        f.write("file "+ os.path.basename(files[len(files)-j])+"\n")
        f.close()
    youtube_title=video_namer(os.path.basename(files[0]),streamer_name)
    # print(youtube_title)
    youtube_title=youtube_title.replace(' ',"_")
    combine_ffmpeg(youtube_title,streamer_name)
    shutil.rmtree('./changed_name')
    path = os.path.join('.', 'changed_name')
    os.mkdir(path)
    filename='./video_logger/'+streamer_name+'_logger.json'
    f=open(filename)
    vid_json=json.load(f)
    vid_json[streamer_name]["videos_id"]=vids_array
    with open(filename, "w") as outfile:
        json.dump(vid_json, outfile) 
    
     
 

def looper(out_streamer):
    
    streamer_name=out_streamer
    
    main_res=[]
    res = []
    
    os.chdir("./"+streamer_name)
    files = glob.glob("./*")
    files.sort(key=os.path.getmtime)
    os.chdir("..")
    filename='./video_logger/'+streamer_name+'_logger.json'
    f=open(filename)
    vid_json=json.load(f)
    vids_array=vid_json[streamer_name]["videos_id"]
   
    for file in files:
    # check if current path is a filec
        if(os.path.basename(file).isascii()):    
            if(os.path.basename(file) in vids_array):
                print(os.path.basename(file)+": already added")
                continue
                
            res.append(os.path.basename(file))

            if len(res) % 10== 0:
                
                 main_res.append(res)
                 vids_array=vids_array+res
                 vid_json[streamer_name]["videos_id"]=vids_array
                 
                
                 res=[]
                 

                 

                          
                    
  
  
    for i in range(len(main_res)):
       
        main(main_res[i],i,streamer_name,vids_array)

if __name__=="__main__":
      
   pass
