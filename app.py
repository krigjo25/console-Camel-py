
#   Prompting the user with a input
def main():
    snake_case= ""

    #   Converting to snake_case
    for i in input('camelCase : '):
        snake_case += f"_{i.lower()}" if i != i.lower() and len(snake_case) > 0 else f"{i.lower()}"
    
    print(f"snake_case : {snake_case}")

if __name__ == "__main__":
    main()