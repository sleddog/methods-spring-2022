program PascalsTriangle;

uses sysutils;

const
	max = 100;
	maxArray = 1000;

var
	count	: integer;
	i	: integer;
	j	: integer;
	firstArray	: array[1..max+1] of integer;
	secondArray	: array[1..max+1] of integer;

begin
	for i := 1 to (max+1) do
	begin
		firstArray[i] := 0;
		secondArray[i] := 0;
	end;

	firstArray[1] := 0;
	firstArray[2] := 1;
	firstArray[3] := 2;

	for i := 1 to max do
	begin
		secondArray[1] := 0;
		for j := 2 to (maxArray+1) do
			secondArray[j] := firstArray[j-1]+firstArray[j];

		for j := 1 to (maxArray+1) do
			firstArray[j] := secondArray[j];
	end;

	writeln('Total numbers inside triangle :' + floattostr(max/2*(max+1)));
end.
