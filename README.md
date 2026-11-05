# Digital Subscription, Licence Usage & Cost Optimisation System

A command-line Python application for managing software subscriptions. It keeps track of what an organisation pays for, shows how many licences are actually being used, and calculates how much money is being wasted on unused licences.

## Features

- View, add, update, and delete subscriptions
- Search by software name or department
- Track vendor, department, cost per licence, licence usage, auto-renewal, and renewal month
- See the monthly cost and wasted cost of each subscription, plus overall totals
- Save data to a text file automatically after each change
- Validate input, including costs, licence counts, yes/no answers, and month names

## How the cost analysis works

| Figure | Calculation |
| --- | --- |
| Monthly cost | Licences bought × cost per licence |
| Unused licences | Licences bought − licences in use |
| Wasted cost | Unused licences × cost per licence |

## Getting started

You need [Python 3.6 or later](https://www.python.org/downloads/). There are no other packages to install. From the project folder, run:

```bash
python subscription_system.py
```

On Mac or Linux, you may need to use `python3` instead. Your data is saved in `subscriptions.txt`, which is created the first time you run the program.

## Example

```text
_____COST ANALYSIS & LICENCE USAGE_____

Subscription ID : 1
Software        : Slack
Licences Bought : 40
Licences Used   : 28
Unused Licences : 12
Monthly Cost    : £250.00
Wasted Cost     : £75.00
-----------------------------------------


Subscription ID : 2
Software        : Zoom
Licences Bought : 15
Licences Used   : 15
Unused Licences : 0
Monthly Cost    : £180.00
Wasted Cost     : £0.00
-----------------------------------------


_____SUMMARY_____
Total Monthly Spend : £430.00
Total Wasted Spend  : £75.00
```

## Concepts demonstrated

- **Modular programming:** separate functions for each feature
- **Data structures:** subscription records stored in a 2D list
- **File handling:** loading and saving records in CSV format
- **Input validation and exception handling:** repeated prompts until valid data is entered

## Author

**Sheikh Ahnaf Ferdous** · [LinkedIn](https://www.linkedin.com/in/sheikh-ahnaf-ferdous-7b3874280/) · [GitHub](https://github.com/axhnf)
