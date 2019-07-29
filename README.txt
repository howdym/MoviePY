UPDATES:
1. There turned out to be a delay, or some misrepresentation of time in the gazedata and the video. Hence, we are back at square one! We do not where or when the gaze data starts so we are back to working with the idea of working backwards and seeing where it goes.

2. Data repeats. Created a script that parses through the data and eliminates repetition. Unfortunately, that causes the script to run at O(n^2) time, which makes it quite slow. Also, there will be times in the video where the circle is not moving. Excessive repetitive data may be the cause of that. 

3. Timestamps repeats. I made a workaround. Can use improvements in elegance. See code for workaround

4. Huge gaps in data. I initially did a threshold check (if the duration is more than half of the video, then the top timestamps
is suspect), but not sure how big these gaps can get. The reason for the threshold check is to check for the junk data.
Have not seen junk data that has a timestamp that is similar to a "normal" line of data, but it can be possible. In this
iteration, I did a check that makes sure that the timestamp is at most 10 digits long, but even then there might be also
be a case where the starting number is more than 10 digits or gaze data lasts so long the timestamp changes to 11 digits yet
can still be a legit data point. Don't really have a great solution for this since the starting number seems to be arbitrary, with the exception that it usually is 9 digits long. 

Overall, these points need either clarification or feedback for improvement for further development.
