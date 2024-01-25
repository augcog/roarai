import openai
import pickle
from dotenv import load_dotenv
import os
from tqdm import tqdm
import tiktoken
import string
import os
import csv

load_dotenv()

# TODO MODEL
# model = 'zephyr'
model = 'openai'
# TODO TOKEN LIMIT
n = 400

if model == 'local' or model == 'zephyr':
    openai.api_key = "empty"
    openai.api_base = "http://localhost:8000/v1"
elif model == 'openai':
    openai.api_key = os.getenv("OPENAI_API_KEY")

def mkdir(directory_path):
    # Check if the directory already exists
    if not os.path.exists(directory_path):
        # If the directory does not exist, create it
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' was created.")
    else:
        # If the directory exists, do nothing
        print(f"Directory '{directory_path}' already exists.")
def token_size(sentence):
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return len(encoding.encode(sentence))

def rfind_punctuation(s, start, end):
    for i in range(end-1, start-1, -1):  # end-1 because Python slices are exclusive at the end
        if s[i] in string.punctuation:
            return i
    return -1  # If no punctuation is found
def send_split_message_user(response, token_limit=300):
    msg_list = []
    # print(token_limit)
    tokens = token_size(response)

    if tokens > token_limit:
        start = 0
        while start < len(response):
            end = start
            while end < len(response) and token_size(response[start:end]) < token_limit:
                end += 1

            if end < len(response):
                # Look for a suitable split position
                split_pos = response.rfind('\n\n', start, end)
                if split_pos == -1:
                    split_pos = response.rfind('\n', start, end)
                if split_pos == -1:
                    split_pos = rfind_punctuation(response, start, end)
                if split_pos == -1:
                    split_pos = response.rfind(' ', start, end)
                if split_pos == -1 or split_pos <= start:
                    split_pos = end - 1

                msg_list.append(response[start:split_pos].strip())
                start = split_pos + 1
            else:
                # Add the last chunk
                msg_list.append(response[start:end].strip())
                break
    else:
        msg_list.append(response)

    return msg_list
def generate_path_question(id, document):
    user_question = ''
    # print(document)
    # function reads all .pkl files in a given directory, extracts text segments from them, and returns a concatenated string of all these segments.
    system_prompt = "Generate a long and specific question that could be asked about this document."
    # Construct the messages list with the current system prompt, documents, and user question
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"document: {document}"
        },
    ]

    # Get the response from OpenAI's model for the current set of messages
    openai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    # Add explanation to dataset
    question = openai_response["choices"][0]["message"]["content"]
    # ask for response
    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant that helps answer the question with the given documentation. Think like you are explaining to a five year old."
        },
        {
            "role": "user",
            "content": f"question: {question}\n---\ndocument: {document}"
        },
    ]
    openai_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
    )
    return (id, question, document, openai_response["choices"][0]["message"]["content"])

def string_subtraction(main_string, sub_string):
    return main_string.replace(sub_string, '', 1)  # The '1' ensures only the first occurrence is removed

def traverse_files(path, start_folder_name):
    results = []
    # Check if the provided path exists
    if not os.path.exists(path):
        raise ValueError(f"The provided path '{path}' does not exist.")
    # print(os.walk(path))
    folder_tree = f"{start_folder_name} (h1)\n"
    for root, dir, files in os.walk(path):
        # print(root, dir, files)

        for file in files:
            if file.endswith('.pkl'):
                path_list = [start_folder_name] + string_subtraction(root, path).split('/')[1:]
                line = ((len(path_list)-1)*"--" + path_list[-1] + f" (L{len(path_list)})")
                folder_tree += f"{line}\n"
    # print(tree)

    for root, dir ,files in os.walk(path):
        # print(root, dir, files)
        for file in files:
            if file.endswith('.pkl'):
                # file path
                file_path = os.path.join(root, file)
                path_list = [start_folder_name] + string_subtraction(root, path).split('/')[1:]
                with open(file_path, 'rb') as pkl_file:
                    content = pickle.load(pkl_file)
                # print(path_list)
                folder_path = ' > '.join(f"{item} (Level{i+1})" for i, item in enumerate(path_list))
                # print(content)
                results.append(([folder_tree, folder_path], content))
    return results
docs = []

questions =[]
i = 20
for doc in tqdm(docs, desc="Generating questions"):

    folder = doc[0]
    file = doc[1]
    folder_tree = folder[0]
    folder_path = folder[1]
    for chunk in file:
        segment_tree = chunk['Page_table']
        segment_path = chunk['Page_path'].split('\n')[-1]
        segment = chunk['Segment_print']
        count = 1
        # seperate recursively
        segment = send_split_message_user(segment, n)
        for smaller_chunk in segment:
            if i == 0:
                break
            i-=1

            id = folder_path + " > " + segment_path + f"({count})"
            count += 1
            questions.append(generate_path_question(id, smaller_chunk))
        if i == 0:
            break
    if i == 0:
        break


mkdir("Dataset")
os.chdir("Dataset")

# New code block for writing questions to a CSV file
csv_filename = f'{model}_{n}_questions.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['ID', 'Question', 'Document', 'Response'])  # Write the header row
    for question in questions:
        csvwriter.writerow([question[0], question[1], question[2], question[3]])  # Write each question

print(f"Saved {len(questions)} questions to '{csv_filename}'")

os.chdir("..")