# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Mihir Singh

## Lab Question Answers

Question 1: 
Under what circumstances do you think it will be worthwhile to offload one or both
of the processing tasks to your PC? And conversely, under what circumstances will it not be
worthwhile?

Answer:
I think it would be worthwile to offload one or both of the processing tasks to the PC if they are very computationally intensive; if the tasks aren't that time-consuming, though, it might not be worth the overhead of offloading the tasks and then retrieving the results.

Question 2: 
Why do we need to join the thread here?

Answer: 
We need to join the thread there to make sure that data1 is ready before calling final_process() on data1 and data2.

Question 3:
Are the processing functions executing in parallel or just concurrently? What is the difference?

Answer:
The processing functions are executing in parallel, as they are running on different cpus on different machines. 
In parallel computation, processes run completely independently so they can run at the same time, while in 
concurrent computation, processes switch back and forth very quickly to give the illusion of running at the same time.
(https://oxylabs.io/blog/concurrency-vs-parallelism)

Question 4:

