#Shell command to run Part1 in Replit:
node part1.js < data.json

#Generate Patch: (patchfile.txt)
diff -u diffexample2.js part1.js > patchfile.txt

# Apply Patch file
patch diffexample2.js < patchfile.txt

# Verify Patch
cat diffexample2.js

# Run the newly patched file
node diffexample2.js < data.json

Github: https://github.com/Cats1337/rit-iste422-project