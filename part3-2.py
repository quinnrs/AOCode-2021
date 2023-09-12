""" 
copied from output of day8_code3.py line 191 and 192
I think def decode_pattern(signals)
    works with parse data as lists
        but does not work with
            parse data as frozensets

"""
# from part3.py  includes len() in tuple
signals = ((frozenset({'e', 'b', 'a', 'f', 'd', 'c', 'g'}), 7), 
           (frozenset({'e', 'b', 'f', 'd', 'c'}), 5), 
           (frozenset({'a', 'f', 'd', 'c', 'g'}), 5), 
           (frozenset({'c', 'a', 'f', 'd', 'b'}), 5), 
           (frozenset({'d', 'b', 'a'}), 3), 
           (frozenset({'e', 'b', 'a', 'f', 'd', 'c'}), 6), 
           (frozenset({'e', 'b', 'f', 'd', 'c', 'g'}), 6), 
           (frozenset({'e', 'f', 'b', 'a'}), 4), 
           (frozenset({'e', 'b', 'a', 'd', 'c', 'g'}), 6), 
           (frozenset({'b', 'a'}), 2))


digits =  ((frozenset({'e', 'b', 'f', 'd', 'c'}), 5), 
           (frozenset({'b', 'a', 'f', 'd', 'c'}), 5), 
           (frozenset({'e', 'b', 'f', 'd', 'c'}), 5), 
           (frozenset({'b', 'f', 'a', 'd', 'c'}), 5))

# with len()in tuple like MeCode
s2s = {
        (frozenset({frozenset({'b', 'f', 'c', 'd', 'e'}), 5}), 2): 1, 
        (frozenset({5, frozenset({'a', 'f', 'c', 'd', 'g'})}), 2): 1, 
        (frozenset({frozenset({'a', 'b', 'f', 'c', 'd'}), 5}), 2): 1, 
        (frozenset({frozenset({'b', 'd', 'a'}), 3}), 2): 1, 
        (frozenset({frozenset({'a', 'b', 'f', 'c', 'd', 'e'}), 6}), 2): 1,
        (frozenset({frozenset({'b', 'f', 'c', 'd', 'e', 'g'}), 6}), 2): 1,
        (frozenset({4, frozenset({'a', 'e', 'f', 'b'})}), 2): 1, 
        (frozenset({frozenset({'a', 'b', 'c', 'd', 'e', 'g'}), 6}), 2): 1,
        (frozenset({2, frozenset({'a', 'b'})}), 2): 1,
        }

d2s =  {1: (frozenset({'b', 'a'}), 2)}

# without len in tuple RSQ Code
s2d =  {frozenset({'f', 'e', 'g', 'c', 'b', 'a', 'd'}): 8,
         frozenset({'b', 'a', 'd'}): 7, 
         frozenset({'b', 'e', 'a', 'f'}): 4, 
         frozenset({'b', 'a'}): 1, 
         frozenset({'f', 'e', 'c', 'b', 'd'}): 5, 
         frozenset({'f', 'g', 'c', 'a', 'd'}): 2, 
         frozenset({'f', 'c', 'b', 'a', 'd'}): 3, 
         frozenset({'f', 'e', 'c', 'b', 'a', 'd'}): 6, 
         frozenset({'f', 'e', 'g', 'c', 'b', 'd'}): 9, 
         frozenset({'e', 'g', 'c', 'b', 'a', 'd'}): 0}


d2s =  {8: frozenset({'f', 'e', 'g', 'c', 'b', 'a', 'd'}), 
        7: frozenset({'b', 'a', 'd'}), 
        4: frozenset({'b', 'e', 'a', 'f'}), 
        1: frozenset({'b', 'a'}), 
        5: frozenset({'f', 'e', 'c', 'b', 'd'}), 
        2: frozenset({'f', 'g', 'c', 'a', 'd'}), 
        3: frozenset({'f', 'c', 'b', 'a', 'd'}), 
        6: frozenset({'f', 'e', 'c', 'b', 'a', 'd'}), 
        9: frozenset({'f', 'e', 'g', 'c', 'b', 'd'}), 
        0: frozenset({'e', 'g', 'c', 'b', 'a', 'd'})}