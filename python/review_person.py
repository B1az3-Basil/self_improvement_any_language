#!/usr/bin/env python3

import sys
import os
import subprocess
import random
from pprint import pprint
from termcolor import colored

final = {}
commands = ['grade', 'check', 'clear', 'comment', 'done', 'invite']
current_hash = ''
my_projects = {'HANGMAN - ITERATION 2' :'9e760d4f-adc7-4184-8c6c-538dd5c02532', 'PROBLEM - PYRAMID':'aeda1496-2eeb-49ed-9c86-d84593456cc3'
, 'HANGMAN - ITERATION 3':'c4ed8104-22a0-4b2b-96a8-879b4c9e6e69', 'PROBLEM - OUTLINE':'0b447f96-8fb9-4876-ae91-046267423a3e'
, 'MASTERMIND - ITERATION 1':'eb04c6dc-ddee-4751-a999-6e28f7861978', 'TOY ROBOT - ITERATION 1':'ef4e20e2-6ed5-4eea-93b6-78116b0083eb'
, 'MASTERMIND - ITERATION 2':'ead9542e-a32a-43d2-bfcf-c60e7559611f', 'MASTERMIND - ITERATION 3':'ec83fd21-6c13-4a78-9396-f57c8ffd3c83',
'PROBLEM - RECURSION':'decea39d-7a2a-45d9-bd08-1af152c94516','TOY ROBOT - ITERATION 2':'e5be25a3-5fd4-4f71-8dc0-67e3b8b211bf',
'PROBLEM - WORD PROCESSING':'254a6e98-30b6-4a8b-b255-a4e7aa0c4547', 'TOY ROBOT - ITERATION 3':'8dea9e69-07da-440d-964c-08e868e11561',
'PROBLEM - ACCOUNTING APP':'da2f7a67-be13-4e03-995d-1c63dc429bd6', 'TOY ROBOT - ITERATION 4':'c96a3dc4-1ee0-4cac-8d78-11a63c8213fd',
'TOY ROBOT - ITERATION 5':'f899e822-161f-4c92-9a42-7c7a2467c021', 'PROBLEM - FIX THE BUGS':'d3c51cf8-c246-478c-a3b2-fac6ac41df67'}

def remove(output):
    output = str(output)
    output = output.split('\\n')
    output[0] = output[1:]
    return output


def clean_list(output):
    output = [u for u in output[0] if u != '']
    return output


def remove_more(output):
    output = [u for u in output if u != 'Reviews:']
    output = [u for u in output if '[Assigned]' in u]
    return output

def get_hash_list(output):
    lis_ = []
    p = ''

    for i in output:
        a = i.split(' ')
        for z in a:
            if '(' in z:
                the_word = ''
                for m in z:
                    if m != '(' and m != ')':
                        the_word += m
                        
                lis_.append(the_word)
    return lis_

