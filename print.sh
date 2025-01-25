#!/bin/bash
################################################################################
# Print Exams
################################################################################

# Shields (Left) printer name: _128_195_51_11
# Lido (Center) printer name:  _128_195_51_13

echo "Enter directory to print: ";
read dir
echo "Enter printer name (ensure printer is set up right correct settings first): ";
read name

for i in $dir/*.pdf
do
    echo "printing 1 file to test...";
    lpr -P $name $i;
    echo "Successfully printed" $i
    break
done

echo "Confirm to print all files in directory (Warning: test file will be printed again as part of the main stack) (y/n)";

read conf
echo $conf
if [ "$conf" = "y" ]; then


for i in $dir/*.pdf
do
    while true; do
        lpr -P $name $i;

        if [[ $? -eq 0 ]]; then
            break
        else
            echo "Print Failed. Retrying in 5 seconds... | " $i
            sleep 5
        fi
    done
    echo "Successfully printed" $i
done

fi