@echo off
setlocal enabledelayedexpansion

:: Define the source and destination folders
set "source=prod_model.keras"
set "destination=.\models"

:: Initialize the counter
set /a count=1

:: Check for existing files and increment the counter
for /f "tokens=*" %%a in ('dir /b "%destination%\*_model.keras"') do (
    set /a count+=1
)

:: Copy the production model to the models folder with the new name
copy "%source%" "%destination%\!count!_model.keras"

:: Delete the original production model
del "%source%"

:: Replace the original production model with the development model
copy "dev_model.keras" "prod_model.keras"

endlocal
