#Project Name: Digital Subscription, Licence Usage & Cost Optimisation System
#Purpose: To manage software subscriptions and identify potential cost inefficiency

file_name = "subscriptions.txt"  #Stores the name of the text file used for saving data
valid_months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]


def load_subscriptions():
    subscriptions = []

    try:
        with open(file_name, "r") as file:  #it opens & reads the file, with allows it to automatically close it
            for line in file:
                clean_line = line.strip()  #removes any whitespaces before & after
                if not clean_line:  #safety check, if line empty it skips to the next line
                    continue
                parts = line.strip().split(",")  #it seperates into individual lists according to their fields wherever there is comma

                record = [
                    int(parts[0]),
                    parts[1],
                    parts[2],
                    parts[3],
                    float(parts[4]),
                    int(parts[5]),
                    int(parts[6]),
                    parts[7] == "True",
                    parts[8] == "True",
                    parts[9]
                ]

                subscriptions.append(record)  #it adds the records according to their fields

    except FileNotFoundError:
        with open(file_name, "w") as file: pass  #if file doesnt exists it creates it, pass creates an empty doc and closes it 
    return subscriptions

################################################################################################
def display_all_subscriptions(data):   #displays all the data

    print('\n_____All Subscriptions:_____')   #/n represents end of the line, it creates a blank line to separate from the previous lines of displayed code
    for i in data :  #loops around the 2D list and prints all the Data according to their fields
        print(f'''     
Subscription ID  :   {i[0]}                
Software Name    :   {i[1]}
Vendor           :   {i[2]}
Department       :   {i[3]}
Monthly Cost     :  £{i[4]}
Licences Bought  :   {i[5]}
Licences In Use  :   {i[6]}
Active           :   {i[7]}
Auto Renew       :   {i[8]}
Renewal Month    :   {i[9]}
------------------------------------------  
''')
# triple quotation marks prints all the lines of code at once


def user_menu():   #menu where the user inputs their choice
    print('\n_____Main Menu_____')
    print('''
1. View all subscriptions
2. Search subscriptions
3. Add new subscription
4. Update subscription
5. Delete subscription
6. View cost analysis
7. Save and exit
''')
#######################################################################################
def search_menu(data):
    print('\n-----Search Menu-----')
    print('''
1. Search by software name
2. Search by Department
3. Go back to Main Menu
''')

    while True:   #it creates an infinite loop until break statement is used

        try:
            user_input = int(input('Please input your choice (1-3): '))
        except ValueError:   #A ValueError occurs if you send a string into a function that requires a number
            print('Please enter a number')
            continue  #this allows to iterate again otherwise there's no user input

        if user_input == 1:
            search_by_software_name(data)
        elif user_input == 2:
            search_by_department_name(data)
        elif user_input == 3:
            break
        else:
            print('Invalid Choice, please input a value between 1-3')
            continue   #this allows the user to try again back to the search_menu

def search_by_software_name(data):

    name = str(input('Enter Software Name: ')).strip().title() #.strip() func removes all the spaces before and after the main string
    found = False

    for i in data:
        if name == i[1]:
            display_all_subscriptions([i])
            found = True
    if not found:
        print('No matching Software Name found')

def search_by_department_name(data):
   name = str(input('Enter Department Name: ')).strip().title()
   found = False

   for i in data:
       if name == i[3]:
           display_all_subscriptions([i])
           found = True
   if not found:
       print('No matching Department Name found')
###################################################################################

def generate_subscription_ID(data):
    highest_id = 0
    for i in data:
        if i[0] > highest_id:
            highest_id = i[0]
    return highest_id +1

