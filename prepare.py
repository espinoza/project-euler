"""This script prepares a Python file to write the solution to
a problem from Project Euler (http://projecteuler.net).

Created by Jorge Espinoza

Argument with the number of problem is required.
Here's an example using the shell:
>>> python prepare.py 23
p023.py created.
Problem 23: Non-abundant sums

If the problem does not exist or the file already exists,
no change will be made.
"""

import os.path, sys, requests

AUTHOR = 'Jorge Espinoza'
GITHUB = 'https://github.com/espinoza/project-euler'


def main(n):
    """Create file for problem n from Project Euler.
    """
    ROOT_URL = 'https://projecteuler.net/problem='
    problem_number = sys.argv[1]
    html = get_html(ROOT_URL, problem_number)
    problem_title = get_problem_title(html)

    # If the problem does not exist, stop
    if problem_title == 'Problems Archives':
        print(f"Problem {problem_number} does not exist in Project Euler.")
        return

    # If the problem exist, continue
    create_file(problem_number, problem_title, ROOT_URL)

    # Print more data about the problem
    print(f"Problem {problem_number}: {problem_title}")
    print(f"{ROOT_URL}{problem_number}")
    pub1 = html.find('Published on')
    pub2 = pub1 + html[pub1:].find(';')
    print(html[pub1:pub2])


def get_html(root_url: str, problem_number: int) -> str:
    """Return a string containing html code from the exercise.
    """
    url = f"{root_url}{problem_number}"
    return requests.get(url).text


def get_problem_title(html: str) -> str:
    """Return the title of a Project Euler problem using its html.
    """
    beginning = html.find('<h2>') + 4
    end = html.find('</h2>')
    return html[beginning:end]


def create_file(problem_number: int, problem_title: str, root_url: str):
    """Create p???.py file with its own header.
    """
    file_title = 'solutions/pe' + str(problem_number).zfill(3) + '.py'

    # Check if the file exists
    if os.path.isfile(file_title):
        print(file_title, 'already exists. No change was made.')
        return

    # If the file does not exists, create and put the header inside
    py_file = open(file_title, 'w')
    header = create_header(problem_number, problem_title, root_url)
    py_file.write(header)
    py_file.close()

    # Notify that the file was created and display information
    print(file_title, 'created')


def create_header(problem_number: int, problem_title: str,
                  root_url: str) -> str:
    """Return a string whith header of py file.
    """
    global AUTHOR
    global GITHUB

    lines = [f'"""Project Euler - Solution to']
    lines.append(f"Problem {problem_number}: {problem_title}")
    lines.append(f"{root_url}{problem_number}")
    lines.append('')
    lines.append(f"Solved by {AUTHOR}")
    lines.append(f'{GITHUB}')
    lines.append('"""')

    return '\n'.join(lines)


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("Problem number required. No change was made.")
    elif len(sys.argv) > 2:
        print("Type just one argument. No change was made.")
    else:
        n = sys.argv[1]
        main(n)
