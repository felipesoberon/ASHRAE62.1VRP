@echo off
setlocal EnableDelayedExpansion

set COUNT=2

set OCC_1=Classrooms (age 9 plus)
set OCC_2=Lecture classroom

set AREA_1=500
set AREA_2=1000

set PEOPLE_1=15
set PEOPLE_2=30

for /L %%I in (1,1,%COUNT%) do (
    set "OCC=!OCC_%%I!"
    set "AREA=!AREA_%%I!"
    set "PEOPLE=!PEOPLE_%%I!"
    echo Running: !OCC!, area !AREA! ft2, !PEOPLE! people
    python mainVRPconsole.py -occupancy "!OCC!" -area_ft2 !AREA! -num_people !PEOPLE!
)

