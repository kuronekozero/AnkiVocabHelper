# English Vocabulary Helper

The English Vocabulary Helper is a tool designed to assist learners in expanding their English vocabulary. It leverages the free Twinword API to assess the difficulty of English words. The application aids in determining which words should be added to Anki next. Typically, learners prefer to start with words that are easier, more common, and frequently used. This is where Twinword’s API comes into play - it evaluates the complexity of words, allowing users to prioritize learning words based on their difficulty level.

The primary purpose of this application is to facilitate the tracking of new words for users, particularly those who use Anki for learning english language. 

By using this application, learners can streamline their vocabulary learning process and focus on the most relevant words first.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
```
git clone https://github.com/kuronekozero/EnglishVocabHelper.git
```
3. Navigate to the `gui` folder in project directory.

## Setting Up the API Key

Before you can use this application, you’ll need to obtain an API key from Twinword. Here’s how:

1. Go to the Twinword API page(they have page on rapidAPI website).
```
https://rapidapi.com/user/twinword
```
3. Sign up for a free account or log in if you already have one.
4. Navigate to your dashboard and create a new application to get your API key(yes, it's free up to 9000 requests a month).
   You'll need an API and X-RapidAPI-Host(it will look something like this "twinword-twinword-bundle-v1.p.rapidapi.com". Actually I think this thing is the same for every user so you can just copy it from here and paste it in `apikey.txt` file) for "Language scoring".

Once you have your API key, you’ll need to add it to the `apikey.txt` file in the project directory. The file should look like this:

```
X-RapidAPI-Key: YOUR_API_KEY
X-RapidAPI-Host: YOUR_X_RAPIDAPI_HOST
```

Replace `YOUR_API_KEY` and `YOUR_X_RAPIDAPI_HOST` with your actual API key and X-RapidAPI-Host.

## Building the Executable

This project uses PyInstaller to build an executable file. If you don’t have PyInstaller installed, you can install it with pip:

```
pip install pyinstaller
```

Also you should ran this two commands:

```
pip install requests
```

and

```
pip install PyQt5
```

Once PyInstaller and requests, PyQt5 libraries are installed, you can build the executable by running the following command in the project directory in gui folder where window.py file is located. Just navigate there, copy the path(it will look something like "C:\Users\user\pythonProject\gui") and write in cmd the following:
Replace my path with your actual path!

```
cd C:\Users\user\pythonProject\gui
```
Ok, after that while you are still in the gui folder just write the following:

```
pyinstaller --onefile --noconsole window.py
```

Ok, now you can close your cmd.
This will create a new executable file in the `dist` subdirectory DON'T LOUNCH IT! IT WON'T WORK FROM `dist` FOLDER!
First move this new .exe file from `dist` folder to the same folder where window.py file is located(to `gui` folder). After that you can just delete `dist` folder.

That's it!

## Running the Application

To run the application, simply execute the built exe file. You can add new words to assess their difficulty and review them later. 
After adding some words just sort the table by difficulty.

## Some additional information about this program.

1. To add a new word you can just press ENTER after typing the word, you don't have to click "add" all the time.
2. If you want to add more than one word at ones you can just write the list of words that you want ot add devided by space. The program will send each word separately to the API.
3. You can sort words in each direction from the simplest to the most difficult and in the opposite way by just clicking twice on the "difficulty" button.
4. The word's difficulty varies from 1 to 10. If you are getting the word with number 11 that means that the API doesn't have this word. It happens very rare, usually with some very unpopular words, slang or some VERY simple words(like "What" for example(idk why really...))



