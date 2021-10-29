#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# this program merges two lists alternately  in python
# https://pythonbaba.com/python-code-that-
# combines-two-lists-by-taking-elements-alternately/


def merge_alternate(first_list, second_list, final_list):
    # this program merges two lists, its items are put alternatly
    # get the length of both lists
    length_of_first_list = len(first_list)
    length_of_second_list = len(second_list)

    # if the length of list 1 is bigger than list 2
    #  assign that length to number of times to loop
    # if not assign the other length to times to loop either = or greater
    if length_of_first_list > length_of_second_list:
        loop_times = length_of_first_list
    else:
        loop_times = length_of_second_list

    # append both list one then the other
    for num_loops in range(0, loop_times):
        final_list.append(first_list[num_loops])
        final_list.append(second_list[num_loops])

    return final_list


def main():
    # this function declares the variables inside the list
    # and prints the output

    # declare and say whats in list
    # p on the list name as "primary"
    p_first_list = ["pink", "yellow", "orange"]
    p_second_list = [679, 123, 453]
    p_final_list = []

    print(
        merge_alternate(p_first_list, p_second_list, p_final_list)
    )  # call the function
    print("\nDone.")


if __name__ == "__main__":
    main()
