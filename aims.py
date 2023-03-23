import time
import random

# Create a dictionary to store the animal data
animal_data = {}

# Define a function to register a new animal
def register_animal(animal_id, animal_name, species):
    animal_data[animal_id] = {
        "name": animal_name,
        "species": species,
        "last_seen": time.time() # Initialize last seen time as current time
    }
    print("Animal registered successfully!")

# Define a function to update the last seen time of an animal
def update_last_seen(animal_id):
    if animal_id in animal_data:
        animal_data[animal_id]["last_seen"] = time.time()
        print("Last seen time updated successfully!")
    else:
        print("Animal not found in database.")

# Define a function to generate a report of animals not seen in a specified time period
def generate_report(time_period):
    current_time = time.time()
    not_seen = []
    for animal_id in animal_data:
        if current_time - animal_data[animal_id]["last_seen"] > time_period:
            not_seen.append(animal_data[animal_id]["name"])
    if len(not_seen) > 0:
        print("The following animals have not been seen in the last " + str(time_period/60) + " minutes:")
        for animal_name in not_seen:
            print(animal_name)
    else:
        print("All animals have been seen in the last " + str(time_period/60) + " minutes.")

def adviser():
    

    import openai

# Define OpenAI API key 
    openai.api_key = "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"

# Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = "possible diseases for "+species+"of weight "+weight+"kg with "+symptoms 

# Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        )

    response = completion.choices[0].text
    print("The possible medical conditions for "+animal_name+" are:")
    print(response)
n=0
while n==0:
#Taking input from user
    animal_id=int(input('ENTER YOUR PET\'S ID: '))
    animal_name=input('ENTER YOUR PET\'S NAME: ')
    weight=input('ENTER YOUR PET\'S WEIGHT: ')
    species=input('ENTER YOUR PET\'S SPECIES: ')
    symptoms=input('ENTER YOUR PET\'S SYMPTOMS(SEPERATE BY COMMAS): ')
    usuage=int(input('ENTER THE CORRESPONDING NUMBER\n1.REGISTER THE PET\n2.SEE LAST SSEN TIME\n3.GENERATE REPORT\n4.ASK ADVICE\n'))

    if usuage==1:
        register_animal(animal_id, animal_name, species)
        ask=input('DO YOU WISH TO WRITE AGAIN[Y/N]')
        if ask=='y':
            n=0
        else:
            exit()
    elif usuage==2:
        time.sleep(2) # Simulate passage of time
        update_last_seen(1)
        ask=input('DO YOU WISH TO WRITE AGAIN[Y/N]')
        if ask=='y':
            n=0
        else:
            exit()
    elif usuage==3:    
        generate_report(60) # Generate report of animals not seen in the last 1 hour
        ask=input('DO YOU WISH TO WRITE AGAIN[Y/N]')
        if ask=='y':
            n=0
        else:
            exit()
    elif usuage==4:
        adviser()
        ask=input('DO YOU WISH TO WRITE AGAIN[Y/N]')
        if ask=='y':
            n=0
        else:
            exit()
    else:
        print('ENTER VALID OPTION')
        ask=input('DO YOU WISH TO WRITE AGAIN[Y/N]')
        if ask=='y':
            n=0
        else:
            exit()

	
            
