import os
import github

categories = ['백준', 'SWEA', '프로그래머스']
numbers = ['1️⃣', '2️⃣', '3️⃣']
content = f"""# {github.repository}\n"""
category_num = 0

def write(category):
    global content, category_num

    url = f'{github.localDir}/{category}/'

    if os.path.isdir(url):
        content += f"""### {numbers[category_num]} {category}\n"""
        category_num += 1
        
        content += """| Level | Problem Number |\n| :------: | :------ |\n"""
        levels = os.listdir(url)

        for level in levels:
            files = os.listdir(url + level)
            content += f"""| {level} | """
            for problem in files:
                dot_index = problem.find('.')
                problem_num = problem[0:dot_index]
                content += f"""[{problem_num}]({github.link}/{category}/{level}/{problem}) """
            content += """ |\n"""
        content += """\n"""

def main():
    github.pull()
    
    for category in categories: write(category)
   
    # Write README.md
    with open(github.localDir + '/README.md', 'w', encoding='UTF8') as readme:
        readme.write(content)
    
    github.push()

main()