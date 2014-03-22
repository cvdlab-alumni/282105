from pyplasm import *
from scipy import *

def base2D(base, x,y,z):
	verts=[[x,y,z],[y+base,y,z],[x+base,y+base,z],[x,y+base,z]]
	cells=[[1,2,3,4]]
	pols=None
	b2D=MKPOL([verts,cells,pols])
	return b2D

floor0=base2D(60,0,0,0)
floor1=base2D(56,2,2,0)
floor2=base2D(52,4,4,0)
floor3=base2D(48,6,6,0)
floor4=base2D(44,8,8,0)
floor5=base2D(40,10,10,0)
floor6=base2D(36,12,12,0)
floor7=base2D(32,14,14,0)
floor8=base2D(28,16,16,0)

floor9=base2D(20,20,20,0)

c=[[1,2,3,4]]
p=None

v1=[[25,68],[35,68],[35,44],[25,44]]
stair1=(MKPOL([v1,c,p]))

v2=[[25,16],[35,16],[35,-8],[25,-8]]
stair2=(MKPOL([v2,c,p]))

v3=[[68,25],[68,35],[44,35],[44,25]]
stair3=(MKPOL([v3,c,p]))

v4=[[16,25],[16,35],[-8,35],[-8,25]]
stair4=(MKPOL([v4,c,p]))

building=STRUCT([COLOR([0.7,0.1,0])(base2D(60,0,0,0)),
COLOR([0.7,0.2,0])(floor0),
COLOR([0.7,0.3,0])(floor1),
COLOR([0.7,0.4,0])(floor2),
COLOR([0.7,0.5,0])(floor3),
COLOR([0.7,0.6,0])(floor4),
COLOR([0.7,0.7,0])(floor5),
COLOR([0.7,0.8,0])(floor6),
COLOR([0.7,0.9,0])(floor7),
COLOR([0.7,1,0])(floor8),
COLOR([0.0,0.7,0.2])(floor9),
COLOR([0.7,0,0.9])(stair1),
COLOR([0.7,0,0.9])(stair2),
COLOR([0.7,0,0.9])(stair3),
COLOR([0.7,0,0.9])(stair4)])
