# Github Trends

This script displays a list of 20 most trending GitHub repositories 
created this week. Script outputs repository`s link, 
number of stars and open issues number. 

# How to install

Python v3.5 should be already installed. 
Then use pip (or pip3 if there is a conflict with old Python 2 setup)
to install dependecies:

```bash
pip install -r requirements.txt # alternatively try pip3
```
Remember that it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) 
for better isolation.

# Quick Start

To run script on Linux:

``` bash
$ python3 github_trending.py
Most popular repositories created this week:
https://github.com/sikaozhe1997/Xin-Yue, stars: 7269, open issues: 35
https://github.com/tensorflow/swift, stars: 1168, open issues: 1
https://github.com/cgoldsby/LoginCritter, stars: 673, open issues: 0
https://github.com/reswitched/fusee-launcher, stars: 610, open issues: 5
https://github.com/will/slacktyping, stars: 606, open issues: 0
https://github.com/francoispqt/gojay, stars: 516, open issues: 5
https://github.com/eriklindernoren/PyTorch-GAN, stars: 503, open issues: 2
https://github.com/fail0verflow/shofel2, stars: 428, open issues: 4
https://github.com/jaymeh13/keyboard-gym, stars: 366, open issues: 0
https://github.com/sksq96/pytorch-summary, stars: 267, open issues: 2
https://github.com/karpathy/pytorch-made, stars: 259, open issues: 0
https://github.com/codrops/ParticleEffectsButtons, stars: 253, open issues: 0
https://github.com/hasura/awesome-live-reloading, stars: 252, open issues: 6
https://github.com/steve-m/fl2k-examples, stars: 237, open issues: 0
https://github.com/schollz/peerdiscovery, stars: 235, open issues: 2
https://github.com/mpangburn/FunctionKit, stars: 223, open issues: 0
https://github.com/Flight-School/AnyCodable, stars: 212, open issues: 3
https://github.com/fail0verflow/switch-linux, stars: 172, open issues: 2
https://github.com/b3log/baidu-netdisk-downloaderx, stars: 171, open issues: 1
https://github.com/yuwind/HHTransition, stars: 166, open issues: 0
```
Windows usage is the same.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
