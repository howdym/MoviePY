UPDATES:
1. There turned out to be a delay, or some misrepresentation of time in the gazedata and the video. Hence, we are back at square one! We do not where or when the gaze data starts so we are back to working with the idea of working backwards and seeing where it goes.
2. Data repeats. Sort of just let it slide; it only gets caught if a chunk of data repeats and the script senses that
the timestamps are off (start is larger than end).
3. Timestamps repeats. I made a workaround. Can use improvements in elegance.
4. Huge gaps in data. I initially did a threshold check (if the duration is more than half of the video, then the top timestamps
is suspect), but not sure how big these gaps can get. The reason for the threshold check is to check for the junk data.
Have not seen junk data that has a timestamp that is similar to a "normal" line of data, but it can be possible. In this
iteration, I did a check that makes sure that the timestamp is at least 9 digits long, but even then there might be also
be a case where the starting number is not 9 digits or gaze data lasts so long the timestamp changes to 10 digits yet
can still be a legit data point.

Overall, these points need either clarification or feedback for improvement for further development.