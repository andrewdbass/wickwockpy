#!/bin/bash
source /home/reaper/Env/wickwock/bin/activate
cd /home/reaper/wickwockpy/
./manage.py get_articles
./manage.py get_videos
./manage.py get_podcasts
