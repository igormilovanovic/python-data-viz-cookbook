import pylab 
import random 

SAMPLE_SIZE = 100 

# seed random generator
# if no argument provided
# uses system current time
random.seed() 

# store generated random values here
real_rand_vars = [] 

# we don't need iterator value, 
# so we can put call it '_'
for _ in range(SAMPLE_SIZE):
    # get next random value
    new_value = random.random() 
    real_rand_vars.append(new_value) 

# create histogram from data in 10 buckets
pylab.hist(real_rand_vars, 10)

# define x and y labels
pylab.xlabel("Number range") 
pylab.ylabel("Count") 

# show figure
pylab.show()
