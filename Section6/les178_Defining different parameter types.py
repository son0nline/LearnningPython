def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...|{}, {}".format(p1, p2))
    print("var-positional (*args):..|{}".format(args))
    print("keyword:.................|{}".format(k))
    print("var-keyword:.............|{}".format(kwargs))


#func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8, somethingelse=9)
func(1 #p1
, 2 #p2
, 3, 4, 5, 9 # *args tuple
, k=6 #required to define end of arg
, key1=7, key2=8, somethingelse="10") # **kwargs dict
