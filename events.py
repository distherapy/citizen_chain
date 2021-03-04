#server()
def get_user_input():
    num_cashiers = input("# of cashiers working: ")
    num_cooks = input("# of cooks working: ")
    num_customers = input("# of customers: ")
    params = [num_cashiers, num_servers, num_customers]
    if all(str(i).isdigit() for i in params):
        params = [int(x) for x in params]
    else:
        print(
            "could not parse input. simulation will use default values:",
            "\n1 cashier, 1 cook, 1 customer.",
        )
        params = [1, 1, 1]
    return params
