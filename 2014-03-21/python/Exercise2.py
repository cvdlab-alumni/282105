from pyplasm import *
from scipy import *

def base2D(base, x,y):
	verts=[[x,y],[x+base,y],[x+base,y+2],[x,y+2]]
	cells=[[1,2,3,4]]
	pols=None
	b2D=MKPOL([verts,cells,pols])
	return b2D

def easytop2D(base, x,y):
	verts=[[x,y],[x+base,y],[x+base,y+6],[x,y+6]]
	cells=[[1,2,3,4]]
	pols=None
	b2D=MKPOL([verts,cells,pols])
	return b2D

def stairleft():
	verts=[[-3,0,-0.2],[17,0,-0.2],[17,18,-0.2]]
	cells=[[1,2,3]]
	pols=None
	tri=MKPOL([verts,cells,pols])
	return tri

def stairright():
	verts=[[63,0,-0.2],[43,0,-0.2],[43,18,-0.2]]
	cells=[[1,2,3]]
	pols=None
	tri=MKPOL([verts,cells,pols])
	return tri

floor0=base2D(60,0,0)
floor1=base2D(56,2,2)
floor2=base2D(52,4,4)
floor3=base2D(48,6,6)
floor4=base2D(44,8,8)
floor5=base2D(40,10,10)
floor6=base2D(36,12,12)
floor7=base2D(32,14,14)
floor8=base2D(28,16,16)

floor9=easytop2D(20,20,18)

stairfront=MKPOL([[[25,0],[35,0],[25,18],[35,18]],[[1,2,3,4]],None])
stairl=stairleft()
stairr=stairright()

east=STRUCT([COLOR([0.5,0.1,0])(floor0),COLOR([0.5,0.1,0])(floor1),COLOR([0.5,0.2,0])(floor2),COLOR([0.5,0.3,0])(floor3),COLOR([0.5,0.4,0])(floor4),COLOR([0.5,0.5,0])(floor5),COLOR([0.5,0.6,0])(floor6),COLOR([0.5,0.7,0])(floor7),COLOR([0.5,0.8,0])(floor8),COLOR([0.2,0.5,0.2])(floor9), COLOR([0.9,0.2,0.2])(stairfront), COLOR([0.9,0.2,0.2])(stairl),COLOR([0.9,0.2,0.2])(stairr)])

west=east

south=east

northdoor=MKPOL([[[28.5,18],[31.5,18],[31.5,20],[28.5,20]],[[1,2,3,4]],None])

north=STRUCT([COLOR([0.5,0.1,0])(floor0),COLOR([0.5,0.1,0])(floor1),COLOR([0.5,0.2,0])(floor2),COLOR([0.5,0.3,0])(floor3),COLOR([0.5,0.4,0])(floor4),COLOR([0.5,0.5,0])(floor5),COLOR([0.5,0.6,0])(floor6),COLOR([0.5,0.7,0])(floor7),COLOR([0.5,0.8,0])(floor8),COLOR([0.2,0.5,0.2])(floor9), COLOR([0.9,0.2,0.2])(stairfront), COLOR([0.9,0.2,0.2])(stairl),COLOR([0.9,0.2,0.2])(stairr), COLOR([1,1,1])(northdoor)])

VIEW(north)
VIEW(east)
VIEW(south)
VIEW(west)
