####################################################################################################
# Clean up Files and Prepare for Run
####################################################################################################

cd ../ # Leave Scripts Directory

echo "Cleaning Up output..."
rm -rf exams/tex_exams/*
rm -rf exams/pdf_exams/*

echo "Prepping Course Roster..."
python prep_roster.py

output_dir_string=$(head -c 12 /dev/urandom | base64 | tr -d /=+ | head -c 16)
echo "$RANDOM_STRING"

echo "Allocating Exams to Seats..."
echo "Generating Exam Tex Files..."
python seat_allocator.py





####################################################################################################
# Generate Tex Files
####################################################################################################





cd exams/pdf_exams
for i in ../tex_exams/*.tex;
do
    pdflatex -interaction=nonstopmode -quiet ../tex_exams/$i;
    rm *.aux
    rm *.log
    echo "$i Successfully Compiled"
done

rm ../tex_exams/*





####################################################################################################
# Print Exams
####################################################################################################





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