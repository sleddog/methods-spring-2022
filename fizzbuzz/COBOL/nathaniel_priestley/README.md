TO OBTAIN COBOL COMPILER:

WEBSITE: https://brew.sh/
1. INSTALL HOMEBREW:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. INSTALL COBOL COMPILER:
brew install gnu-cobol

3. VERIFY COMMAND:
cobc -v


TO COMPILE:
cobc -free -x -o FizzBuzz-exe FizzBuzz


TO RUN:
./run.sh
