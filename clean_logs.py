import boto3

# --------------------------------------------------------------
# Delete all CloudWatch log streams.
# --------------------------------------------------------------
def delete_log_streams():
    logs = boto3.client('logs')
    log_groups = logs.describe_log_groups()

    for log_group in log_groups['logGroups']:
        next_token = None
        log_group_name = log_group['logGroupName']
        print(f'\nFound Log Group:  {log_group_name} .....\n')

        answer = None
        # acceptable_answer_list = ("yes", "y", "Yes", "YES", "Y", "no", "n", "No", "NO", "N")
        affirmative_answer_list = ("yes", "y", "Yes", "YES","Y")
        negagive_answer_list = ("no", "n", "No", "NO", "N")
        acceptable_answer_list = affirmative_answer_list + negagive_answer_list

        while answer not in acceptable_answer_list:
            answer = input("Delete Log Group and Log Streams? (yes or no): ")
            if answer in affirmative_answer_list:
                # Do this.
                answer = True
                break
            elif answer in negagive_answer_list:
                # Do that.
                answer = False
                break
            else:
                print("Please enter yes or no.")

        message = f"""
        ************************************************************

        Displaying Log streams in Log group {log_group_name}:

        If you answered 'yes' (True), the logs will be displayed and DELETED
        If you answered 'no' (False), the logs will be displayed only and Not Deleted

        Your answer: {answer}
        ************************************************************
        """

        print(message)

        if answer == True:
            print(f"....DELETING Log Group: {log_group_name} \n")
            logs.delete_log_group(logGroupName=log_group_name)
        if answer == False:
            print(f"....(Not)Deleting Log Group: {log_group_name} \n")


        # while next_token == None:

        #     log_streams = logs.describe_log_streams(logGroupName=log_group_name)

        #     next_token = log_streams.get('nextToken', None)

        #     for stream in log_streams['logStreams']:
        #         log_stream_name = stream['logStreamName']
        #         print("Delete log stream:", log_stream_name)
        #         if answer == True:
        #             # logs.delete_log_stream(log_group_name, log_stream_name, logs)
        #             print("Fake Delete")

        #     if next_token:
        #         log_streams = logs.describe_log_streams(logGroupName=log_group_name,
        #                                                 nextToken=next_token)
        #     else:
        #         if not next_token and len(log_streams['logStreams']) == 0:
        #             print("No remaining Log streams in Log group....Deleting Log Group")
        #             logs.delete_log_group(logGroupName=log_group_name)




# START the main function 
delete_log_streams()


