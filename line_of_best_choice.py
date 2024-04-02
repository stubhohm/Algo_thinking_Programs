MAX_LINES = 100

def shortest_line(lines):
    shortest_line_index = 0
    shortest_line = lines[shortest_line_index]
    for i, line in enumerate(lines):
        if line < shortest_line:
            shortest_line = line
            shortest_line_index = i
    return shortest_line_index

    
def join_best_line(num_of_lines, new_people, line_lenghts):
    lines = [0] * num_of_lines
    lines = line_lenghts
    while new_people > 0:
        short_line_index = shortest_line(lines)
        current_len = lines[short_line_index]
        print(current_len)
        lines[short_line_index] +=1
        new_people -= 1

def main():
    num_of_lines, new_people = map(int, input('Enter the number of Number of lines and number of New people:').split())
    num_of_lines = MAX_LINES if num_of_lines > MAX_LINES else num_of_lines
    line_lengths = list(map(int, input('Enter the length of each existing line:').split()))
    join_best_line(num_of_lines, new_people, line_lengths)

main()