def invite_review():
    global commands
    choose = ['hangman', 'pyramid', 'outline', 'robot', 'mastermind', 'accounting', 'word', 'fix', 'recursion']
    check_num = ['Mastermind - Iteration 1', 'Mastermind - Iteration 2', 'Mastermind - Iteration 3', 'Outline', 'Word'
    , 'Toy Robot - Iteration 1', 'Toy Robot - Iteration 2', 'Toy Robot - Iteration 3', 'Toy Robot - Iteration 4', 'Toy Robot - Iteration 5', 'Pyramid',
    'Accounting App', 'Hangman - Iteration 1', 'Hangman - Iteration 2','Hangman - Iteration 3', 'Recursion', 'Bug']
    p = subprocess.Popen("wtc-lms reviews", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = remove(output)
    
    output[0].pop(len(output[0]) - 1)
    output = clean_list(output)
    output = [u for u in output if u != 'Reviews:']
    output = [u for u in output if '[Invited]' in u]
    print('*'*197)

    for z in check_num:
        output_num  = [u for u in output if z in u]
        num = len(output_num)
        if num != 0:
            print(z + ' - ' + str(num))

    print('*'*197)

    while True:
        chose = input('Which: ')
        chose = chose.split(' ')
        if chose[0].lower() in choose:
            break

    chose[0] = chose[0].lower()
    chose[0] = chose[0][0].upper() + chose[0][1:]
    output = [u for u in output if f'{chose[0]}' in u]

    if len(chose) > 1:
        output = [u for u in output if f'Iteration {chose[1]}' in u]
    
    if len(output) == 0:
        print('Not available!')
        return
    
    lis_ = get_hash_list(output)
    
    
    ran = random.randint(0, len(lis_) - 1)
    p = subprocess.Popen(f"wtc-lms accept {lis_[ran]}", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()

    return [lis_[ran]]

def is_int(value):
    """
    Tests if the string value is an int or not
    :param value: a string value to test
    :return: True if it is an int
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_user():
    while True:
        current_hash = ''
        user_name = input("Enter Users Name: ")
        user_name = user_name.lower()
        if is_available(user_name):
            current_hash = final[f'{user_name}@student.wethinkcode.co.za']
            return current_hash

        elif user_name == 'invite':
            current_hash = invite_review()
            break

        elif user_name == 'area51':
            for each_project in my_projects.keys():
                p = subprocess.Popen(f"wtc-lms history {my_projects[each_project]}" , stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                output = remove(output)
                output = clean_list(output)
                output.pop(len(output) - 1)
                
                if 'Passed Review' in output[5]:

                    print(f'{each_project} -> ' + colored('Passed', 'green'))
                
                elif 'Failed Review' in output[5]:
                    print(f'{each_project} -> ' + colored('FAILED', 'red'))
                
                else:
                    print(f'{each_project} -> ' + colored('In progress', 'yellow'))
    
            continue
            
        elif user_name == 'count':
            p = subprocess.Popen(f"wtc-lms reviews" , stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            output = remove(output)
            output = clean_list(output)
            output.pop(len(output) - 1)
            output = [out for out in output if 'Graded' in out]
            print(len(output))
            continue
        print('NO MATCH! TRY AGAIN')

    return current_hash


def done_every(current_hash):
    global commands
    p = subprocess.Popen(f"wtc-lms review_details {current_hash}" , stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = remove(output)
    output = clean_list(output)
    output.pop(len(output) - 1)
    print_details(output)
   
    return

def print_details(output):
    print('Details')
    print('*'*197)
    for s in output:
        print(s)
    print('*'*197)
    return

def is_available(value):
    global final 
    try:
        final[f'{value}@student.wethinkcode.co.za']
        return True
    except KeyError:
        return False

def to_do():
    global commands, current_hash
    while True:
        get = input('What to do: ')
        get = get.lower()
        if get in commands:
            if get == 'check':
                p = subprocess.Popen(f"wtc-lms review_details {current_hash[0]}" , stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                output = remove(output)
                output = clean_list(output)
                output.pop(len(output) - 1)
                for i in output:
                    print(i)

            elif get == 'comment':
                comment = input("What to say: ")
                p = subprocess.Popen(f"wtc-lms add_comment {current_hash[0]} '{comment}'" , stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                
            elif get == 'grade':
                comment = input("Grade: ")

                if is_int(comment):

                    p = subprocess.Popen(f"wtc-lms grade_review {current_hash[0]} {int(comment)}" , stdout=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    output = remove(output)
                    output = clean_list(output)
                    p = subprocess.Popen(f"rm -rf {current_hash[1]}" , stdout=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()

                else:
                    print('NOT INT')
            
            elif get == 'clear':
                os.system('clear')
            
            elif get == 'invite':
                current_invite = invite_review()   
                p = subprocess.Popen(f"wtc-lms review_details {current_invite[0]}" , stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                output = remove(output)
                output = clean_list(output)
                output.pop(len(output) - 1)
                print_details(output)

           
                    
            
            elif get == 'done':
                print('We are done!')
                break
        

def collect_info():
    global final, commands, current_hash
    p = subprocess.Popen("wtc-lms reviews", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = remove(output)
    output[0].pop(len(output[0]) - 1)
    output = clean_list(output)
    output = remove_more(output)

    lis_ = get_hash_list(output)

    name_user = []
    locations_file_ = []

    for i in lis_:
        p = subprocess.Popen(f"wtc-lms review_details {i}" , stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = remove(output)
        output = clean_list(output)
        output.pop(len(output) - 1)
        
        for h in output:
            if '@student.wethinkcode.co.za' in h:
                name_user.append(h[19:])
            elif '/goinfre/bkganyag/problems/' in h:
                locations_file_.append(h[10:])
    final = {}
    i = 0
    
    for each in name_user:
        final[each] = [lis_[i], locations_file_[i]]
        i += 1
    pprint(final)
    current_hash = get_user()
    done_every(current_hash[0])
    p = subprocess.Popen(f"wtc-lms sync_review {current_hash[0]}" , stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    try:
        p = subprocess.Popen(f"code {current_hash[1]}" , stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
    except IndexError:
        pass
    to_do()

             
if __name__ == "__main__":
    collect_info()
