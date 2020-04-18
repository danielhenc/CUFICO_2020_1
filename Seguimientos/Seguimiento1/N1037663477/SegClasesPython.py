
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class Particula:

    #Atributos
    cargada = True

    #Instancias
    def __init__(self,x,y,z,vx,vy,vz,m,carga):

        self.X=x
        self.Y=y
        self.Z=z
        self.VX=vx
        self.VY=vy
        self.VZ=vz
        self.M=m
        self.Carga=carga
    

    def fuerza(self,Ex,Ey,Ez):

        BZ = 10
        Fx = self.Carga*(Ex + self.VY*BZ)
        Fy = self.Carga*(Ey - self.VX*BZ)
        Fz = self.Carga*Ez

        return Fx,Fy,Fz

        
    def Vel_evo(self,ax,ay,az,t):

        

        self.VX = self.VX + ax*t
        self.VY = self.VY + ay*t
        self.VZ = self.VZ + az*t



    def Pos_evol(self,ax,ay,az,t):

       self.X= self.X + (self.VX * t) + (0.5*ax*t*t)
       self.Y= self.Y + (self.VY * t) + (0.5*ay*t*t)
       self.Z= self.Z + (self.VZ * t) + (0.5*az*t*t)
       



Par1 = Particula(0.0,0.0,0.0,0.0,0.0,0.0,10.0,1)
Par2 = Particula(1.0,0.0,0.0,0.0,0.0,0.0,10.0,-1)



x1 = []
y1 = []
z1 = []

x2 = []
y2 = []
z2 = []

for i in range(0,10000):
    if ((Par2.X-Par1.X)**(2) + (Par2.Y-Par1.Y)**(2) + (Par2.Z-Par1.Z)**(2))==0: break

    Ex2 = (Par2.Carga*(Par1.X-Par2.X))/(4*np.pi*(8.8541e-12)*((Par1.X-Par2.X)**(2) + (Par1.Y-Par2.Y)**(2) + (Par1.Z-Par2.Z)**(2))**(3/2))
    Ey2 = (Par2.Carga*(Par1.Y-Par2.Y))/(4*np.pi*8.8541e-12*((Par1.X-Par2.X)**(2) + (Par1.Y-Par2.Y)**(2) + (Par1.Z-Par2.Z)**(2))**(3/2))
    Ez2 = (Par2.Carga*(Par1.Z-Par2.Z))/(4*np.pi*8.8541e-12*((Par1.X-Par2.X)**(2) + (Par1.Y-Par2.Y)**(2) + (Par1.Z-Par2.Z)**(2))**(3/2))
    
    Ex1 = (Par1.Carga*(-Par1.X+Par2.X))/(4*np.pi*8.8541e-12*((Par2.X-Par1.X)**(2) + (Par2.Y-Par1.Y)**(2) + (Par2.Z-Par1.Z)**(2))**(3/2))
    Ey1 = (Par1.Carga*(-Par1.Y+Par2.Y))/(4*np.pi*8.8541e-12*((Par2.X-Par1.X)**(2) + (Par2.Y-Par1.Y)**(2) + (Par2.Z-Par1.Z)**(2))**(3/2))
    Ez1 = (Par1.Carga*(-Par1.Z+Par2.Z))/(4*np.pi*8.8541e-12*((Par2.X-Par1.X)**(2) + (Par2.Y-Par1.Y)**(2) + (Par2.Z-Par1.Z)**(2))**(3/2))

    Fx,Fy,Fz =Par1.fuerza(Ex2,Ey2,Ez2)
    Fx2,Fy2,Fz2 =Par2.fuerza(Ex1,Ey1,Ez1)
    
    Par1.Vel_evo(Fx/Par1.M,Fy/Par1.M,Fz/Par1.M,0.1)
    Par1.Pos_evol(Fx/Par1.M,Fy/Par1.M,Fz/Par1.M,0.1)
    Par2.Vel_evo(Fx2/Par2.M,Fy2/Par2.M,Fz2/Par2.M,0.1)
    Par2.Pos_evol(Fx2/Par2.M,Fy2/Par2.M,Fz2/Par2.M,0.1)
 

    x1.append(Par1.X)
    y1.append(Par1.Y)
    z1.append(Par1.Z)

    x2.append(Par2.X)
    y2.append(Par2.Y)
    z2.append(Par2.Z)
    


fig = plt.figure(figsize = (8,8))
ax = Axes3D(fig)
ax.plot(x1,y1,z1, label = "Particula 1", color = 'red')
ax.plot(x2,y2,z2, label = "Particula 2", color = 'darkblue')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Trayectoria de las particulas')
plt.legend()
plt.show()

