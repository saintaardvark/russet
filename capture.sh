#!/bin/bash

mkdir data
raspistill -e png -o data/"russet-$(date +'%s').png"
