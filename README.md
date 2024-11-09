# Exam Seat Assigner and PDF Generator for ICS 6B/6D at UC Irvine

## Dependencies:
- Python 3.10+
    - Check installation with ``python --version`` or ``python3 --version``
- Pdflatex (comes with Miktex among other distributions of TeX/LaTeX)
    - Check installation with ``pdflatex --version``

## Directions for Use:
1. Clone repository into Python environment
2. Create folders for exams
    1. ``mkdir exams``
    2. ``mkdir exams/pdf_exams`` (This will store your individually compiled test pdf's)
    3. ``mkdir exams/tex_exams`` (This will store your individual test tex files)
    4. ``mkdir exams/versions`` (Store your versions in this file named [VERSIONLETTER].tex
        1. Directory must contain A.tex, B.tex, C.tex
3. Create new directory called roster (``mkdir roster``) in the root project directory
    1. Create new empty text file called "roster.txt" inside the roster directory
4. Copy text from "Display Tabbed Text" option of [WebRoster](https://www.reg.uci.edu/perl/WebRoster) for correct lecture and paste this text into roster.txt
    1. Script only works lecture-by-lecture, so run script for lecture A and B separately with different roster files
5. Run script by typing ``./run.sh`` file in a bash terminal
6. If script ran successfully, load all the generated test files into desired storage device to print exams (usually a USB flash drive)
7. To rerun script for different lectures and exams,
    1. Replace the versions in the "exams/versions" directory with new versions as needed
    2. Replace "roster.txt" file text with the "Display Tabbed Text" option of the new lecture's [WebRoster](https://www.reg.uci.edu/perl/WebRoster)
    3. Rerun the script!

Name Variable
``\newcommand{\NameVar}{STUDENT_NAME}``
NetID Variable
``\newcommand{\NetIDVar}{STUDENT_NETID}``
NumberID Variable
``\newcommand{\NetIDVar}{STUDENT_NUMID}``
Seat Variable
``\newcommand{\SeatVar}{SEAT_NUMBER}``
Version Variable
``\newcommand{\VerVar}{VER_NUMBER}``