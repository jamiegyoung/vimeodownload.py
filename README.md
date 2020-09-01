# vimeo-download-py
This is a simple module that downloads private and public vimeo videos.

```py
vimeo.get_video(url, destination, replace=False)
```

## Example
The below example will download a video to `./downloads/vid.mp4` and `./downloads/other/vid.mp4`.

```py
import vimeo_download as vimeo

vimeo.get_video("https://vimeo.com/148751763", "vid.mp4")
vimeo.get_video("https://vimeo.com/148751763", "/other/vid.mp4")
```

This example is the same but instead downloads to `./videos/vid.mp4` and `./videos/bob/vid.mp4`. It will also replace `./vidoes/vid.mp4` if it is found without prompt.
```py
import vimeo_download as vimeo

vimeo.download_directory = "./videos"
vimeo.get_video("https://vimeo.com/148751763", "vid.mp4", True)
vimeo.get_video("https://vimeo.com/148751763", "bob/vid.mp4")
```
