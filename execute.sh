################################################################################
# Clean up Files and Prepare for Run
################################################################################

cd ../ # Leave Scripts Directory

echo "Cleaning Up Output..."
rm -rf exams/tex_exams/*
rm -rf exams/pdf_exams/*


output_dir_string=$(head -c 12 /dev/urandom | base64 | tr -d /=+ | head -c 16)
echo "$RANDOM_STRING"

python main.py $RANDOM_STRING

################################################################################
# Generate Tex Files
################################################################################

cd exams/pdf_exams
for i in ../tex_exams/*.tex;
do
    pdflatex -interaction=nonstopmode -quiet ../tex_exams/$i;
    rm *.aux
    rm *.log
    echo "$i Successfully Compiled"
done

rm ../tex_exams/*