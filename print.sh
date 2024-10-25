
echo "Enter directory to print: ";
read dir
for i in $dir/*.pdf
do
    echo "printing 1 file to test...";
    echo $i;
    break
done

echo "Confirm to print all files in directory (y/n)";
read conf
echo $conf
if [ "$conf" = "y" ]; then
    for i in $dir/*.pdf
    do
        echo $i;
        echo "Successfully printed" $i
    done
else
    echo "Exiting..."
fi