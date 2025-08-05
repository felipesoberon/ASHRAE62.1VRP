#!/bin/bash

# Parallel lists (same length)
OCCUPANCY=(
  "Break rooms (General)"
  "Lobbies"
  "Lobbies"
  "Office space"
  "Office space"
  "Office space"
  "Office space"
  "Break rooms (General)"
  "Conference/meeting"
)

AREA=(472 878 205 78 209 204 207 102 231)
PEOPLE=(12 29 7 1 2 2 2 3 12)

N=${#OCCUPANCY[@]}

for ((i=0; i<N; i++)); do
  echo "Running: ${OCCUPANCY[i]}, area ${AREA[i]} ft2, ${PEOPLE[i]} people"
  python3 mainVRPconsole.py -occupancy "${OCCUPANCY[i]}" -area_ft2 "${AREA[i]}" -num_people "${PEOPLE[i]}"
done
