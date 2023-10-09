# English Vocabulary Helper

The English Vocabulary Helper is a free tool designed to assist learners in expanding their English vocabulary. It leverages the wordfreq python library to assess the difficulty of English words. The application aids in determining which words should be added to Anki next. Typically, learners prefer to start with words that are easier, more common, and frequently used. This is where wordfreq library comes into play - it evaluates the complexity of words, allowing users to prioritize learning words based on their difficulty level.

![Screenshot](Screenshot_1.png)

The primary purpose of this application is to facilitate the tracking of new words for users, particularly those who use Anki for learning english language. 

By using this application, learners can streamline their vocabulary learning process and focus on the most relevant words first.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine.
```
git clone https://github.com/kuronekozero/EnglishVocabHelper.git
```
2. (Optional) You may require to run the following 2 commands for program to work properly if the step 4 won't work.
```
pip install requests
```

and

```
pip install PyQt5
```

3. Navigate to the `gui` folder in project directory.

4. Run main.exe file.

That's it!

Now you can create a shortcut of main.exe and put it to your desktop screen.

## Running the Application

To run the application, simply execute the built exe file. You can add new tables and words to assess their difficulty and review them later. 
After adding some words just sort the table by difficulty.

## Development Updates

### Fixes and Improvements

- ~~**Issue 1**: Fix sorting order.~~ (Completed)
- ~~**Issue 2**: Fix upper case lower case problem.~~ (Completed)
- **Issue 3**: Fix sorting words by date.
- **Issue 4**: Fix colors of tables menu.  

### Planned Additions and Changes

- **Addition/Change 1**: Add other languages support.
- **Addition/Change 2**: Add option to add sentences of phrases.
- ~~**Addition/Change 3**: Add option to create more than one table.~~ (Completed)
- ~~**Addition/Change 4**: Add stars near each word so the word will be in priority while sorting.~~  (Completed)

## Troubleshooting

This section describes some known issues you may encounter while using the English Vocabulary Helper,

### 1. Error (225, 'BeginUpdateResource', 'The operation was not completed successfully because the file contains a virus or potentially unwanted software.') while running pyinstaller

If you encounter this error, it is recommended to completely disable the Windows 10/11 antivirus in your system settings and then try to rebuild the exe file again. I honestly speaking have no idea why this problem occurs. In earlier versions of my program everything worked great without disabling antivirus.

## Some additional information about this program.

1. To add a new word you can just press ENTER after typing the word, you don't have to click "add" all the time.
2. If you want to add more than one word at ones you can just write the list of words that you want ot add devided by space. The program will send each word separately to the API.
3. You can sort words in each direction from the simplest to the most difficult and in the opposite way by just clicking twice on the "difficulty" button.
4. The word's difficulty varies from 1 to 10. If you are getting the word with number 11 that means that the API doesn't have this word. It happens very rare, usually with some very unpopular words, slang or some VERY simple words(like "What" for example(idk why really...))



