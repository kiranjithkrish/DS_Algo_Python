def optimalFreelancing(jobs):
    # Write your code here.
    profit = 0
    LENGTH_OF_WEEK = 7
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    timeLine = [False] * LENGTH_OF_WEEK
    for job in jobs:
        maxTime = min(LENGTH_OF_WEEK,job["deadline"])
        for day in reversed(range(maxTime)):
            if timeLine[day] == False:
                timeLine[day] = True
                profit += job["payment"]
                break
    return profit


jobs =  [
    {
      "deadline": 2,
      "payment": 1
    },
    {
      "deadline": 1,
      "payment": 4
    },
    {
      "deadline": 3,
      "payment": 2
    },
    {
      "deadline": 1,
      "payment": 3
    },
    {
      "deadline": 4,
      "payment": 3
    },
    {
      "deadline": 4,
      "payment": 2
    },
    {
      "deadline": 4,
      "payment": 1
    },
    {
      "deadline": 5,
      "payment": 4
    },
    {
      "deadline": 8,
      "payment": 1
    }
  ]
profit = optimalFreelancing(jobs)
print(profit)
