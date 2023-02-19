from prefect import flow

@flow
def my_favorite_function():
    print("What is your favorite number?")
    return 43

if __name__ == "__main__":
    print(my_favorite_function())
