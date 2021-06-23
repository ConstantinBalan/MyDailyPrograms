import os
import subprocess
import webbrowser

slack = os.environ['SLACK_LINK']
jira = os.environ['JIRA_LINK']
adm = os.environ['ADM_LINK']
discord = os.environ['DISCORD_PATH']
steam = os.environ['STEAM_PATH']
spotify = os.environ['SPOTIFY_PATH']


def work_programs():
    print("Opening work programs...")
    brave = webbrowser.get(using='chromium')
    try:
        brave.open(slack, new=2)
        brave.open(jira, new=2)
        brave.open(adm, new=2)
    except RuntimeError as e:
        print("Could not open work programs")


def gaming_programs():
    print("Opening gaming programs...")
    try:
        subprocess.Popen([discord])
        subprocess.Popen([steam])
        subprocess.Popen([spotify])
    except RuntimeError as e:
        print("Could not open gaming programs")


def main():
    user_prompt = input("What would you like to open?"
                        "\n 'W' or 'w' for Work Programs "
                        "\n 'G' or 'g' for Gaming Programs"
                        "\n Input: ")
    print("User Prompt is " + user_prompt)
    if user_prompt == 'W' or user_prompt == 'w':
        work_programs()
    elif user_prompt == 'G' or user_prompt == 'g':
        gaming_programs()
    else:
        print("Please enter a valid option")
        main()


if __name__ == "__main__":
    main()