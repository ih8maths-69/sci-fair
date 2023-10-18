from vpython import *
grey=vector(0.5, 0.5, 0.5)
lightblue=vector(0.5, 0.6, 0.8)
yellowishbrown=vector(0.8, 0.7, 0.5)


sun=sphere(radius=120,emissive=True,texture='sun.jpg')
mercury=sphere(radius=5,pos=vector(138.9,0,0),make_trail=True)
venus=sphere(radius=10,pos=vector(210.2,0,0),texture='venus.jpg',emissive=True,make_trail=True)
earth=sphere(radius=12.5,pos=vector(280,0,0),texture=textures.earth,make_trail=True)
mars=sphere(radius=15,pos=vector(300.6,0,0),texture='mars.jpg',emissive=True,make_trail=True)
jupiter=sphere(radius=40,pos=vector(800,0,0),texture='jupiter.jpg',emissive=True,make_trail=True)
saturn=sphere(radius=35,pos=vector(1000,0,0),color=yellowishbrown,make_trail=True)
uranus=sphere(radius=20,pos=vector(1200,0,0),color=lightblue,make_trail=True)
neptune=sphere(radius=18,pos=vector(1400,0,0),color=color.blue,make_trail=True)

ring_radius = 70  
ring_thickness = 50  
saturn_ring = cylinder(pos=vector(1000, 0, 0),axis=vector(0, 1, 0),radius=ring_radius,thickness=ring_thickness,color=color.gray(0.7))

mercury.trail_radius = 1
venus.trail_radius=1
earth.trail_radius = 1
mars.trail_radius=1
jupiter.trail_radius=1
saturn.trail_radius=1
uranus.trail_radius=1

mercury_text=label(pos=vector(138.9,140,0),text='Mercury',height=13,box=False)
venus_text=label(pos=vector(210.2,211,0),text='Venus',height=13,box=False)
earth_text=label(pos=vector(280,200,0),text='Eath',height=13,box=False)
mars_text=label(pos=vector(300.6,200,0),text='Mars',height=13,box=False)
jupiter_text=label(pos=vector(800,85,0),text='Jupiter',height=13,box=False)
saturn_text=label(pos=vector(1000,75,0),text='Saturn',height=13,box=False)
uranus_text=label(pos=vector(1200,45,0),text='Uranus',height=13,box=False)
neptune_text=label(pos=vector(1400,41,0),text='Neptune',height=13,box=False)

mercuryAngle=2*pi/88/10
venusAngle=2*pi/225/10
earthAngle=2*pi/365/10
marsAngle=2*pi/687/10
jupiterAngle=2*pi/4333/10
saturnAngle=2*pi/10756/10
uranusAngle=2*pi/30687/10
neptuneAngle=2*pi/60190/10


mercury_rotations=0
venus_rotations=0
earth_rotations=0
mars_rotations=0
jupiter_rotations=0
saturn_rotations=0
uranus_rotations=0
neptune_rotations=0
ring_rotations=0


while True:
    rate(100)
    mercury.rotate(angle=mercuryAngle,axis=vector(0,1,0),origin=sun.pos)
    venus.rotate(angle=venusAngle,axis=vector(0,1,0),origin=sun.pos)
    earth.rotate(angle=earthAngle,axis=vector(0,1,0),origin=sun.pos)
    mars.rotate(angle=marsAngle,axis=vector(0,1,0),origin=sun.pos)
    jupiter.rotate(angle=jupiterAngle,axis=vector(0,1,0),origin=sun.pos)
    saturn.rotate(angle=saturnAngle,axis=vector(0,1,0),origin=sun.pos)
    uranus.rotate(angle=uranusAngle,axis=vector(0,1,0),origin=sun.pos)
    neptune.rotate(angle=neptuneAngle,axis=vector(0,1,0),origin=sun.pos)

    saturn_ring.rotate(angle=saturnAngle,axis=vector(0,1,0),origin=sun.pos)

    mercury_text.rotate(angle=mercuryAngle,axis=vector(0,1,0),origin=sun.pos)
    venus_text.rotate(angle=venusAngle,axis=vector(0,1,0),origin=sun.pos)
    earth_text.rotate(angle=earthAngle,axis=vector(0,1,0),origin=sun.pos)
    mars_text.rotate(angle=marsAngle,axis=vector(0,1,0),origin=sun.pos)
    jupiter_text.rotate(angle=jupiterAngle,axis=vector(0,1,0),origin=sun.pos)
    saturn_text.rotate(angle=saturnAngle,axis=vector(0,1,0),origin=sun.pos)
    uranus_text.rotate(angle=uranusAngle,axis=vector(0,1,0),origin=sun.pos)
    neptune_text.rotate(angle=neptuneAngle,axis=vector(0,1,0),origin=sun.pos)

    mercury_rotations+=mercuryAngle
    venus_rotations+=venusAngle
    earth_rotations+=earthAngle
    mars_rotations+=marsAngle
    jupiter_rotations+=jupiterAngle
    saturn_rotations+=saturnAngle
    uranus_rotations+=uranusAngle
    neptune_rotations+=neptuneAngle

    ring_rotations+=saturnAngle

    
    if earth_rotations >= 2 * pi:
        earth.make_trail = False
    if mercury_rotations >= 2 * pi:
        mercury.make_trail = False
    if venus_rotations>=2 * pi:
        venus.make_trail=False
    if mars_rotations>=2 * pi:
        mars.make_trail=False
    if jupiter_rotations>=2 * pi:
        jupiter.make_trail=False
    if saturn_rotations>=2 * pi:
        saturn.make_trail=False
    if uranus_rotations>=2 * pi:
        uranus.make_trail=False
    if neptune_rotations>=2 * pi:
        neptune.make_trail=False

