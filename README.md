[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15318936&assignment_repo_type=AssignmentRepo)
# Mood Assessor

Create an app whereby a user can enter their mood every day, and the program will diagnose any mood disorders detected over the course of the last week (7 days).

_Please note that this application is for educational and fun purposes only. It is intentionally simplistic, and does not attempt to accurately diagnose moods or psychiatric conditions._

## Requirements

You will create one function named `assess_mood()` in a file named `mood_assessor.py`, which performs the following tasks. Running this file directly will do nothing. You will call this function from a file named `main.py` - running `main.py` is how the program should be run.

You are welcome to break up the code into multiple funcitons within the `mood_assessor.py` file, as you have learned to do. But it must be possible to call only `assess_mood()` from `main.py` and have the entire program run from start-to-finish, regardless of how many other functions are called within `assess_mood()`.

### Asking for a mood entry

Every day the program is run, it should do the following once:

1. ask the user to input their current mood
1. validate the user's response (the code must accept the following moods: `happy`, `relaxed`, `apathetic`, `sad`, and `angry`)
1. if the response was invalid, repeat starting from step 1 until valid response is gathered
1. translate the user's response to an integer (`happy` -> 2, `relaxed` -> 1, `apathetic` -> 0, `sad` -> -1, `angry` -> -2)
1. store the integer as a new line in a text file named `mood_diary.txt` within a subdirectory named `data`.

### Limit input to once-per-day

If the user has already entered a valid mood on any given day, and the user attempts to run the program again on that same day, the program must simply print, "Sorry, you have already entered your mood today." and quit.

Use the `datetime` module's `date.today()` function to determine the current date. For example:

```python
import datetime
date_today = datetime.date.today() # get the date today as a date object
date_today = str(date_today) # convert it to a string
```

Your program **must** call this function once or twice when it runs:

1. Call it while checking whether the user has already entered a mood today.
1. If the user has not already entered a mood today, you **must** call this function a second time while storing the user's mood today, along with today's date, to a file. Don't just reuse the date you got when calling this function the first time, since the user might have left the program running for more than a day.

### Diagnosing disorders

The first time the program is run each day, after gathering the mood from the user according to the instructions above, the program should also do the following:

1. check whether there are at least 7 entries in the `mood_diary.txt` file.
1. if not, do nothing further.
1. if so, retrieve the most recent 7 entries from the `mood_diary.txt` text file (i.e. the last 7 lines)
1. calculate the average mood from those entries (take the rounded numeric average of the 7 entries, and convert that to the appropriate string representing their average mood.)
1. if the user has been happy for 5 or more days out of the last 7 days, the user should be diagnosed as `manic`
1. if the user has been sad for 4 or more days out of the last 7, the user should be diagnosed as `depressive`
1. if the user has been apathetic for 6 or more days out of the last 7, the user should be diagnosed as `schizoid`
1. if none of the above apply, the user should be diagnosed with their average mood over the last 7 days
1. print out the user's diagnosis, following the format, "`Your diagnosis: schizoid!`", where `schizoid` is replaced with the correct diagnosis.

## Clone this repository

First, clone this repository to your local computer, using Visual Studio Code's cloning feature.

Helpful video:

