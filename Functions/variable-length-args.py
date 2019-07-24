
def test_var_kwargs(farg, **abc):

    print ("formal arg:", farg)

    for key in abc:
        print ("another keyword arg: %s: %s" % (key, abc[key]))

test_var_kwargs(farg = "Welcome to Python World", a = 10, b = 20, c = 30, d = 40)