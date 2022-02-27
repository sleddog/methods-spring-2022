!FizzBuzz
!Bryn Wilkerson

Program FizzBuzz
    character(100) :: num
    integer :: n 

    call get_command_argument(1,num)
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
            print *, i
        end if
    end do
End Program FizzBuzz
