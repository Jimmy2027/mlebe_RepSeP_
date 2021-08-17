#!/usr/bin/env bash

rsync -avP poster.pdf jimmy:~/ppb/ || exit 1
echo  https://hendrikklug.xyz/ppb/poster.pdf