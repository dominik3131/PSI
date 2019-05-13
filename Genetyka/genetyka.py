import random
pool_size=10
mutation_prob=0.2
def marking_function(x):
    value=int(x, 2)
    return 2*(value*value+1)
def roulette_sum(genes):
    sum=0
    for x in genes:
        sum+=marking_function(x)
    return sum
def prob(x,sum):
    return marking_function(x)/sum
def select_genes(genes):
    roulette=[]
    sum = roulette_sum(genes)
    roulette.append(prob(genes[0],sum))
    for i in range(1,len(genes)):
        roulette.append(prob(genes[i],sum))
        roulette[i]+=roulette[i-1]
    selected_genes=[]
    for i in range(0,len(genes)):
        selected_genes.append(genes[choose(roulette)])
    return selected_genes
def cross_genes(genes):
    random.shuffle(genes)
    crossed_genes=[]
    for i in range(0,len(genes),2):
        locus=random.randint(0,len(genes[0]))
        crossed_genes.append(cross(genes[i+1],genes[i],locus))
        crossed_genes.append(cross(genes[i],genes[i+1],locus))
    return crossed_genes
        
def cross(gene1,gene2,locus):
    crossed_gene=gene1[:locus]+gene2[locus:]
    return crossed_gene
def mutate_genes(genes):
    mutated_genes=[]
    for x in genes:
        mutated_genes.append(mutate(x))
    return mutated_genes
def mutate(gene):
    if random.random()<mutation_prob:
        locus=random.randint(0,len(gene)-1)
        temp=list(gene)
        if temp[locus]=='1':
            temp[locus]='0'
        else:
            temp[locus]='1'
        return "".join(temp)
    return gene
def choose(roulette):
    val=random.random()
    index=0
    for i in range(0,len(roulette)):
        if val<float(roulette[i]):
            index=i
            break
    return index
    
    
all_genes=[]
for i in range(1,128):
    all_genes.append(i)
genes=[]
for i in range(0,pool_size):
    genes.append("{:08b}".format(all_genes.pop(random.randint(0, len(all_genes)))))

for i in range(0,1000):
    genes=select_genes(genes)
    genes=cross_genes(genes)
    genes=mutate_genes(genes)
print(genes)




