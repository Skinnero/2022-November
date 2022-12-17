import sys

def add_idea(idea):  
    with open ('ideas.txt','a') as f:
        f.write(f'{idea}\n')
        
def list_ideas():
    with open ('ideas.txt','r') as f:
        ideas = f.read().splitlines()
        for item in ideas:
            print(f'{ideas.index(item) + 1}. {item}')
            
def length_of_ideas():
    with open('ideas.txt','r') as f:
        return len(f.readlines())    
    
def delete_idea(number):
    with open ('ideas.txt','r') as f:
        try:
            idea_to_remove = f.read().splitlines()[number-1]
            f.close()
        except IndexError:
            print(f'The list contains only {length_of_ideas()}')
            exit()
    
    with open('ideas.txt','r') as f:
        lines = f.readlines()
        f.close()
    
    with open('ideas.txt','w') as f:
        for line in lines:
            if line.strip("\n") != idea_to_remove:
                f.write(line)  

if sys.argv[-1] == '--list':
    list_ideas()   
    
elif len(sys.argv) == 3 and sys.argv[-2] == '--delete':
    try:
        item = int(sys.argv[-1])
        delete_idea(item)
        list_ideas()
    except ValueError:
        print("Specify a number after '--delete'")
    
else:
    while True:
        try:
            idea = input('What is your new idea? ')
            add_idea(idea)
        except KeyboardInterrupt:
            break
        