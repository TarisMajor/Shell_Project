def flexible_function(arg1, *args, kwarg1="default", **kwargs):
    print("Fixed argument:", arg1)
    print("Additional arguments:", args)
    print("Keyword argument:", kwarg1)
    print("Additional keyword arguments:", kwargs)

flexible_function("fixed", "extra1", "extra2", kwarg1="custom", key1="value1", key2="value2")