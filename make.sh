################################################################################
# Clean up Files and Prepare for Run
################################################################################


output_dir_string=$(head -c 12 /dev/urandom | base64 | tr -d /=+ | head -c 10)

python scripts/main.py $output_dir_string

./scripts/compile.sh $output_dir_string