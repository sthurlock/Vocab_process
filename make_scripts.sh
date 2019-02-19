rm -f do_tess do_process
ls *.jpg | awk '{print "tesseract "$1,$1}' > do_tess
ls *.jpg | awk '{print "python3 process_vocab.py "$1".txt"}' > do_process
chmod +x do_tess do_process


