def word_count(string):
    list1 = string.lower().split()
    new_dict = {}
    number_count = 1
    for x in list1:
        if x in new_dict:
            number_count =  list1.count(x)
        else:
            number_count = 1

        new_dict.update({"{}".format(x): number_count})

    print(new_dict)

word_count("I like my new potato chips and I like diping sos. Who am I to you")
