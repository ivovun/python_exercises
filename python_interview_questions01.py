# https://www.interviewcake.com/python-interview-questions
# Slicing lists from the end

# We want to run some analytics on our investments. To start, we're given a list containing
# the balance at the end of the day for some number of days. The last item in the list
# represents yesterday's closing balance and each previous item refers to the day before.
#
#   daily_balances = [107.92, 108.67, 109.86, 110.15]
# Python 2.7
# The first step in the process is to grab adjacent items in the list. To get started, we want
# a function that takes in our list of daily_balances and prints pairs of adjacent balances fo
# r the last 3 days:
#
#   show_balances(daily_balances)
# Python 2.7
# should print:
#
#   "slice starting 3 days ago: [108.67, 109.86]"
# "slice starting 2 days ago: [109.86, 110.15]"
#
#   "slice starting 3 days ago: [108.67, 109.86]"
# "slice starting 2 days ago: [109.86, 110.15]"

daily_balances = [107.92, 108.67, 109.86, 110.15]



def show_balances(daily_balances_):

    num_balances = len(daily_balances_)

    # do not include -1 because that slice will only have 1 balance, yesterday
    for day in range(num_balances - 3, num_balances - 1):
        balance_slice = daily_balances_[day: day + 2]

        days_ago = num_balances - day

        # use positive number for printing
        print("slice starting %d days ago: %s" % (abs(days_ago), balance_slice))


show_balances(daily_balances)



print(daily_balances[-2: -1])