def add_subscription(data):
    print('\n_____ADD SUBSCRIPTION ID_____')

    subscription_id = generate_subscription_ID(data)
    software_name = str(input('Enter Software Name: ')).strip().title()
    department = str(input('Enter Department: ')).strip().title()
    vendor = str(input('Enter Vendor Name: ')).strip().title()

    #Monthly Costs
    while True:

        try:
            monthly_cost = float(input('Enter monthly cost (£): '))
            if monthly_cost <= 0:
                print('Please enter a valid monthly cost')
            else:
                break
        except ValueError:
            print('Please enter a valid monthly cost')

    #Licencees Purchased
    while True:
        try:
            licences_purchased = int(input('Enter number of licences purchased: '))
            if licences_purchased <= 0:
                print('Please enter a valid number of licences purchased')
            else:
                break
        except ValueError:
            print('please enter a valid number of licences purchased')

    #Licences In Use
    while True:
        try:
            licences_in_use = int(input('Enter number of licences currently being used: '))
            if licences_in_use <= 0:
                print('Please enter a valid number of licences currently being used')
            elif licences_in_use > licences_purchased:
                print('Licences in use cannot exceed licences purchased')
            else:
                break
        except ValueError:
            print('Please enter a valid number of licences currently being used')

    #Activity Status
    while True:
        active_input = input("Is the licence currently active? (yes/no): ").strip().lower()
        if active_input == "yes":
            activity_status = True
            break
        elif active_input == "no":
            activity_status = False
            break
        else:
            print("Please enter yes or no.")

    #Auto Renew
    while True:
        auto_renew_input = input("Will it be automatically renewed? (yes/no): ").strip().lower()
        if auto_renew_input == "yes":
            auto_renew = True
            break
        elif auto_renew_input == "no":
            auto_renew = False
            break
        else:
            print("Please enter yes or no.")

    # Renewal Month
    while True:
        renewal_month = input("Enter renewal month: ").strip().title()
        if renewal_month in valid_months:
            break
        else:
            print("Please enter a valid month name (e.g. March).")

    #the new subscription is being added here
    new_record = [subscription_id,software_name,vendor,
                  department,monthly_cost,licences_purchased,
                  licences_in_use,activity_status,auto_renew,renewal_month]

    data.append(new_record)   #append adds it to the list
    save_to_file(data)
    print("New subscription has been added successfully.")
##################################################################################################

def find_subscription_id(sub_id, data):
    for i in data:
        if i[0] == sub_id:  #runs the loop to search for data for index 0 and returns accordingly
            return i
    return None

def update_subscription(data):
    display_all_subscriptions(data)

    print('\n_____UPDATE SUBSCRIPTION ID_____')
    print('Please print ENTER if you do not want to update a specific field')  #python registers it as empty string

    try:   #to avoid any input error (ValueError) which is only triggered when inputting other than int
        sub_id = int(input('Enter Subscription ID to update: '))
    except ValueError:
        print('Please enter a valid Subscription ID')
        return
        #empty return exits the function

    record_index = find_subscription_id(sub_id, data)
    if record_index is None:
        print('No such subscription found')
        return

    print("\nCurrent details:")
    display_all_subscriptions([record_index])
    save_to_file(data)

    #Software
    new_software= input(f"Software name [{record_index[1]}]: ").strip().title()
    if new_software != '':
        record_index[1] = new_software

    #Vendor
    new_vendor = input(f"Vendor name [{record_index[2]}]: ").strip().title()
    if new_vendor != '':
        record_index[2] = new_vendor

    #Department
    new_department = input(f"Department name[{record_index[3]}]: ").strip().title()
    if new_department != '':
        record_index[3] = new_department

    #Monthly cost
    while True:
        new_cost = input(f"Monthly cost (£{record_index[4]:.2f}): ").strip()
        if new_cost == "":
            break

        try:
            new_cost = float(new_cost)
            if new_cost < 0:
                print("Cost cannot be negative.")
            else:
                record_index[4] = new_cost
                break
        except ValueError:
            print("Enter a valid cost number.")

    #Licences purchased
    while True:
        new_licence = input(f"Licences purchased [{record_index[5]}]: ").strip()
        if new_licence == "":
            break

        try:
            new_licence = int(new_licence)
            if new_licence <= 0:
                print("Must be greater than zero.")
            elif new_licence < record_index[6]:
                print("Cannot be less than licences in use.")
            else:
                record_index[5] = new_licence
                break
        except ValueError:
            print("Enter a whole number please.")

    #Licences in use
    while True:
        new_in_use = input(f"Licences in use [{record_index[6]}]: ").strip()
        if new_in_use == "":
            break

        try:
            new_in_use = int(new_in_use)
            if new_in_use < 0:
                print("Cannot be negative.")
            elif new_in_use > record_index[5]:
                print("Cannot exceed licences purchased")
            else:
                record_index[6] = new_in_use
                break
        except ValueError:
            print("Enter a whole please")

    #Activity status
    new_active = input(f"Activity Status (yes/no) [{record_index[7]}]: ").strip().lower()

    if new_active == "yes":
        record_index[7] = True
    elif new_active == "no":
        record_index[7] = False

    #Auto Renewal
    new_autorenewal = input(f"Auto Renew (yes/no) [{record_index[8]}]: ").strip().lower()
    if new_autorenewal == "yes":
        record_index[8] = True
    elif new_autorenewal == "no":
        record_index[8] = False

    # Renewal month
    while True:
        new_month = input(f"Renewal month [{record_index[9]}]: ").strip().title()
        if new_month == "":
            break
        elif new_month in valid_months:
            record_index[9] = new_month
            break
        else:
            print("Invalid month. Please enter a full month name.")

    save_to_file(data)
    print("\nSubscription updated successfully.")
