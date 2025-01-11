# Input: tuples_list is an unsorted list of interval tuples
# Output: A sorted and merged list of interval tuples, where
#         no interval in the merged list has any overlap.
def merge_tuples (tuples_list):
    merged_list = []
    tuples_list.sort()

    for interval in tuples_list:
        if not merged_list or interval[0] > merged_list[-1][1]:
            merged_list.append(interval)
        else:
            merged_list[-1] = (merged_list[-1][0], max(merged_list[-1][1], interval[1]))

    return merged_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: A list of tuples sorted by ascending order of the size
#         of the interval. If two intervals have the size then it breaks
#         ties putting the interval with the lower starting number first
def sort_by_interval_size (tuples_list):
    for i in range(len(tuples_list)):
        min_index = i
        for j in range(i + 1, len(tuples_list)):
            if (tuples_list[j][1] - tuples_list[j][0]) < (tuples_list[min_index][1] - tuples_list[min_index][0]) or \
                    ((tuples_list[j][1] - tuples_list[j][0]) == (tuples_list[min_index][1] - tuples_list[min_index][0]) and tuples_list[j][0] < tuples_list[min_index][0]):
                min_index = j

        tuples_list[i], tuples_list[min_index] = tuples_list[min_index], tuples_list[i]

    return tuples_list



def main():
    """
    Uses input redirection to read the data and create a list of tuples
    """
    num_cases = int(input())

    tuples_list = []
    for i in range(num_cases):
        line = input()
        start, end = line.split()
        tuples_list.insert(i, (int(start), int(end)))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
