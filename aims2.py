#install openai module before use


def adviser():
    name=input('ENTER YOUR PET\'S NAME: ')
    weight=input('ENTER YOUR PET\'S WEIGHT: ')
    species=input('ENTER YOUR PET\'S SPECIES: ')
    symptoms=input('ENTER YOUR PET\'S SYMPTOMS(SEPERATE BY COMMAS): ')

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
    print("The possible medical conditions for "+name+" are:")
    print(response)
adviser()
	
            
