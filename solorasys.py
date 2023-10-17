from vpython import *
brown = vector(0.6, 0.3, 0.1)
grey=vector(0.5, 0.5, 0.5)
lightblue=vector(0.5, 0.5, 1.0)
yellowishbrown=vector(0.8, 0.7, 0.5)


sun=sphere(radius=100,emissive=True,texture='sun.jpg')
mercury=sphere(radius=5,pos=vector(127.9,0,0))
venus=sphere(radius=10,pos=vector(210.2,0,0),texture='venus.jpg')
earth=sphere(radius=12.5,pos=vector(280,0,0),texture=textures.earth)
mars=sphere(radius=15,pos=vector(300.6,0,0),texture='mars.jpg',emissive=True)
jupiter=sphere(radius=40,pos=vector(800,0,0),texture='jupiter.jpg',emissive=True)
saturn=sphere(radius=35,pos=vector(900,0,0),color=yellowishbrown)
uranus=sphere(radius=20,pos=vector(1100,0,0),color=lightblue)
neptune=sphere(radius=18,pos=vector(1300,0,0),color=color.blue)

ring_radius = 70  
ring_thickness = 50  
saturn_ring = cylinder(pos=vector(900, 0, 0),axis=vector(0, 1, 0),radius=ring_radius,thickness=ring_thickness,color=color.gray(0.7))


mercuryAngle=2*pi/88
venusAngle=2*pi/225
earthAngle=2*pi/365
marsAngle=2*pi/687
jupiterAngle=2*pi/4333
saturnAngle=2*pi/10756
uranusAngle=2*pi/30687
neptuneAngle=2*pi/60190


mercury_rotaions=0
venus_rotations=0
earth_rotations=0
mars_rotations=0
jupiter_rotations=0
saturn_rotations=0
uranus_rotations=0
neptune_rotations=0
ring_rotations=0


while True:
    rate(200)
    mercury.rotate(angle=mercuryAngle,axis=vector(0,1,0),origin=sun.pos)
    venus.rotate(angle=venusAngle,axis=vector(0,1,0),origin=sun.pos)
    earth.rotate(angle=earthAngle,axis=vector(0,1,0),origin=sun.pos)
    mars.rotate(angle=marsAngle,axis=vector(0,1,0),origin=sun.pos)
    jupiter.rotate(angle=jupiterAngle,axis=vector(0,1,0),origin=sun.pos)
    saturn.rotate(angle=saturnAngle,axis=vector(0,1,0),origin=sun.pos)
    uranus.rotate(angle=uranusAngle,axis=vector(0,1,0),origin=sun.pos)
    neptune.rotate(angle=neptuneAngle,axis=vector(0,1,0),origin=sun.pos)

    saturn_ring.rotate(angle=saturnAngle,axis=vector(0,1,0),origin=sun.pos)

    mercury_rotaions+=mercuryAngle
    venus_rotations+=venusAngle
    earth_rotations+=earthAngle
    mars_rotations+=marsAngle
    jupiter_rotations+=jupiterAngle
    saturn_rotations+=saturnAngle
    uranus_rotations+=uranusAngle
    neptune_rotations+=neptuneAngle

    ring_rotations+=saturnAngle
