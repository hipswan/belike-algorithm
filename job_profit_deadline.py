
# def jobschedule():
#     profit = [10,20,30,40,50,60]
#     deadline = [1,2,3,4,5,6]
#     n = len(profit)
#     dp = [[0 for x in range(n)] for x in range(n)]
#     for i in range(n):
#         dp[i][i] = profit[i]
#     for l in range(2,n+1):
#         for i in range(0,n-l+1):
#             j = i+l-1
#             dp[i][j] = max(profit[i] + dp[i+1][j], profit[j] + dp[i][j-1])
#     return dp[0][n-1]

from typing_extensions import final


def jobschedulegreedy1():
    final_job = []
    total_deadline = 0
    total_profit = 0
    jobs_copy = jobs
    no_jobs = len(jobs)
    while no_jobs:
        # find deadlines for job having max profit
        profit =jobs_copy[0]["profit"]
        deadline = jobs_copy[0]["deadline"]
        job = jobs_copy[0]["job"]
        # if(no_jobs==1):
        #     total_deadline+=deadline
        #     total_profit+=profit
        #     final_job.append(job)
        #     return final_job
        
        for i in range(1,no_jobs):
            if(deadline == jobs_copy[i]["deadline"]):
                # compare profit
                if(profit < jobs_copy[i]["profit"]):
                    profit = jobs_copy[i]["profit"]
                    job  = jobs_copy[i]["job"]
                no_jobs-=i
            else:
                
                
                jobs_copy = jobs_copy[i:]
                break
            
        total_deadline+=deadline
        total_profit+=profit
        final_job.append(job)
        no_jobs-=1
    return final_job,total_profit,total_deadline

deadlines = [2, 1, 1, 4]
profits = [3, 2, 5, 3]

jobs = [{"job": "job1", "profit": 3, "deadline": 2}, {"job": "job2",
                                                      "profit": 2, "deadline": 1}, {"job": "job3", "profit": 5, "deadline": 1}, {"job": "job4",
                                                                                                                                 "profit": 3, "deadline": 4} ]

# j1 1 ,1 
# j2 4 , 5
# j3 5 , 3
# j4 5 , 2
# j5 5 , 4
# j6 5 , 2

# 5 > 1
# take max deadlines - > 5 

# desc profit
# 1 - > check if max deadline is > 0 add to the set and decrement max deadlines
# j2 added to set
# max_deadline -1  => 4
# 2 - > j5 added to set , max dealine - 1 => 3
# 3 - > j3 added to set , 

def jobschedulegreedy2():
    max_deadline = jobs[-1]["deadline"]
    final_job =[]
    for job in job_profit:
        if(max_deadline):
            final_job.append(job["job"])
            max_deadline-=1
        else:
            return final_job
    
    return final_job



# og_jobs = [{"job": "job1", "profit": 3, "deadline": 2}, {"job": "job2",
#                                                       "profit": 2, "deadline": 1}, {"job": "job3", "profit": 5, "deadline": 1}, {"job": "job4",
#                                                                                                                                  "profit": 3, "deadline": 4} ]

og_jobs = [{"job": "job1", "profit": 10, "deadline": 1}, {"job": "job2",
                                                      "profit": 2, "deadline": 2}, {"job": "job3", "profit": 3, "deadline": 2}]
  
jobs = sorted(og_jobs,key=lambda x:x["deadline"])
job_profit = sorted(og_jobs,key=lambda x:x["profit"],reverse=True)
print(jobschedulegreedy2())



