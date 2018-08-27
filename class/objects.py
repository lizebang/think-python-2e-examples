import copy


class Point:
    """Represents a point in 2−D space."""


blank = Point()
blank.x = 1.5
blank.y = 2.5
print('(%g, %g)\n' % (blank.x, blank.y))


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


print_point(blank)
print()


class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner.
    """


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height / 2
    return p


center = find_center(box)
print_point(center)
print()

# object is modifiable
box.width = box.width + 50
box.height = box.height + 100


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


print('before grow_rectangle, box.width = %g, box.height = %g' %
      (box.width, box.height))
grow_rectangle(box, 100, 100)
print('after grow_rectangle, box.width = %g, box.height = %g' %
      (box.width, box.height), '\n')

# copy
p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = copy.copy(p1)
print_point(p1)
print_point(p2)
print('p2 is p1 =', p2 is p1, '\n')

box2 = copy.copy(box)
print('box2 is box =', box2 is box)
print('box2.corner is box.corner =', box2.corner is box.corner, '\n')

# deepcopy
box3 = copy.deepcopy(box)
print('box3 is box =', box3 is box)
print('box3.corner is box.corner =', box3.corner is box.corner)
