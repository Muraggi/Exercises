'''Assignment: Administration
    created on 18 Nov. 2020
    @author: Gamze Senturk'''


def averages(student):
    name_grades = student.split('_')
    student_name = name_grades[0]
    grades = []
    for grade in name_grades[-1].split(' '):
        grades.append(float(grade))

    average_grade = sum(grades) / len(grades)
    final_grade = round(average_grade Z* 2) / 2

    if 5.5 <= average_grade < 6.0:
        final_grade = '6-'
    else:
        final_grade = str(final_grade)
    print('%s has an average of %s' % (student_name, final_grade))


def graph_similarity_score(similarity_score):
    similarity_score_student_match = similarity_score.split(';')
    similarity_score = similarity_score_student_match[0].split('=')
    score_to_character = ''
    for score in similarity_score:
        if score == '0':
            score_to_character += '_'
        elif score < '20':
            score_to_character += '-'
        else:
            score_to_character += '^'
    print('\t%s' % score_to_character)


def display_student_match(student_match):
    name_student_match = student_match.split(';')[1]
    matches = name_student_match.split(',')
    for i in matches:
        if i == '':
            print('\tNo matches found')
        else:
            print('\t%s' % i)


lines = open('administration.in.txt').read().splitlines()
students = lines[::2]
similarity_scores_student_matches = lines[1::2]


for student in students:
    averages(student)

for similarity_score in similarity_scores_student_matches:
    graph_similarity_score(similarity_score)

for student_match in similarity_scores_student_matches:
    display_student_match(student_match)
