from scrape_class import RSTParser

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Scrape_header')))

from header import MarkdownParser
import requests
import json
import os
import re
from termcolor import colored
from rst_to_myst import rst_to_myst
global parser
ignore=["glossary","*"]
def fetch_and_save_data(filename, url):
    """
    Fetch data from a given URL, save it to a file, and print certain parts of the JSON.

    :param url: The URL to fetch data from.
    :return: None
    """
    print(f"url:{url}")
    response = requests.get(url)

    # Error handling for HTTP request
    if response.status_code != 200:
        print(colored("Failed to retrieve the content.","red"))
        return 1
    try:
        data = json.loads(response.text)
    except json.JSONDecodeError:
        print("Failed to parse the response as JSON.")
        return 

    # Saving the entire fetched JSON to a file
    data='\n'.join(data['payload']['blob']['rawLines'])
    # print(data)
    filename = filename.split("/")[-1]
    with open(f"{filename}.rst", "w", encoding='utf-8') as outfile:
        outfile.write(data)
    with open(f"{filename}.md", "w", encoding='utf-8') as outfile:
        md_data=rst_to_myst(data).text
        outfile.write(md_data)
    print("Saved the fetched data to a file.")

def mkdir(dir_name):
    # Normalize the directory path to handle cases like "dir1//dir2"
    dir_name = os.path.normpath(dir_name)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print(f"{dir_name} created!")
    else:
        print(f"{dir_name} already exists!")

def tree_call(cur_file, url, home_url, home_dir):
    filename=f"{cur_file}"
    code=fetch_and_save_data(filename,url)
    if code==1:
        return
    def cd_back_link(url, num_parts_to_remove=1):
        if not url:
            return ""

        for _ in range(num_parts_to_remove):
            url = url.rsplit('/', 1)[0]

        return url + '/'
    def cd_dir(num=1):
        for _ in range(num):
            os.chdir('..')
        # To verify, let's print the current working directory after the change(s)
        print(os.getcwd())
    parser = RSTParser(f"{filename}.rst")
    parser_md = MarkdownParser(f'{filename}.md')
    parser_md.print_header_tree()
    parser_md.print_segment()
    parser_md.concat_print()
    # parser.print_header_tree()
    # parser.save_parsed_data()
    # parser.concat_print()
    # print(parser.toctree_content)
    # print(f"prev:{url}")
    url=cd_back_link(url)
    # print(f"cur:{url}")
    current_directory = os.getcwd()
    # print(f"Current directory is {current_directory}")
    
    for sublink in parser.toctree_content:
        if sublink.startswith('/'):
            # print("case1")
            sublink=sublink[1:]
            part=sublink.split("/")
            # print(f"part:{part}")
            cur_name,dir=part[-1],'/'.join(part[:-1])
            if cur_name=='*' or re.match(r'^https.*',sublink) is not None:
                continue
            # print(f"cur_name:{cur_name}")
            os.chdir(home_dir)
            # print(f"dir_before:{dir}")
            mkdir(dir)
            
            if dir:
                os.chdir(dir)
            # print(f"dir:{dir}")
            sublink=sublink[:-4] if sublink.endswith('.rst') else sublink
            temp_url=url
            url=home_url+sublink+".rst?plain=1"
            print(url)
            tree_call(cur_name, url, home_url, home_dir)
            url=temp_url
            os.chdir(current_directory)
            
        else:
            # print("case2")
            part=sublink.split("/")
            cur_name,dir=part[-1],'/'.join(part[:-1])
            if cur_name in ignore or re.match(r'^https.*',sublink) is not None:
                continue    
            # print(f"cur_name:{cur_name}")
            # print(f"dir_before:{dir}")
            mkdir(dir)
            if dir:
                os.chdir(dir)
            # print(f"dir:{dir}")
            sublink=sublink[:-4] if sublink.endswith('.rst') else sublink
            url+=sublink+".rst?plain=1"
            print(url)
            tree_call(cur_name, url, home_url, home_dir)
            url=cd_back_link(url, len(part))
            os.chdir(current_directory)



if __name__ == "__main__":
    # Numpy
    # mkdir('numpy')
    # os.chdir('numpy')
    # starting='index'
    # url=f"https://github.com/numpy/numpy/blob/main/doc/source/index.rst?plain=1"

    # Sawyer
    mkdir('Sawyer_md')
    os.chdir('Sawyer_md')
    starting='index'
    url = f"https://github.com/ros-planning/moveit_tutorials/blob/master/index.rst?plain=1"
    
    home_url= url.rsplit('/', 1)[0]
    # Current directory
    home_dir=os.getcwd()
    tree_call(starting,url,home_url,home_dir)