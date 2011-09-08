#!/bin/sh                     
for file in $(ls *.pov); do
  povray +H512 +W512 +q11 +ua +a $file
done