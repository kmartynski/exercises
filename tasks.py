import pandas as pd
from datetime import datetime
from cmd import Cmd
import os

time_format = '%Y-%m-%d'

class MyPrompt(Cmd):
    prompt = '/> '
    intro = "Welcome to your to do list, here you can list, add, delete or update your tasks!\n" \
            "If you are just getting started, please remember to create your file! Type 'create' to do so!"

    def do_exit(self, inp):
        print("Exit")
        return True

    def do_create(self, file):
        df = pd.DataFrame(columns=["Name", "Deadline", "Description"])
        if os.path.exists(f'./{file}.csv'):
            print("This file already exists!")
        else:
            df.to_csv(f'./{file}.csv', index=False)
            print("CSV file has been created!")

    def help_create(self):
        print("Type 'create' and a name of your .csv file. Just as the following:\n"
              "create test")

    def do_list(self, inp):
        file, action = [s for s in inp.split()]
        df = pd.read_csv(f'./{file}.csv')
        if action == "all":
            print(df)
        elif action == "today":
            today = datetime.today()
            print(df.loc[df['Deadline'] == str(today.strftime(time_format))])

    def help_list(self):
        print("Type 'list <filename>' to see all records in your .csv\n"
              "Add <all> to see the whole file or add <today> to see today's tasks.")

    def do_add(self, inp):
        file, name, deadline, desc = [s for s in inp.split()]
        description = f"{desc.replace('-', ' ')}"
        df = pd.read_csv(f'./{file}.csv')
        df = df.append({'Name': name, "Deadline": deadline, "Description": description}, ignore_index=True)
        print(f"New record has been added!")
        df.to_csv(f'./{file}.csv', index=False)

    def help_add(self):
        print("Type 'add <filename> <taskname> <deadline> <description>' to add a new file.\n"
              f"Deadline format {time_format}\n"
              f"All fields required!\n"
              "If you want to parse sentences use '-' between each word, like here:(Go-for-a-walk)")

    def do_delete(self, inp):
        file, record = [s for s in inp.split()]
        df = pd.read_csv(f'./{file}.csv')
        df = df.drop(int(record))
        df.to_csv(f'./{file}.csv', index=False)
        print("The record has been removed!")

    def help_delete(self):
        print("Type 'delete <filename> <row>' to remove it.")

    def do_update(self, inp):
        file, record, column, value = [s for s in inp.split()]
        if '-' in value:
            value = f"{value.replace('-', ' ')}"
        df = pd.read_csv(f'./{file}.csv')
        df.at[int(record), column] = value
        print(f"Row {record} has been updated!\n"
              f"Value in {column} column updated to: {value}!")
        df.to_csv(f'./{file}.csv', index=False)

    def help_update(self):
        print("Type 'update <filename> <record> <columnname> <value>' to updated your record!\n"
              "record -> row number\n"
              "colmnnname -> e.g 'Name'\n"
              "value -> what ever you want to add here (keep in mind time format\n"
              "If you want to parse sentences use '-' between each word, like here:(Go-for-a-walk)")

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)

        print("Default: {}".format(inp))

    do_EOF = do_exit

if __name__ == '__main__':
    MyPrompt().cmdloop()