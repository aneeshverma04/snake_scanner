import pickle
import pickletools

l = [b"(dp0\nS'serum'\np1\nccopy_reg\n_reconstructor\np2\n(c__main__\nanti_pickle_serum\np3\nc__builtin__\nobject\np4\nNtp5\nRp6\ns."]
l2 = [b"Aasdad"]
for val in l2:
    pickletools.dis(val)