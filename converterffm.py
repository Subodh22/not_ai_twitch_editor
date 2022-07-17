import subprocess
import os
from numpy import diff, number 
from video_editor import looper
from thumbnail_maker import mainer
from master import upload_to_yt
import sys
import getopt
import json
import shutil
import glob

arg_streamer = ""
arg_videonum = ""
def myfunc(argv):
    global arg_videonum
    global arg_streamer
    arg_help = "{0} -s <streamer> -v <videonum> ".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hs:v:", ["help", "streamer=", 
        "videonum="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-s", "--streamer"):
            arg_streamer = arg
        elif opt in ("-v", "--videonum"):
            arg_videonum = arg
         

    print('streamer:', arg_streamer)
    print('videonumber:', arg_videonum)
   
def not_ai():
   f=open('./video_logger/'+arg_streamer+'_logger.json')
   hash_json=json.load(f)
#    number_of_vids=str(len(hash_json[arg_streamer]["videos_id"])+int(arg_videonum))
   number_of_vids=int(arg_videonum)
   os.chdir('./'+arg_streamer)
    
#    probe2=subprocess.run('twitch-dl clips '+arg_streamer+' --download --period last_week --limit '+number_of_vids,shell=True)
#    files = glob.glob("./*")
#    h=int(number_of_vids)
#    if(len(files)<h):
#     differnce=str((h-len(files))+h)
#     print(differnce)
#     probeh=subprocess.run('twitch-dl clips '+arg_streamer+' --download --period last_week --limit '+differnce,shell=True)
#    files = glob.glob("./*")
   h=int(arg_videonum)
   download_switch=True
   while download_switch:
   
    print(h)
    probe2=subprocess.run('twitch-dl clips '+arg_streamer+' --download --period last_week --limit '+str(h),shell=True)
    files = glob.glob("./*")
    if(len(files)<number_of_vids):
        h=(h-len(files))+number_of_vids
    else:
        download_switch=False



   
   os.chdir('..')
    
   print(len(files))
   if len(files)>=10:
        looper_bol=True
        while(looper_bol):
            try:
                print("bombom")
                looper(arg_streamer)
                looper_bol=False
            except:
                looper_bol=True
                shutil.rmtree('./changed_name')
                path = os.path.join('.', 'changed_name')
                os.mkdir(path)
    
        
        mainer(arg_streamer)
            
        upload_to_yt(arg_streamer)
    
        
# def cheat():
#     looper("xqc")
#     mainer("xqc")
  
#     upload_to_yt("xqc")
 
if __name__ == "__main__":
    #  cheat()
    myfunc(sys.argv)
    not_ai()
 