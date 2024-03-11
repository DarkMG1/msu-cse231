from operator import itemgetter
from typing import List

def get_file_contents() -> List[str]:
    data = []
    for file in ["data1.txt", "data2.txt"]:
        with open(file, "r") as f:
            lines = f.readlines()
            lines.pop(0)
            for line in lines:
                data.append(line.strip())
    return data

def main():
    score_map = {}
    data = get_file_contents()
    for line in data:
        name, score = line.split()
        score_map[name] = score_map.get(name, 0) + int(score)
    score_map = sorted(score_map.items(), key=itemgetter(0))
    print("{:10s} {:<10s}".format("Name", "Total"))
    for name, score in score_map:
        print("{:10s} {:<10d}".format(name, score))

if __name__ == "__main__":
    main()