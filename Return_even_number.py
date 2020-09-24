Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> def check_even_list(*args):
    even_number = []
    for a in args:
        if a%2==0:
            even_number.append(a)
        else:
            pass
               
    return even_number
