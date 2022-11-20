# OBJECT ORIENTED PROGRAMMING

# Class: A blueprint consisting of methods and attributes
# Object: An instance of a class
# Attribute: A descriptor or characteristic i.e. Data
# Method: An action that a class or object can perform
# Encapsulation: Combining functions and data in a single entity

# class defined with "class" keyword and a class_name usually with first letter Capital
class Shirt:
    # class definition always contails __init__() method for data inside the class.
    # __init__() method takes in all the inputs passed during object creation as its parameters with pre-defined first parameter as "self" 
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        # attributes of created object are stored as self.attribute_name, which are assigned the respective input values
        self.color=shirt_color
        self.size=shirt_size
        self.style=shirt_style
        self.price=shirt_price

    # methods are defined similar to a function with only difference that first keyword is "self"
    # all the self.attrubutes of a given object are accessible inside the method with the "self" keyword
    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1- discount)

# Creating new Object of class type "Shirt" / Instantiating Object

# syntax -- class_name(arguments)
# the required attributes are passed in parenthesis 
Shirt('red','S','short sleeve',15)

#storing object in a variable
new_shirt= Shirt('red','S','short sleeve',15)

# accessing attributes of object

# syntax -- object_name.attribute
print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

# executing methods of object

# syntax -- object_name.method_name(parameters except those present in object )
new_shirt.change_price(16)
print(new_shirt.price)

print(new_shirt.discount(.2))


t_shirt_collection = []
shirt_one= Shirt('orange','M','short sleeve',25)
shirt_two= Shirt('red','S','short sleeve',15)
shirt_three= Shirt('purple','XL','short sleeve',10)

t_shirt_collection.append(shirt_one)
t_shirt_collection.append(shirt_two)
t_shirt_collection.append(shirt_three)

for i in range( len(t_shirt_collection) ):
    print( t_shirt_collection[i].color )

# see the oop_example.py and oop_shirt.py files in demo folder


#  gaussian CLASS

# Refer other files folder for binomial and normal distribution and standard deviation

# import math
# import matplotlib.pyplot as plt

# class Gaussian():
#     '''gaussian distribution class for visualizing a gaussian distribution'''
#     def __init__(self, mu=0,sigma=1):
#         self.mean=mu
#         self.stdev=sigma
#         self.data=[]

#     def calculate_mean(self):
#         '''Calculates mean of data set'''
#         avg = 1.0 * sum(self.data) / len(self.data)
#         self.mean = avg
#         return self.mean

#     def calculate_stdev(self, sample=True):
#         '''Calculates std deviation of data set'''
#         if sample:
#             n= len(self.data)-1 # for justification of taking n=n-1 for sample data see the other files folder
#         else:
#             n=len(self.data)
#         mean = self.mean
#         sigma=0
#         for d in self.data:
#             sigma += (d-mean)**2
#         sigma= math.sqrt(sigma/n) 
#         # std deviation = sqrt( (data_point - mean)^2 / len(data) )
#         self.stdev = sigma
#         return self.stdev

#     def read_data_file(self, file_name, sample=True):
#         '''Method to read data from text file. The text file should have one number(float) per line. The numbers are stored in data attribute. After file reading mean and std deviation are calculated'''
#         with open(file_name) as file:
#             data_list=[]
#             line= file.readline()
#             while line:
#                 data_list.append(int(line))
#                 line=file.readline()
#         file.close()
#         self.data = data_list
#         self.mean = self.calculate_mean()
#         self.stdev=self.calculate_stdev(sample)

#     def plot_histogram(self):
#         '''Method to output histogram of instance variable data usinf matplotlib pyplot library'''
#         plt.hist(self.data)
#         plt.title("Histogram of data")
#         plt.xlabel('data')
#         plt.ylabel('count')

#     def pdf(self,x):
#         '''PDF Probability density function calculator for gaussian distribution'''
#         return(1.0/(self.stdev * math.sqrt(2*math.pi)))*math.exp(-0.5*((x-self.mean)/self.stdev)**2)
#         # formula for gaussian/ normal distribution function

#     def plot_histogram_pdf(self, n_spaces=50):
#         '''Method to plot normalized histogram of the data and a plot of pdf along the same range'''
#         mu=self.mean
#         sigma=self.stdev

#         min_range=min(self.data)
#         max_range=max(self.data)

#         # calculates interval between x values
#         interval=1.0*(max_range - min_range/n_spaces )

#         x=[]
#         y=[]

#         # calculate x values to visualize
#         for i in range(n_spaces):
#             tmp=min_range + interval*i
#             x.append(tmp)
#             y.append(self.pdf(tmp))

#         # make the plots
#         fig,axes = plt.subplots(2,sharex=True)
#         fig.subplots_adjust(hspace=.5)
#         axes[0].hist(self.data, density=True)
#         axes[0].set_title('Normal histogram of data')
#         axes[0].set_ylabel('Density')

#         axes[1].plot(x,y)
#         axes[1].set_title('Normal distribution for\n Sample mean and sample standard deviation')
#         axes[1].set_ylabel('Density')

#         return x,y
#     def __add__(self,other):
#         result=Gaussian()
#         result.mean=self.mean+other.mean
#         result.stdev=math.sqrt(self.stdev**2 + other.stdev**2)

