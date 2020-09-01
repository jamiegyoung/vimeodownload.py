import requests
import re
import json
import os
import sys

download_directory = "./downloads"

def __download_video(url, file_name):
  with open(os.path.join(download_directory, file_name), "wb") as f:
    print("Downloading video...")
    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')
    
    if total_length is None:
      print("Unknown size, attempting to download anyway")
      f.write(response.content)
    else:
      dl = 0
      total_length = int(total_length)
      for data in response.iter_content(chunk_size=4096):
        dl += len(data)
        f.write(data)
        done = int(50 * dl / total_length)
        sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
        sys.stdout.flush()
  print("\n")

def __find_largest_video(video_options):
  largest_video = {
    "index": 0,
    "url": "",
    "width": 0
  }
  
  for index, video in enumerate(video_options):
    if video["width"] > largest_video["width"]:
      largest_video["index"] = index
      largest_video["url"] = video["url"]
      largest_video["width"] = video["width"]
  return largest_video

def __get_video_options(url):
  vimeo_html = requests.get(url)
  # This may be criminal but im doing it anyway
  config_url_match = re.search("\"https:\\\/\\\/player.vimeo.com\\\/video\\\/.+?\\\/config\?.+?\"" , vimeo_html.text) 
  if not config_url_match.group(0):
    raise RuntimeError("Failed to get video config")
    return

  config_url = config_url_match.group(0)[1:-1].replace("\\/", "/")
  config_html = requests.get(config_url)
  return config_html.json()["request"]["files"]["progressive"]

def __check_if_file_exists(file_name, replace):
  if os.path.isfile(os.path.join(download_directory, file_name)):
    if replace:
      os.remove(os.path.join(download_directory, file_name))
      return False
    else:
      new_replace = input("This file already exists, do you want to replace it? (Y/N): ")
      if new_replace.lower() == "y":
        os.remove(os.path.join(download_directory, file_name))
        return False
      else:
        return True

def get_video(url, destination, replace=False):
  if not os.path.isdir(os.path.dirname(os.path.join(download_directory, destination))):
    os.makedirs(os.path.dirname(os.path.join(download_directory, destination)))

  if __check_if_file_exists(destination, replace):
    print("File already exists, not overwriting...")
    return
  video_options = __get_video_options(url)
  video_url = __find_largest_video(video_options)["url"]
  __download_video(video_url, destination)
