def a_p(l*b):
  area = l*b
  peri = 2(l+b)
  return(area,peri)
  (a p) = a_p(2,3)
  print(a)
  print(p)


def area_of_rectangel(l,b):
  return l*b
  l = 8
  b = 10
  area = area_of_rectangle(l,b)
  print("area of the rectangle:",area)

def cub_rec(l,b,h):
    if h==0:
        s="rectangle"
        a=l*b
        p=2*(l+b)
        return(s, a, p)
    else:
        s="cuboid"
        v=l*b*h
        p=8*(l+b+h)
        return(s,v,p)
a,b,c=cub_rec(2,3,4)
print("Shape=",a)
print("Volume=",b)
print("Perimeter=",c)
