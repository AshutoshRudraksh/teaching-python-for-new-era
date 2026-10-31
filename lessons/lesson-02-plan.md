# Vineet lesson 2 prep, functions

Prepared Sun Oct 25, 2026 for the next Vineet lesson. The Oct 24 morning briefing listed a Vineet session at 11:00 PM CT on Thu Oct 29, 2026; if his new Saturday 11:00 AM CT slot is booked first instead, this same prep works unchanged. Student context is from the Oct 23 first lesson plan and his learning needs form in the same folder.

## Where lesson 1 left him
True beginner, first lesson went well. He typed and ran code himself: variables, a list of patient ages, an average, filtering patients 50 and over, and counting visits by condition in a small healthcare records list. The promised next step, stated in the lesson 1 close, is functions. Micro task he was given: bring three repeat spreadsheet or report tasks from his work. If he sends them before the lesson, swap the practice block below to his first task.

## Lesson shape
0 to 5 min, recap by recall. Ask him to say, without looking, how he calculated the average age last time. Then have him retype those three lines from memory. Recall first, correction second.

5 to 15 min, one new idea. A function is a named recipe: you write the steps once, then call the name whenever you need them. Show it on his own lesson 1 code first, nothing new yet:

def average_age(ages):
    total = sum(ages)
    return total / len(ages)

print(average_age([42, 35, 58, 29, 64]))

Have him predict the printed value before running it. Prediction before output, same rule as lesson 1.

15 to 30 min, hands on, he types. Extend the recipe idea to his healthcare world:
1. Write a function count_visits(records) that returns the visits by condition counts he built with a loop last time.
2. Call it on the same four record list from lesson 1 so he can check the answer against what he already knows is right.
3. If that lands cleanly, change one record together and predict the new count before running.

30 to 42 min, bridge to his work. Show why functions matter for his repeat reports: the same steps run every week, so the recipe gets written once and reused. If he brought his three tasks, pick the smallest one and name, together, what its function would be called and what it would take in and return. Naming only, no build yet.

42 to 50 min, close. Confirm the rhythm in person while he is warm: Saturdays at 9 AM his time, plus the weekday he picks. Tell him the next lesson applies functions to reading a small spreadsheet style table, which is where his own report tasks start becoming the lesson material.

## Delivery notes
Speak slowly and define every new word the first time it appears. He types, you guide. If the technology fights you, protect the 15 to 30 minute block and drop the bridge section. A finished count_visits function he wrote himself is the win to protect.
