read x
read y

if [ $y -gt $x ]; then #need spaces before and after [] of condiitonal
    echo X is less than Y
fi

if [ $x -gt $y ]; then
    echo X is greater than Y
fi

if [ $x -eq $y ]; then
    echo X is equal to Y
fi