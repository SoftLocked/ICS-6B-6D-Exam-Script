################################################################################
# Print Exams
################################################################################

cd ../
echo "Enter directory to print: ";
read dir
for i in $dir/*.pdf
do
    echo "printing 1 file to test...";
    lpr -P _128_195_51_11 $i;
    echo "Successfully printed" $i
    break
done

echo "Confirm to print all files in directory (Warning: test file will be printed again as part of the main stack) (y/n)";

read conf
echo $conf
if [ "$conf" = "y" ]; then
    for i in $dir/*.pdf
    do
        lpr -P _128_195_51_11 $i;
        echo "Successfully printed" $i
    done
else
    echo "Exiting..."
fi