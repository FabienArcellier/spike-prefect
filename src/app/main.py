from prefect import flow


@flow(name="main.my_favorite_function")
def my_favorite_function():
    print("What is your favorite number?")
    print(43)


@flow(name="main.my_favorite_function_2")
def my_favorite_function_2():
    print("What is your favorite number?")
    print(45)

