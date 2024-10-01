
#import argparse
#import string
import matplotlib.pyplot as plt
import numpy as np

from scipy.interpolate import InterpolatedUnivariateSpline 

#se non è il modello e voglio capire andamento non posso fare il fil 

#è una classe che interpola tra tutti i punti 
#from loguru import logger


class ProbabilityDesityDistribution:
    def __init__(self,x,y):  #gli passo x e y

        self._x=x  #non vogliamo che tocchiamo x e y da fuori della classe 
        self._y=y
        self._spline = InterpolatedUnivariateSpline(x,y)  #fa interpolazione tra i valori x e y, facciamo la pline 
        
        

  #  def evaluate(self,x): 
        return self._spline(x)         #dettaglio di implementazione, voglio funzione in un punto arbitrario. 
        #io scelgo di farlo con una spline. Non è un interfaccia e quindi non glielo foglio dare
    
    #Pposso usare metodi speciali per renderlo chiamabile 
    def __call__(self,x)    #questa caso da capire meglio mi permette di passare da 
        return self._spline(x)   

    def plot(self):
         x=np.linespace(self._x.min(), self._x.max(),250) 
        plt.plot(x,self.evaluate(x))  #da questo 
    
    #a questa riga    plt.plot(x,self(x))    self istanza della classe da cui lo chiamo 
            


#ma sto solo chiamando metodi della spline
#questa non ha una spline ma è una spline è piu comodo ereditare 
    def integral (self,x1,x2)
        return self._spline.integral(x1,x2)  #la spline ha il metodo integral di sa derivare e integrare da sola
    
    def normalization(self):
        return self.integral(self._xmin(),self._x.max())   # se deve essere una pdf deve essere normalizzata

if __name__=='__main__':
    x=np.linspace(0.,1.,10)
    y=np.exp(x)
    pdf = ProbabilityDesityDistribution(x,y)
    
    #e quindi di passare da   pdf(x) e non devo dare anche la x, mi dice di valutare la mia pdf in x  #istanza della mia classe 
  
    pdf.plot()




#SE HO UNA FUNZIONE PER PUNTI INVERTIRLA SIGNIFICA SCAMBIARE LA X CON LA Y
#FUNZIONE COMULATIVA: LA CDF è CRESCENTE. DATA X E CDF INVERTIRLA SIGNIFICA FARE UNA SPLINE IN CUI SCAMBIO X E Y E HO INVERTITO E OTTEMG ....BO 











    ## cambiamo ereditiamo
    
class ProbabilityDesityDistribution:(InterpolatedUnivariateSpline): #ereditiamo dalla classe dentro () tutti i suoi metodi
    def __init__(self,x,y):  #gli passo x e y
        #per normalizzarlo calcolo con il suo metodo l'integrae e poi divido y per la norma 
        self._x=x  #non vogliamo che tocchiamo x e y da fuori della classe 
        self._y=y
        super().__init__(self.x,self.y)

    
    def plot(self):   #la spline nom ha questo metodo quindi lo metto
         x=np.linespace(self._x.min(), self._x.max(),250) 
        plt.plot(x,self.evaluate(x)) 
    
    def normalization(self):
        return self.integral(self._xmin(),self._x.max())   # se deve essere una pdf deve essere normalizzata
