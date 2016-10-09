#!/bin/sh

export DROPBOX_FOLDER="$HOME/Dropbox"
export folders=( files posts presentations stories weeklies )

for what in "${folders[@]}"
do
echo "Symlinking $what..."
ln -s "$DROPBOX_FOLDER/blog/$what" "$what"
done
echo "Done!"
