
import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

def read_file(fp):
    reader = csv.reader(fp)
    for i in range(4):
        next(reader)
    lists = []
    for row in reader:
        if row[0] == "":
            continue
        lists.append(row)
    return lists  # temporary return value so main runs

def get_totals(L):
    us_pop = 0
    total_pop = 0
    for row in L:
        pop = int(row[1].replace('<', '').replace(',', ''))
        if row[0] == "U.S.":
            us_pop += pop
        else:
            total_pop += pop
    return us_pop, total_pop

def get_industry_counts(L):
    counters = [0] * 5
    for i in range(1, len(L)):
        row = L[i]
        if row[9] in INDUSTRIES:
            counters[INDUSTRIES.index(row[9])] += 1
    zipped = sorted(zip(INDUSTRIES, counters), key=itemgetter(1), reverse=True)
    return [list(item) for item in zipped]

def get_largest_states(L):
    us_val = 0
    larger_states = []
    for row in L:
        if row[0] == "U.S.":
            us_val = float(row[2].replace('%', ''))
            continue
        potential = float(row[2].replace("%", ""))
        if potential > us_val:
            larger_states.append(row[0])
    return sorted(larger_states)

def main():    
    fp = open("immigration.csv")
    L = read_file(fp)
    
    us_pop,total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)
    
    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n',' ')
            print(state)        
    
    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry","count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0],tup[1]))
        
if __name__ == "__main__":
    main()
