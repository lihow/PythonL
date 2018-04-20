#产生测试集
import numpy as np
import matplotlib.pyplot as plt

L = 10
data = np.random.rand(L, 2)
hit = np.random.randint(0, L, size = 4)
x = data[:, 0]
y = data[:, 1]
print(data) 

##计算点和直线的关系
def Point3(p1, p2, p3):
   # print(p1, p2, p3)
    k = (p1[0, 1] - p2[0, 1])/(p1[0, 0] - p2[0, 0])
    re = k * (p3[0, 0] - p2[0, 0]) + (p3[0, 1] - p2[0, 1])
    return re
def Point4Line(p1, p2, p3, p4):
    #plot point
    #plt.figure('1')
    #plt.plot(X, Y)
    '''
    for idx,i in enumerate([p1, p2, p3, p4]):
        plt.scatter(i[0, 0], i[0, 1])
        plt.annotate(s = r'p%s' % str(idx+1), xy=(i[0, 0], i[0, 1]),xytext=(+20,-20), \
                     xycoords='data',textcoords='offset points', \
                     fontsize=16,arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2")) 
    plt.show()
    '''
    
    
    #select p1
    if Point3(p2, p3, p1)*Point3(p2, p3, p4)>=0 and Point3(p2, p4, p1)*Point3(p2, p4, p3)>=0 \
        and Point3(p3, p4, p1)*Point3(p3, p4, p2)>=0:
        print('p1 is in inner')
        #return p2, p3, p4
        return np.concatenate((p2, p3, p4), axis= 0)
    #select p2 
    if Point3(p1, p3, p2)*Point3(p1, p3, p4)>=0 and Point3(p1, p4, p2)*Point3(p1, p4, p3)>=0 \
        and Point3(p3, p4, p2)*Point3(p3, p4, p1)>=0:
        print('p2 is in inner')
        #return p1, p3, p4
        return np.concatenate((p1, p3, p4), axis= 0)
    #select p3
    if Point3(p1, p2, p3)*Point3(p1, p2, p4)>=0 and Point3(p1, p4, p3)*Point3(p1, p4, p2)>=0 \
        and Point3(p2, p4, p3)*Point3(p2, p4, p1)>=0:
        print('p3 is in inner')
        #return p1, p2, p4
        return np.concatenate((p1, p2, p4), axis= 0)
    #select p4
    if Point3(p1, p2, p4)*Point3(p1, p2, p3)>=0 and Point3(p1, p3, p4)*Point3(p1, p3, p2)>=0 \
        and Point3(p2, p3, p4)*Point3(p2, p3, p1)>=0:
        print('p4 is in inner')
        return p1, p2, p3
    return np.concatenate((p1, p2, p3, p4), axis= 0) 

result = np.array([[]])
def fun(data, N, k):
    #随机找出四个点
    global result
    for i in range(N - 4):
        p1 = np.array([data[i, :]])
        for j in range(i+1, N -3):
            p2 = np.array([data[j, :]])
            for k in range(j+1, N-2):
                p3 =  np.array([data[k, :]])
                for l in range(k+1, N):
                    p4 = np.array([data[l, :]]) 
                    #print(i, j, k ,l)
                    print(p1, p2, p3, p4)
                    temp = Point4Line(p1, p2, p3, p4)
                    print(temp.shape)
                    print(result.shape)
                    if result.shape == (1, 0):
                        result = temp
                    else:
                        result = np.concatenate((result, temp), axis = 0)
                    print(result)
    return result
print(fun(data, L, 4))