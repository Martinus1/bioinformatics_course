import operator

def h_d(seq_one, seq_two):
    ne = operator.ne
    return sum(map(ne, seq_one, seq_two))

def approx_pattern_count(sequence, kmer, d):
    list_of_kmers =[]
    count = 0
    for the_index in range(len(sequence) - len(kmer) + 1):
        new_kmer = sequence[the_index:the_index+len(kmer)]
        if h_d(kmer, new_kmer) <= d:
            list_of_kmers.append(new_kmer)
            count += 1
    print(count)


approx_pattern_count("CATGCCATTCGCATTGTCCCAGTGA", "CC", 2)
