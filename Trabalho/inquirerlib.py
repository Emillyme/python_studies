import inquirer

questions = [
    inquirer.Text('name', message="What's your name?"),
    inquirer.List('gender', message="Select your gender", choices=['Male', 'Female', 'Other']),
]

answers = inquirer.prompt(questions)

print("Hello, {}!".format(answers['name']))
print("You selected gender as: {}".format(answers['gender']))