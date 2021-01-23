docker build -t t-tetromino/minimal .
docker run --name minimal_file_run t-tetromino/minimal
docker cp minimal_file_run:/tmp/working/output.txt output.txt

