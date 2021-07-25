


def hypothesis(m1,m2 , x , c):
    h=m1*(x**2)+m2*x+c
    return h

def cost(m1,m2,x,c,y):
    n=len(x)
    sum=0
    for i in range (n):
        h=hypothesis(m1, m2, x[i], c)
        temp=(h-y[i])**2
        #temp=(m1*(x[i]*x[i])+(m2*x[i])+c-y[i])**2
        sum+=temp
    cost=sum/(2*n)
    return cost

def gradient (m1,m2,x,c,y,learningRate):
    t1=0
    t2=0
    t3=0
    n=len(x)
    for i in range (n):
        t1=(m1*(x[i]*x[i])+(m2*x[i])+c-y[i])*(x[i]*x[i])
        t2=(m1*(x[i]*x[i])+(m2*x[i])+c-y[i])*x[i]
        t3=(m1*(x[i]*x[i])+(m2*x[i])+c-y[i])
        m1=m1-((learningRate*t1)/n)
        m2=m2-((learningRate*t2)/n)
        c=c-((learningRate*t3)/n)
    
    return m1,m2,c


def loadcsv (x,y):
    for line in open("data_poly.csv"):
        vals = line.split(',')
        x.append(float(vals[0]))
        y.append(float(vals[1]))
 
        
def main():
    
    m1=0
    m2=0
    c=0
    x=[]
    y=[]
    learningRate=0.000002
    loadcsv(x,y)
    result=[]
    for i in range (1000):
        loss=cost(m1,m2, x, c, y)
        m2,m2,c=gradient(m1,m2, x, c, y, learningRate)
        result.append(loss)
    print("m1 = ",m1)
    print("m2 = ",m2)
    print("c = ",c)
    print("cost = ",result[-1])

main()