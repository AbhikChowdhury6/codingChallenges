read a

if [[ $a = "y" ]] || [[ $a = "Y" ]]; then  # use the double brackets for string expressions?
    echo YES                            # can use the || or &&
fi

if [[ $a = "n" ]] || [[ $a = "N" ]]; then  # can use the = 
    echo NO
fi
