try:
    raise Exception('aws',10)
except Exception as abc:
    print(type(abc))
    print(abc.args)
    print(abc)
