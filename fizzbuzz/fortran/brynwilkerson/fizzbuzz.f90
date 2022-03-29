!FizzBuzz
!Bryn Wilkerson

Program FizzBuzz
    character(8) :: num, i_char
    integer :: n 
        
    ! reads in and stores the number to character
    call get_command_argument(1,num)
    ! converts character to integer
    read(num,*)n
        
    do i = 1, n
        if (mod(i,3) == 0) then
             if (mod(i,5) == 0) then
                print *, "Fizz Buzz "
            else
                print *, "Fizz "
            end if
        else if (mod(i,5) == 0) then
            print *, "Buzz "
        else
            ! if the integer is not divisible by 3 and/or 5,
            ! convert to character for formatting purposes
            write(i_char, '(i8)') i
            print *, adjustl(i_char)
        end if
    end do
End Program FizzBuzz
