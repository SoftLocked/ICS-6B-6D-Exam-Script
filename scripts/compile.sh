echo "Compiling Tex Files..."
cd output/$1

file_count=$(ls -1 | wc -l)
index=1

for i in *.tex;
do
    pdflatex --interaction=nonstopmode $i;
    rm *.aux
    rm *.log
    percent=$(($index+1))/$file_count
    echo -ne "--- Exam $index of $file_count\r"
    ((index++))
done

rm *.tex

echo ""
echo "Compilation Complete!"

cd ../../

