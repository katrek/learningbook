def main():
    # Opening the the video_times.txt
    video_file = open('video_times.txt', 'r')

    # Setting the accumulator to 0.0
    total = 0.0

    # Initialize the variable to keep count of the videos
    count = 0

    print('Here are the running times for each video: ')

    # Get the lines values from the file and total them.
    for line in video_file:
        # Convert line into a float
        run_time = float(line)

        # Add 1 to the count variable
        count += 1

        # Display the time
        print('Video#', count, ':', run_time, sep='')

        # Add the time to total
        total += run_time

        # Close the file
        video_file.close()

main()