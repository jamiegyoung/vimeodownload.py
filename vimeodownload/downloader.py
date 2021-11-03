import requests
import re
# import json
import os
import sys


def __download_video(url, destination, original_url, quiet):
    with open(destination, "wb") as f:
        if not quiet:
            print("Downloading: " + original_url)
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:
            if not quiet:
                print("Unknown size, attempting to download anyway")
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                if not quiet:
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" %
                                     ('=' * done, ' ' * (50-done)))
                    sys.stdout.flush()
    if not quiet:
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
    config_url_match = re.search(
        "\"https:\\\/\\\/player\.vimeo.com\\\/video\\\/\d+?\\\/config\?.+?\"", vimeo_html.text)
    if not config_url_match.group(0):
        raise RuntimeError("Failed to get video config")
        return
    config_url = config_url_match.group(0)[1:-1].replace("\\/", "/")
    config_html = requests.get(config_url)
    return config_html.json()["request"]["files"]["progressive"]


# Only returns true if either the file doesn't exist or replace is true
def __check_if_file_exists(destination, replace):
    if os.path.isfile(destination):
        if replace:
            os.remove(destination)
            return False
        else:
            return True


def get_video(url, destination, replace=False, quiet=False):
    if not os.path.isdir(os.path.dirname(destination)):
        os.makedirs(os.path.dirname(destination))

    # Check if the video is a vimeo video before removing the replaced file
    video_options = __get_video_options(url)

    if __check_if_file_exists(destination, replace):
        raise FileExistsError(
            "File already exists (hint: enable replace if you want to replace the file)")

    video_url = __find_largest_video(video_options)["url"]
    __download_video(video_url, destination, url, quiet)
