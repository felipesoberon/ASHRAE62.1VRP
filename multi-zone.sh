#!/bin/bash

# Parallel lists (must be same length)
OCCUPANCY=(
    "Office space"
    "Conference/meeting"
    "Conference/meeting"
    "Conference/meeting"
    "Break rooms (General)"
)

AREA=(  5000  300  300  250  200)
PEOPLE=(15    10   10   8    3)
EZ=(    1.0   0.8  0.8  0.8  1.0)

N=${#OCCUPANCY[@]}

# Assemble command-line lists
OCC_ARGS=""
AREA_ARGS=""
PEOPLE_ARGS=""
EZ_ARGS=""

for ((i=0; i<N; i++)); do
  OCC_ARGS="$OCC_ARGS \"${OCCUPANCY[i]}\""
  AREA_ARGS="$AREA_ARGS ${AREA[i]}"
  PEOPLE_ARGS="$PEOPLE_ARGS ${PEOPLE[i]}"
  EZ_ARGS="$EZ_ARGS ${EZ[i]}"
done

# VRP Multi-zone recirculating system run (system_type 3)

eval python3 mainVRPconsole.py \
  -system_type 3 \
  -occupancy $OCC_ARGS \
  -area_ft2 $AREA_ARGS \
  -Ez $EZ_ARGS    > temp.txt              
# -num_people $PEOPLE_ARGS  
  
grep People temp.txt
rm temp.txt

eval python3 mainVRPconsole.py \
  -system_type 3 \
  -occupancy $OCC_ARGS \
  -area_ft2 $AREA_ARGS \
  -Ez $EZ_ARGS \
  -num_people $PEOPLE_ARGS 


