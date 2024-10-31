from groq import Groq
from groq.types.chat import ChatCompletionUserMessageParam, ChatCompletionSystemMessageParam
import sys
import os
from datetime import date

g = Groq()


def main():
    files_to_summarize = sys.argv[1:]

    if not files_to_summarize:
        print('expected files to summarize in every command line argument, got none')
        sys.exit(-1)
    
    text_file_contents = ''
    
    for file in files_to_summarize:
        if not os.path.exists(file):
            print('file does not exist:', file)
            sys.exit(-2)

        file_name = os.path.basename(file)
        
        d = date(
            2000 + int(file_name[4:6]),
            int(file_name[0:2]),
            int(file_name[2:4])
        )
        
        text_file_contents += f"{d.strftime('%B %d, %Y')}:\n```\n"

        with open(file, 'rt') as fp:
            text_file_contents += fp.read()
        
        text_file_contents += "```\n\n"
    
    completion = g.chat.completions.create(
        model="llama-3.1-70b-versatile",
        stream=True,
        messages=[
            ChatCompletionSystemMessageParam(
                role="system",
                content="""Respond ONLY with a summary the following text files into one, cohensive summary of the entire period (most likely only a month). Write as if you are a member of the team writing this--say "we" did something instead of saying "the team" did something."""
            ),
            ChatCompletionUserMessageParam(
                role="user",
                content=text_file_contents.strip()
            ),
            ChatCompletionSystemMessageParam(
                role="assistant",
                content="Here is a cohesive and detailed summary of the entire period:\n\n"
            )
        ],
    )

    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end='', flush=True)

if __name__ == "__main__":
    main()
