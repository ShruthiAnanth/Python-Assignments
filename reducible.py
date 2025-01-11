def is_prime(n):
    if (n == 1):
        return False
    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

def hash_word(s, size):
    hashIndex = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hashIndex = (hashIndex * 26 + letter) % size
    return hashIndex

def step_size(s, const):
    n = len(s)
    idx = 0
    for j in range(n):
        letter = ord(s[j]) - 96
        idx = (const - (idx * 26 + letter) % const) % const
    return idx if idx > 0 else 1

def insert_word(s, hash_table):
    n = len(hash_table)
    init_insert_idx = hash_word(s, n)
    if hash_table[init_insert_idx] == "":
        hash_table[init_insert_idx] = s
    else:
        coll_step = step_size(s, 3)
        coll_idx = init_insert_idx
        while hash_table[coll_idx] != "":
            coll_idx = (coll_idx + coll_step) % n
        hash_table[coll_idx] = s

def find_word(s, hash_table):
    idx = hash_word(s, len(hash_table))
    if hash_table[idx] != s:
        idx_2 = step_size(s, 11)
        s_count = 0
        coll_idx = idx + s_count * idx_2
        if hash_table[coll_idx] == s:
            return True
        while hash_table[coll_idx] != s:
            s_count += 1
            coll_idx = (idx + s_count * idx_2) % len(hash_table)
            if hash_table[coll_idx] == "":
                return False
        if hash_table[coll_idx] == s:
            return True
        return False
    return True

def is_reducible(s, hash_table, hash_memo):
    test = list(s)
    if ("a" not in test and "i" not in test) and "o" not in test:
        return False
    if len(s) == 1 and (s == "a" or s == "i" or s == "o"):
        insert_word(s, hash_memo)
        return True
    elif find_word(s, hash_memo):
        return True
    elif find_word(s, hash_table):
        reducible = False
        for i in range(len(s)):
            temp = s[:i] + s[i + 1:]
            if is_reducible(temp, hash_table, hash_memo):
                reducible = True
        if reducible:
            insert_word(s, hash_memo)
            return True
    return False

def get_longest_words(string_list):
    longest = []
    max_len = len(max(string_list, key=len))
    for i in string_list:
        if len(i) == max_len:
            longest.append(i)
    return longest

def main():
    word_list = []
    with open("words.txt") as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
        word_list.append(data[i])

    n = len(word_list)
    for i in range((n * 2) + 1, n**4, 2):
        if is_prime(i):
            p2 = i
            break

    hash_list = [""] * p2

    for i in word_list:
        insert_word(i, hash_list)

    for i in range(27001, 27000**2, 2):
        if is_prime(i):
            hash_memo = [""] * i
            break

    reducible_words = []

    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)

    to_print = get_longest_words(reducible_words)

    for i in to_print:
        print(i)

if __name__ == "__main__":
    main()
