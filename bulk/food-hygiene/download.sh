#!/bin/sh

# curl files sent from stdin

url="$1"
dir="$2"
set -e

curl --silent --location "$url" |
  grep 'http://ratings.food.gov.uk/OpenDataFiles' |
  sed -e 's/^.*href="//' -e 's/".*$//' |
  while read url
  do
    file=$dir$(basename "$url")
    z=""
    [ -f "$file" ] && z="-z $file"
    curl $z -o "$file" --silent --location "$url" --write-out "$file	%{http_code}\n"
  done
