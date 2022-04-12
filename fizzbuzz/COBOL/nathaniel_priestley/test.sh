#!/bin/bash
# remove previous files
rm 1.txt 1_diff.txt
./run.sh 1 >> 1.txt
# compare to expected
diff 1.txt 1_expected.txt >> 1_diff.txt
# asset diff is blank
file1_size=`du -k 1_diff.txt | cut -f1`

# test the file size
echo "file size = "
echo $file1_size
if [ $file1_size -gt 0 ]
then
  echo "failed test"
else
  echo "test passed"
fi
