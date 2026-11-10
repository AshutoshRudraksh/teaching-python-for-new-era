# Vineet lesson 2 run sheet, Functions & Modules

For Mon Nov 9, 2026, 11:00 PM CT (9:00 PM his time). Notebook: lesson-02-functions-and-modules.ipynb (25 cells, executed clean Nov 9; expected outputs below). This replaces the Oct 25 functions only prep for tonight; the older prep stays on file.

## State going in
Lesson 1 (Oct 31) taught and confirmed once: variables, lists, an average, filtering 50 plus, counting by condition. The Nov 7 lesson was missed on our side, so open warm and brief, acknowledge the reschedule once, then teach. He proposed Monday evening himself twice; no reply to our booking confirmation as of the evening check, booking live on his subscription.

## Timing map, 50 minutes
0 to 4, settle and recall. Ask him to say from memory how he calculated the average age in lesson 1. Recall first, correction second.
4 to 14, Part A theory. Function as a named recipe; parameters vs arguments; return vs print, the distinction to land hardest; scope in one minute, local variables live and die inside the function. He predicts every output before any cell runs.
14 to 20, Part B theory. Module as a file of recipes; import and namespace; the standard library as other people's tested functions. The statistics.mean demo proves his own function matches Python's built in one, a confidence moment, use it.
20 to 38, Part C walkthrough, he types everything. Build clinic_tools.py with %%writefile (average_age, count_by_condition, older_names), import it, hand calculate the report first (average age 51.4, Checkup 2, Diabetes 2, Blood pressure 1, 50 plus: Ravi, Arun, Kiran), then run the report cell. Protect this block if tech fights you; drop challenges, never this.
38 to 45, new data rerun. Add Sana, 29, Diabetes; predict the full new report together (average age drops to 47.7, Diabetes becomes 3), rerun the report cell unchanged. This is the payoff moment: same code, new week.
45 to 50, close. Recap checklist in the notebook, out loud. Next lesson reads a real spreadsheet file. Confirm Thursday 11 PM CT stands, and Saturday 9 AM his time as the second weekly slot.

## Delivery notes
Speak slowly, define every new word at first use: parameter, argument, return, scope, module, import, namespace. He types, you guide. No stats talk (no price, no lesson length) per standing rule. If he brought his three repeat spreadsheet tasks, swap challenge 3 discussion to his first task and name its functions together.