#         return result
    
#     def __repr__(self):
#         return "mean {}, standard deviation {}".format(self.mean,self.stdev)

# gaussian_one=Gaussian()
# gaussian_one.read_data_file('demo/numbers.txt')
# print(gaussian_one.mean)
# print(gaussian_one.stdev)
# gaussian_one.plot_histogram()
# gaussian_one.plot_histogram_pdf()

# gaussian_one=Gaussian(5,2)
# gaussian_two=Gaussian(10,1)
# gaussian_sum=gaussian_one + gaussian_two
# print(gaussian_sum.mean)
# print(gaussian_sum.stdev)

# NOTE: The above code will not run as matplotlib installation has some problems


# MAGIC METHODS

# the last two methods in Gaussian() class are magic methods


# INHERITANCE

class Clothing:

    def __init__(self, color,size,style,price):
        self.color=color
        self.size=size
        self.style=style
        self.price=price

    def change_price(self,price):
        self.price=price
    
    def calculate_discount(self,discount):
        return self.price*(1-discount)

class Shirt(Clothing):

    def __init__(self,color,size,style,price,long_or_short):
        # init method of parent class
        Clothing.__init__(self,color,size,style,price)
        self.long_or_short=long_or_short

    def double_price(self):
        self.price*=2

class Pants(Clothing):

    def __init__(self,color,size,style,price,waist):
        # init method of parent class
        Clothing.__init__(self,color,size,style,price)
        self.waist=waist

    def calculate_discount(self, discount): # ovverrides Clothing.calculate_discount()
        return self.price*(1-discount/2)




# import math
# import matplotlib.pyplot as plt
# from .Generaldistribution import Distribution

# class Binomial(Distribution):
#     """ Binomial distribution class for calculating and 
#     visualizing a Binomial distribution.
    
#     Attributes:
#         mean (float) representing the mean value of the distribution
#         stdev (float) representing the standard deviation of the distribution
#         data_list (list of floats) a list of floats to be extracted from the data file
#         p (float) representing the probability of an event occurring
#         n (int) number of trials """
    
    
#     def __init__(self, prob=.5, size=20):
                
#         self.n = size
#         self.p = prob
        
#         Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    
                        
    
#     def calculate_mean(self):
    
#         """Function to calculate the mean from p and n
        
#         Args: 
#             None
        
#         Returns: 
#             float: mean of the data set
    
#         """
        
#         self.mean = self.p * self.n
                
#         return self.mean



#     def calculate_stdev(self):

#         """Function to calculate the standard deviation from p and n.
        
#         Args: 
#             None
        
#         Returns: 
#             float: standard deviation of the data set
    
#         """
        
#         self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        
#         return self.stdev
        
        
#     def replace_stats_with_data(self):
    
#         """Function to calculate p and n from the data set
        
#         Args: 
#             None
        
#         Returns: 
#             float: the p value
#             float: the n value
    
#         """
    
#         self.n = len(self.data)
#         self.p = 1.0 * sum(self.data) / len(self.data)
#         self.mean = self.calculate_mean()
#         self.stdev = self.calculate_stdev()
        
#         return self.p, self.n

    
        
#     def plot_bar(self):
#         """Function to output a histogram of the instance variable data using 
#         matplotlib pyplot library.
        
#         Args:
#             None
            
#         Returns:
#             None
#         """
                
#         plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
#         plt.title('Bar Chart of Data')
#         plt.xlabel('outcome')
#         plt.ylabel('count')
        
        
        
#     def pdf(self, k):
#         """Probability density function calculator for the binomial distribution.
        
#         Args:
#             x (float): point for calculating the probability density function
            
        
#         Returns:
#             float: probability density function output
#         """
        
#         a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
#         b = (self.p ** k) * (1 - self.p) ** (self.n - k)
        
#         return a * b
        

#     def plot_bar_pdf(self):

#         """Function to plot the pdf of the binomial distribution
        
#         Args:
#             None
        
#         Returns:
#             list: x values for the pdf plot
#             list: y values for the pdf plot
            
#         """
        
#         x = []
#         y = []
        
#         # calculate the x values to visualize
#         for i in range(self.n + 1):
#             x.append(i)
#             y.append(self.pdf(i))

#         # make the plots
#         plt.bar(x, y)
#         plt.title('Distribution of Outcomes')
#         plt.ylabel('Probability')
#         plt.xlabel('Outcome')

#         plt.show()

#         return x, y
        
#     def __add__(self, other):
        
#         """Function to add together two Binomial distributions with equal p
        
#         Args:
#             other (Binomial): Binomial instance
            
#         Returns:
#             Binomial: Binomial distribution
            
#         """
        
#         try:
#             assert self.p == other.p, 'p values are not equal'
#         except AssertionError as error:
#             raise
        
#         result = Binomial()
#         result.n = self.n + other.n
#         result.p = self.p
#         result.calculate_mean()
#         result.calculate_stdev()
        
#         return result
        
        
#     def __repr__(self):
    
#         """Function to output the characteristics of the Binomial instance
        
#         Args:
#             None
        
#         Returns:
#             string: characteristics of the Gaussian
        
#         """
        
#         return "mean {}, standard deviation {}, p {}, n {}".\
#         format(self.mean, self.stdev, self.p, self.n)