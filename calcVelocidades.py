import numpy

def calculoVelocidades(m1, x1, y1, u1x, u1y, m2, x2, y2, u2x, u2y):

    ub1x = ((u1x * (x1 - x2) + u1y * (y1 - y2)) / (numpy.pow(x1-x2,2) + numpy.pow(y1-y2,2) )) * (x1-x2)
    ub1y = ((u1x * (x1 - x2) + u1y * (y1 - y2)) / (numpy.pow(x1-x2,2) + numpy.pow(y1-y2,2) )) * (y1-y2)
    ub1 = numpy.sqrt(numpy.pow(ub1x,2) + numpy.pow(ub1y,2))

    ub2x = ((u2x * (x1 - x2) + u2y * (y1 - y2)) / (numpy.pow(x1-x2,2) + numpy.pow(y1-y2,2) )) * (x1 - x2)
    ub2y = ((u2x * (x1 - x2) + u2y * (y1 - y2)) / (numpy.pow(x1-x2,2) + numpy.pow(y1-y2,2) )) * (y1 - y2)
    ub2 = numpy.sqrt(numpy.pow(ub2x, 2) + numpy.pow(ub2y, 2))

    dx = u1x - ub1x
    dy = u1y - ub1y

    ex = u2x - ub2x
    ey = u2y - ub2y

    pbx = m1*ub1x + m2*ub2x
    pby = m1*ub1y + m2*ub2y
    pb = numpy.sqrt(numpy.pow(pbx, 2) + numpy.pow(pby, 2))
    c = ((x1 - x2) * pbx + (y1 - y2) * pby) / (numpy.sqrt(numpy.pow(x1 - x2, 2) + numpy.pow(y1 - y2, 2)) * pb)
    if c<0:
        c = -1
    else:
        c = 1
    pb = c*pb

    cte = m1*ub1*ub1 + m2*ub2*ub2

    vb1 = (2*pb*m1+numpy.sqrt(numpy.pow(-2*pb*m1,2)-4*(m1*m2+m1*m1)*(pb*pb-cte*m2)))/(2*(m1*m2+m1*m1)) #vai me dizer a direção do vb1 (nem sempre vai ser positivo)
    vb2 = (pb - m1 * vb1) / m2

    vb1x = ((x1-x2)/numpy.sqrt(numpy.pow(x1-x2,2)+numpy.pow(y1-y2,2)))*vb1
    vb1y = ((y1-y2)/numpy.sqrt(numpy.pow(x1-x2,2)+numpy.pow(y1-y2,2)))*vb1

    vb2x = ((x1-x2)/numpy.sqrt(numpy.pow(x1-x2,2)+numpy.pow(y1-y2,2)))*vb2
    vb2y = ((y1 - y2) / numpy.sqrt(numpy.pow(x1 - x2, 2) + numpy.pow(y1 - y2, 2))) * vb2

    v1x = vb1x+dx
    v1y = vb1y+dy
    v2x = vb2x+ex
    v2y = vb2y+ey

    print("########################")
    print(u1x * m1 + u2x * m2)
    print(u1y*m1+u2y*m2)
    print(((m1*(u1x*u1x+u1y*u1y))/2)+((m2*(u2x*u2x+u2y*u2y))/2))
    print("########################")
    print(v1x * m1 + v2x * m2)
    print(v1y * m1 + v2y * m2)
    print(((m1 * (v1x * v1x + v1y * v1y)) / 2) + ((m2 * (v2x * v2x + v2y * v2y)) / 2))
    print(x1, " ", y1)
    print(x2, " ", y2)

    return v1x, v1y, v2x, v2y