################################################################################

def delete_subscription(data):
    print("\n_____DELETE SUBSCRIPTION_____")

    try:
        sub_id = int(input("Enter Subscription ID to delete: "))
    except ValueError:
        print("Please enter a valid Subscription ID.")
        return

    record_index = find_subscription_id(sub_id, data)

    if record_index is None:  #this allows the function not to crash and trying to delete something thats not there
        print("No subscription found with that ID.")
        return

    print("\nSubscription found:")
    display_all_subscriptions([record_index])

    user_confirm = input("Are you sure you want to delete this subscription? (yes/no): ").strip().lower()

    if user_confirm == "yes":
        data.remove(record_index)
        save_to_file(data)
        print("Subscription has been DELETED successfully.")
    else:
        print("DELETION cancelled.")
#################################################################################
def cost_analysis(data):
    print("\n_____COST ANALYSIS & LICENCE USAGE_____")

    total_monthly_cost = 0
    total_wasted_cost = 0

    for record_index in data:
        subscription_id = record_index[0]
        software = record_index[1]
        monthly_cost = record_index[4]
        licences_bought = record_index[5]
        licences_used = record_index[6]

        cost_per_licence = monthly_cost
        unused_licences = licences_bought - licences_used
        wasted_cost = unused_licences * cost_per_licence

        total_monthly_cost += licences_bought * cost_per_licence
        total_wasted_cost += wasted_cost

    #reads and outputs the data in format given below
        print(f"""
Subscription ID : {subscription_id}
Software        : {software}
Licences Bought : {licences_bought}
Licences Used   : {licences_used}
Unused Licences : {unused_licences}
Monthly Cost    : £{licences_bought * cost_per_licence:.2f} 
Wasted Cost     : £{wasted_cost:.2f}
-----------------------------------------
""")
#':.2f' rounds it to 2 dp

    print("\n_____SUMMARY_____")
    print(f"Total Monthly Spend : £{total_monthly_cost:.2f}")
    print(f"Total Wasted Spend  : £{total_wasted_cost:.2f}")
#################################################################################


def save_to_file(data):
    try:
        with open(file_name, "w") as file: #The file is automatically created if it does not exist
            for record in data:            #with automatically closes the file safely
                line = ",".join(str(item) for item in record)  #it looks for ','(comma) to
                file.write(line + "\n")
        print("Data saved successfully.")
    except Exception as e:
        print("Error saving data:", e)

#################################################################################
subscriptions = load_subscriptions()

while True:
    try:
        user_menu()    #calls the function to input their choice of action
        choice = int(input('\nEnter your choice (from 1-7): '))
    except ValueError:
        print('Please enter a number')
        continue

    if choice == 1:
        display_all_subscriptions(subscriptions)
    elif choice == 2:
        search_menu(subscriptions)
    elif choice == 3:
        add_subscription(subscriptions)
    elif choice == 4:
        update_subscription(subscriptions)
    elif choice == 5:
        delete_subscription(subscriptions)
    elif choice == 6:
        cost_analysis(subscriptions)
    elif choice == 7:
        save_to_file(subscriptions)
        print("Data saved. Exiting the program.")
        break
    else:
        print('Invalid Choice, please input a value between 1-7')

