python prep_roster.py
rm -rf exams/tex_exams/*
python seat_allocator.py

rm -rf exams/pdf_exams/*

# Compile Exam Tex's
cd exams/pdf_exams;
for i in ../tex_exams/*.tex;
do
    pdflatex -interaction=nonstopmode -quiet ../tex_exams/$i;
    rm *.aux
    rm *.log
    echo "$i Successfully Compiled"
done

rm ../tex_exams/*.tex