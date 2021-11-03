# vimeodownload.py
This is a simple package that downloads public and private Vimeo videos.

***NOTE:*** *This module is not extensively tested so use at your own risk. If you do find an issue, please report it on the [GitHub repository](https://github.com/jamiegyoung/vimeo-download-py)*

## Usage
```py
vimeodownload.get_video(url, destination, replace=False, quiet=False)
```

The `quiet` argument will make the script not print any output.
The `replace` argument will overwrite existing files.

## Example
```py
import vimeodownload

vimeodownload.get_video("https://vimeo.com/148751763", "./vid.mp4")
vimeodownload.get_video("https://vimeo.com/148751763", "./other/vid.mp4", replace=True, quiet=True)
```
The above example will download a video to `./vid.mp4` with output and `./other/vid.mp4` without any output.
