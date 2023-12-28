#!/bin/bash

DIR = "portfolio\static\portfolio\pictures"
cd $DIR

python3 manage.py shell

from django.db import models
from portfolio.models import Works

