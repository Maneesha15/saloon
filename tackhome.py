class Saloon():
    def __init__(self,maxsize):
        self.queue=[]
        self.count=0                #constructor
        self.maxsize=maxsize
        self.back=self.maxsize-1
        self.front=0
        self.baber='sleep'
        

    def isEmpty(self):
        if self.queue==[]:
            return True             #check whether queue is empt.or no
        else:
            return False

    def isFull(self):                   #check queue is Empty or nor
        return self.count==self.maxsize

    def enqueue(self,data):
        if self.count!=self.maxsize:
            self.queue.insert(self.back,data)       #client come 
            self.back=(self.back+1)%self.maxsize
            self.count+=1
        

    def dequeue(self):
        if self.count!=0:                   #client went
            return self.queue.pop(self.front)
        self.front=(self.front+1)%self.maxsize
        self.count-=1

        

        
    def client(self,name):
        if(self.isFull()):
            print ("no space,please leave client '"+name+"'")
        elif(self.baber=='sleep'):
            print("wakes the baber")
            print ('client'+name+ ' can have haircut')
            self.baber='busy'       #client come to the saloon     
        else:
            self.enqueue(name)
            self.baber='busy'
        
    
    def clientGo(self):
        if(self.isEmpty()):
            self.baber='sleep'
            print ("no clients,baber goint to sleep")
        else:                           
            n=self.dequeue()
            self.baber='busy'
            print ("client "+n+" can have hairecut")

        
    
    
Q=Saloon(4)
Q.client('m')
Q.client('n')
Q.client('k')
Q.client('p')
Q.client('t')
Q.client('a')
Q.clientGo()
Q.clientGo()
Q.clientGo()
Q.clientGo()
Q.clientGo()

