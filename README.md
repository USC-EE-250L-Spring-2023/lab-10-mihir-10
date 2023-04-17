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
What is the best offloading mode? Why do you think that is?

Answer:
The best offloading modes were when one of process 1 and process 2 was offloaded. This could be because the local machine was slower than the machine the process was offloaded to, so it was faster to offload one process while running the other locally. However, offloading both could have been detrimental due to overhead (next question).

Question 5: 
What is the worst offloading mode? Why do you think that is?

Answer:
The worst modes were "none" and "both," "none" could have performed poorly because of the lower speed of the local machine, and "both" could have performed poorly because the overhead in sending the processes out and retrieving the results could have offset the faster speed of the non-local machine.

Question 6: 
The processing functions in the example aren't very likely to be used in a real-world application.
What kind of processing functions would be more likely to be used in a real-world application?
When would you want to offload these functions to a server?

Answer:
Functions that work on huge amounts of data and are more computationally complex are more likely to be used in a real-world application (testing and training large ML datasets for example). You would want to offload these functions to a server when you know that the overhead involved will still result in getting the results faster than running locally.



