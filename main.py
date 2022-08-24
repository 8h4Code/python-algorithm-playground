# This is a sample Python script.
import numpy


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

arr = [7, 3, 9, 2, 0, 4, 8, 1, 6, 5]


def bubble_sort(the_seq):
    n = len(the_seq)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if the_seq[j] > the_seq[j + 1]:
                temp = the_seq[j]
                print(f"temp: {temp}")
                the_seq[j] = the_seq[j + 1]
                the_seq[j + 1] = temp
            return the_seq


print(bubble_sort(arr))



