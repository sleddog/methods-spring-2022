Program main
	USE fizz
	implicit none

	character(8) :: num
    integer :: n, i
        
    ! reads in and stores the number to character
    call get_command_argument(1,num)
    ! converts character to integer
    read(num,*)n
	
	do i = 1, n
		print *, fizzString(i)
	end do
	
End program main