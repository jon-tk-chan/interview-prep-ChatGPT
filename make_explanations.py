import openai
import json 
import pandas as pd
import time

import credentials as keys

in_file = "data/key_terms.csv"
out_file = "explanations.json"

def explain_short(in_prompt, max_words=250, model_engine="text-davinci-003"):
    """Returns the explanation of key_term in 250 words or next
    
    input: key_term (str)
    """
    prompt_q = "Explain the concept of " + in_prompt + " in" + str(max_words) + " words or less."
    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_q,
        max_tokens=1024, #prompt restricts length of response, but max_tokens determines cutoff tokens 
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response


def explain_simple(in_prompt, model_engine="text-davinci-003"):
    """Returns the explanation of key_term like you are 5 (or a stressed out Director)
    
    input: key_term (str)
    """
    prompt_q = "Explain the concept of " + in_prompt + "like I am 5 years old."
    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_q,
        max_tokens=1024, #prompt restricts length of response, but max_tokens determines cutoff tokens 
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response

def explain_expert(in_prompt, model_engine="text-davinci-003"):
    """Returns the explanation of key_term to a technical expert.
    
    input: key_term (str)
    """
    prompt_q = "Explain the concept of " + in_prompt + "to a technical expert."
    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_q,
        max_tokens=1024, #prompt restricts length of response, but max_tokens determines cutoff tokens 
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    return response

def print_progress(iteration, total): 
    """Print progress to command line"""
    i = iteration + 1
    percent = 100 * (i / float(total))
    filled_num = int(100*i / total)
    filled_bar = '█'*filled_num
    unfilled_num = 100-filled_num
    unfilled_bar = "-"*unfilled_num
    print(f'\r|{filled_bar}{unfilled_bar}| {percent}%')
    if i == total: 
        print("COMPLETE")


def main():
    """
    outputs a JSON containing the terms from 'keyTerms' column in in_file with an explanation at each level
    """
    openai.api_key = keys.API_KEY

    out_json = {}
    df = pd.read_csv(in_file)
    key_terms = df['keyTerms'].tolist()
    num_terms = len(key_terms)
    start_time = time.time()

    print("Reading in data from", in_file, " .....")
    for i, key_term in enumerate(key_terms):

        out_json[key_term] = {
            "TERM": key_term,
            "exp_short": explain_short(key_term,100),
            "exp_5yo": explain_simple(key_term),
            "exp_expert":explain_expert(key_term)
        }
        
        print_progress(i, num_terms)
        print("--- %s seconds ---" % (time.time() - start_time))
        
    with open(out_file, "w") as f:
        json.dump(out_json, f)
    print("CREATED JSON: ", out_file)
    print("TERMS WRITEN: ", out_json.keys())

if __name__ == "__main__":
    main()