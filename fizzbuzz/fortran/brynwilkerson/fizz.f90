MODULE fizz
	contains
	function fizzString(i)
		implicit none
		integer :: i
		Character(len = 20) :: fizzString
		character(8) :: i_char
		fizzString = ""
		if (mod(i,3) == 0) then
			 fizzString = trim(fizzString)//"Fizz"
		end if
		if (mod(i,5) == 0) then
			fizzString = trim(fizzString)//"Buzz"
		end if
		if (mod(i,7) == 0) then
			fizzString = trim(fizzString)//"Ping"
		end if
		if (mod(i,11) == 0) then
			fizzString = trim(fizzString)//"Pong"
		end if
		if (mod(i,3) /= 0 .and. mod(i,5) /= 0 .and. mod(i,7) /= 0 .and. mod(i,11) /= 0) then
			write(i_char, '(i8)') i
			fizzString = trim(fizzString)//adjustl(i_char)
		end if
		return
	end function	
END MODULE fizz
