#!/bin/bash

INPUT_DIR=/backup/russet/
CODE_DIR=/backup/russet/russet
ARCHIVE_DIR=/backup/russet/done
SECRET_FILE=/backup/russet/russet/.secret.sh

cd $CODE_DIR

source venv/bin/activate
source $SECRET_FILE
mkdir -p $ARCHIVE_DIR

find_files_to_process() {
    find ${INPUT_DIR} -maxdepth 1 -name \*png -type f 
}

process_file() {
    FILE="$1"
    ./russet.py send_image_data $FILE
}

archive_file() {
    FILE="$1"
    mv $FILE ${ARCHIVE_DIR}/
}

find_files_to_process | while read file ; do
    process_file $file && \
	archive_file $file
done
