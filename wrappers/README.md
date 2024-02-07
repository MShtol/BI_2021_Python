## Task 1
Write a simple wrapper that replaces the return value of the function being decorated for the duration of its execution. To measure time, use the time module.
## Task 2
Write a decorator that allows you to log function runs by printing out the input and return type. You can use the `__name__` attribute to get the class name as a string.
## Task 3
Make a decorator - `Russian roulette`, which will make sure that the decorated function with a given probability replaces the return value with the value passed to the decorator.
## Task 4
Implement a decorator similar to `staticmethod` without using any modules.
## Task 5. Wrapper to repclace emthods return type
Imagine that we have installed a certain library that contains two classes `MyString` and `MySet`, which are inheritors of `str` and `set`, but also carry additional methods.

The problem is that the library was written by not very careful people, so it turned out that some methods do not return the data type that we expect. For example, `MyString().reverse()` returns an object of class `str`, although it would be more logical to expect an object of class `MyString`.

Find and implement a convenient way to make such methods return an instance of the current class, not the parent. In this case, **method code cannot be changed**
## Task 6. OpenFasta context Manager
Context managers are special objects that can work with the `with ... as ...`: construct. 

- The object should work like regular files in python (no need to inherit, it would be better to use composition here), but:
    - When iterating over an object, we will have to get not a line from a file, but a special `FastaRecord` object. It will store information about the sequence. It is important, not lines, but sequences, in fasta files, a sequence is often split into many lines
    - You need to write read_record and read_records methods, which in meaning correspond to `readline()` and `readlines()` in ordinary files, but they should not produce lines, but the `FastaRecord` object (s)
- The constructor must take one argument - the path to the file
- The class must manage memory efficiently, with the expectation of working with very large files.

`FastaRecord` object. It should be a data class with three fields:
- `seq` - sequence
- `id_` - sequence ID (this is what is in the fast file in the line that starts with > before the first space. For example, >GTD326487.1 Species anonymous 24 chromosome)
- `description` - what is left after the ID (For example, >GTD326487.1 Species anonymous 24 chromosome)
## Task 7. Wrapping with lru_cache  
1. Write a code that will allow you to get all possible (non-unique) genotypes when two organisms are crossed. It can be a function or a class, whichever is more convenient for you. 

For example, all possible outcomes of crossing "Aabb" and "Aabb" (non-unique) are
```
AAbb
AAbb
AAbb
AAbb
Aabb
Aabb
Aabb
Aabb
Aabb
Aabb
Aabb
Aabb
aabb
aabb
aabb
aabb
```
2. Write a function that calculates the probability of occurrence of a certain genotype (its expected proportion in the offspring). 

For example,
```python
get_offspting_genotype_probability(parent1="Aabb", parent2="Aabb", target_genotype="Aabb") # 0.5
```

3. Write a code that outputs all unique genotypes when crossing `'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'` and `'АаббВвГгДДЕеЖжЗзИиЙйКкЛлМмНН'`, which contain the following combination of alleles `'АаБбВвГгДдЕеЖжЗзИиЙйКкЛл'`

4. Write a code that calculates the probability of occurrence of the genotype `'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'` when crossing `АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн` and `АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн`


Important notes:

1. The order of the alleles in the case of heterozygotes should always be as follows: first a capital letter, then a small one (AaBb is acceptable, but aAbB should not be)
2. Subtasks 3 and 4 can be computationally intensive (up to 15+ minutes depending on the hardware), so make sure you test your code well on small data before doing these tasks. If your code runs longer than 20 minutes, then most likely your solution is not optimal, try to optimize something. If the optimal solution does not work at all, then try to remove the last gene from the input data in all tasks (this should reduce the execution time by about 4 times), but 2 points will be deducted for such a solution
3. Although it is possible to solve subtasks 2, 3 and 4 mathematically without resorting to obtaining all possible genotypes directly, it is the brute-force version of the algorithm that is required from you.