- [cloning a code repository from GitHub to Visual Studio Code on your local machine](https://www.youtube.com/watch?v=Xyr3cU5FhSQ&list=PL-DdwrWUDZnMCYaUqegGMPKDVJcPn-QJm&index=5).

## Set up Visual Studio Code

Once cloned, set Visual Studio Code to be suitable for Python development using the "command palette":

- set the interpreter to a Python 3.x interpreter, such as that by [`Anaconda`](https://www.anaconda.com/).
- set the linter to by `pylint`.
- set the test framework to be `pytest` using the `tests` directory.

Helpful video:

- [Setting up Visual Studio Code for Python development](https://www.youtube.com/watch?v=iYhplpI-79Y&list=PL-DdwrWUDZnMCYaUqegGMPKDVJcPn-QJm&index=4)

## Create the code

You must create three files:

- `mood_assessor.py` - this file must include a function named `assess_mood()` that takes no arguments and outputs the user's mood, based on the data found in the file named `mood_diary.txt`.
- `main.py` - this file must call the `assess_mood()` function defined in the file named `mood_assessor.py`.
- `data` / `mood_diary.txt` - this file must be automatically created by your program. It will store the user's mood entries.

## Verify your program runs correctly

Make sure that your program behaves as expected when you run it. Review the requirements and compare your work to them. Any requests for user input or printed output should match exactly the samples given in the instructions. Pay attention to details, such as the number of spaces, the number of newlines, the use of punctuation, etc.

To run a program, open the **Run and Debug** panel within Visual Studio Code. When you first open this panel, it will offer an option to "`Create a launch.json file`". Click that option, it may ask what type of file you intend to run - if so, select regular `Python file`. Then, immediately close down the `launch.json` file that pops open, since it is a settings file for Visual Studio Code that we do not need to change.

Run the file named `main.py`. The code in this file makes use those functions you have modified in the other file to produce and output the text.

A best practice is to focus on one problem at a time. Comment out any lines in the `main.py` program that run parts of the code you are not interested in trying out at the moment.

Helpful video:

- [Modifying and running a Python program in Visual Studio Code](https://www.youtube.com/watch?v=itXffzwRLaE&list=PL-DdwrWUDZnMCYaUqegGMPKDVJcPn-QJm&index=3)

### Verify that the tests pass

Pytest-based tests are included in the `tests` directory that will help you determine whether each function is operating as expected. If the code has been completed correctly, all tests should pass. If not, they will fail. You should not modify any files in the `tests` directory and you should never run the test files directly.

**To run the tests**, open the **Tests** panel in Visual Studio Code and click the _Run All Tests_ button, usually represented as a "play" button icon. This will run all the tests in all the files in the `tests` directory. There are also run buttons next to each individual test that can be clicked to run specific tests. Running the tests will show which tests pass and which fail. Passing tests are generally shown with a green checkmark icon, while failing tests are shown with a red cross icon.

**If the tests pass**, this means that your code is generally correct. These automated tests cannot check the correctness of all features of your code, so you should always verify that the behavior of your program matches the requirements by running the code and trying it yourself manually.

**If the tests fail**, this means there are errors/mistakes in your solution. For those tests that fail, clicking on the test will show an _AssertionError_ message that may be helpful identifying where the error is in your code.

**If the tests never load**, most likely there are major errors in your code that prevent it from working. The tests will not work if your code does not run, so always try running your code first. You can find out why the tests don’t load by opening Visual Studio Code’s **Terminal** panel and running the command `pytest --collect-only` (If your computer says the command, `pytest` is not found, try installing it with `pip install pytest` or `pip3 install pytest`. Then try running it again. If it still says `pytest` is not found, try `python -m pytest --collect-only` instead). This will show error messages explaining why the tests did not load correctly.

- If an errors says the `freezegun` module is not installed, try running the command `pip install freezegun` or `pip3 install freezegun` and then try again.
- If the command above doesn't show any erorrs yet the editor still doesn't load the tests, you can run the tests entirely from the **Terminal** with the `pytest` command.
- If the command above doesn't show any error and the tests still don't load you can also try to delete any directories in the project named `__pycache__`, `.pytest_cache` and `tests/__pycache__`, close down your code editor window, open it again, and try running the tests again. If that still fails, try running the tests from the **Terminal** with the `pytest` command as indicated above.
- If error messages that show up when running the `pytest --collect-only` command indicate an error in your code files, fix those errors and try to load the tests again. A common error is, "`reading from stdin while output is captured!`" - this is always due to incorrect indentation of your code, where code that is meant to be nested within a function is, in fact, not indented beneath the function definition line and thus not considered by Python to be part of that functino.

**If, for whatever reason, you are not able to get the tests to load**, this should not stop you from completing the work. Carry on and make sure your programs perform as expected the “old fashioned way” - verify they behave correctly yourself by running them and trying them out. In most cases, the instructions are clear and following them exactly will result in a correct program.

Helpful video:

- [Running unit tests in Visual Studio Code](https://www.youtube.com/watch?v=FCICe3Tua2g&list=PL-DdwrWUDZnMCYaUqegGMPKDVJcPn-QJm&index=2)

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "`Source Control"` and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)

Helpful video:

- [Submitting work from Visual Studio Code to GitHub](https://www.youtube.com/watch?v=ePIOee1D8Js&list=PL-DdwrWUDZnMCYaUqegGMPKDVJcPn-QJm&index=1)
