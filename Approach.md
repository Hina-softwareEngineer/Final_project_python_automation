# How to Approach the Problem

Use these tips to help you:

**Break the problem down into smaller pieces**. If you’re not sure how to solve a piece of the puzzle, look for an even smaller piece that you can solve. Build up those smaller pieces into a larger solution!

**Make one change at a time**. Write unit tests to make sure that each new part of the solution works the way you think it does. Run your unit tests frequently to make sure that each part of your solution keeps working as you make changes.

**Use version control**. Check each part of your solution into version control as you complete it, so you can always roll back to a known version of your code if you make a mistake.

**_Review module documentation!_** You are going to need to use these modules to complete the final project. Reading the documentation takes time, but as you become more familiar with the APIs provided by these modules, it could save you from writing a bunch of custom code that could have just been a call to a module function!

- [Python Image Library](https://pillow.readthedocs.io/en/stable/) (PIL) - [Tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
- [Requests](https://requests.readthedocs.io/en/master/) (HTTP client library) - [Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/)
- [ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf) (PDF creation library)
- [email](https://docs.python.org/3/library/email.examples.html) (constructing email)
- [psutil](https://psutil.readthedocs.io/en/latest/) (processes and system utilization)
- [shutil](https://docs.python.org/3/library/shutil.html) (file operations)
- [smtplib](https://docs.python.org/3/library/smtplib.html) (sending email)

To get the Data, first run :

- ./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz

- tar xf ~/supplier-data.tar.gz

#### To test out your script, you can install the `stress` tool.

`sudo apt install stress`

To produce stress on cpu
`stress --cpu 8`

You can set a cron job that executes the script `health_check.py` every 60 seconds and sends health status to the respective user.

To set a user cron job use the following command:
`crontab -e`

> Enter 1 to open in the nano editor. Now, set the complete path for health_check.py script, and save by clicking Ctrl-o, Enter key, and Ctrl-x.
