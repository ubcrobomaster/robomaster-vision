# Autoaim
See the code [architecture diagram](https://app.diagrams.net/#G1Gtw_IO4ovWzlRxqMIo0SwGJ7QCxx_Pnp).

Apart from in-code comments, we host [guides and documentation](https://ubcrobomaster.slite.com/app/channels/dA4dO1hHij/notes/ZYTtyAq~lp) on the vision Slite channel.

[Autoaim Intro](https://ubcrobomaster.slite.com/app/channels/dA4dO1hHij/notes/xn1FDEEL2l) provides a general introduction to get you started. The following more specific guides are also available.
* [Panel Classifier](https://ubcrobomaster.slite.com/app/channels/dA4dO1hHij/notes/PBxt9ou6BB) for how to train, convert, and do inference with our panel classification model.
* [Raspberry Pi Setup](https://ubcrobomaster.slite.com/app/channels/dA4dO1hHij/notes/dBspLGe9VC) for how to setup a Pi to run our source code.

More documentation is always welcome!


## Getting Started
* Install Python 3.8 or above
* Run `pip install -r requirements.txt` to obtain required packages
* Run autoaim on your camera feed or a video obtained from [Drive](https://drive.google.com/drive/folders/1YaJ2r4S1ThzvY1khYDgWm0C09EJl-k43)

## Notes
* If using conda, run `conda install -c menpo opencv` to install OpenCV
* If using PyCharm, mark all module directories as Sources Root to avoid import errors
