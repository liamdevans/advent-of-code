#!/bin/bash
year=$1

cd $year

for i in {1..25}
do
	mkdir $i
	cd $i
	touch $i.ipynb
	cd ..
done


