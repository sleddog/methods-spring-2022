
#!/bin/bash
# remove previous files
rm 1.txt 1_diff.txt
./runMod.sh 1 >> 1.txt
# compare to expected
diff 1.txt 1_expected.txt >> 1_diff.txt
# asset diff is blank
file1_size=`du -k 1_diff.txt | cut -f1`

# test the file size
echo "file size = "
echo $file1_size
if [ $file1_size -gt 0 ]
then
  echo "Size 1: test failed"
else
  echo "Size 1: test passed"
fi

	# TEST WITH 10
# remove previous files
rm 10.txt 10_diff.txt
./runMod.sh 10 >> 10.txt
# compare to expected
diff 10.txt 10_expected.txt >> 10_diff.txt
# asset diff is blank
file10_size=`du -k 10_diff.txt | cut -f1`

# test the file size
echo "file size = "
echo $file10_size
if [ $file10_size -gt 0 ]
then
  echo "Size 10: test failed"
else
  echo "Size 10: test passed"
fi

        # TEST WITH 25
# remove previous files
rm 25.txt 25_diff.txt
./runMod.sh 25 >> 25.txt
# compare to expected
diff 25.txt 25_expected.txt >> 25_diff.txt
# asset diff is blank
file25_size=`du -k 25_diff.txt | cut -f1`

# test the file size
echo "file size = "
echo $file25_size
if [ $file25_size -gt 0 ]
then
  echo "Size 25: test failed"
else
  echo "Size 25: test passed"
fi

        # TEST WITH 50
# remove previous files
rm 50.txt 50_diff.txt
./runMod.sh 50 >> 50.txt
# compare to expected
diff 50.txt 50_expected.txt >> 50_diff.txt
# asset diff is blank
file50_size=`du -k 50_diff.txt | cut -f1`

# test the file size
echo "file size = "
echo $file50_size
if [ $file50_size -gt 0 ]
then
  echo "Size 50: test failed"
else
  echo "Size 50: test passed"
fi

        # TEST WITH 70
# remove previous files
rm 70.txt 70_diff.txt
./runMod.sh 70 >> 70.txt
# compare to expected
diff 70.txt 70_expected.txt >> 70_diff.txt
# asset diff is blank
file70_size=`du -k 70_diff.txt | cut -f1`

# test the file size
echo "file size = "
echo $file70_size
if [ $file70_size -gt 0 ]
then
  echo "Size 70: test failed"
else
  echo "Size 70: test passed"
fi

        # TEST WITH 98
# remove previous files
rm 98.txt 98_diff.txt
./runMod.sh 98 >> 98.txt
# compare to expected
diff 98.txt 98_expected.txt >> 98_diff.txt
# asset diff is blank
file98_size=`du -k 98_diff.txt | cut -f1`

# test the file size
echo "file size = "
echo $file98_size
if [ $file98_size -gt 0 ]
then
  echo "Size 98: test failed"
else
  echo "Size 98: test passed"
fi

        # TEST WITH 100
# remove previous files
rm 100.txt 100_diff.txt
./runMod.sh 100 >> 100.txt
# compare to expected
diff 100.txt 100_expected.txt >> 100_diff.txt
# asset diff is blank
file100_size=`du -k 100_diff.txt | cut -f1`

# test the file size
echo "file size = "
echo $file100_size
if [ $file100_size -gt 0 ]
then
  echo "Size 100: test failed"
else
  echo "Size 100: test passed"
fi

