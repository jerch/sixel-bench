## Sixel performance benchmark


To run the benchmark, unzip the data file and execute the python script:

```bash
gzip -d data.sixel.gz
python3 run.py
```


**Note:** To avoid false high throughput artefacts by aggressive prebuffering,
the script waits for a cursor position report sent from the terminal after the Sixel data.



### Credits


- The test data was extracted from the movie "Sintel" created by the Blender Foundation, licensed under the Creative Commons Attribution 3.0 license.
- Movie conversion was done with `mpv` and their new sixel video output with this command:
  ```bash
  mpv sintel_short.mp4 --vo=sixel --vo-sixel-width=320 --vo-sixel-height=200 --profile=sw-fast --vo-sixel-fixedpalette=no --vo-sixel-reqcolors=256 --really-quiet > data.sixel
  ```
