import numpy as np 
import matplotlib.pyplot as plt 



def displayHeisenbergWalk(ax1='z',ax2='x',n=1000,N=500,visu3d=False,ax3='y'):
    """
    Cette fonction réalise N marches aléatoires de n pas sur le groupe de Heisenberg discret et affiche la projection du résultat en deux dimensions. 
    ax1,ax2 : axes de projection à choisir parmi 'x', 'y' et 'z' 
    'z' correspond à la dimension associée au centre du groupe de Heisenberg. 
    Une représentation en 3d est également possible, dans ce cas il faut spécifier ax3
    """
    
    if visu3d:
        ax = plt.axes(projection='3d')
    
    X = np.eye(3) 
    Y = np.eye(3)
    Z = np.eye(3)
    X[0,1] = 1
    Y[1,2] = 1 
    Z[0,2] = 1 #Z est le générateur du centre du groupe 
    
    S = np.zeros((6,3,3))
    S[0],S[1],S[2],S[3],S[4],S[5] = X,Y,Z,np.linalg.inv(X),np.linalg.inv(Y),np.linalg.inv(Z)
    
    def proj(A,ax='x'):
        if ax=='y':
            return A[1,2]
        elif ax=='z':
            return A[0,2]
        return A[0,1]
        
    
    
    steps = np.random.randint(low=0,high=6,size=(N,n))
    
    for i in range(N):
        T = np.eye(3)
        traj1 = np.zeros(n)
        traj2 = np.zeros(n)
        traj3 = np.zeros(n)
        for k in range(n):
            T=T@S[steps[i,k]]
            traj1[k] = proj(T,ax1)
            traj2[k] = proj(T,ax2)
            traj3[k] = proj(T,ax3)
        if visu3d:
            ax.plot3D(traj1,traj2,traj3)
        else:
            plt.plot(traj1,traj2)
    
    plt.xlabel(ax1)
    plt.ylabel(ax2)
    
    
    plt.show()
    
    

# Appel à la fonction :
displayHeisenbergWalk()

