#!/usr/bin/env python
# coding: utf-8

# # Iterrators are beautifull. Generators - even more beautifull

# In[1]:


import random


# ## 1. fasta reader

# In[2]:


def fasta_reader(path: str):
    """This generator reads fasta file and returns sequence and its id"""
    with open(path) as file:
        id_ = file.readline().strip()
        value = ''
        while True:
            line = file.readline().strip()
            if not line:
                yield id_, value
                break
            if line.startswith('>'):
                yield id_, value
                id_ = line
                value = ''
            else:
                value += line


# ## Mutato class

# In[3]:


class Mutato:
    """This class iterates over fasta file and randomly modifies sequences"""

    nucleo = "ACGT"  # Possible nucleotides for substitutions

    def __init__(self, path):
        """This function initializes object with path to fasta file"""
        self.path = path
        self.fastag = fasta_reader(path)


    def __iter__(self):
        return self

    def __next__(self):
        """This function returns next item of iterator"""
        try:
            id_, seq = next(self.fastag)
        except StopIteration:
            self.fastag = fasta_reader(self.path)
            id_, seq = next(self.fastag)
        seq = self.genetic_lottery(seq)
        return id_, seq

    def genetic_lottery(self, seq: str):
        """This function recieves sequence and decides to apply
        every of 5 types of mutations with 0.5 chance
        Returns modified sequence
        """
        if random.choice([True, False]):
            seq = self.substitution(seq)
        if random.choice([True, False]):
            seq = self.deletion(seq)
        if random.choice([True, False]):
            seq = self.insertion(seq)
        if random.choice([True, False]):
            seq = self.inversion(seq)
        if random.choice([True, False]):
            seq = self.duplication(seq)
        return seq

    def substitution(self, seq: str):
        """At randomly chosen position of sequence one nucleotide is
        replaced with a random one from A,C,G and T
        Returns modified sequence
        """
        seq = list(seq)
        pos = random.randint(0, len(seq)-1)
        seq[pos] = random.choice(self.nucleo)
        return ''.join(seq)

    def deletion(self, seq: str):
        """Deletes chunk of sequence of random size
        Returns modified sequence
        """
        start = random.randrange(len(seq))
        end = random.randint(start, len(seq)-1)
        seq = seq[:start] + seq[end:]
        return seq

    def insertion(self, seq: str):
        """inserts random combination of nucletides of random size
        in random place of sequence.
        Returns modified sequence
        """
        point = random.randrange(len(seq))
        insert_size = random.randint(1, 42)
        insert = ''.join(random.choices(self.nucleo, k=insert_size))
        seq = seq[:point] + insert + seq[point:]
        return seq

    def inversion(sekf, seq: str):
        """Inverts random chunk of sequence
        Returns modified sequence
        """
        start = random.randrange(len(seq))
        end = random.randint(start, len(seq)-1)
        seq = seq[:start] + seq[end:start:-1] + seq[end:]
        return seq

    def duplication(self, seq: str):
        """Duplicates random chunk of sequence, inserting its copy right after it.
        Returns modified sequence
        """
        start = random.randrange(len(seq))
        end = random.randint(start, len(seq)-1)
        seq = seq[:end] + seq[start:end] + seq[end:]
        return seq


# ## 3. Consecutive iterration

# In[4]:


def iter_append(iterable, item):
    """
    This generator iterates over one iterable,
    and after that yields item
    """
    yield from iterable  # Really cool stuff! Consecutive iteration
    yield item


# ## 4. Recursive generator (list flattening)

# In[5]:


def nested_list_unpacker(lst: list):
    """
    This function can unpack (flatten) lists of any depth.
    With respect to maximum iteration depth? of course.
    Returns flattened list.
    """
    def unpack_gen(lst: list):
        """Generator itself"""
        for elem in lst:
            if isinstance(elem, list):
                yield from nested_list_unpacker(elem)
            else:
                yield elem
    unpacked = list(unpack_gen(lst))
    return unpacked


# In[6]:


if __name__ == "__main__":
    path = 'sequences.fasta'
    print('________________________FASTA_READER_________________________')
    reader = fasta_reader(path)
    for id_, seq in reader:
        print(id_, seq[:50])
    print('________________________MUTATO_CLASS_________________________')
    myMutato = Mutato(path)
    for i in range(10):
        id_, seq = next(myMutato)
        print(id_, seq)
    print('________________________ITER_APPEND__________________________')
    generator = iter_append([1, 2, 4, 7, 8, 0, 99], 11235813)
    for i in generator:
        print(i)
    print('________________________LIST_UNPACKER________________________')
    test_list = [1, 2, 3, [1, 2, [3, 4, []], [1], [], 12, 3], [1, [5, 6]]]
    print(nested_list_unpacker(test_list))
