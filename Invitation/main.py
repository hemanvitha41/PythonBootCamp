#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

def generate_letter(letter, invited, output):
    with open(letter, 'r') as file:
        letter_content = file.read()
    with open(invited, 'r') as file:
        names = file.read().splitlines()
        
    for name in names:
        personalized_letter = letter_content.replace("[name]", name)
        with open(f"{output}/{name}.txt", 'w') as file:
            file.write(personalized_letter)
    print("Letters generated successfully")


letter_path = "./Input/Letters/starting_letter.txt"
invited_path = "./Input/Names/invited_names.txt"
output_path = "./Output/ReadyToSend"

generate_letter(letter_path, invited_path, output_path)