def div(a,b):
    print(a/b)


def change_behaviour(func):
     def inner(a,b):
         if a<b:
           a,b=b,a
         return func(a,b)

     return inner

div=change_behaviour(div)
div(2,3)
div(4,3)