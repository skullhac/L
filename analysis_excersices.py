import random
import time
import matplotlib.pyplot as plt

MAX_LEN = 200  # Maximum length of input list.


def count_common_elements_nested_loops(l1, l2):
    common_elements = []
    count = 0
    for v in l1:
        for w in l2:
            if w == v:
                common_elements.append(w)
                count += 1
    return count


def count_common_elements_list_comp(l1, l2):
    common_elements = [x for x in l1 if x in l2]
    return len(common_elements)


def count_common_elements_sets(l1, l2):
    common_elements = set(l1).intersection(l2)
    return len(common_elements)


def count_common_elements_hash_table(l1, l2):
    table = {}
    common_elements = []
    for v in l1:
        table[v] = True
    count = 0
    for w in l2:
        if table.get(w):  # Avoid KeyError that would arise with table[w]
            common_elements.append(w)
            count += 1
    return count


if __name__ == "__main__":

    # Initialise results containers
    lengths_nested = []
    times_nested = []
    lengths_comp = []
    times_comp = []
    lengths_hash_table = []
    times_hash_table = []
    lengths_sets = []
    times_sets = []

    for length in range(0, MAX_LEN, 10):
        # Generate random lists
        l1 = [random.randint(0, 99) for _ in range(length)]
        l2 = [random.randint(0, 99) for _ in range(length)]

        # Time execution for nested lists version
        start = time.perf_counter()
        count_common_elements_nested_loops(l1, l2)
        end = time.perf_counter()

        # Store results
        lengths_nested.append(length)
        times_nested.append(end - start)

        # Time execution for list comprehension version
        start = time.perf_counter()
        count_common_elements_list_comp(l1, l2)
        end = time.perf_counter()

        # Store results
        lengths_comp.append(length)
        times_comp.append(end - start)

        # Time execution for hash table version
        start = time.perf_counter()
        count_common_elements_hash_table(l1, l2)
        end = time.perf_counter()

        # Store results
        lengths_hash_table.append(length)
        times_hash_table.append(end - start)

        # Time execution for sets version
        start = time.perf_counter()
        count_common_elements_sets(l1, l2)
        end = time.perf_counter()

        # Store results
        lengths_sets.append(length)
        times_sets.append(end - start)

    # Plot results
    plt.style.use("dark_background")
    plt.figure().canvas.manager.set_window_title("Common List Elements Algorithm - Time Complexity")
    plt.xlabel("List Length")
    plt.ylabel("Execution Time (s)")
    plt.plot(lengths_nested, times_nested, label="count_common_elements_nested_loops()")
    plt.plot(lengths_comp, times_comp, label="count_common_elements_list_comp()")
    plt.plot(lengths_hash_table, times_hash_table, label="count_common_elements_hash_table()")
    plt.plot(lengths_sets, times_sets, label="count_common_elements_sets()")
    plt.legend()
    plt.tight_layout()
    plt.show()