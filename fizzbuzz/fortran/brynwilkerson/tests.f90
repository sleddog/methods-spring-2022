Program tests

	USE fizz
	implicit none
	

	if (fizzString(3) /= "Fizz") then
		print *, "Test 3 failed"
	else if (fizzString(2) /= "2") then
		print *, "Test 2 failed"
	else if (fizzString(109) /= "109") then
		print *, "Test 109 failed"
	else if (fizzString(7) /= "Ping") then
		print *, "Test 7 failed"
	else if (fizzString(5) /= "Buzz") then
		print *, "Test 5 failed"
	else if (fizzString(8) /= "8") then
		print *, "Test 8 failed"
	else if (fizzString(11) /= "Pong") then
		print *, "Test 11 failed"
	else if (fizzString(21) /= "FizzPing") then
		print *, "Test 21 failed"
	else if (fizzString(15) /= "FizzBuzz") then
		print *, "Test 15 failed"
	else if (fizzString(33) /= "FizzPong") then
		print *, "Test 33 failed"
	else if (fizzString(35) /= "BuzzPing") then
		print *, "Test 35 failed"
	else if (fizzString(55) /= "BuzzPong") then
		print *, "Test 55 failed"
	else if (fizzString(77) /= "PingPong") then
		print *, "Test 77 failed"
	else if (fizzString(385) /= "BuzzPingPong") then
		print *, "Test 385 failed"
	else if (fizzString(105) /= "FizzBuzzPing") then
		print *, "Test 105 failed"
	else if (fizzString(1155) /= "FizzBuzzPingPong") then
		print *, "Test 1155 failed"
	else
		print *, "All tests passed :)"
	end if

END program tests
	