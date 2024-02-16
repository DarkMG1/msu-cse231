file_str = input("Input a file: ")
file = None

while True:
    try:
        file = open(file_str, "r")
        break
    except FileNotFoundError:
        print("\nFile does not exist.")
        file_str = input("Input a file: ")

lines = file.readlines()
file.close()
full_contents = []
for line in lines:
    element = line.split()
    name = ' '.join(element[:2])
    scores = tuple(map(int, element[2:]))
    total_score = 0
    for score in scores:
        total_score += score
    mean_score = total_score / len(scores)
    full_contents.append((name, scores, mean_score))

full_contents.sort()

total_exam_1, total_exam_2, total_exam_3, total_exam_4 = 0, 0, 0, 0

# Sum up the scores for each exam
for line in full_contents:
    total_exam_1 += line[1][0]
    total_exam_2 += line[1][1]
    total_exam_3 += line[1][2]
    total_exam_4 += line[1][3]

# Calculate the average score for each exam
average_exam_1 = total_exam_1 / len(full_contents)
average_exam_2 = total_exam_2 / len(full_contents)
average_exam_3 = total_exam_3 / len(full_contents)
average_exam_4 = total_exam_4 / len(full_contents)

print("\n{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}"
      .format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))

for content in full_contents:
    print("{:20s}{:6d}{:6d}{:6d}{:6d}{:10.2f}"
          .format(content[0], content[1][0], content[1][1], content[1][2], content[1][3], content[2]))
print("{:20s}{:6.1f}{:6.1f}{:6.1f}{:6.1f}"
      .format("Exam Mean", average_exam_1, average_exam_2, average_exam_3, average_exam_4))