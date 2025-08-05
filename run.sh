#!/bin/bash

# Parallel lists (same length)
OCCUPANCY=(
  "Classrooms (age 9 plus)"
  "Lecture classroom"
)
AREA=(500 1000 )
PEOPLE=(15 30 )

N=${#OCCUPANCY[@]}

for ((i=0; i<N; i++)); do
  echo "Running: ${OCCUPANCY[i]}, area ${AREA[i]} ft2, ${PEOPLE[i]} people"
  python3 mainVRPconsole.py -occupancy "${OCCUPANCY[i]}" -area_ft2 "${AREA[i]}" -num_people "${PEOPLE[i]}"
done
